import flet as ft
from controls.buttons import LargeButton, NextButton
from flet import Image, Text
from utils.colors import *
from utils.measures import SCREEN_HEIGHT, SCREEN_WIDTH, TOP_PADDING
from utils.constants import *
from controls.effects import gradient_effect
from controls.inputs import TextField
from utils.fonts import DEFAULT

import requests


class SignUpPage:

    def __init__(self, screen):
        """

        """
        self.screen = screen
        self.image_logo_path = IMAGE_LOGO_PATH
        self.image_homepage_art_path = IMAGE_HOMEPAGE_ART_PATH
        self.image_footer = IMAGE_LOGIN

    def on_click_sign_up(self, e):
        page = self.screen.get_page()

        data = {
            "name": self.username_field.value,
            "email": self.email_field.value,
            "password": self.password_field.value
        }

        response = requests.post(USERS_URL, json=data)

        if response.ok:
            data = {
                "username": self.email_field.value,
                "password": self.password_field.value
            }
            response = requests.post(LOGIN_USERS_URL, data=data)
            token = response.json()
            if response.ok:
                page.session.set("auth_header",
                                 {"Authorization": f"{token['token_type']} {token['access_token']}"})
                page.route = "/choices_page"
                page.go(page.route)
            else:
                # Account created, but a mysterious error happened
                # TODO: make a better logic for this
                page.route = "/homepage"
                page.go(page.route)
        else:
            # TODO: show some invalid credentials text
            pass

    def on_click_go_to_login(self, e):
        page = self.screen.get_page()

        page.route = "/login_page"
        page.go(page.route)

    def return_home(self, e):
        page = self.screen.get_page()
        page.route = "/homepage"
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

        sign_up_text = ft.Row(controls=[Text("Sign up",
                                             size=30,
                                             color=WHITE,
                                             font_family=DEFAULT,
                                             weight=ft.FontWeight.BOLD)],
                              alignment=ft.MainAxisAlignment.CENTER)

        self.email_field = TextField(label="Email",
                                     hint_text="Email address",
                                     icon=ft.icons.ACCOUNT_CIRCLE)
        email_box = ft.Row(controls=[self.email_field],
                           alignment=ft.MainAxisAlignment.CENTER,
                           )

        self.username_field = TextField(label="Username",
                                        hint_text="Choose a username...",
                                        icon=ft.icons.ACCOUNT_CIRCLE)
        username_box = ft.Row(controls=[self.username_field],
                              alignment=ft.MainAxisAlignment.CENTER,
                              )

        self.password_field = TextField(label="Password",
                                        hint_text="Enter password...",
                                        password=True,
                                        icon=ft.icons.KEY)
        password_box = ft.Row(controls=[self.password_field],
                              alignment=ft.MainAxisAlignment.CENTER,
                              )
        password_confirm_box = ft.Row(controls=[TextField(label="Confirm Password",
                                                          hint_text="Confirm password...",
                                                          password=True,
                                                          icon=ft.icons.KEY,
                                                          on_submit=self.on_click_sign_up)],
                                      alignment=ft.MainAxisAlignment.CENTER,
                                      )

        sign_up_button = ft.Row(
            controls=[NextButton("Sign up", on_click=self.on_click_sign_up)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        login_text = ft.Row(controls=[Text("Already have an account? Sign in",
                                           size=15,
                                           color=WHITE,
                                           font_family=DEFAULT,
                                           weight=ft.FontWeight.BOLD)],
                            alignment=ft.MainAxisAlignment.CENTER)

        login_button = ft.Row(
            controls=[NextButton("Log in", on_click=self.on_click_go_to_login)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        col = ft.Column(width=SCREEN_WIDTH,
                        height=0.75 * SCREEN_HEIGHT,
                        controls=[white_logo,
                                  sign_up_text,
                                  email_box,
                                  username_box,
                                  password_box,
                                  password_confirm_box,
                                  sign_up_button,
                                  login_text,
                                  login_button,
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
                         padding=ft.padding.only(left=0, top=TOP_PADDING),
                         width=SCREEN_WIDTH,
                         height=SCREEN_HEIGHT)

        return c
