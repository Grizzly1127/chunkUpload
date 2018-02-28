#!/usr/bin/env python
# encoding: utf-8

__all__ = ['urls_pattern']

from handlers.home.index import IndexHandler
from handlers.home.upload import FileUploadHandler, UploadSuccessHandler

urls_pattern = [
    ('/', IndexHandler),
    ('/fileupload', FileUploadHandler),
    ('/uploadsuccess', UploadSuccessHandler)
]