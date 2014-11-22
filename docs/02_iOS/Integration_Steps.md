This tutorial will run you through the Colatris integration process.

You will need:

1. Colatris.framework
2. colatris-build

### Colatris.framework

The framework is designed to require minimal changes to your app's code, and yet cover nearly app of the app's text. Strings declared in code, using `NSLocalizedString`, as well as strings types into Interface Builder are both supported.

### colatris-build

The build tool is a Mac OS X executable that comes with the Colatris SDK. The purpose of this tool is to automatically extract strings from the app’s Xcode project, normalize their format, and export them into a .colatris localization file. This file is bundled with the app’s Xcode project and will be bundled with the target iOS app. We recommend to run this tool in a build phase of the Xcode project, but it can also be run manually.

# Integration

1. Add `Colatris.framework` to your project.


2. In your AppDelegate, add `#import <Colatris/Colatris.h>` to your imports, and `[Colatris startInWindow:self.window withAppId:@"<pid>" andOptions:<options>];` right after your window creation code in the `application:didFinishLaunchingWithOptions:` method. Use the PID (Project Id) that was assigned to your app.
	
	
3. Copy colatris-build into `/usr/local/bin/`, or wherever you like your executables to be, and add a run script build phase to your project, with the following contents:
`/usr/local/bin/colatris-build "${PROJECT_DIR}"`
The build phase must be placed before "Compile Sources".


4. Create an empty file and name it `<base locale>.colatris`, add this file to the project and make sure it is included in the app's bundled resources.

## Options

The options parameter of the `startInWindow:withAppId:andOptions:` method is an integer bit mask that can be specified by combining the following options:

* `CONone` Logging is disabled and the Colatris actions panel is disabled. Will only let users see published strings in their phone's locale. Suitable for App Store builds.

* `COEnableActions` Enables the Colatris actions panel, which lets users pull, edit and push strings from within the app.

* `COEnableLogging` enables console debug messages from the Colatris SDK.

## Translator invitation

You can allow your users to sign up for Colatris and help translate your app. The method `[Colatris showTranslatorInvitationMessage];` opens a popup in your app that explains what Colatris does and includes an invitation request form. Simply insert this line in your code wherever you see fit.

