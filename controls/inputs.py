import flet as ft
from utils.measures import SCREEN_WIDTH
from utils.colors import *
from utils.fonts import *


def TextField(label=None, hint_text=None, password=False, icon=None, on_submit=None):
    return ft.TextField(label=label,
                        hint_text=hint_text,
                        bgcolor=ft.colors.TRANSPARENT,
                        password=password,
                        width=0.8 * SCREEN_WIDTH,
                        border_color=WHITE,
                        border_radius=30,
                        color=WHITE,
                        cursor_color=WHITE,
                        label_style=ft.TextStyle(color=WHITE, font_family=DEFAULT),
                        prefix_icon=icon,
                        on_submit=on_submit)
