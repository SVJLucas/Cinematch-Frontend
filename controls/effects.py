import flet as ft

from utils.colors import *


def gradient_effect(content):
    return ft.ShaderMask(
        content,
        blend_mode=ft.BlendMode.DST_IN,
        shader=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.BLACK, ft.colors.TRANSPARENT],
            stops=[0.8, 1.0],
        ),
        border_radius=10, )


def shadow():
    return ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    )
