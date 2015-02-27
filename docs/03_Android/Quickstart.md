## Colatris-enabled in no time.
Pre-requisites: text/resources must be externalized (ie. live in resource files and not hardcoded into UI elements) **and** you must be on the Gradle build system (the standard for Android studio).

1. Add Colaris Maven Repo to your Gradle Project. 

    ```groovy
    buildscript {
        repositories {
            jcenter()
            maven { url 'http://repos.colatris.com/releases' } //HERE
        }

        dependencies {
            classpath 'com.android.tools.build:gradle:1.0.1'
            classpath 'com.colatris:colatris-plugin:0.8.0' //HERE
        }
    }

    repositories {
        jcenter()
        maven { url 'http://repos.colatris.com/releases' } //HERE
    }
    
    //INCLUDE THE COLATRIS DEPENDENCY
    dependencies {
        compile 'com.colatris:colatris-sdk:0.8.0' //HERE
    }
    
    //APPLY THE COLATRIS PLUGIN (note: Order matters. Put Colatris after the Android plugin.)
    apply plugin: 'com.android.application'
    apply plugin: 'com.colatris.plugin' //HERE

    /*USE YOUR OWN PROJECT INFORMATION BELOW
    //projectId = the id tied to your project on the dashboard (int) Ex. projectId = 1
    //contentVersion = your self-defined version of this build's copy (must be incrementing int) Ex. contentVersion = 3 
    //apiKey = this project's API key (secret string) Ex. apiKey = "JdfafKJLJj23434KDFdDFKJKweqDQ"
    //editorMode = boolean to enable in-app editing by Colatris authed users
    //prodServing = option to specify frequency of copy update for end users. Options: "none", "once", "daily", "weekly"
    */
    colatris {
        projectId = your_projectid_int //HERE
        contentVersion = content_version_int //HERE
        apiKey = "your_api_key" //HERE
        editorMode = true //HERE
        prodServing = "daily" //HERE
    }
    ```

2.  Add a `meta-data` element to the `application` element in your main `AndroidManifest.xml`.  This is how the the Colatris Plugin passes configuration to the Colatris SDK.

    ```xml
    <manifest>
      <application>
        <meta-data android:name="colatrisConfig" android:value="${colatrisConfig}" />
      </application>
    </manifest>
    ```

3. Override `Activity#attachBaseContext(Context)` in your base `Activity` or in each `Activity` that you want to enable Colatris for.

    ```java
    public class MyActivity extends Activity {

        @Override
        protected void attachBaseContext(Context newBase) {
            super.attachBaseContext(Colatris.proxy(newBase, this));
        }
    }
    ```

4.  If you are using Proguard or Dexguard be **sure** to add the following to your configuration.
    
    ```
    -keep public class com.colatris.**
    -keepclassmembers public class com.colatris.* { *; }
    ```

5.  Push up a new Content Version.  If it was already published the task will fail.  Simply increment `project.colatris.contentVersion` to publish a new one. You can also create a new Content version from the Dashboard or from within the Colatris in-app editor.
    ```
    gradle pushMainContentToColatris
    ```

6. **Optional.** Send us a build of your app so that translation can happen in-context.

    ```
    gradle sendMainBuildToColatris
    ```

7.  Now you can go ahead and order translations from the Dashboard! Sign in. Navigate to your project. And click "Translate Now". Once your translations are finished they can pulled back into your app's resouces.  Only directories with locale suffixes will be merged.  Colatris handles updating your existing string xml files and creating a new one if needed per each locale.

    ```
    gradle pullReleaseContentFromColatris
    ```

Note:  These steps will enable Colatris Manual Mode for all of your app's Build Variants.  To configure Colatris more granuarly please see the full Intengration Steps document.  In a stock Android app only two variants exist, `debug` and `release`. Colatris supports gradle commands .  Source sets that aren't part of a variant are respected.
