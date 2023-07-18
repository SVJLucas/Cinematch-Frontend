import flet as ft

from flet import FloatingActionButton, Text
from controls.buttons import CircleButton
from flet import Image, Container, Row, Column
from utils.colors import *
from utils.measures import SCREEN_HEIGHT, SCREEN_WIDTH
from utils.fonts import *
from utils.constants import *
from controls.effects import gradient_effect, shadow
from controls.animations import animation
from controls.headers import header_discover

class MainPage:

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
        self.animated_container = None
        self.show_synopsis = False

    def update_card(self):

        synopsis = Text("Synopsis - bla bla bla bla bla bla bla bla bla bla bla bla bla",
                        text_align="CENTER",
                        font_family=DEFAULT,
                        width=0.9 * SCREEN_WIDTH,
                        size=15,
                        color=BLACK)

        title = Text("The Great Gatsby",
                     width=0.9 * SCREEN_WIDTH,
                     text_align="CENTER",
                     font_family=DEFAULT,
                     size=25,
                     weight=ft.FontWeight.BOLD,
                     color=BLACK)

        genres = Text("Drama . Comedy",
                      width=0.9 * SCREEN_WIDTH,
                      text_align="CENTER",
                      font_family=DEFAULT,
                      size=15,
                      color=BLACK)

        content_card_movie = ft.Column(controls=[synopsis, title, genres],
                                       alignment=ft.alignment.center)

        if self.show_synopsis:
            return ft.Container(content=ft.Card(content=content_card_movie,
                                                elevation=30,
                                                color=BEGE_LIGHT,
                                                width=0.8 * SCREEN_WIDTH,
                                                height=0.55 * SCREEN_HEIGHT,
                                                ),
                                padding=0,
                                alignment=ft.alignment.center,
                                on_click=self.on_click_card
                                )
        else:
            poster = ft.Row(controls=[ft.Container(content=
                                                   ft.Image(src=self.image_dummy_poster_path,
                                                            width=0.65 * SCREEN_WIDTH,
                                                            ),
                                                   margin=5)],
                            alignment=ft.MainAxisAlignment.CENTER
                            )

            content_card_movie = ft.Column(controls=[poster, title, genres],
                                           alignment=ft.alignment.center)

            return ft.Container(content=ft.Card(content=content_card_movie,
                                                elevation=30,
                                                color=BEGE_LIGHT,
                                                width=0.8 * SCREEN_WIDTH,
                                                height=0.55 * SCREEN_HEIGHT,
                                                ),
                                padding=0,
                                alignment=ft.alignment.center,
                                on_click=self.on_click_card
                                )

    def on_click_card(self, e):
        page = self.screen.get_page()
        self.show_synopsis = not self.show_synopsis
        self.animated_container.content = self.update_card()
        page.update()

    def build(self):
        discover_txt = header_discover()

        card_movie = self.update_card()

        c = ft.Row(controls=[card_movie],
                   alignment=ft.MainAxisAlignment.CENTER
                   )

        self.animated_container = animation(c)

        love = CircleButton(self.icon_love)
        like = CircleButton(self.icon_like)
        neutral = CircleButton(self.icon_neutral)
        dislike = CircleButton(self.icon_dislike)
        hate = CircleButton(self.icon_broken_heart)

        button_menu = ft.Container(ft.Row(controls=[hate, dislike, neutral, like, love],
                                          alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                   width=SCREEN_WIDTH,
                                   padding=0,
                                   margin=0.05 * SCREEN_WIDTH)

        content = ft.Container(content=ft.Column(controls=[discover_txt, self.animated_container, button_menu]),
                               bgcolor=DARK_RED,
                               padding=ft.padding.only(left=0),
                               width=SCREEN_WIDTH,
                               height=SCREEN_HEIGHT,
                               shadow=shadow)

        return content
