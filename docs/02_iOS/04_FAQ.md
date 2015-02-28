#### What operations are performed by the Colatris SDK when the app starts?


For end users, when the option `COOptionsDialogEnabled` isn't set, the following operations are performed by Colatris at launch time:

* The device locale is detected
* If no language files are stored on the device for this locale, one is downloaded synchronously from the Colatris CDN
* Strings are loaded from the file


If `COOptionsDialogEnabled` is set, some additional steps are taken.


This first network request is attempted synchronously the first time the app is launched in order to try and display strings in the user’s language from the very beginning, and thus avoid the bad experience of seeing the app switch languages after that. This happens only the first time the app is launched. The timeout delay for this request is very short (3 seconds). On subsequent launches, and after a configurable grace period, async calls are made to update these strings.



#### I'm noticing some discrepancies when using `hasPrefix:`, `hasSuffix:` or `length` on localized strings

When the option `COOptionsDialogEnabled` is set, the Colatris SDK adds some invisible characters to localized strings. This is so editable strings can be recognized in the UI when the edition dialog is being invoked. These characters won't be visible in the UI but will still be picked up by string matching, comparison and length methods. This may cause some unit tests to fail if they rely on these methods. 

We do not recommend relying on localized string comparison or matching in your unit tests, but if it is an absolute necessity, either of these solutions will fix the issue:

* Run tests with the option `COOptionsDialogEnabled` disabled.
* Use the provided `stringByRemovingColatrisCues` method contained in the `NSString+Colatris.h` category. This method returns the localized string without invisible characters.