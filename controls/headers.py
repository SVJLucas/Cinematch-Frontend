import flet as ft

from flet import Text
from utils.fonts import *
from utils.colors import *


def header_discover():
    return ft.Container(
        Text("Discover",
             font_family=DEFAULT,
             size=30,
             weight=ft.FontWeight.BOLD,
             color=WHITE),
        margin=10
    )
