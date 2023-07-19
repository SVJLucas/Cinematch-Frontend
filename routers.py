import flet as ft
from screen import Screen
from pages.homepage import HomePage
from pages.main_page import MainPage
from pages.choices_page import ChoicesPage
from pages.tutorial_page import TutorialPage


class Router:

    def __init__(self):

        self.screen = None

    def connect_screen(self, screen: Screen):
        self.screen = screen
        page = self.screen.get_page()
        page.on_route_change = self.route_change

    def init_homepage(self):
        page = self.screen.get_page()

        home = HomePage(self.screen)

        hp = ft.View("/homepage", [home.build()])
        page.views.append(hp)

    def init_main_page(self):
        page = self.screen.get_page()

        second_page = MainPage(self.screen)

        page.views.append(ft.View("/main_page", [second_page.build()]))

    def init_tutorial_page(self):
        page = self.screen.get_page()

        second_page = TutorialPage(self.screen)

        page.views.append(ft.View("/tutorial_page", [second_page.build()]))

    def init_choices_page(self):
        page = self.screen.get_page()

        second_page = ChoicesPage(self.screen)

        page.views.append(ft.View("/choices_page", [second_page.build()]))

    def route_change(self, route):
        page = self.screen.get_page()

        page.views.clear()
        if page.route == "/homepage":
            self.init_homepage()

        if page.route == "/main_page":
            self.init_main_page()

        if page.route == "/tutorial_page":
            self.init_tutorial_page()

        if page.route == "/choices_page":
            self.init_choices_page()

    def rout_init(self, route: str):
        page = self.screen.get_page()
        page.route = route

        page.go(page.route)
