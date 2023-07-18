import flet as ft

from flet import Card, Text, Container
from utils.fonts import *
from utils.colors import *
from utils.measures import SCREEN_WIDTH, SCREEN_HEIGHT
from controls.headers import header_discover
from controls.buttons import GenreButton

class TutorialPage:

    def __init__(self, screen):
        self.screen = screen

    def build(self):
        discover = header_discover()

        title = Text("What kind of movie do you want to watch today?",
                     font_family=DEFAULT,
                     size=30,
                     color=BLACK,
                     italic=True,
                     weight=ft.FontWeight.BOLD,
                     text_align="CENTER"
                     )

        genre = GenreButton("Comedy")

        content_tutorial_card = ft.Column(controls=[title, genre])

        tutorial_card = Container(content=Card(content=content_tutorial_card,
                                               elevation=30,
                                               color=BEGE_LIGHT,
                                               width=0.8 * SCREEN_WIDTH,
                                               height=0.55 * SCREEN_HEIGHT,
                                               ),
                                  padding=0,
                                  alignment=ft.alignment.center,
                                  )

        content = Container(content=ft.Column(controls=[discover, tutorial_card]),
                            bgcolor=DARK_RED,
                            padding=ft.padding.only(left=0),
                            width=SCREEN_WIDTH,
                            height=SCREEN_HEIGHT,
                            )

        return content
