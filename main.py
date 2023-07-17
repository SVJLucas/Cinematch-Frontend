import flet as ft
from screen import Screen
from utils import measures
from routers import Router

screen = Screen(measures.SCREEN_WIDTH, measures.SCREEN_HEIGHT)

router = Router()

def main(page : ft.Page):

    screen.set_page(page)
    router.connect_screen(screen)
    router.rout_init("/homepage")








ft.app(target=main)