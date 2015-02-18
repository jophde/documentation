1. Add Colaris Maven Repo to your Gradle Project.  Unfortunately, it needs to be declared in both `project.buildscript.repositories` and `project.respositories`.  Then, declare a dependency on both the Colatris Plugin and the SDK.  Next, apply the Colatris Plugin after the Android Plugin. Finally, setup `project.colatris` with your project's information.

    ```groovy
    buildscript {
        repositories {
            jcenter()
            maven { url 'http://repos.colatris.com/releases' } 
        }

        dependencies {
            classpath 'com.android.tools.build:gradle:1.0.1'
            classpath 'com.colatris:colatris-plugin:0.8.0'
        }
    }

    repositories {
        maven { url 'http://repos.colatris.com/releases' }
    }

    dependencies {
        compile 'com.colatris:colatris-sdk:0.8.0'
    }

    apply plugin: 'com.android.application'
    apply plugin: 'com.colatris.plugin'

    // USE YOUR OWN PROJECT'S INFORMATION
    colatris {
        projectId = 1
        contentVersion = 1
        apiKey = "JdfafKJLJj23434KDFdDFKJKweqDQ"
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

4.  Optional.  If you are using Proguard or Dexguard be sure to add the following to your configuration.
    
    -keep public class com.colatris.**
    -keepclassmembers public class com.colatris.* { *; }

5.  Push up the Content Version declared in `project.colatris.contentVersion` to the Colatris Dashboard.  If it was already published the task will fail.  Simply increment `project.colatris.contentVersion` to publish a new one.  This should be done when your next app release is ready to translation.

    gradle pushReleaseContentToColatris

6. Send us a build of your app so that translation can happen in-context.  Content Versions can also be published from the Colatris app if step 5 is skipped.

    gradle sendReleaseBuildToColatris

7.  Once your translations are finished they can pulled back into your app's resouces.  Only values directories with locale suffixes will be merged.  Colatris handles updating your existing string xml files and creating a new one if needed per each locale.

    gradle pullReleaseContentFromColatris

Note:  These steps will enable Colatris Manual Mode for all of your app's Build Variants.  To configure Colatris more granuarly please see the full Intengration Steps document.  In a stock Android app only two variants exist, `debug` and `release`.  Source sets that aren't part of a variant are respected.
