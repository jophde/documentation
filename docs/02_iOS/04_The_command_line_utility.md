If you have installed the Colatris SDK using CocoaPods, the command line utility is located in the `Pods/Colatris` directory of your project. You can run commands from that folder or copy the utility to a folder contained in your `PATH`.


If you have installed the Colatris SDK manually, the colatris command line tool is included in [the package](https://github.com/colatris/colatris-ios-sdk/archive/master.zip) you've downloaded.


## Commands

#### Setup

	colatris setup -p <Project path> -k %%apik%%

Sets up auto push for the project on this computer, and saves the API key locally so you don't need to specify it for subsequent commands.


#### Extract


    colatris extract -p <Project path>

Extract project strings into a `<locale>.base.colatris` file.


#### Push Content


    colatris pushContent -p <Project path> [-k %%apik%%] [-d <Description>] [-pid %%pid%% -cv %%pbuild%%]

Create a new content version for the project on the Colatris backend with the strings contained in the project's `<locale>.base.colatris` file.

* If you have run `colatris setup` for this project on this computer in the past, you don't need to specify the API token with the `-k` parameter.
* Use both the -pid and -cv options to specify your project ID and app version manually if those can't be found in the project's `Info.plist` file or if your project contains multiple `Info.plist` files.

#### Pull Content


    colatris pullContent -p <Project path> -k %%apik%% [-l <Locale>] [-pid %%pid%% -cv %%pbuild%%]

Pull latest strings for the app’s content version into the project’s `<locale>.colatris` file. Pull base locale if no locale is specified.

* If you have run `colatris setup` for this project on this computer in the past, you don't need to specify the API token with the `-k` parameter.
* Use both the -pid and -cv options to specify your project ID and app version manually if those can't be found in the project's `Info.plist` file or if your project contains multiple `Info.plist` files.

#### Version

	colatris version

Display the version of the CLI tool.
