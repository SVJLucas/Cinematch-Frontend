import flet as ft

class Screen:

    def __init__(self, width, height):
        self._page = None
        self.width = width
        self.height = height

    def set_page(self, page: ft.Page):
        page.window_width = self.width
        page.window_height = self.height
        page.window_resizable = False
        self._page = page

    def get_page(self) -> ft.Page:
        return self._page
