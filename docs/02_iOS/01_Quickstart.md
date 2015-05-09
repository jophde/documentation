# Jargon-enabled in no time.

* Add `pod 'Jargon'` to your Podfile and run `pod install`.

* In your project's Info.plist file, add the following keys/value pair: 
    * `JargonAppId` (String): `%%pid%%`
    
* Run `Pods/Jargon/jargon setup -p . -k %%apik%%`

* In your AppDelegate, initialize Jargon:

```objc
#import <Jargon/Jargon.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{   
    [Jargon startWithAPIKey:@"%%apik%%" andOptions:@{COOptionsDialogEnabled: @YES, COOptionsLoggingLevel: @(COLoggingLevelDebug)}];
    //  ...
}
```

Not using CocoaPods? Check out the [manual integration steps](/#/colatris/docs/02_iOS/02_Advanced)