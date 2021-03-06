## The Jargon App

If `jargon.manualMode` in your app's `build.gradle` is set to `true` all users will be able to press and hold with 3 fingers anywhere in your app.  If the Jargon app is not installed they will be sent to its Google Play Store listing to download it.  Once installed they can log into their Jargon account.  If you added them to your app's Jargon project they will be able edit text inside of your running application.  

## The Jargon Actions Panel

If the Jargon app is installed then 3 finger pressing anywhere in your app will open the Jargon App to your app's Jargon action panel.  

The available actions are:

* Edit project information
* Select locale
* Select string environment
* Get Latest Text
* Save My Changes

### Edit project information

This panel allows you to edit your project's name and logo.  It will also display messages such whether or not your app is installed on the phone or if the current app version is pushed.

### Select locale

This dropdown allows you to change the locale of your app *without* changing the system locale.  This is very useful for translators. After you change the locale be sure to click the *Get Latest Text* button and pull down the current set of translations for your project. 

### Select string environment

This dropdown allows you to switch between the working and productions strings.  Working strings are the strings on the translate tab of the Jargon dashboard. Production strings are strings you have published. 

### Get Latest Text

Gets the text for your app's version and the currently selected locale.  You will only need to get the text the first time you want to see a locale.  Subsequently the text will be saved.  However, it is good practice to pull frequently so that you are in sync with the rest of the team.

### Save My Changes

This button allows you send your translations back to the Jargon dashboard.  Jargon provides tools for merging your local text with the upstream project text.

### Publish App Version

If you didn't publish your app's strings for the version it was built for from the Gradle plugin you can do it from the Jargon app.  If the version was already published this part of the Jargon Actions Panel will be disabled.  You can also provide a description to easily identify the version on the Jargon Dashboard.

## Editing Strings

If you are logged into the Jargon app and added to an app's Jargon project you can edit text in the running application in context.  Simply get the latest text for a locale by pressing the "Get Latest Text" button in the Jargon Actions panel.  This has to be done at least once before text will be editable.  Afterwards, simply press and hold any piece of text app to edit it.  You can also press and hold with two fingers to edit all of the text on the screen at once. 