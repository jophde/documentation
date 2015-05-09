## Integrate the Jargon SDK into your iOS app

The framework is designed to require minimal changes to your app's code, and yet cover nearly app of the app's text. Strings declared in code, using NSLocalizedString, as well as strings types into Interface Builder are both supported.

### Using CocoaPods

* Add `pod 'Jargon'` to your Podfile and run `pod install`.

* In your project's Info.plist file, add the following keys/value pair: 
    * `JargonAppId` (String): `%%pid%%`

* Run `Pods/Jargon/jargon setup -p . -k %%apik%%`

* In your AppDelegate, initialize Jargon: (see below for options)

```objc
#import <Jargon/Jargon.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{   
    [Jargon startWithAPIKey:@"%%apik%%" andOptions:<options>];
    //  ...
}
```

### Manual installation

You will need:

1. Jargon.framework
2. The Jargon binary


Download a .zip of both [here](https://github.com/colatris/colatris-ios-sdk/archive/master.zip).


The `jargon` build tool is a Mac OS X executable that comes with the Jargon SDK. The purpose of this tool is to automatically extract strings from the app’s Xcode project, normalize their format, and export them into a .jargon localization file. This file is bundled with the app’s Xcode project and will be bundled with the target iOS app. We recommend to run this tool in a build phase of the Xcode project, but it can also be run manually.


* Add `Jargon.framework` to your project.

* Copy the jargon binary into `/usr/local/bin/`, or wherever you like your executables to be, 

* In your project's Info.plist file, add the following keys/value pair: 
    * `JargonAppId` (Number): `%%pid%%`

* Run `/usr/local/bin/jargon setup -p <Project path> -k %%apik%%`

* In your AppDelegate, initialize Jargon: (see below for options)

```objc
#import <Jargon/Jargon.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{   
    [Jargon startWithAPIKey:@"%%apik%%" andOptions:<options>];
    //  ...
}
```
   
* Add a run script build phase to your project, with the following contents:

```bash
/usr/local/bin/jargon sync -p "${PROJECT_DIR}"
```

The build phase must be placed before "Compile Sources".


* In your target's Build Settings, in "Other Linker Flags", add `-all_load` if it's not already present.


* Create an empty file and name it `<base locale>.base.jargon`, add this file to the project and make sure it is included in the app's bundled resources.


## Options

The options parameter of the `startWithAPIKey:andOptions:` method is an `NSDictionary`. Here are the possible keys:

* `COOptionsDialogEnabled` (`NSNumber` `Boolean`, default: `NO`) Enables the Jargon actions panel, which lets users pull, edit and push strings from within the app.

* `COOptionsLoggingLevel` (`NSNumber` `COLoggingLevel`, default: `COLoggingLevelNone`) sets the level of console debug messages from the Jargon SDK.

    * `COLoggingLevelNone`
    * `COLoggingLevelError`
    * `COLoggingLevelWarn`
    * `COLoggingLevelInfo`
    * `COLoggingLevelDebug`
    * `COLoggingLevelVerbose`

* `COOptionsServingFrequency` (`NSNumber` `COServingFrequency`, default: `COServingNone`)
    * `COServingNone` Never downloads most recent strings. Strings packaged in the `<locale>.jargon` files will be used.
    * `COServingOnce` Downloads most recent strings the first time the app is launched.
    * `COServingDaily` Downloads most recent strings once a day when the app is launched.
    * `COServingWeekly` Downloads most recent strings once a week when the app is launched.


During your development and QA process, you can use the following options:

```objc
@{COOptionsDialogEnabled: @YES, COOptionsLoggingLevel: @(COLoggingLevelDebug)}
```

For your App Store builds, you can then use the following options:

```objc
@{COOptionsServingFrequency: @(COServingDaily)}
```


### Provide better context

Once you've gone through the integration process and built your app for the first time, you'll notice that the `<locale>.base.jargon` file that is now part of your project resources has been populated with all of your app's strings. Some of these strings may contain format specifiers (such as `%@` or `%.2f`), and you can see that these specifiers are followed by a tag in the `.base.jargon` file. By default, this tag will be `{{value}}`. You can change it to whatever makes more sense in the context of each particular string to make it easier for translators to understand what this placeholder stands for. Here are some examples:
    
* `"Today is %@{{date}}"`

* `"%ld{{number}} contacts found"`


