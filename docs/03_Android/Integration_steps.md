## Introduction

Colatris is designed to work with the Android Resource System. It uses the same string resources IDs that were already used in an app's string files. It can handle nearly all of an app's text including the ActionBar, Tabs, ListViews, and drop downs.

*Colatris is designed so that it interferes with the regular app experience in almost no way, even for translators.* If an authorized translator is using the app, text will become editable and syncable with the Colatris servers.Colatris will provide a top notch experience for translators, while maintaining the current state of the app for regular users.

## Installation

#### Gradle

Colatris components are distributed via a private Maven repository.  Both the Plugin and the SDK are required for Colatris to function.  The Plugin handles expensive things like String extraction at build time.  It also allows you to specify separate Colatris Project IDs and Content Versions for each of your flavors and variants.  You are also able to just specify a single Colatris Project and Content Version in your default config.  This functionality allows you to keep top-scecret alpha strings seperate from your current release.  A new Colatris project must be created for each flavor on the Colatris [dashboard](https://dashboard-preview.colatris.com/). 

```groovy
buildscript {
  repositories {
    maven { url 'http://repos.colatris.com/releases' } // Unfortunately, the repo must be specified separetely in the buildscript closure
  }

  dependencies {
    // Colatris targets the new 1.0.0 Gradle plugin.  However, it should work fine with 0.14.*. It requires Groovy 2.1 +.
    classpath 'com.android.tools.build:gradle:1.0.0'  
    classpath 'com.colatris:colatris-plugin:0.2.0'
  }
}

apply plugin: 'com.android.application'
apply plugin: 'com.colatris.plugin' // Must be applied after the Android Gradle Plugin!

repositories {
    maven { url 'http://repos.colatris.com/releases' }
}

dependencies {
    compile 'com.colatris:colatris-sdk:0.2.1'
}

android {
    compileSdkVersion 21
    buildToolsVersion '21.1.1'
    defaultConfig {
        minSdkVersion 16
        targetSdkVersion 21
        versionCode 1
        versionName '1.0.0'
        manifestPlaceholders = [colatrisProjectId: 1, colatrisContentVersion: 1]
    }

    // Colatris allows flavors to specify separate project IDs and Content Versions.  These
    // will override the default mainfest placeholders.
    productFlavors {
        alpha {
          manifestPlaceholders = [colatrisProjectId: 2, colatrisContentVersion: 1]     
        }

        beta {
          manifestPlaceholders = [colatrisProjectId: 3, colatrisContentVersion: 1]      
        }
    }
}
```

#### Manifest

Colatris uses the Android Gradle Plugin's Manifest Placeholder functionality to provide your Colatris Project ID and Content Version as Meta Data.  This allows the Colatris app to do things such as recreate activities after pulling the latest text.  It also ensures that the Colatris app can communicate in private with your app instead of sending broadcasts to all of the Colatris enabled apps that may be on a users phone.

Even if your project has multiple flavors, such as alpha, beta, paid, free, etc, these declarations only need to be in the main source set's Manifest.  The Android Gradle Plugin Manifest Merger will take care of adding the Meta Data to each individual flavor when you build.

```xml
<manifest>
  <application>
    <meta-data android:name="colatrisProjectId" android:value="${colatrisProjectId}" />
    <meta-data android:name="colatrisContentVersion" android:value="${colatrisContentVersion}" />
  </application>
</manifest>
```

#### Application 

Next, the implementing app needs to initialize the Colatris SDK.  This is done in [Application#onCreate()](http://developer.android.com/reference/android/app/Application.html#onCreate()).

```java
public class SampleApplication extends Application {
    // ...

    @Override public void onCreate() {
        super.onCreate();
        Colatris.Config config = new Colatris.Config();
        
        // Allows users authenticated through the Colatris app to get and set text.  If this is true, production serving will be disabled.
        // When manual mode is enabled users will be able to do a three finger press and hold anywhere in your app.  This action will
        // direct them to Play Store to download the Colatris app.  If the Colatris app is installed they will be taken to your app's
        // project control panel where they can perform actions.  Once authenticated, users can also press and hold individual peices of
        // text.  This will open a dialog that allows them to make edits in-context.  The default is false.
        config.setManualMode(true);  

        // Makes the Colatris SDK print logs.  Uses the standard Android logging levels.  Defaults to Colatris.Config.LogLevel.NONE
        config.setLogLevel(Colatris.Config.LogLevel.DEBUG);

        // The config parameter is optional, however the default config will do almost nothing.
        Colatris.init(this, config);
    }

    // ...
}
```

#### Activity

Colatris works by proxying the Android resource system.  In needs to receive views to work with as they are inflated.  This can be accomplished by overriding [Activity#attachBaseContext(Context)](http://developer.android.com/reference/android/view/ContextThemeWrapper.html#attachBaseContext(android.content.Context)) in Activities. The second parameter, `this` is a [LayoutInflater.Factory](http://developer.android.com/reference/android/view/LayoutInflater.Factory.html) instance. It is also proxied by Colatris in order for it localize views with text as they are inflated from XML.  Passing it also ensures that Colatris interfers with the rest of Android as little as possible. All activities, including support Actiivties implement the `LayoutInflater.Factory` interface so passing `this` is enough.

```java
public class SampleActivity extends Activity {
    // ...

   @Override protected void attachBaseContext(Context newBase) { 
        super.attachBaseContext(Colatris.proxy(newBase, this)); 
   }
   
   // ...
}
```

This method can be overridden in a base Activity class instead of putting it in each one.

#### Proguard

If you are using Proguard, or Dexguard, the following lines need to be in your configuration.

```
-keep public class com.colatris.**
-keepclassmembers public class com.colatris.* { *; }
-dontwarn com.colatris.**
```

#### Issues
There is also a known issue with Android Support Library Fragments that prevent their layouts from being localized via Colatris.  This issue
only effects the newest libraries for Lollipop, 21.0.+.  There is a work around for now.  Simply use the `Activity` `LayoutInflater` instead
of the support `Fragment` inflater.

```java
public cass SampleFragment extends Fragment {
  //... 
  
  @Override public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle state) {
    return getActivity().getLayoutInflater().inflate(R.layout.fragment_main, container, false);
  }

  //...
}
```

This is known issue and future versions of the support library should address it.

## Usage

When using a build with manual mode enabled simply press and hold with three fingers anywhere in your app to get the [Colatris app.](https://play.google.com/store/apps/details?id=com.colatris.app&hl=en)  Login to the Colatris app and select your project.  From the project control panel you can get the latest text, save your changes, and even change locale without changing the system locale.

The Colatris app also allows your publish Content Versions of your text.  Simply hit the "Create New Build" button on your Project control panel in the Colatris app.  If an app with the corresponding Colatris Project ID is installed on the phone the strings for it's default locale will be sent to Colatris Web Dashboard.  Once a Content Version is published it can not be overwritten. To publish a new Content Version you must increment the Content Version in your `build.gradle`.  We recommend incrementing each Content Version by one but the only thing enforced is that the next version must be a larger integer.

## Coming Soon

The next version of the Colatris Plugin will include Gradle tasks for sending APKs for each flavor to us with a simple command.  Tasks for each individual flavor will also be created.

```
gradle colatrisSendApk
gradle colatrisSendAlphaApk
```

There will also be tasks to pull down the text for the specifed Content Version in each Flavor.  The text will be automatically merged back into the `/res` directoy for each flavor.

```
gradle colatrisGetContentVersion
gradle colatrisGetAlphaContentVersion
```

The SDK will continue to see improvements in editor coverage and speed.
