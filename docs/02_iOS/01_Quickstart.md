# Colatris-enabled in no time.

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
    [Colatris startInWindow:self.window withAPIKey:<api key> andOptions:@{COOptionsDialogEnabled: @YES, COOptionsLoggingLevel: @(COLoggingLevelDebug)}];
    //  ...
}
```

Admins and project owners can view the project's API key on the Colatris dashboard in _Home > Project info_.

* After you build your app, the `<base locale>.base.colatris` file that was automatically created in your project should contain strings extracted from your project. You can now create a content version on Colatris with these strings. To do so, run the following command from your project root directory, using the project API key displayed on the Colatris dashboard in _Home > Project info_:

```bash
Pods/Colatris/colatris pushContent -p <project path> -k <project API key> [-d <description>]
```

Not using CocoaPods? Check out the [manual integration steps]('/#/colatris/docs/02_iOS/02_Integration_steps')