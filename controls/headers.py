import flet as ft

from flet import Text
from utils.fonts import *
from utils.colors import *
from utils.constants import IMAGE_LOGO_NAME
from utils.measures import SCREEN_WIDTH, SCREEN_HEIGHT


def header_discover():
    return ft.Container(
        Text("Discover",
             font_family=DEFAULT,
             size=30,
             weight=ft.FontWeight.BOLD,
             color=WHITE),
        margin=10
    )


def footer_logo():

    return ft.Container(content=ft.Row(controls=[ft.Image(src=IMAGE_LOGO_NAME)],
                                       alignment=ft.MainAxisAlignment.CENTER),
                        bgcolor=WHITE,
                        width=1.1*SCREEN_WIDTH,
                        border_radius=16)


    #
    # return ft.Column(controls=[ft.Container(
    #     content=ft.Column(controls=[ft.Image(src=IMAGE_LOGO_NAME)],
    #                       alignment=ft.MainAxisAlignment.END),
    #     width=SCREEN_WIDTH,
    #     height=0.1 * SCREEN_HEIGHT,
    #     alignment=ft.alignment.bottom_center,
    #     bgcolor=WHITE)],
    #     alignment=ft.MainAxisAlignment.END)
