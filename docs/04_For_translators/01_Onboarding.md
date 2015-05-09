## Translator onboarding

This page will onboard a translator into working with a Jargon-enabled app

### Registration

In order to start translating/QA-ing a customer's mobile app, a new translator needs to complete the following steps:

* Go to the Jargon [sign-up page](https://dashboard-preview.colatris.com/user/sign-in).
* Fill out the fields in the _Register_ column on the right. (If one of the languages you speak is not in the list, you can add it later)
* Make note of the e-mail address you used during registration.
* Press _Register_.
* Check your e-mail and click on the confirmation link.
* Log-in with your new credentials.

You will land on the _Home_ page, which might be initially empty. Now that you have a Jargon account you need to provide the e-mail you used during registration to your translation manager/admin so they can add you to the relevant projects.

### Using the Dashboard

Once you've been added to some projects, click on one of them in the _Projects_ dropdown.

Here on the dashboard you will most likely submit/upload the first batch of translations completed on your native translation environment/software. All the translations that are uploaded to Jargon are accessible via the _Translate page_.

### Translate page

At the top of the page you can see three blue buttons. On the right drop-down button you can select which language to work on. 

#### Main grid

Below these buttons is the main translation grid. It shows the original string on the left, and the translation for the chosen language on the right. 

You can search the set of strings using the search bar on the top, sort the strings using the Sort dropdown at the top left, or filter by a one or several string statuses with the Filter dropdown.

The leftmost part of the grid might contain a Checkmark icon, which means a translation has been submitted for that string. 

You can select a given string by clicking on the row. This will expose an info panel on the right, which shows the original strings on top, and the translation underneath, which you can edit. 


#### Uploading translations

In order to upload a set of translations for a given language, press the _Upload translations_ button at the top right of the page.

* Chose which locale the upload is for
* Chose which Content version this upload is for. The customer's app has different versions. This is there to make sure you are uploading translations for the correct version. You will most likely want to upload for the most recent version in which English is available.
* Select the file from your file system
* Press upload

#### Submitting translations from the dashboard

You can change the uploaded translations right from the dashboard. 

* Just click on the desired English string in the list, and enter the new translation in the input field on the right panel. 
* On the top of the page press the _Save_ button.


Now that an initial set of translations has been uploaded you can check and review them directly inside the customer's application.

### Using the mobile SDK

Ask your translation manager/admin to give you a build of the customer's application (with the Jargon SDK integrated). You might need to provide an e-mail address.

Once you have the app installed on your phone, you have all components needed to start reviewing. 

#### Accessing the Jargon dialogue

Launch the customer application. On any page of the app, press and hold 3 fingers on the screen for 3 seconds, or until the Jargon dialogue pops up.

Via this dialogue you can control which language you want to see the customer's application in, pull down select versions of copy, and even submit translations/edits. 

Unauthenticated users can only pull down select versions of copy. To make edits and submit changes in the app, it is necessary to authenticate yourself via the dialogue. To do so:

* First press _Log in_.
* Enter your credentials created during step 1

Once you do that, you should see your personal information in the dialogue and should now be able to submit changes.

#### Reviewing the customer's app in many languages.

In order to see the translations you (or others) uploaded to the dashboard, follow these steps:

* On the Jargon dialogue find the _Translation_ group of buttons.
* Press the _Locale_ field and select which language you want to review.
* Make sure the _Strings environment_ is set to _Working_.
* Press the _Get Latest Text_ button
* Close the dialogue 

You should now see the application in the requested language. To switch languages, repeat the process.

#### Editing translations in the app

As you go through the app, you have the option to submit and correct translations. 

* Press on a string element in the app until the Jargon Edit Dialogue pops up.
* In the provided input field, enter the new translation.
* Repeat for n strings.

Note that you may have to swipe between strings in the Edit Dialogue to find the particular text you are looking to make changes to. Also, if you experience problems with in-app editing, then please feel free to make edits in the dashboard, save said changes, and then pull down the latest copy via the Jargon dialogue (aforementioned process) to review in-app. 

#### Saving your work/edits

When you are done with corrections and want to save your work, press and hold 3 fingers on the screen until the Jargon main dialogue pops up.

* Make sure the locale is set correctly.
* Pressing _Save My Changes_ will save all the strings you edited on your phone since the last _Pull_ to the Jargon servers. 

Attention: This is a destructive action and will overwrite existing translations on the Dashboard.

After you pushed from the phone, you should see the changes in the _Translate_ page on the dashboard. Simply search for the string you are looking for. 

For example, if you just changed the English string _Sign up_ in French, type in _Sign up_ in the search bar of the main grid and find your submitted French string.

### Download and publish (for Project admins only)

Once you are done with your edits and want to port changes into the translation medium of your choice, you can download your work in a commonly accepted format. 

* Log into the Jargon dashboard.
* Click on the _Manage_ page in the top navigation bar.
* Choose a language.
* Press _Download all_ in the right pane.
* Choose a format using the dropdown at the top.
* Press _Download_

This will download the latest build file in the chosen language and format.

### Bugs and suggestions

While using the Jargon dashboard please keep in mind that some features are WIP. We ship updates every week and would love to hear your suggestions and bug reports.

Feel free to e-mail [bugs@colatris.com](mailto:bugs@colatris.com) to report a bug or make feature requests.



