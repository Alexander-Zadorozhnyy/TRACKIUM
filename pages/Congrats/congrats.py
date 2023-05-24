from flet import *
from utils.config import *


class Congrats(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

    def build(self):
        return Column(
            height=WINDOW_HEIGHT,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Row(
                    controls=[
                        Container(
                            height=WINDOW_WIDTH,
                            width=WINDOW_WIDTH,
                            content=Image(
                                src="assets/icons/congrats.svg"
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        Text(
                            f'Добро пожаловать, {self.user.user_name}!',
                            size=BASE_FONT_SIZE,
                            font_family='Poppins Regular',
                            color=TEXT_COLOR,
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        Container(
                            content=FilledTonalButton(
                                text="Главная",
                                style=ButtonStyle(color=BTN_BASE_COLOR),
                                width=WINDOW_WIDTH * 0.6,
                                on_click=lambda _: self.page.go('/home'),
                            ),
                            padding=padding.only(top=WINDOW_HEIGHT * 0.05),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            spacing=50,
        )
