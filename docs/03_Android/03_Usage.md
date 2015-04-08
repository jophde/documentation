## The Colatris App

If `colatris.manualMode` in your app's `build.gradle` is set to `true` all users will be able to press and hold with 3 fingers anywhere in your app.  If the Colatris app is not installed they will be sent to its Google Play Store listing to download it.  Once installed they can log into their Colatris account.  If you added them to your app's Colatris project they will be able edit text inside of your running application.  

## The Colatris Actions Panel

If the Colatris app is installed then 3 finger pressing anywhere in your app will open the Colatris App to your app's Colatris action panel.  

The available actions are:

* Edit project information
* Select locale
* Select string environment
* Get Latest Text
* Save My Changes
* Publish Content Version

### Edit project information

This panel allows you to edit your project's name and logo.  It will also display messages such whether or not your app is installed on the phone or if the current content version is pushed.

### Select locale

This dropdown allows you to change the locale of your app *without* changing the system locale.  This is very useful for translators. After you change the locale be sure to click the *Get Latest Text* button and pull down the current set of translations for your project. 

### Select string environment

This dropdown allows you to switch between the working and productions strings.  Working strings are the strings on the translate tab of the Colatris dashboard. Production strings are strings you have published. 

### Get Latest Text

Gets the text for your app's Colatris Content Version and the currently selected locale.  You will only need to get the text the first time you want to see a locale.  Subsequently the text will be saved.  However, it is good practice to pull frequently so that you are in sync with the rest of the team.

### Save My Changes

This button allows you send your translations back to the Colatris dashboard.  Colatris provides tools for merging your local text with the upstream project text.

### Publish Content Version

If you didn't publish your app's strings for the Content Version it was built for from the Gradle plugin you can do it from the Colatris app.  If the Content Version was already published this part of the Colatris Actions Panel will be disabled.  You can also provide a description to easily identify the Content Version on the Colatris Dashboard.

## Editing Strings

If you are logged into the Colatris app and added to an app's Colatris project you can edit text in the running application in context.  Simply get the latest text for a locale by pressing the button the Colatris Actions panel.  This has to be done at least once before text will be editable.  Afterwards simply press and hold any piece of text app to edit it.  You can also press and hold with two fingers to edit all of the text on the screen at once. 