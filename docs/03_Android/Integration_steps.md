## Introduction

Colatris is designed to work with the Android Resource System. It uses the same string resources IDs that were already used in an
app's string files. It can handle nearly all of an app's text including the ActionBar, Tabs, ListViews, and drop downs.

*Colatris is designed so that it interferes with the regular app experience in almost no way, even for translators.*
If an authorized translator is using the app, text will become editable and syncable with the Colatris servers.
Colatris will provide a top notch experience for translators, while maintaining the current state of the app for regular
users.

## Installation

#### Android Studio/IntelliJ + Gradle

Colatris is distributed via a private Maven repository.  This allows users of the new Android Gradle Build System
to simply declare a dependency to the SDK and repository in `build.gradle`.

```groovy
buildscript {
    // ...
}

repositories {
    maven { url 'http://repos.colatris.com/releases' }
}

dependencies {
    compile 'com.colatris:colatris-sdk:0.1.4'
}

android {
    // ...
}
```

#### Android Maven Plugin

The Android Maven Plugin now supports AAR libraries just like Gradle.  Simply add the Colatris repo and a dependency on the Colatris SDK to `pom.xml`

```xml
<project>
    <!-- ... -->

    <repositories>
        <!-- ... -->
        
        <repository>
	        <id>Colatris</id>
	        <url>http://repos.colatris.com/releases</url>
        </repository>
        
        <!-- ... -->
    </repositories>

    <!-- ... -->
    
    <dependencies>
        <!-- ... -->
        
        <dependency>
            <groupId>com.colatris</groupId>
            <artifactId>colatris-sdk</artifactId>
            <version>0.1.4</version>
            <type>aar</type>
        </dependency>
        
        <!-- ... -->
    </dependencies>
    
    <!-- ... -->
    
</project>
```

#### Eclipse Ant

Things are a little more involved on the old build system. 

1.  [Download](https://www.dropbox.com/s/5yiv9c224c8zvxs/colatris-sdk-0.1.4.jar?dl=0) the Colatris SDK jar.
2.  Place the jar in your app's `libs/`
3.  Add required items to your app's `AndroidManifest.xml`
4.  [Download](https://www.dropbox.com/s/02q6cqtxkn68742/colatris-sdk-0.1.4-javadoc.jar?dl=0) the Javadoc jar and place it in `libs/`

```xml
<manifest>
  <!-- ... -->
        
  <uses-permission android:name="android.permission.INTERNET" />
        
  <!-- ... -->
        
  <application>
    <!-- ... -->
            
    <service android:name="com.colatris.sdk.CsService" />

    <receiver
      android:name="com.colatris.sdk.CsSyncReceiver"
      android:permission="com.colatris.app.SYNC"
      android:enabled="false">
      <intent-filter>
        <action android:name="com.colatris.sdk.PULL" />
      </intent-filter>
      <intent-filter>
        <action android:name="com.colatris.sdk.PUSH" />
      </intent-filter>
      <intent-filter>
        <action android:name="android.intent.action.PACKAGE_REPLACED" />
        <data android:scheme="package" />
      </intent-filter>
      <intent-filter>
        <action android:name="android.intent.action.LOCALE_CHANGED" />
      </intent-filter>
    </receiver>
    <!-- ... -->
    </application>
</manifest>

## Proguard

If you are using Prograud a few lines will need to added to your configuration.

```
-keep public class com.colatris.sdk.**
-keepclassmembers public class com.colatris.sdk.* { *; }
-keepattributes InnerClasses
-keep class **.R
-keep class **.R$* { ; }
```

## Application 

Next, the implementing app needs to initialize the Colatris.  This is done in the 
app's [Application#onCreate()](http://developer.android.com/reference/android/app/Application.html#onCreate()).

```java
// ...

public class SampleApplication extends Application {
    
    // ...

    @Override public void onCreate() {
        super.onCreate();
        // long pid (of your app, not 1), Class r, Context c, boolean log
        Colatris.init(1, R.class, this, false);
    }
    
    // ...
}
```

## Activity

Colatris works by proxying the Android resource system.  In needs to receive views to work with as they are inflated.  This can
be accomplished by overriding 
[Activity#attachBaseContext(Context)](http://developer.android.com/reference/android/view/ContextThemeWrapper.html#attachBaseContext(android.content.Context)) 
in Activities and Services. The code below needs to run for each Activity and Services that show localizable notifications.

```java
// ...

public class SampleActivity extends Activity {
    // ...

   @Override 
   protected void attachBaseContext(Context newBase) { 
        super.attachBaseContext(Colatris.proxy(newBase)); 
   }
   
   // ...
}
```

This method can be overridden in a base Activity or Service class instead of putting it in each one.

## Notes
The Colatris SDK will only attach the in-context-editor to views that are inflated. However, views that aren't inflated 
will still be able to load string resources from Colatris. When enabled, Colatris will proxy all calls to the Android resource 
system. Even calls like [Activity#getText(int)](http://developer.android.com/reference/android/content/Context.html#getText(int)) 
will be proxied.


Currently there is a bug in Android Studio and IntelliJ that prevents Javadoc from being linked with the SDK in the IDE.  If the 
Javadoc for the public SDK is needed please download the jar linked in the Eclipse Ant instructions and extract them.  They will be hosted
shortly.
