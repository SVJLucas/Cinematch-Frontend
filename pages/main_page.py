import flet as ft

from flet import FloatingActionButton, Text
from controls.buttons import CircleButton
from flet import Image, Container, Row, Column
from utils.colors import *
from utils.measures import SCREEN_HEIGHT, SCREEN_WIDTH
from utils.fonts import *
from utils.constants import *
from controls.effects import gradient_effect, shadow


class SecondPage:

    def __init__(self, screen):
        """

        """
        self.screen = screen

        self.image_dummy_poster_path = IMAGE_DUMMY_POSTER_PATH
        self.icon_love = ICON_LOVE
        self.icon_like = ICON_LIKE
        self.icon_neutral = ICON_NEUTRAL
        self.icon_dislike = ICON_DISLIKE
        self.icon_broken_heart = ICON_BROKEN_HEART

    def on_click_button(self):
        page = self.screen.get_page()

        page.route = "/second_page"
        page.go(page.route)

    def build(self):
        discover_txt = ft.Container(
                            Text("Discover",
                                font_family=DEFAULT,
                                size=35,
                                color=WHITE),
                            margin=10
                        )

        poster = ft.Image(src=self.image_dummy_poster_path,
                          width=0.9 * SCREEN_WIDTH)
        title = Text("The Great Gatsby",
                     width=0.9 * SCREEN_WIDTH,
                     text_align="CENTER",
                     font_family=DEFAULT,
                     size=25,
                     color=BLACK)

        genres = Text("Drama . Comedy",
                      width=0.9 * SCREEN_WIDTH,
                      text_align="CENTER",
                      font_family=DEFAULT,
                      size=15,
                      color=BLACK)

        card_movie = ft.Column(controls=[poster, title, genres],
                               alignment=ft.alignment.center)

        c = ft.Container(content=card_movie,
                         padding=0,
                         width=0.7 * SCREEN_WIDTH,
                         height=0.55 * SCREEN_HEIGHT,
                         margin= 0.1*SCREEN_WIDTH,
                         alignment=ft.alignment.center,
                         bgcolor=BEGE_LIGHT,
                         border_radius=30,
                         )

        love = CircleButton(self.icon_love)
        like = CircleButton(self.icon_like)
        neutral = CircleButton(self.icon_neutral)
        dislike = CircleButton(self.icon_dislike)
        hate = CircleButton(self.icon_broken_heart)

        button_menu = ft.Container(ft.Row(controls=[hate, dislike, neutral, like, love]),
                                   width=SCREEN_WIDTH,
                                   padding=0,
                                   alignment=ft.alignment.center,
                                   margin=0.05*SCREEN_WIDTH)

        content = ft.Container(content=ft.Column(controls=[discover_txt, c, button_menu]),
                               bgcolor=DARK_RED,
                               padding=ft.padding.only(left=0),
                               width=SCREEN_WIDTH,
                               height=SCREEN_HEIGHT,
                               shadow=shadow)

        grad = gradient_effect(content)

        return grad
