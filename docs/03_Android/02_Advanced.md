## Introduction

Jargon is designed to work with the Android Resource System. It uses the same string resource IDs that were already used in an app's string files. It can handle nearly all of an app's text including the ActionBar, Tabs,ListViews, and drop downs.  It works just fine with Android Layout XML and the Layout Editor.  In Production Serving mode, Jargon allows the resources in your app to be changed live for end users from our Web Dashboard.  Or if you build your app in editor mode users that you add to your Jargon project will be able to change and translate text in-context and sync their changes.  The Jargon Plugin offloads some work to compile and allows strings to be synced via Gradle tasks.

##### Jargon Editor Mode

This mode is designed so that it interferes with the regular app experience in almost no way, even for translators.* If an authorized translator is using the app, text will become editable and syncable with the Jargon servers.  Jargon will provide a top notch experience for translators, while maintaining the current state of the app for regular users.  The SDK will do nothing for users that do not have the Jargon app on their phone and even less if they aren't logged into it.

##### Jargon Production Serving Mode

This mode causes an app to sync it's resources at runtime with the Jargon Servers.  This means that any text resource in your app can be edited live for users from the Jargon dashboard.  Editor mode will not be enabled for any users even if an authorized user in the Jargon App is present.

##### Usage

When using a build with *editor mode* enabled simply press and hold with *three fingers* anywhere in your app to get the [Jargon app.](https://play.google.com/store/apps/details?id=com.usejargon.app&hl=en)  Login to the Jargon app and select your project.  From the project control panel you can get the latest text, save your changes, and even change locale without changing the system locale.

Anyone added to your Jargon project will be able to login to the Jargon app and start translating your app in-context, assuming it's built in editor mode.  Once logged in, simply press and hold any piece of text with one finger.  This will open a dialog where the raw text resource can be edited.  Once the edits are complete the text is saved in the Jargon SDK's storage and the started activities are recreated.  The new text will be display in place of the old text.  Press and hold with *two fingers* anywhere on the screen to translate all of the text on all views in the current `Activity`.

##### Plugin

In addition to offloading some work to build time from the Coaltris SDK, the plugin will also add Gradle tasks to your project.  The tasks allow you to push strings for an app version, pull text back into your project, and even send us a build of your app so our translators can work in context.  Tasks will be added for each of your app's build variants if `apiKey` is present in the `jargon`config.  

Examples:
```
// Push strings
gradle pushMainContentToJargon
gradle pushReleaseContentToJargon
gradle pushDebugContentToCoaltris

// Pull strings
gradle pullMainContentFromJargon
gradle pullReleaseContentFromJargon
gradle pullDebugContentFromJargon

// Send builds
gradle sendDebugBuildToJargon
gradle sendReleaseBuildToJargon
```

These are the tasks that will be added to a default Android project.  When using debug tasks the release `sourceSet` will be ignored if it exists and vice versa. Main only take resources from the main sourceSet.  When pulling, you can choose from the published and working string environments.  Published strings are served via CDN to users when Production Serving mode is enabled.  Working strings are the current strings on the dashboard regardless of status.

## Installation

#### Gradle

Jargon components are distributed via a private Maven repository.  Both the Plugin and the SDK are required for Jargon to function.  The Plugin handles expensive things like String extraction at build time.  The SDK will be statically linked to your app.  Jargon is configurable for each buildVariant you may have.  For example, you can make debug builds in `editorMode` and only use `prodServing` for release builds.  You could also use `editorMode` for an alpha build.  The possibilities are endless.

```
buildscript {
    repositories {
        jcenter()
        maven { url 'http://repos.usejargon.com/releases' } // HERE
    }

    // INCLUDE THE COLATRIS PLUGIN DEPENDENCY
    dependencies {
        classpath 'com.android.tools.build:gradle:1.0.0' // MINIMUM
        classpath 'com.usejargon:jargon-plugin:1.0.0' // HERE
    }
}

repositories {
    jcenter()
    maven { url 'http://repos.usejargon.com/releases' } // HERE
}

// INCLUDE THE COLATRIS SDK DEPENDENCY
dependencies {
    compile 'com.usejargon:jargon-sdk:1.0.0' // HERE
}

// APPLY THE COLATRIS PLUGIN (note: Order matters. Put Jargon after the Android plugin.)
apply plugin: 'com.android.application'
apply plugin: 'com.usejargon.plugin' // HERE

/* USE YOUR OWN SETTINGS BELOW
 * projectId = the id tied to your project on the dashboard (int)
 * description = description of your app's version to make it more memorable
 * apiKey = this project's API key displayed on the Jargon dashboard in Home > Project info
 * editorMode = boolean to enable in-app editing by Jargon authed users. Default: false
 * prodServing = option to specify frequency of copy update for end users. Options: "none", "once", "daily", "weekly" Default: "none"
 * autoPush = boolean that specifies if strings are sent up when release builds are made. Default: true
 */
usejargon {
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

If your app had prod and beta productFlavors you could configure buildVariants such as prodRelease or betaDebug.  Likewise, if your app had an additional avd buildType and no additional sourceSets you could configure the avd buildVariant.  By default a project does not have productFlavors. Jargon also handles flavor dimensions in a similar way.  If you have an abi flavor with the dimensions x86 and arm you could configure the variants releaseAbiX86Release.  The tasks Jargon adds will also follow a similar pattern.  Jargon attempts to adhere to the standards set forth by the [Android Gradle Plugin](http://tools.android.com/tech-docs/new-build-system/user-guide) as much as possible.

#### Custom Attributes

Jargon is capable of handling text set on custom attributes of custom views.  However, It does require a little bit more implementation.
Simply implement the `jargonCustomView` interface and provide Jargon with the `R.attr` values of your custom view. Jargon will then be able
to work with the custom view just like stock views.

```java
public class SampleCustomView extends TextView implements jargonCustomView {

    private CharSequence jargonText, jargonHint;
   
    public SampleCustomView(Context context, AttributeSet attrs, int defStyleAttr, int defStyleRes) {
        super(context, attrs, defStyleAttr, defStyleRes);

        TypedArray a = context.obtainStyledAttributes(attrs, R.styleable.SampleCustomView, defStyle, defStyleRes);

        setjargonText(a.getText(R.styleable.SampleCustomView_jargonText));
        setjargonHint(a.getText(R.styleable.SampleCustomView_jargonHint));

        a.recycle();
    }

    @Override
    public int[] getCustomAttributes() {
        return new int[]{ R.attr.jargonText, R.attr.jargonHint };  // Provide attrs here
    }

}
```

#### Proguard

If you are using Proguard, or Dexguard, the following lines need to be in your configuration.

```
-keep public class com.usejargon.**
-keepclassmembers public class com.usejargon.* { *; }
```