from fabric.api             import *
from fabric.contrib.files   import exists, contains, append
from fabric.api             import settings

from boto.s3.key            import Key
import boto
import os

#constants
ENVIRONMENT             = None
S3_BUCKET_NAME          = None
SOURCE_DIR              = 'docs/'
DEST_DIR                = 'assets/docs/'
URL                     = None

@task
def prod():
    global ENVIRONMENT
    global S3_BUCKET_NAME
    global URL
    ENVIRONMENT     = 'prod'
    S3_BUCKET_NAME  = 'co-static-preview'
    URL             = 'https://pstatic01.colatris.com/'

@task
def stage():
    global ENVIRONMENT
    global S3_BUCKET_NAME
    global URL
    ENVIRONMENT     = 'stage'
    S3_BUCKET_NAME  = 'co-static-stage'
    URL             = 'https://s3-us-west-1.amazonaws.com/co-static-stage/'

@task
def dev():
    global ENVIRONMENT
    global S3_BUCKET_NAME
    global URL
    ENVIRONMENT     = 'dev'
    S3_BUCKET_NAME  = 'co-static-dev'
    URL             = 'https://s3-us-west-1.amazonaws.com/co-static-dev/'

@task
def upload_docs():
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_SECRET)
    bucket = conn.get_bucket(S3_BUCKET_NAME)

    #get names of files from directory
    file_paths = []
    for (source_dir, dname, fnames) in os.walk(SOURCE_DIR):
        for fname in fnames:
            file_paths.append(source_dir + '/' + fname)

    for path in file_paths:
        dest_path = os.path.join(DEST_DIR + path.replace(SOURCE_DIR, ''))
        print 'Uploading %s to S3 bucket %s at %s' % \
        (path, S3_BUCKET_NAME, dest_path)

        k = boto.s3.key.Key(bucket)
        k.key = dest_path
        k.set_contents_from_filename(path)
        print('Done')

    print('---------------------')
    print('UPLOAD:          [OK]')
    print('Files available at %s' % URL + DEST_DIR)
