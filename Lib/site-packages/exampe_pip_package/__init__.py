#!/usr/bin/env python
# -*- coding: utf-8 -*-

class pip_test(object):
    def __init__(self):
        self.name = "exampe_pip_package"

    def get_info(self):
        print("Hello, this is just a pip package example.")
        print("Package name is %s." % self.name)

