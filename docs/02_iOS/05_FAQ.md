### What operations are performed by the Jargon SDK when the app starts?

For end users, when the option `JNOptionsDialogEnabled` isn't set, the following operations are performed by Jargon at launch time:

* The device locale is detected
* If no language files are stored on the device for this locale, one is downloaded synchronously from the Jargon CDN
* Strings are loaded from the file


If `JNOptionsDialogEnabled` is set, some additional steps are taken.


This first network request is attempted synchronously the first time the app is launched in order to try and display strings in the user’s language from the very beginning, and thus avoid the bad experience of seeing the app switch languages after that. This happens only the first time the app is launched. The timeout delay for this request is very short (3 seconds). On subsequent launches, and after a configurable grace period, async calls are made to update these strings.



### A network request on the main thread? Isn't that a crime?

It is true that you should never make a synchronous network request on the UI thread. That would make the UI freeze and you’d get a terrible user experience. This is __not__ what the Jargon SDK does. 


With Jargon, you’re packaging strings some languages in your shipping app, but your app may support more languages than these. You can add more languages from the Jargon dashboard. For these other languages, strings files have to be downloaded at runtime. So the first time the app is launched, Jargon detects the user’s language, and downloads the corresponding strings file to the device. It is primordial that this operation happens __before any UI is displayed__, otherwise what language would that UI be displayed in? 


That’s why this first network request is made synchronously. And because it is called from the `application: didFinishLaunchingWithOptions:` method, it occurs while your app’s loading screen is still displayed, and before any UI is displayed. This results in a slightly longer load time the first time your app is launched. That’s a way more desirable user experience than displaying the app in the wrong language the first time, and switching to the right one after that, which would be confusing at best. 


This network request has a very short timeout delay (3 seconds). This means that if the right language file can’t be downloaded fast enough, the app will load using packaged strings in your development language. The request is then attempted again asynchronously with a longer timeout delay. So in that case, the app will be displayed in the wrong language the first time. But since strings files are so small and are hosted on a first rate Content Delivery Network, this should not happen very often, only when users have very bad or no internet access.  


Note that the timeout delay for this synchronous network request is configurable. If you don’t think 3 seconds is the right value, you can set a `syncTimeout` option in the Options dict of Jargon' `startWithAPIKey: andOptions:` method, with an `NSNumber` value in seconds. However, we do not recommend you set a long timeout delay, because iOS will make your app terminate should it take too long to start. 


To avoid this synchronous network request altogether, you can package strings for all your locales in your shipping app. This can be done using the pullContent command of the command line tool.


### I'm noticing some discrepancies when using `hasPrefix:`, `hasSuffix:` or `length` on localized strings

When the option `JNOptionsDialogEnabled` is set, the Jargon SDK adds some invisible characters to localized strings. This is so editable strings can be recognized in the UI when the edition dialog is being invoked. These characters won't be visible in the UI but will still be picked up by string matching, comparison and length methods. This may cause some unit tests to fail if they rely on these methods. 

We do not recommend relying on localized string comparison or matching in your unit tests, but if it is an absolute necessity, running tests with the option `JNOptionsDialogEnabled` disabled will fix the issue.

