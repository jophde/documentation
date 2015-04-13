# Colatris-enabled in no time.

**Pre-requisite:** Strings in your code must be internationalized using the standard NSLocalizedString methods in order to be picked up by the Colatris SDK. Strings from Interface Builder files (Storyboards, NIBs, XIBs) will be picked up automatically.

* Add `pod 'Colatris'` to your Podfile and run `pod install`.

* In your project's Info.plist file, add the following keys/value pairs: 
    * `ColatrisAppId` (Number): `%%pid%%`
    * `ColatrisContentVersion` (Number): `%%pbuild%%`

* In your AppDelegate, initialize Colatris: (see below for options)

```objc
#import <Colatris/Colatris.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{   
    // your window creation code if you're not using a Storyboard
    // ...
    [Colatris startInWindow:self.window withAPIKey:@"%%apik%%" andOptions:@{COOptionsDialogEnabled: @YES, COOptionsLoggingLevel: @(COLoggingLevelDebug)}];
    //  ...
}
```

* After you build your app, the `<base locale>.base.colatris` file that was automatically created in your project should contain strings extracted from your project. You can now create a content version on Colatris with these strings. To do so, run the following command from your project root directory:

```bash
Pods/Colatris/colatris pushContent -p . -k %%apik%% [-d <description>]
```

Not using CocoaPods? Check out the [manual integration steps](/#/colatris/docs/02_iOS/02_Advanced)