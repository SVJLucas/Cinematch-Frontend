import flet as ft
import time

from flet import FloatingActionButton, Text
from controls.buttons import CircleButton, CircleButtonBase
from flet import Image, Container, Row, Column
from utils.database import get_non_rated_movie
from utils.colors import *
from utils.measures import SCREEN_HEIGHT, SCREEN_WIDTH, TOP_PADDING
from utils.fonts import *
from utils.constants import *
from controls.effects import gradient_effect, shadow
from controls.animations import animation
from controls.headers import header_discover

import requests


def send_rating(data, e):
    response = requests.post(RATINGS_URL, headers=e.page.session.get("auth_header"), json=data)


class MainPage:

    def __init__(self, screen):
        """

        """
        self.screen = screen

        self.card_title = "The Great Gatsby"
        self.card_genres = "Drama . Comedy"
        self.card_poster = IMAGE_DUMMY_POSTER_PATH
        self.card_movie_id = "42"
        self.card_synopsis = "Synopsis - bla bla bla bla bla bla bla bla bla bla bla bla bla"
        self.update_movie()

        self.icon_profile = ft.Icon(ft.icons.PERSON)
        self.icon_love = ICON_LOVE
        self.icon_like = ICON_LIKE
        self.icon_neutral = ICON_NEUTRAL
        self.icon_dislike = ICON_DISLIKE
        self.icon_broken_heart = ICON_BROKEN_HEART
        self.icon_next = ft.Icon(ft.icons.ARROW_FORWARD)
        self.animated_container = None
        self.show_synopsis = False

    def update_card(self):

        synopsis = Text(self.card_synopsis,
                        text_align="CENTER",
                        font_family=DEFAULT,
                        width=0.9 * SCREEN_WIDTH,
                        size=15,
                        color=BLACK)

        title = Text(self.card_title,
                     width=0.9 * SCREEN_WIDTH,
                     text_align="CENTER",
                     font_family=DEFAULT,
                     size=25,
                     weight=ft.FontWeight.BOLD,
                     color=BLACK)

        genres = Text(self.card_genres,
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
                                                   ft.Image(src=self.card_poster,
                                                            width=0.65 * SCREEN_WIDTH,
                                                            height=0.4 * SCREEN_HEIGHT),
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

    def update_movie(self):
        movie = get_non_rated_movie()
        self.card_title = movie["title"]
        self.card_genres = ' . '.join([genre["name"] for genre in movie["genres"]])
        self.card_poster = movie["image_url"]
        self.card_synopsis = movie["synopsis"]
        self.card_movie_id = movie["movie_id"]

    def on_click_card(self, e):
        page = self.screen.get_page()
        self.show_synopsis = not self.show_synopsis
        self.animated_container.content = self.update_card()
        page.update()

    def on_click_profile(self, e):
        page = self.screen.get_page()
        page.route = "/recommendations_page"
        page.go(page.route)

    def on_click_rating_wrapper(self, rating):
        def on_click_rating(e):
            page = self.screen.get_page()
            data = {"movie_id": self.card_movie_id,
                    "score": rating}
            send_rating(data, e)
            time.sleep(0.2)
            self.update_movie()
            self.animated_container.content = self.update_card()
            page.update()

        return on_click_rating

    def on_click_skip(self, e):
        # TODO
        page = self.screen.get_page()
        # data = {"score": 5}
        # send_rating(data, e)

    def build(self):
        discover_txt = header_discover()
        profile_button = CircleButtonBase(content=self.icon_profile,
                                          on_click=self.on_click_profile)
        header = ft.Row(controls=[discover_txt, profile_button],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        card_movie = self.update_card()

        c = ft.Row(controls=[card_movie],
                   alignment=ft.MainAxisAlignment.CENTER
                   )

        self.animated_container = animation(c)

        love = CircleButton(self.icon_love, on_click=self.on_click_rating_wrapper(SCORE_LOVE))
        like = CircleButton(self.icon_like, on_click=self.on_click_rating_wrapper(SCORE_LIKE))
        neutral = CircleButton(self.icon_neutral, on_click=self.on_click_rating_wrapper(SCORE_NEUTRAL))
        dislike = CircleButton(self.icon_dislike, on_click=self.on_click_rating_wrapper(SCORE_DISLIKE))
        hate = CircleButton(self.icon_broken_heart, on_click=self.on_click_rating_wrapper(SCORE_HATE))

        button_menu = ft.Container(ft.Row(controls=[hate, dislike, neutral, like, love],
                                          alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                   width=SCREEN_WIDTH,
                                   padding=0,
                                   margin=0.05 * SCREEN_WIDTH)

        skip_button = CircleButtonBase(self.icon_next, on_click=self.on_click_skip)
        skip_menu = ft.Container(ft.Row(controls=[skip_button],
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                 width=SCREEN_WIDTH,
                                 padding=0,
                                 margin=0.05 * SCREEN_WIDTH)

        content = ft.Container(content=ft.Column(controls=[header, self.animated_container,
                                                           button_menu, skip_menu]),
                               bgcolor=DARK_RED,
                               padding=ft.padding.only(left=0, top=TOP_PADDING),
                               width=SCREEN_WIDTH,
                               height=SCREEN_HEIGHT,
                               shadow=shadow)

        return content
