# -*- coding: utf-8 -*-

from selenium import webdriver

from .constants import GAMES_URL


class Webdriver(object):
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_lottery_game_webpage(self, game):
        try:
            self.driver.get(GAMES_URL[game])
        except AttributeError as e:
            raise Warning('Incorrect Game Name!')
