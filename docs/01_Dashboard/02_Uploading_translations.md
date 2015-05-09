## Uploading files

You have the option to upload translation and string files via the _Translate_ page of the Jargon dashboard.

This will let you:

* Add already completed translations to your project so you can review them in context and publish
* Upload a set of strings to be translated

File uploads are submitted in two common formats.

### _*.strings_ for iOS

You can upload _.strings_ file from your Xcode project onto the dashboard. 
Our parser supports both inline `//` and star `/* */` comments.

String IDs (SID) are only allowed to contain the following characters: alphanumeric, `_`, `-`, `.`

Sample formatting:

![alt text](/images/docs/ios_sample.png ".strings example")

### _*.xml_ for Android

_.xml_ is the standard for externalized resources in Android development. 
String IDs (SID) are only allowed to contain the following characters: alphanumeric, `_`, `-`, `.`

For strings, your uploads need to match this sample document structure:

![alt text](/images/docs/xml_sample.png ".xml example")
