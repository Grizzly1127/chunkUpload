#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.web
import os
import datetime
import subprocess
import sys

sys.path.append("../../")
import settings

class FileUploadHandler(tornado.web.RequestHandler):
    def post(self):
        upload_file = self.request.files['file']
        task_id = self.get_argument('guid')
        chunk = self.get_argument('chunk')
        file_name = '%s_%s' % (task_id, chunk)
        for meta in upload_file:
            settings.logger.info("FileUploadHandler uplaod : {0}".format(file_name))
            with open('./upload/%s' % file_name,'wb') as up:
                up.write(meta['body'])


class UploadSuccessHandler(tornado.web.RequestHandler):
    def get(self):
        task_id = self.get_argument('guid')
        ext = self.get_argument('ext')
        upload_type = self.get_argument('type')
        file_name = self.get_argument('name')
        settings.logger.info("task_id : {0}".format(task_id))
        settings.logger.info("next : {0}".format(ext))
        settings.logger.info("upload_type : {0}".format(upload_type))
        settings.logger.info("filename : {0}".format(file_name))
        if len(ext) == 0 and upload_type:
            ext = upload_type.split('/')[1]
        ext = '' if len(ext) == 0 else '.%s' % ext  # 构建文件后缀名
        chunk = 0
        with open('./upload/%s' % (file_name), 'wb') as target_file:  # 创建新文件
            while True:
                try:
                    file_name = './upload/%s_%d' % (task_id, chunk)
                    settings.logger.info("FileUploadHandler merge: {0}".format(file_name))
                    source_file = open(file_name, 'rb')  # 按序打开每个分片
                    target_file.write(source_file.read())  # 读取分片内容写入新文件
                    source_file.close()
                except IOError:
                    settings.logger.info("FileUploadHandler merge over.")
                    break
                chunk += 1
                os.remove(file_name)  # 删除该分片，节约空间
        self.render('home/index.html')