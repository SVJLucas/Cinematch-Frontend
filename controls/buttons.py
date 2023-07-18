import flet as ft

from utils.fonts import *
from utils.measures import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.colors import *

from flet import (
    FloatingActionButton,
    ElevatedButton,
    BorderSide,
    Text,
    RoundedRectangleBorder
)


def LargeButton(text: str, on_click=None):
    return ElevatedButton(
            content=Text(text,
                     font_family=DEFAULT,
                     color=DARK_RED,
                     size=20),
            width=0.7*SCREEN_WIDTH,
            on_click=on_click,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: RED_LIGHT,
                    ft.MaterialState.FOCUSED: RED,
                    ft.MaterialState.DEFAULT: WHITE,
                },
                bgcolor={ft.MaterialState.HOVERED: PINK_WHITE, ft.MaterialState.FOCUSED: PINK_WHITE, "": ft.colors.WHITE},
                padding={ft.MaterialState.DEFAULT: 20,
                         ft.MaterialState.HOVERED: 21,
                         },
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 20},
                animation_duration=500,
                shape={
                    ft.MaterialState.HOVERED: RoundedRectangleBorder(radius=22),
                    ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=20),
                },
            )
    )


def CircleButton(src, onclick=None):
    return ElevatedButton(content=ft.Image(src=src),
                          style=ft.ButtonStyle(
                              color={
                                  ft.MaterialState.HOVERED: RED_LIGHT,
                                  ft.MaterialState.FOCUSED: RED,
                                  ft.MaterialState.DEFAULT: WHITE,
                              },
                              bgcolor={ft.MaterialState.HOVERED: BEGE_HOVER, ft.MaterialState.FOCUSED: BEGE_DARK,
                                       ft.MaterialState.DEFAULT: BEGE_LIGHT},
                              padding={ft.MaterialState.DEFAULT: 20,
                                       ft.MaterialState.HOVERED: 21,
                                       },
                              overlay_color=ft.colors.TRANSPARENT,
                              elevation={"pressed": 0, "": 20},
                              animation_duration=500,
                              side={
                                  ft.MaterialState.DEFAULT: BorderSide(1, BEGE_LIGHT),
                                  ft.MaterialState.HOVERED: BorderSide(2, BEGE_LIGHT),
                              },
                              shape={
                                  ft.MaterialState.HOVERED: ft.CircleBorder(),
                                  ft.MaterialState.DEFAULT: ft.CircleBorder(),
                              },
                          ),
                          )


'''
def CircleButton(src, onclick=None):
    return FloatingActionButton(content=ft.Image(src=src), bgcolor=BEGE_LIGHT,
                                shape=ft.CircleBorder())
'''