import flet as ft
import requests

from controls.buttons import LargeButton, NextButton
from flet import Image, Text
from utils.colors import *
from utils.measures import SCREEN_HEIGHT, SCREEN_WIDTH
from utils.constants import *
from controls.effects import gradient_effect
from controls.inputs import TextField
from utils.fonts import DEFAULT


class LoginPage:

    def __init__(self, screen):
        """

        """
        self.screen = screen
        self.image_logo_path = IMAGE_LOGO_PATH
        self.image_homepage_art_path = IMAGE_HOMEPAGE_ART_PATH
        self.image_footer = IMAGE_LOGIN

    def on_click_log_in(self, e):
        page = self.screen.get_page()

        data = {
            "username": self.email_field.value,
            "password": self.password_field.value
        }
        response = requests.post(LOGIN_USERS_ROUTE, data=data)
        token = response.json()

        if response.ok:
            page.session.set("auth_header",
                             {"Authorization": f"{token['token_type']} {token['access_token']}"})
            page.route = "/choices_page"
            page.go(page.route)
        else:
            # TODO: show some invalid credentials text
            pass

    def return_home(self, e):
        page = self.screen.get_page()
        page.route = "/homepage"
        page.go(page.route)

    def on_click_go_to_sign_up(self, e):
        page = self.screen.get_page()

        page.route = "/sign_up_page"
        page.go(page.route)

    def build(self):
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
                                                   ),
                                                   on_click=self.return_home
                                                   )],
                            alignment=ft.MainAxisAlignment.CENTER)

        login_text = ft.Row(controls=[Text("Login",
                                           size=30,
                                           color=WHITE,
                                           font_family=DEFAULT,
                                           weight=ft.FontWeight.BOLD)],
                            alignment=ft.MainAxisAlignment.CENTER)

        self.email_field = TextField(label="Email",
                                     hint_text="Email address",
                                     icon=ft.icons.ACCOUNT_CIRCLE)
        email_box = ft.Row(controls=[self.email_field],
                           alignment=ft.MainAxisAlignment.CENTER)

        self.password_field = TextField(label="Password",
                                        hint_text="Enter password...",
                                        password=True,
                                        icon=ft.icons.KEY)
        password_box = ft.Row(controls=[self.password_field],
                              alignment=ft.MainAxisAlignment.CENTER)

        empty_space = ft.Container(width=SCREEN_WIDTH, height=0.10 * SCREEN_HEIGHT)

        login = ft.Row(
            controls=[NextButton("Login", on_click=self.on_click_log_in)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        sign_up_text = ft.Row(controls=[Text("Don't have an account yet? Sign up",
                                             size=15,
                                             color=WHITE,
                                             font_family=DEFAULT,
                                             weight=ft.FontWeight.BOLD)],
                              alignment=ft.MainAxisAlignment.CENTER)

        sign_up_button = ft.Row(
            controls=[NextButton("Sign up", on_click=self.on_click_go_to_sign_up)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        col = ft.Column(width=SCREEN_WIDTH,
                        height=0.75 * SCREEN_HEIGHT,
                        controls=[white_logo,
                                  empty_space,
                                  login_text,
                                  email_box,
                                  password_box,
                                  login,
                                  sign_up_text,
                                  sign_up_button,
                                  ],
                        alignment=ft.alignment.center
                        )

        lower_col = ft.Container(content=ft.Column(controls=[ft.Row(controls=[Image(src=self.image_footer)],
                                                                    alignment=ft.MainAxisAlignment.CENTER)],
                                                   alignment=ft.MainAxisAlignment.START),
                                 )

        concat_col = ft.Column(controls=[col, lower_col])

        c = ft.Container(content=concat_col,
                         bgcolor=DARK_RED,
                         padding=0,
                         width=SCREEN_WIDTH,
                         height=SCREEN_HEIGHT)

        return c
