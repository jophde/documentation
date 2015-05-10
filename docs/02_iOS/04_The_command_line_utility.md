If you have installed the Jargon SDK using CocoaPods, the command line utility is located in the `Pods/Jargon` directory of your project. You can run commands from that folder or copy the utility to a folder contained in your `PATH`.


If you have installed the Jargon SDK manually, the jargon command line tool is included in [the package](https://github.com/colatris/jargon-ios-sdk/archive/master.zip) you've downloaded.


## Commands

#### Setup

	jargon setup -p <Project path> -k %%apik%%

Sets up auto push for the project on this computer, and saves the API key locally so you don't need to specify it for subsequent commands.


#### Extract


    jargon extract -p <Project path>

Extract project strings into a `<locale>.base.jargon` file.


#### Push Content


    jargon pushContent -p <Project path> [-k %%apik%%] [-d <Description>] [-pid %%pid%% -cv %%pbuild%%]

Create a new content version for the project on the Jargon backend with the strings contained in the project's `<locale>.base.jargon` file.

* If you have run `jargon setup` for this project on this computer in the past, you don't need to specify the API token with the `-k` parameter.
* Use both the -pid and -cv options to specify your project ID and app version manually if those can't be found in the project's `Info.plist` file or if your project contains multiple `Info.plist` files.

#### Pull Content


    jargon pullContent -p <Project path> -k %%apik%% [-l <Locale>] [-pid %%pid%% -cv %%pbuild%%]

Pull latest strings for the app’s content version into the project’s `<locale>.jargon` file. Pull base locale if no locale is specified.

* If you have run `jargon setup` for this project on this computer in the past, you don't need to specify the API token with the `-k` parameter.
* Use both the -pid and -cv options to specify your project ID and app version manually if those can't be found in the project's `Info.plist` file or if your project contains multiple `Info.plist` files.

#### Version

	jargon version

Display the version of the CLI tool.
