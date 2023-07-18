import flet as ft

# Rotation effect

rotate = ft.transform.Rotate(0, alignment=ft.alignment.center)


def animation(content: ft.Control) -> ft.AnimatedSwitcher:
    return ft.AnimatedSwitcher(
        content,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=500,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )
