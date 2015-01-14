## The Colatris actions panel

When the option `COEnableActions` is specified, users can open the Colatris actions panel using a special gesture, a 2-second long press with 4 fingers on a real device (2 fingers in the iOS simulator).


The available actions are:
* Log in to Colatris
* Pull strings for the current locale
* Choose between Working or Published strings

### Logging in

Logging in with a Colatris account will give users access to additional actions according to their role on the project. Once they log in, their credentials are saved in the keychain and loaded on subsequent app launches.


The additional actions available for translators are:
* Change locale
* Push translations
* Edit strings

And for project owners and admins:
* Change locale
* Push translations
* Push main locale strings
* Edit strings


### Pulling translations

Pulling translations will download all strings in the current selected locale for the current project build. It will overwrite any previously edited strings on the device for the selected locale.


### Changing locale

By default, the locale selected in the device's regional settings is used. Being logged in lets users select a different locale among the ones added to the project on the Colatris dashboard. 


Once a new locale is selected, the app will be immediately switched to that locale if strings are present on the device. The SDK will do its best to refresh the currently displayed strings, and any strings in views loaded after the change will be loaded directly in the new locale.


If the new locale has never been selected before on the device, the user should pull strings right after changing locale.

### Changing the Strings environment

* "Working" lets you pull, edit and push working strings. These are also editable in the Translations tab of the Colatris dashboard. 

* "Published" only lets you pull published strings.

### Pushing translations

Pushing translations will upload the strings that have been edited on the device to the Colatris backend. 


### Creating new content versions

For each new build of the app that contains new texts, an admin must create a new content version to add these new strings to the Colatris backend. Once they have been added, these new strings can be translated into other languages.

## Editing strings

Whenever a user is logged in to Colatris within the app, UI strings can be edited in context. A long press on the string brings up the edition popup. A long press on any view will bring up the edition popup for all the strings contained in subviews of this view.
