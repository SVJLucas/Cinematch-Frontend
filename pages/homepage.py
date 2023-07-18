import flet as ft
from flet import FloatingActionButton, Text
from controls.buttons import LargeButton
from flet import Image, Container, Row, Column
from utils.colors import *
from utils.measures import SCREEN_HEIGHT, SCREEN_WIDTH
from utils.constants import *
from controls.effects import gradient_effect, gradient_alt
from controls.animations import rotate, animation


class HomePage:

    def __init__(self, screen):
        """

        """
        self.screen = screen
        self.image_logo_path = IMAGE_LOGO_PATH
        self.image_homepage_art_path = IMAGE_HOMEPAGE_ART_PATH

    def on_click_button(self, e):
        page = self.screen.get_page()

        page.route = "/main_page"
        page.go(page.route)

    def build(self):
        login = ft.Row(
            controls=[LargeButton("Login", on_click=self.on_click_button)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        signup = ft.Row(
            controls=[LargeButton("Sign up")],
            alignment=ft.MainAxisAlignment.CENTER
        )

        img = Image(src=self.image_logo_path)

        white_logo = ft.Row(controls=[ft.Container(content=ft.Row(controls=[img],
                                                                  alignment=ft.MainAxisAlignment.CENTER),
                                                   bgcolor=WHITE,
                                                   border_radius=20,
                                                   width=0.8 * SCREEN_WIDTH,
                                                   height=0.2 * SCREEN_HEIGHT,
                                                   margin=5,
                                                   padding=0,
                                                   shadow=ft.BoxShadow(
                                                       spread_radius=1,
                                                       blur_radius=15,
                                                       color=ft.colors.BLUE_GREY_300,
                                                       offset=ft.Offset(0, 0),
                                                       blur_style=ft.ShadowBlurStyle.OUTER,
                                                   )
                                                   )],
                            alignment=ft.MainAxisAlignment.CENTER)

        empty_space = ft.Container(width=SCREEN_WIDTH, height=0.15 * SCREEN_HEIGHT)

        img_center = Image(src=self.image_homepage_art_path)

        col = ft.Column(width=SCREEN_WIDTH,
                        controls=[white_logo,
                                  empty_space,
                                  img_center,
                                  login,
                                  signup
                                  ],
                        alignment=ft.alignment.center
                        )

        c = ft.Container(content=col,
                         bgcolor=DARK_RED,
                         padding=0,
                         width=SCREEN_WIDTH,
                         height=SCREEN_HEIGHT)

        grad_c = gradient_effect(c)

        return c
