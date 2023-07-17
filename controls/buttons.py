import flet as ft

from utils.fonts import *
from utils.measures import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.colors import *

from flet import (
    FloatingActionButton,
    Text
)


def LargeButton(text: str, on_click=None):
    return FloatingActionButton(
            content=Text(text,
                     font_family=DEFAULT,
                     color=DARK_RED,
                     size=20),
            width=0.7*SCREEN_WIDTH,
            bgcolor=WHITE,
            on_click=on_click)


def CircleButton(src, onclick=None):
    return FloatingActionButton(content=ft.Image(src=src), bgcolor=BEGE_LIGHT,
                                shape=ft.CircleBorder())


