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
        width=0.7 * SCREEN_WIDTH,
        on_click=on_click,
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.HOVERED: RED_LIGHT,
                ft.MaterialState.FOCUSED: RED,
                ft.MaterialState.DEFAULT: WHITE,
            },
            bgcolor={ft.MaterialState.HOVERED: PINK_WHITE, ft.MaterialState.FOCUSED: PINK_WHITE, "": WHITE},
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


def GenreButton(text: str, on_click=None, bg_color=BEGE_DARK):
    return ElevatedButton(
        content=Text(text,
                     font_family=DEFAULT,
                     color=BLACK,
                     size=20),
        width=0.3 * SCREEN_WIDTH,
        on_click=on_click,
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.HOVERED: RED,
                ft.MaterialState.FOCUSED: RED,
                ft.MaterialState.DEFAULT: DARK_RED
            },
            bgcolor={ft.MaterialState.HOVERED: RED_LIGHT,
                     ft.MaterialState.FOCUSED: RED_LIGHT,
                     ft.MaterialState.DEFAULT: bg_color,
                     ft.MaterialState.PRESSED: RED_LIGHT},
            padding={ft.MaterialState.DEFAULT: 3,
                     ft.MaterialState.HOVERED: 8,
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


def NextButton(text: str, on_click=None, bg_color=RED):
    return ElevatedButton(
        content=Text(text,
                     font_family=DEFAULT,
                     color=WHITE,
                     size=25),
        width=0.4 * SCREEN_WIDTH,
        on_click=on_click,
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.HOVERED: RED,
                ft.MaterialState.FOCUSED: RED,
                ft.MaterialState.DEFAULT: DARK_RED
            },
            bgcolor={ft.MaterialState.HOVERED: RED_LIGHT,
                     ft.MaterialState.FOCUSED: RED_LIGHT,
                     ft.MaterialState.DEFAULT: bg_color,
                     ft.MaterialState.PRESSED: RED_LIGHT},
            padding={ft.MaterialState.DEFAULT: 7,
                     ft.MaterialState.HOVERED: 9,
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
