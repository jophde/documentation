## The Jargon actions panel

When the option `COEnableActions` is specified, users can open the Jargon actions panel using a special gesture, a 2-second long press with 3 fingers on a real device (2 fingers in the iOS simulator).


The available actions are:

* Log in to Jargon
* Get latest strings for the current locale
* Choose between Working or Published strings

### Logging in

Logging in with a Jargon account will give users access to additional actions:

* Change locale
* Save translations
* Edit strings


Once they log in, their credentials are saved in the keychain and loaded on subsequent app launches.


### Getting latest translations

Getting latest translations will download all strings in the current selected locale for the current project build. It will overwrite any previously edited strings on the device for the selected locale.


### Changing locale

By default, the locale selected in the device's regional settings is used. Logging in allows users to select a different locale among the ones added to the project on the Jargon dashboard. 


Once a new locale is selected, the app will be immediately switched to that locale if strings are present on the device. The SDK will do its best to refresh the currently displayed strings, and any strings in views loaded after the change will be loaded directly in the new locale.


If the new locale has never been selected before on the device, the user must pull strings right after changing locale.

### Changing the Strings environment

* _Working_ lets you pull, edit and push working strings. These are also editable in the _Translate_ page of the Jargon dashboard. 

* _Published_ only lets you pull published strings.

### Saving translations

Saving translations will upload the strings that have been edited on the device to the Jargon backend. 


## Editing strings

Whenever a user is logged in to Jargon within the app, UI strings can be edited in context. A long press on the string brings up the edition popup. A long press on any view will bring up the edition popup for all the strings contained in subviews of this view.

Strings can also be marked as Reviewed or Rejected from the edition popup.


