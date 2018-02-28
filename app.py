#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options
from settings import settings,url_handlers,logger

define("port", default=5000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self, handlers, **settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        
application = Application(url_handlers, **settings)
if __name__ == "__main__":
    logger.info("start uplaod web!")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port, address="0.0.0.0")
    tornado.ioloop.IOLoop.instance().start()