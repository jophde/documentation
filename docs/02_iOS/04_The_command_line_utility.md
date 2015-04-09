If you have installed the Colatris SDK using CocoaPods, the command line utility is located in the `Pods/Colatris` directory of your project. You can run commands from that folder or copy the utility to a folder contained in your `PATH`.


If you have installed the Colatris SDK manually, the colatris command line tool is included in [the package](https://github.com/colatris/colatris-ios-sdk/archive/master.zip) you've downloaded.


## Commands

#### Extract


    colatris extract -p <Project path> [-f YES]

Extract project strings into a `<locale>.base.colatris` file.

* Use the _force_ (-f YES) option to clear all changes you've made to the `<locale>.base.colatris` file and reload all strings from your project.

#### Push Content


    colatris pushContent -p <Project path> -k %%apik%% [-d <Description>] [-pid %%pid%% -cv %%pbuild%%]

Create a new content version for the project on the Colatris backend with the strings contained in the project's `<locale>.base.colatris` file.

* Use both the -pid and -cv options to specify your project ID and content version manually if those can't be found in the project's `Info.plist` file or if your project contains multiple `Info.plist` files.

#### Pull Content


    colatris pullContent -p <Project path> -k %%apik%% [-l <Locale>] [-pid %%pid%% -cv %%pbuild%%]

Pull latest strings for the app’s content version into the project’s `<locale>.colatris` file. Pull base locale if no locale is specified.

* Use both the -pid and -cv options to specify your project ID and content version manually if those can't be found in the project's `Info.plist` file or if your project contains multiple `Info.plist` files.

#### Version

	colatris version

Display the version of the CLI tool.
