#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By KK Studio

from app.SaltAdmin import SaltAdmin

if __name__ == "__main__":
    app = SaltAdmin()
    #app.run() # Multi Processes Model
    import ipdb;ipdb.set_trace()
    app.run_single()
