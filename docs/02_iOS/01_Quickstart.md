# Colatris-enabled in no time.

* Add `pod 'Colatris'` to your Podfile and run `pod install`.

* In your project's Info.plist file, add the following keys/value pair: 
    * `ColatrisAppId` (String): `%%pid%%`
    
* Run `Pods/Colatris/colatris setup -p . -k %%apik%%`

* In your AppDelegate, initialize Colatris:

```objc
#import <Colatris/Colatris.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{   
    [Colatris startWithAPIKey:@"%%apik%%" andOptions:@{COOptionsDialogEnabled: @YES, COOptionsLoggingLevel: @(COLoggingLevelDebug)}];
    //  ...
}
```

Not using CocoaPods? Check out the [manual integration steps](/#/colatris/docs/02_iOS/02_Advanced)