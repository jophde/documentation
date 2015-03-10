Colatris documentation
=============

This repo will contain the marked down documentation for all Colatris components.

#### Editing

Please follow the current styleguide and refer to existing pages for inspiration.
The numbers on the elements correspond to their order in the menu.
Keep the exact format with '_'s.

Add any new files/folders to docs/contents.json

#### Deployment

Documentation is deployed through our static tier. To upload files to S3 get the following dependencies:

```bash
pip install boto
pip install fabric
```

Then `cd` to root of this repo and type the following command:

```bash
fab <ENV> upload_docs
```

Where `<ENV> = [stage, prod]`

Your files will be available at the url outputed by the script.

