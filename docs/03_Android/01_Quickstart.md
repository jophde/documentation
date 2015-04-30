# Colatris-enabled in no time.

**Pre-requisites:** text/resources must be externalized (ie. live in resource files and not hardcoded into UI elements) **and** you must be on the Gradle build system (the standard for Android Studio).  Colatris supports the Android Gradle Plugin 1.0.+.

#### Add the Colatris Maven Repository and a Colatris Plugin dependency to your buildscript configuration.

```
buildscript {
    repositories {
        maven { url 'http://repos.colatris.com/releases' }
    }
    
    dependencies {
        classpath 'com.colatris:colatris-plugin:0.9.6'
    }    
}
```

#### Add the Colatris Maven Repository and a Colatris SDK dependency to your project configuration.

```
repositories {
    maven { url 'http://repos.colatris.com/releases' }
}

dependencies {
    compile 'com.colatris:colatris-sdk:0.9.6' 
}
```

#### Apply the Colatris Plugin *after* the Android Gradle Plugin.

```
apply plugin: 'com.android.application'
apply plugin: 'com.colatris.plugin'
```

####  Configure Colatris entirely in build.gradle, no Java needed.

<<<<<<< HEAD
=======
* **projectId:** **(int)** the id tied to your project on the dashboard. *Required*
* **description:** **(String)** description of the app's version to make it more memorable. *Required*
* **apiKey:** **(String)** this project's API key displayed on the Colatris dashboard in Home > Project info. *Required*
* **editorMode:** **(boolean)** boolean to enable in-app editing by Colatris authed users. *Optional*
    * **Options:** *true*, *false*
    * **Default:** *false*
* **prodServing:** **(String)** option to specify frequency of copy update for end users. 
    * **Options:** *"none", "once", "daily", "weekly"*
    * **Default:** *"none"*
* **autoPush:** **(boolean)** boolean to specify if Colatris pushes strings whenever you build releases. *Optional*
    * **Options:** *true*, *false*
    * **Default:** *true*

>>>>>>> ab1729b66e9251787b49837692aa7a2858099707
```
colatris {
    projectId = %%pid%%
    description = "New app version"
    apiKey = "%%apik%%"
    editorMode = true
    prodServing = "daily"
    autoPush = true
}
```

#### Make release builds like you normally do.

Whenever you make release builds your apps strings will be sent to Colatris.

#####  If you are using Proguard or Dexguard be **sure** to add the following to your configuration.
    
```
-keep public class com.colatris.**
-keepclassmembers public class com.colatris.* { *; }
```

Have a complicated build or custom views?  Check out the [Advanced docs](/#/colatris/docs/03_Android/02_Advanced).

