If you have installed the Colatris SDK using CocoaPods, the command line utility is located in the `Pods/Colatris` directory of your project. You can run commands from that folder or copy the utility to a folder contained in your `PATH`.


If you have installed the Colatris SDK manually, the colatris command line tool is included in [the package](https://github.com/colatris/colatris-ios-sdk/archive/master.zip) you've downloaded.


## Commands

#### Extract

```bash
colatris extract -p <project path>
```
Extract project strings into a `<locale>.colatris` file.

#### Push Content

```bash
colatris pushContent -p <project path> -k <API Key> [-d <description>]
```
Create a new content version for the project on the Colatris backend with the strings contained in the project's `<locale>.colatris` file. The API Key can be found in the Colatris dashboard in Home > Project Info.

#### Pull Content

```bash
colatris pullContent -p <project path>
```
Pull latest strings for the app’s content version into the project’s `<locale>.colatris` file.