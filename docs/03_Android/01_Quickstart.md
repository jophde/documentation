# Jargon-enabled in no time.

**Pre-requisites:** text/resources must be externalized (ie. live in resource files and not hardcoded into UI elements) **and** you must be on the Gradle build system (the standard for Android Studio).  Jargon supports the Android Gradle Plugin 1.0.+.

#### Add the Jargon Maven Repository and a Jargon Plugin dependency to your buildscript configuration.

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

#### Add the Jargon Maven Repository and a Jargon SDK dependency to your project configuration.

```
repositories {
    maven { url 'http://repos.colatris.com/releases' }
}

dependencies {
    compile 'com.colatris:colatris-sdk:0.9.6' 
}
```

#### Apply the Jargon Plugin *after* the Android Gradle Plugin.

```
apply plugin: 'com.android.application'
apply plugin: 'com.colatris.plugin'
```

####  Configure Jargon entirely in build.gradle, no Java needed.

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

Whenever you make release builds your apps strings will be sent to Jargon.

#####  If you are using Proguard or Dexguard be **sure** to add the following to your configuration.
    
```
-keep public class com.colatris.**
-keepclassmembers public class com.colatris.* { *; }
```

Have a complicated build or custom views?  Check out the [Advanced docs](/#/jargon/docs/03_Android/02_Advanced).

