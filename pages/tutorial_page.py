import flet as ft

from flet import Card, Text, Container
from utils.fonts import *
from utils.colors import *
from utils.measures import SCREEN_WIDTH, SCREEN_HEIGHT, TOP_PADDING
from utils.constants import movie_genres
from controls.headers import header_discover, footer_logo
from controls.buttons import GenreButton, NextButton, CircleButton

from utils.constants import ICON_LOVE, ICON_LIKE, ICON_NEUTRAL, ICON_DISLIKE, ICON_BROKEN_HEART


class TutorialPage:

    def __init__(self, screen):
        self.screen = screen
        self.icon_love = ICON_LOVE
        self.icon_like = ICON_LIKE
        self.icon_neutral = ICON_NEUTRAL
        self.icon_dislike = ICON_DISLIKE
        self.icon_broken_heart = ICON_BROKEN_HEART

    def on_click_next_button(self, e):
        page = self.screen.get_page()
        page.route = "/main_page"
        page.go(page.route)

    def build(self):
        discover = header_discover()

        title = ft.Row(controls=[Text("How to start...",
                                      font_family=DEFAULT,
                                      size=30,
                                      color=BLACK,
                                      italic=True,
                                      weight=ft.FontWeight.BOLD,
                                      text_align="CENTER"
                                      )],
                       alignment=ft.MainAxisAlignment.CENTER
                       )

        subtitle = ft.Row(controls=[Text("Our buttons",
                                         font_family=DEFAULT,
                                         size=20,
                                         color=BLACK,
                                         weight=ft.FontWeight.BOLD,
                                         text_align="CENTER"
                                         )],
                          alignment=ft.MainAxisAlignment.CENTER
                          )
        love = ft.Row(controls=[ft.Image(src=self.icon_love), Text("Loved this movie!",
                                                                   font_family=DEFAULT,
                                                                   size=20,
                                                                   color=BLACK)],
                      alignment=ft.MainAxisAlignment.START)

        like = ft.Row(controls=[ft.Image(src=self.icon_like), Text("I Liked this movie",
                                                                   font_family=DEFAULT,
                                                                   size=20,
                                                                   color=BLACK)],
                      alignment=ft.MainAxisAlignment.START)

        neutral = ft.Row(controls=[ft.Image(src=self.icon_neutral), Text("I haven't watched",
                                                                         font_family=DEFAULT,
                                                                         size=20,
                                                                         color=BLACK)],
                         alignment=ft.MainAxisAlignment.START)

        dislike = ft.Row(controls=[ft.Image(src=self.icon_dislike), Text("I didn't like this movie",
                                                                         font_family=DEFAULT,
                                                                         size=20,
                                                                         color=BLACK)],
                         alignment=ft.MainAxisAlignment.START)

        hate = ft.Row(controls=[ft.Image(src=self.icon_broken_heart), Text("I hated this movie",
                                                                           font_family=DEFAULT,
                                                                           size=20,
                                                                           color=BLACK)],
                      alignment=ft.MainAxisAlignment.START
                      )

        list_icons = ft.Container(content=ft.Column(controls=[love, like, neutral, dislike, hate]),
                                  margin=0.1 * SCREEN_WIDTH)

        next_button = ft.Row(controls=[NextButton("Next", on_click=self.on_click_next_button)],
                             alignment=ft.MainAxisAlignment.CENTER)

        content_tutorial_card = ft.Container(content=ft.Column(controls=[title, subtitle, list_icons, next_button]),
                                             width=0.7 * SCREEN_WIDTH
                                             )

        tutorial_card = Container(content=Card(content=content_tutorial_card,
                                               elevation=30,
                                               color=WHITE,
                                               width=0.8 * SCREEN_WIDTH,
                                               height=0.55 * SCREEN_HEIGHT,
                                               ),
                                  padding=0,
                                  alignment=ft.alignment.center
                                  )

        column_upper = ft.Column(controls=[discover, tutorial_card],
                                 height=0.8*SCREEN_HEIGHT)

        column_lower = ft.Column(controls=[footer_logo()],
                                 height=0.2 * SCREEN_HEIGHT,
                                 alignment=ft.MainAxisAlignment.CENTER
                                 )

        content = Container(content=ft.Column(controls=[column_upper, column_lower]),
                            bgcolor=DARK_RED,
                            padding=ft.padding.only(left=0, top=TOP_PADDING),
                            width=SCREEN_WIDTH,
                            height=SCREEN_HEIGHT,
                            )

        return content
