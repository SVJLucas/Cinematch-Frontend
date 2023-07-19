import flet as ft

from flet import Card, Text, Container
from utils.fonts import *
from utils.colors import *
from utils.measures import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.constants import movie_genres
from controls.headers import header_discover
from controls.buttons import GenreButton, NextButton


class ChoicesPage:

    def __init__(self, screen):
        self.screen = screen
        self.button_pressed = {}
        self.genres_selected = []

        for genre in movie_genres:
            self.button_pressed[genre] = 0

    def on_click_genre_button(self, e):
        page = self.screen.get_page()
        genre = e.control.content.value
        self.button_pressed[genre] = not self.button_pressed[genre]
        # Implementing toggle functionality
        if self.button_pressed[genre]:
            self.genres_selected.append(genre)
            e.control.style.bgcolor = RED_LIGHT
        else:
            self.genres_selected.remove(genre)
            e.control.style.bgcolor = BEGE_DARK

        page.update()

    def on_click_next_button(self, e):
        page = self.screen.get_page()
        page.route = "/tutorial_page"
        page.go(page.route)

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

        list_content = [title]
        button_accumulator = []
        for i, genre in enumerate(movie_genres):

            if i % 2 == 0 and i >= 2:
                list_content.append(ft.Row(controls=button_accumulator.copy(),
                                           alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                    )
                button_accumulator = []

            button_accumulator.append(GenreButton(genre,
                                                  on_click=self.on_click_genre_button,
                                                  bg_color=BEGE_DARK))

        list_content.append(ft.Row(controls=button_accumulator.copy(),
                                   alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            )

        white_space = ft.Container(height=0.15 * SCREEN_HEIGHT)

        list_content.append(white_space)

        next_button = ft.Row(controls=[NextButton("Next", on_click=self.on_click_next_button)],
                             alignment=ft.MainAxisAlignment.CENTER)

        list_content.append(next_button)

        content_choices_card = ft.Container(content=ft.Column(controls=list_content),
                                            width=0.7 * SCREEN_WIDTH)

        choices_card = Container(content=Card(content=content_choices_card,
                                              elevation=30,
                                              color=WHITE,
                                              width=0.8 * SCREEN_WIDTH,
                                              height=0.55 * SCREEN_HEIGHT,
                                              ),
                                 padding=0,
                                 alignment=ft.alignment.center,
                                 )

        content = Container(content=ft.Column(controls=[discover, choices_card]),
                            bgcolor=DARK_RED,
                            padding=ft.padding.only(left=0),
                            width=SCREEN_WIDTH,
                            height=SCREEN_HEIGHT,
                            )

        return content
