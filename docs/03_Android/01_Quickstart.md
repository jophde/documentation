# Colatris-enabled in no time.

**Pre-requisites:** text/resources must be externalized (ie. live in resource files and not hardcoded into UI elements) **and** you must be on the Gradle build system (the standard for Android Studio).  Colatris supports the Android Gradle Plugin 1.0.+.

#### Add the Colatris Maven repo to the buildscript configuration.

```
buildscript {
    repositories {
        maven { url 'http://repos.colatris.com/releases' }
    }
}
```

#### Declare a buildscript dependency on the Colatris Gradle plugin.

```
buildscript {
    dependencies {
        classpath 'com.colatris:colatris-plugin:0.9.2'
    }    
}
```

#### Add the Colatris Maven repo to the top-level project configuration.

```
repositories {
    maven { url 'http://repos.colatris.com/releases' }
}
```

####  Decalare a project dependency on the Colatris SDK.

```
dependencies {
    compile 'com.colatris:colatris-sdk:0.9.2' 
}
```

#### Apply the Colatris Plugin.  It must be applied after the android plugin.

```
apply plugin: 'com.colatris.plugin'
```

####  Configure Colatris entirely in build.gradle, no Java needed.

* **projectId:** **(int)** the id tied to your project on the dashboard. *Required*
* **contentVersion:** **(int)** your self-defined version of this build's copy (must be incrementing). *Required*
* **description:** **(String)** description of the content version to make it more memorable. *Required*
* **apiKey:** **(String)** this project's API key displayed on the Colatris dashboard in Home > Project info. *Required*
* **editorMode:** **(boolean)** boolean to enable in-app editing by Colatris authed users. *Optional*
	* **Options:** *true*, *false*
	* **Default:** *false*
* **prodServing:** **(String)** option to specify frequency of copy update for end users. 
	* **Options:** *"none", "once", "daily", "weekly"*
	* **Default:** *"none"*


```
colatris {
    projectId = %%pid%%
    contentVersion = %%pbuild%%
    description = "New content version"
    apiKey = "<project API key>"
    editorMode = true
    prodServing = "daily"
}
```

####  Add a `meta-data` element to the `application` element in your main `AndroidManifest.xml`.

This is how the the Colatris Plugin passes configuration to the Colatris SDK.

```
<manifest>
  <application>
    <meta-data android:name="colatrisConfig" android:value="${colatrisConfig}" />
  </application>
</manifest>
```

#### Override `Activity#attachBaseContext(Context)` in your base `Activity` 

Or in each `Activity` that you want to enable Colatris for.

```
public class MyActivity extends Activity {

    @Override
    protected void attachBaseContext(Context newBase) {
        super.attachBaseContext(Colatris.proxy(newBase, this));
    }
}
```

# DONE!

####  If you are using Proguard or Dexguard be **sure** to add the following to your configuration.
    
```
-keep public class com.colatris.**
-keepclassmembers public class com.colatris.* { *; }
```
####  Push up a new Content Version.  

If it was already published the task will fail.  Simply increment `project.colatris.contentVersion` to publish a new one. You can also create a new Content version from the Dashboard or from within the Colatris in-app editor.

```
gradle pushMainContentToColatris
```

##### Send us a build of your app so that translation can happen in-context.  

**Optional.** Each type of build can be sent sperately.

```
gradle sendReleaseBuildToColatris
```

####  Now you can go ahead and order translations from the Dashboard! 


Sign in. Navigate to your project. And click "Translate Now". Once your translations are finished they can pulled back into your app's resouces.  Only directories with locale suffixes will be merged.  Colatris handles updating your existing string xml files and creating a new one if needed per each locale.

```
gradle pullMainWorkingContentFromColatris
```

__Note:__  These steps will enable Colatris Editor Mode for all of your app's Build Variants.  To configure Colatris more granuarly please see the full Intengration Steps document.
