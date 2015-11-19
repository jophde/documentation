# Jargon-enabled in no time.

* Add `pod 'Jargon'` to your Podfile and run `pod install`.

* In your project's Info.plist file, add the following keys/value pair: 
    * `JargonAppId` (String): `%%pid%%`
    
* Run `Pods/Jargon/jargon setup -p . -k %%apik%%`

* Check that a <locale>.base.jargon was created in your project, typically in the Supporting Files group. If it's not the case please follow the [manual integration steps](/#/jargon/docs/02_iOS/02_Advanced).

* In your AppDelegate, initialize Jargon:

```objc
#import <Jargon/Jargon.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{   
    [Jargon startWithAPIKey:@"%%apik%%" andOptions:@{JNOptionsDialogEnabled: @YES, JNOptionsLoggingLevel: @(JNLoggingLevelDebug)}];
    //  ...
}
```

Not using CocoaPods? Check out the [manual integration steps](/#/jargon/docs/02_iOS/02_Advanced)


[How to use Jargon in your app](/#/jargon/docs/02_iOS/03_Usage)