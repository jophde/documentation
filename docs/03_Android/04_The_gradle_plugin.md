Jargon makes use of a Gradle Plugin to do a lot of the heavy lifting at build time.  It also makes it easy to send us your strings and merge them back into your source when your translations are finished. 

## Build Variant Based Config

By default, an Android app has two [Build Variants](https://developer.android.com/tools/building/configuring-gradle.html), Release and Debug.  A more complex app may have many more.  For some tasks, such as build upload, Jargon will create tasks for each variant.  Other tasks, such as pulling content will have a task depending on your app's source sets.  Each Build Variant will add a source set to your project.  These tasks will also have a task for the main source set.  Jargon also allows you to configure each variant separately.  For example you can turn on `jargon.editorMode` for internal debug builds and `jargon.prodServing` for release builds.

```
jargon {
    projectId = %%pid%%
    description = "New app version"
    apiKey = "<project API key>"

    buildVariants {
    	debug {
    		editorMode = true
    	}

    	release {
    		prodServing = "daily"
    	}
    }
}
```

In order to see what tasks Jargon has added to your project just run `gradle tasks` in your project root or checkout out the Gradle panel within Android Studio.

#### Push Content

A Gradle task will be created for each source set in your app.  A basic Android app will have the following tasks added by the Jargon plugin.

`pushMainContentToJargon`

`pushDebugContentToJargon`

`pushReleaseContentToJargon`

Most likely you just have all of your app's strings in `src/main/res`.  Running `pushMainContentToJargon` will only touch those strings and no strings in `src/debug/res` or `src/release/res`.  If you did run the debug or release task then all of the strings in that source set in addition to the main source set will be sent to Jargon.

#### Pull Content

A Gradle task will be created for each source set in your app.  A basic Android app will have the following tasks added by the Jargon plugin.

`pullMainContentFromJargon`

`pullReleaseContentFromJargon`

`pullReleaseContentFromJargon`


###### Working Tasks


Source sets behave just like the push content tasks.  Pulling tasks also differentiate between your published production strings and your working strings.  Published strings are for your released app and are pushed to end users if `jargon.prodServing` is on.  Working strings are just the current state of strings on the Jargon Dashboard under the translate tab.  Both sets of strings share the same keys.  Usually you will want to merge production strings.

These tasks will update your `res` xml files in place.  Removing the need to manually copy and paste your translations back into your project.

#### Send Build

You can easily send us a Jargon enabled build without releasing it to the Play Store.  A regular Android app will have the following commands available.  

`sendDebugBuildToJargon`

`sendReleaseBuildToJargon`

These commands will build your app and upload it to Jargon.  Our translators will then be able to work in context.

