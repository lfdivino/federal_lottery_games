# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Webdriver(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
