## Introduction

Colatris is designed to work with the Android Resource System. It uses the same string resource IDs that were already used in an app's string files. It can handle nearly all of an app's text including the ActionBar, Tabs,ListViews, and drop downs.  It works just fine with Android Layout XML and the Layout Editor.  In Production Serving mode, Colatris allows the resources in your app to be changed live for end users from our Web Dashboard.  Or if you build your app in editor mode users that you add to your Colatris project will be able to change and translate text in-context and sync their changes.  The Colatris Plugin offloads some work to compile and allows strings to be synced via Gradle tasks.

##### Colatris Editor Mode

This mode is designed so that it interferes with the regular app experience in almost no way, even for translators.* If an authorized translator is using the app, text will become editable and syncable with the Colatris servers.  Colatris will provide a top notch experience for translators, while maintaining the current state of the app for regular users.  The SDK will do nothing for users that do not have the Colatris app on their phone and even less if they aren't logged into it.

##### Colatris Production Serving Mode

This mode causes an app to sync it's resources at runtime with the Colatris Servers.  This means that any text resource in your app can be edited live for users from the Colatris dashboard.  Editor mode will not be enabled for any users even if an authorized user in the Colatris App is present.

##### Usage

When using a build with *editor mode* enabled simply press and hold with *three fingers* anywhere in your app to get the [Colatris app.](https://play.google.com/store/apps/details?id=com.colatris.app&hl=en)  Login to the Colatris app and select your project.  From the project control panel you can get the latest text, save your changes, and even change locale without changing the system locale.

Anyone added to your Colatris project will be able to login to the Colatris app and start translating your app in-context, assuming it's built in editor mode.  Once logged in, simply press and hold any piece of text with one finger.  This will open a dialog where the raw text resource can be edited.  Once the edits are complete the text is saved in the Colatris SDK's storage and the started activities are recreated.  The new text will be display in place of the old text.  Press and hold with *two fingers* anywhere on the screen to translate all of the text on all views in the current `Activity`.

##### Plugin

In addition to offloading some work to build time from the Coaltris SDK, the plugin will also add Gradle tasks to your project.  The tasks allow you to push strings for an app version, pull text back into your project, and even send us a build of your app so our translators can work in context.  Tasks will be added for each of your app's build variants if `apiKey` is present in the `colatris`config.  

Examples:
```
// Push strings
gradle pushMainContentToColatris
gradle pushReleaseContentToColatris
gradle pushDebugContentToCoaltris

// Pull strings
gradle pullMainContentFromColatris
gradle pullReleaseContentFromColatris
gradle pullDebugContentFromColatris

// Send builds
gradle sendDebugBuildToColatris
gradle sendReleaseBuildToColatris
```

These are the tasks that will be added to a default Android project.  When using debug tasks the release `sourceSet` will be ignored if it exists and vice versa. Main only take resources from the main sourceSet.  When pulling, you can choose from the published and working string environments.  Published strings are served via CDN to users when Production Serving mode is enabled.  Working strings are the current strings on the dashboard regardless of status.

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
        classpath 'com.colatris:colatris-plugin:0.9.6' // HERE
    }
}

repositories {
    jcenter()
    maven { url 'http://repos.colatris.com/releases' } // HERE
}

// INCLUDE THE COLATRIS SDK DEPENDENCY
dependencies {
    compile 'com.colatris:colatris-sdk:0.9.6' // HERE
}

// APPLY THE COLATRIS PLUGIN (note: Order matters. Put Colatris after the Android plugin.)
apply plugin: 'com.android.application'
apply plugin: 'com.colatris.plugin' // HERE

/* USE YOUR OWN SETTINGS BELOW
 * projectId = the id tied to your project on the dashboard (int)
 * description = description of your app's version to make it more memorable
 * apiKey = this project's API key displayed on the Colatris dashboard in Home > Project info
 * editorMode = boolean to enable in-app editing by Colatris authed users. Default: false
 * prodServing = option to specify frequency of copy update for end users. Options: "none", "once", "daily", "weekly" Default: "none"
 * autoPush = boolean that specifies if strings are sent up when release builds are made. Default: true
 */
colatris {
    projectId = %%pid%%
    description = "New app release" // HERE
    apiKey = "%%apik%%"
    editorMode = false // HERE
    prodServing = "none" // HERE
    autoPush = true // HERE

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

If your app had prod and beta productFlavors you could configure buildVariants such as prodRelease or betaDebug.  Likewise, if your app had an additional avd buildType and no additional sourceSets you could configure the avd buildVariant.  By default a project does not have productFlavors. Colatris also handles flavor dimensions in a similar way.  If you have an abi flavor with the dimensions x86 and arm you could configure the variants releaseAbiX86Release.  The tasks Colatris adds will also follow a similar pattern.  Colatris attempts to adhere to the standards set forth by the [Android Gradle Plugin](http://tools.android.com/tech-docs/new-build-system/user-guide) as much as possible.

#### Custom Attributes

Colatris is capable of handling text set on custom attributes of custom views.  However, It does require a little bit more implementation.
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