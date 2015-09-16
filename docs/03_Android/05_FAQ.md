### How will integrating Jargon effect my app?

Jargon has two modes.  Production Serving and Editor Mode.  Both of these modes can be on at the same time.  

If Production Serving mode is on, all users of your app will have their strings synced in the background. The sync interval is configurable.  Once it happens, Jargon' internal storage will be updated.  The next time the user launches the app they will see the updated text with your translations.  

If Editor Mode is on Jargon will add a secret gesture to your app.  Any user will be able to 3 finger press and hold in your app.  If the Jargon app isn't installed they will be taken to the Play Store to download it.  If they make a Jargon account and you add them to your app's project they can get the Jargon app, log in, and start making translations.  Jargon will do nothing but add the gesture if there isn't a user logged into the Jargon app with permissions for your project.  

###  How fast is the Jargon string lookup?  

Yes, Jargon bypasses the stock Android Resource system. However, in our testing the performance difference is marginal.  Jargon makes use of the NDK to provide blazing fast string storage.  You can rest assured that app performance will not be affected.  

###  How much memory does Jargon use?

Jargon uses almost no memory.  Because of it's blazing fast string storage it doesn't need to store strings in memory so that they can be looked up on the UI thread.

### I am scared of the Dalvik method limit. How many does Jargon have?

Most of the logic for Jargon is in the Jargon App not the Jargon SDK.  Because of Android IPC we were able to offload much of the work from the runtime.  Our SDK is very and has less than a thousand methods.  Rest assured, Jargon is not like Google Play Services ;).

###  Will Jargon hurt the battery usage of my app?

No.  Jargon only syncs on an interval and in the background.  It is not constantly making network requests.

###  Can I have my regular users translate my app?

Yes!  Simply ask them to make a Jargon account and add them to your project.  They will then be able to get the Jargon app, login, and start translating in-context.


### Can Jargon really handle all of the text in my app?

Yes! Jargon can handle FORMAT strings, strings with HTML in them, arrays, and even plurals.  Everything you can do with the regular Android Resource system you can do with Jargon.

### Will Jargon strings appear in the Android Layout Editor.

Yes!  Simply pull down the current state of your text with the Jargon Gradle plugin and you will see your translations in the layout editor.  Jargon works with the Android resource system, not against it.  

### Why localize my app?

Jargon makes localization not suck.  Localization is a tried and true method to acquire more users.  In addition it's just the right thing to do.  All of your users deserve to have a quality product. 

### Does implementing Jargon really take 10 minutes and only requires one line of Java?

Yes!  Unless you don't get Gradle.  The Java is probably more readable as 3 lines but it will compile as one ;).
