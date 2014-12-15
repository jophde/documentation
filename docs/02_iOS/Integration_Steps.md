This tutorial will run you through the Colatris integration process.

# Using CocoaPods

1. Add `pod 'Colatris'` to your Podfile and run `pod install`.


2. In your target's Info.plist file, find the following keys and insert the correct values:
	* `ColatrisAppId` (String): Your app's PID as found in the Colatris dashboard.
	* `ColatrisContentVersion` (Number): The content version corresponding to your build.


3. In your AppDelegate, add `#import <Colatris/Colatris.h>` to your imports, and `[Colatris startInWindow:self.window withOptions:<options>];` right after your window creation code in the `application:didFinishLaunchingWithOptions:` method. See below for options.


# Manual installation

You will need:

1. Colatris.framework
2. colatris-build


Download a .zip of both [here](https://github.com/colatris/colatris-ios-sdk/archive/master.zip).


The `colatris-build` build tool is a Mac OS X executable that comes with the Colatris SDK. The purpose of this tool is to automatically extract strings from the app’s Xcode project, normalize their format, and export them into a .colatris localization file. This file is bundled with the app’s Xcode project and will be bundled with the target iOS app. We recommend to run this tool in a build phase of the Xcode project, but it can also be run manually.


1. Add `Colatris.framework` to your project.


2. In your target's Info.plist file, add the following keys:
	* `ColatrisAppId` (String): Your app's PID as found in the Colatris dashboard.
	* `ColatrisContentVersion` (Number): The content version corresponding to your build.


3. In your AppDelegate, add `#import <Colatris/Colatris.h>` to your imports, and `[Colatris startInWindow:self.window withOptions:<options>];` right after your window creation code in the `application:didFinishLaunchingWithOptions:` method. See below for options.
	
	
4. Copy colatris-build into `/usr/local/bin/`, or wherever you like your executables to be, and add a run script build phase to your project, with the following contents:
`/usr/local/bin/colatris-build "${PROJECT_DIR}"`
The build phase must be placed before "Compile Sources".


5. Create an empty file and name it `<base locale>.colatris`, add this file to the project and make sure it is included in the app's bundled resources.

# Options

The options parameter of the `startInWindow:withOptions:` method is an NSDictionary. Here are the possible keys:

* `COOptionsDialogEnabled` (NSNumber Boolean, default: `NO`) Enables the Colatris actions panel, which lets users pull, edit and push strings from within the app.

* `COOptionsLoggingLevel` (NSNumber COLoggingLevel, default: `COLoggingLevelNone`) sets the level of console debug messages from the Colatris SDK.
	* `COLoggingLevelNone`
	* `COLoggingLevelError`
	* `COLoggingLevelWarn`
	* `COLoggingLevelInfo`
	* `COLoggingLevelDebug`
	* `COLoggingLevelVerbose`

* `COOptionsServingFrequency` (NSNumber COServingFrequency, default: `COServingNone`)
	* `COServingNone` Never downloads most recent strings. Strings packaged in the `<locale>.colatris` file will be used.
	* `COServingOnce` Downloads most recent strings the first time the app is launched.
	* `COServingDaily` Downloads most recent strings once a day when the app is launched.
	* `COServingWeekly` Downloads most recent strings once a week when the app is launched.


During your development and QA process, you can use the following options:

```objc
@{COOptionsDialogEnabled: @YES, COOptionsLoggingLevel: @(COLoggingLevelDebug)}
```

For your App Store builds, you can then use the following option:

```objc
@{COOptionsServingFrequency: @(COServingDaily)}
```


# Provide better context

Once you've gone through the integration process and built your app for the first time, you'll notice that the `<locale>.colatris` file that is now part of your project resources has been populated with all of your app's strings. Some of these strings may contain format specifiers (such as `%@` or `%.2f`), and you can see that these specifiers are followed by a tag in the `.colatris` file. By default, this tag will be `{{value}}`. You can change it to whatever makes more sense in the context of each particular string to make it easier for translators to understand what this placeholder stands for. Here are some examples:
	
* `"Today is %@{{date}}"`

* `"%ld{{number}} contacts found"`


# Translator invitation

You can allow your users to sign up for Colatris and help translate your app. The method `[Colatris showTranslatorInvitationMessage];` opens a popup in your app that explains what Colatris does and includes an invitation request form. Simply insert this line in your code wherever you see fit.

