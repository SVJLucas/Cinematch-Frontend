import flet as ft
from math import pi
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

def gradient_alt():
    return ft.LinearGradient(
        begin=ft.alignment.top_left,
        end=ft.Alignment(0.8, 1),
        colors=[
            "0xff1f005c",
            "0xff5b0060",
            "0xff870160",
            "0xffac255e",
            "0xffca485c",
            "0xffe16b5c",
            "0xfff39060",
            "0xffffb56b",
        ],
        tile_mode=ft.GradientTileMode.MIRROR,
        rotation= pi / 3,
    )
