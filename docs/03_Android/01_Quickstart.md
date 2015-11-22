# Jargon-enabled in no time.

**Pre-requisites:** text/resources must be externalized (ie. live in resource files and not hardcoded into UI elements) **and** you must be on the Gradle build system (the standard for Android Studio).  Jargon supports the Android Gradle Plugin 1.0.+.

#### Add the Jargon Maven Repository and a Jargon Plugin dependency to your buildscript configuration.

```
buildscript {
    repositories {
        maven { url 'http://repos.usejargon.com/releases' }
    }
    
    dependencies {
        classpath 'com.usejargon:jargon-plugin:1.1.0'
    }    
}
```

#### Add the Jargon Maven Repository and a Jargon SDK dependency to your project configuration.

```
repositories {
    jcenter() // Must specify jcenter as repo to get Jargon's dependencies
    maven { url 'http://repos.usejargon.com/releases' }
}

dependencies {
    compile 'com.usejargon:jargon-sdk:1.1.0' 
}
```

#### Apply the Jargon Plugin *after* the Android Gradle Plugin.

```
apply plugin: 'com.android.application'
apply plugin: 'com.usejargon.plugin'
```

####  Configure Jargon entirely in build.gradle, no Java needed.

```
jargon {
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
-keep public class com.usejargon.**
-keepclassmembers public class com.usejargon.* { *; }
```

Have a complicated build or custom views?  Check out the [Advanced docs](/#/jargon/docs/03_Android/02_Advanced).

