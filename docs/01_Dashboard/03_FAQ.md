#### Q: I created a Project, the translation tab is empty. What's next?

A: Once you create a Project you need upload your app's English strings to start the translation process. To achieve that you need to add a new content version (what the heck is a content version? see answer below).
You can do this in one of two ways:
 * Through the command line (see  the [Command Line Utility](https://dashboard.usejargon.com/#/jargon/docs/02_iOS/03_The_command_line_utility) page)
 * Through the dashboard by clicking the '+ Content version' button in the navigation bar of the Translate tab.
You will need to choose a file containing your English strings (.strings || .xml || || .json)

#### Q: What is a Content version?

A: Content versions are used to track your app's copy changes. Each content version is tied to your app's build number so you have an easy reference. 
Adding a new content version to your project basically means uploading the English strings that exist in your app.
This way, if your build only contains code changes and copy is untouched - it won't pollute your localization dashboard. You have explicit control over your app's copy versioning. 

#### Q: Ok I can see my English strings how do I get translations?

A: This is where Jargon really shines. All you need to do is go to the Home tab and click the Translate now button. 
Depending on the type of translations you chose it will take anywhere from a few seconds to 48 hours until you see the translations.
You can always track your requests in the Jobs tab. Read more in [Home](https://dashboard.usejargon.com/#/jargon/docs/01_Dashboard/03_Home).

#### Q: My app contains many placeholder strings that won't appear in the UI, but I can see them in the Jargon dashboard. How do I prevent these from being translated?

A: If you're the owner or an admin in the project, go to the _Manage_ page of the Jargon dashboard. From there you can select multiple strings and then press _Mark selected as 'Do not translate'_. Translators will ignore these strings, and they won't be included in the published strings.