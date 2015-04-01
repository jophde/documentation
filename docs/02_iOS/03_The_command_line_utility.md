If you have installed the Colatris SDK using CocoaPods, the command line utility is located in the `Pods/Colatris` directory of your project. You can run commands from that folder or copy the utility to a folder contained in your `PATH`.


If you have installed the Colatris SDK manually, the colatris command line tool is included in [the package](https://github.com/colatris/colatris-ios-sdk/archive/master.zip) you've downloaded.


## Commands

#### Extract


    colatris extract -p <project path>

Extract project strings into a `<locale>.base.colatris` file.

#### Push Content


    colatris pushContent -p <project path> -k <project API key> [-d <description>]

Create a new content version for the project on the Colatris backend with the strings contained in the project's `<locale>.base.colatris` file.
Admins and project owners can view the project's API key on the Colatris dashboard in _Home > Project info_.

#### Pull Content


    colatris pullContent -p <project path> -k <project API key> [-l <locale>]

Pull latest strings for the app’s content version into the project’s `<locale>.colatris` file. Pull base locale if no locale is specified.
Admins and project owners can view the project's API key on the Colatris dashboard in _Home > Project info_.

#### Version

	colatris version

Display the version of the CLI tool.