import flet as ft
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

    def on_click_log_in(self, e):
        page = self.screen.get_page()

        page.route = "/choices_page"
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
                                                   )
                                                   )],
                            alignment=ft.MainAxisAlignment.CENTER)

        login_text = ft.Row(controls=[Text("Login",
                            size=30,
                            color=WHITE,
                            font_family=DEFAULT,
                            weight=ft.FontWeight.BOLD)],
                           alignment=ft.MainAxisAlignment.CENTER)

        email_box = ft.Row(controls=[TextField(label="email",
                                               hint_text="email address",
                                               icon=ft.icons.ACCOUNT_CIRCLE)],
                           alignment=ft.MainAxisAlignment.CENTER,
                           )

        password_box = ft.Row(controls=[TextField(label="password",
                                                  hint_text="enter password...",
                                                  password=True,
                                                  icon=ft.icons.KEY)],
                              alignment=ft.MainAxisAlignment.CENTER,
                              )

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
            controls=[NextButton("Sign up", on_click=self.on_click_log_in)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        col = ft.Column(width=SCREEN_WIDTH,
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

        c = ft.Container(content=col,
                         bgcolor=DARK_RED,
                         padding=0,
                         width=SCREEN_WIDTH,
                         height=SCREEN_HEIGHT)

        return c