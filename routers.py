import flet as ft
from screen import Screen
from pages.homepage import HomePage
from pages.main_page import SecondPage


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

        second_page = SecondPage(self.screen)

        page.views.append(ft.View("/main_page", [second_page.build()]))

    def route_change(self, route):
        page = self.screen.get_page()

        page.views.clear()
        if page.route == "/homepage":
            self.init_homepage()

        if page.route == "/main_page":
            self.init_main_page()

    def rout_init(self, route: str):
        page = self.screen.get_page()
        page.route = route

        page.go(page.route)