## Introduction

Colatris is designed to work with the Android Resource System. It uses the same string resource IDs that were already used in an app's string files. It can handle nearly all of an app's text including the ActionBar, Tabs,ListViews, and drop downs.  It works just fine with Android Layout XML and the Layout Editor.  In Production Serving mode, Colatris allows the resources in your app to be changed live for end users from our Web Dashboard.  Or if you build your app in editor mode users that you add to your Colatris project will be able to change and translate text in-context and sync their changes.  The Colatris Plugin offloads some work to compile and allows strings to be synced via Gradle tasks.

##### Colatris Editor Mode

This mode is designed so that it interferes with the regular app experience in almost no way, even for translators.* If an authorized translator is using the app, text will become editable and syncable with the Colatris servers.  Colatris will provide a top notch experience for translators, while maintaining the current state of the app for regular users.  The SDK will do nothing for users that do not have the Colatris app on their phone and even less if they aren't logged into it.

##### Colatris Production Serving Mode

This mode causes an app to sync it's resources at runtime with the Colatris Servers.  This means that any text resource in your app can be edited live for users from the Colatris dashboard.  Editor mode will not be enabled for any users even if an authorized user in the Colatris App is present.

##### Usage

When using a build with *editor mode* enabled simply press and hold with *three fingers* anywhere in your app to get the [Colatris app.](https://play.google.com/store/apps/details?id=com.colatris.app&hl=en)  Login to the Colatris app and select your project.  From the project control panel you can get the latest text, save your changes, and even change locale without changing the system locale.

The Colatris app also allows your publish Content Versions of your text.  Simply hit the "Create New Build" button on your Project control panel in the Colatris app.  If an app with the corresponding Colatris Project ID is installed on the phone the strings for it's default locale will be sent to Colatris Web Dashboard.  Once a Content Version is published it can not be overwritten. To publish a new Content Version you must increment the `contentVersion` in `build.gradle`.  We recommend incrementing each Content Version by one but the only thing enforced is that the next version must be a larger integer.

Anyone added to your Colatris project will be able to login to the Colatris app and start translating your app in-context, assuming it's built in editor mode.  Once logged in, simply press and hold any piece of text with one finger.  This will open a dialog where the raw text resource can be edited.  Once the edits are complete the text is saved in the Colatris SDK's storage and the started activities are recreated.  The new text will be display in place of the old text.  Press and hold with *two fingers* anywhere on the screen to translate all of the text on all views in the current `Activity`.

##### Plugin

In addition to offloading some work to build time from the Coaltris SDK, the plugin will also add Gradle tasks to your project.  The tasks allow you to push a content version, pull text back into your project, and even send us a build of your app so our translators can work in context.  Tasks will be added for each of your app's build variants if `apiKey` is present in the `colatris`config.  

Examples:
```
// Push content version
gradle pushMainContentToColatris
gradle pushReleaseContentToColatris
gradle pushDebugContentToCoaltris

// Pull working strings
gradle pullMainWorkingContentFromColatris
gradle pullReleaseWorkingContentFromColatris
gradle pullDebugWorkingContentFromColatris

// Pull production strings
gradle pullMainProductionContentFromColatris
gradle pullReleaseProductionContentFromColatris
gradle pullDebugProductionContentFromColatris

// Send builds
gradle sendDebugBuildToColatris
gradle sendReleaseBuildToColatris
```

These are the tasks that will be added to a default Android project.  When using debug tasks the release `sourceSet` will be ignored if it exists and vice versa. Main only take resources from the main soruceset.  When pulling, you can choose from the published and working string environments.  Published strings are served via CDN to users when Production Serving mode is enabled.  Working strings are the current strings on the dashboard regardless of status.

## Installation

#### Gradle

Colatris components are distributed via a private Maven repository.  Both the Plugin and the SDK are required for Colatris to function.  The Plugin handles expensive things like String extraction at build time.  The SDK will be statically linked to your app.  Colatris is configurable for each buildVariant you may have.  For example, you can make debug builds in `editorMode` and only use `prodServing` for release builds.  You could also use `editorMode` for an alpha build.  The possibilities are endless.

```
buildscript {
    repositories {
        jcenter()
        maven { url 'http://repos.colatris.com/releases' } // HERE
    }

    // INCLUDE THE COLATRIS PLUGIN DEPENDENCY
    dependencies {
        classpath 'com.android.tools.build:gradle:1.0.0' // MINIMUM
        classpath 'com.colatris:colatris-plugin:0.9.2' // HERE
    }
}

repositories {
    jcenter()
    maven { url 'http://repos.colatris.com/releases' } // HERE
}

// INCLUDE THE COLATRIS SDK DEPENDENCY
dependencies {
    compile 'com.colatris:colatris-sdk:0.9.2' // HERE
}

// APPLY THE COLATRIS PLUGIN (note: Order matters. Put Colatris after the Android plugin.)
apply plugin: 'com.android.application'
apply plugin: 'com.colatris.plugin' // HERE

/* USE YOUR OWN SETTINGS BELOW
 * projectId = the id tied to your project on the dashboard (int)
 * contentVersion = your self-defined version of this build's copy (must be incrementing int)
 * description = description of the content version to make it more memorable
 * apiKey = this project's API key displayed on the Colatris dashboard in Home > Project info
 * editorMode = boolean to enable in-app editing by Colatris authed users. Default: false
 * prodServing = option to specify frequency of copy update for end users. Options: "none", "once", "daily", "weekly" Default: "none"
 */
colatris {
    projectId = %%pid%%
    contentVersion = %%pbuild%%
    description = "New content version" // HERE
    apiKey = "<project API key>" // HERE
    editorMode = false // HERE
    prodServing = "none" // HERE

    buildVariants {  // Only editorMode and prodServing can be overriden
        debug {
            editorMode = true
            prodServing = "none"
        }

        release {
            editorMode = false
            prodServing = "daily"
        }
    }
}
```

If your app had prod and beta productFlavors you could configure buildVariants such as prodRelease or betaDebug.  Likewise, if your app had an additional avd buildType and no additional sourceSets you could configure the avd buildVariant.  By default a project does not have productFlavors. Colatris also handles flavor dimensions in a similar way.  If you have an abi flavor with the dimenions x86 and arm you could configure the variants releaseAbiX86Release.  The tasks Colatris adds will also follow a similar pattern.  Colatris attempts to adhere to the standards set forth by the [Android Gradle Plugin](http://tools.android.com/tech-docs/new-build-system/user-guide) as much as possible.

#### Manifest

Colatris uses the Android Gradle Plugin's Manifest Placeholder functionality to provide your Colatris Configuration as Meta Data.  This allows the Colatris app to do things such as recreate activities after pulling the latest text.  It also ensures that the Colatris app can communicate in private with your app instead of sending broadcasts to all of the Colatris enabled apps that may be on a user's phone.

Even if your project applies colatris to multiple variants such as alphaRelease, betaRelease, paidDebug, freeDebug, etc, these declarations only need to be in the main sourceSet's Manifest.  The Android Gradle Plugin Manifest Merger will take care of adding the Meta Data to each individual variants when you build.

```xml
<manifest>
  <application>
    <meta-data android:name="colatrisConfig" android:value="${colatrisConfig}" />
  </application>
</manifest>
```

#### Activity

Colatris can be enabled by overriding `Activity#attachBaseContext(Context)`.  This will work on individual activites or on a base activity. If an Activity does not have `attachBaseContext` overridden it will use the regular Android resource system and not the Colatris resource system.  This addition is required for both `editorMode` and `prodServing`.

```java
public class MyActivity extends Activity {

    @Override
    protected void attachBaseContext(Context newBase) {
        super.attachBaseContext(Colatris.proxy(newBase, this));
    }
}
```

The technique can also be used on `Service` classes that display text on notifications.

#### Custom Attributes

Colatris is capable of handling text set on custom attributes of custom views.  However, It does require a little bit more implmentation.
Simply implement the `CsCustomView` interface and provide Colatris with the `R.attr` values of your custom view. Colatris will then be able
to work with the custom view just like stock views.

```java
public class SampleCustomView extends TextView implements CsCustomView {

    private CharSequence csText, csHint;
   
    public SampleCustomView(Context context, AttributeSet attrs, int defStyleAttr, int defStyleRes) {
        super(context, attrs, defStyleAttr, defStyleRes);

        TypedArray a = context.obtainStyledAttributes(attrs, R.styleable.SampleCustomView, defStyle, defStyleRes);

        setCsText(a.getText(R.styleable.SampleCustomView_csText));
        setCsHint(a.getText(R.styleable.SampleCustomView_csHint));

        a.recycle();
    }

    @Override
    public int[] getCustomAttributes() {
        return new int[]{ R.attr.csText, R.attr.csHint };  // Provide attrs here
    }

}
```


#### Proguard

If you are using Proguard, or Dexguard, the following lines need to be in your configuration.

```
-keep public class com.colatris.**
-keepclassmembers public class com.colatris.* { *; }
```