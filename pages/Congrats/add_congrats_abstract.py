from flet import *
from utils.config import *


class AddCongratsAbstract(UserControl):
    def __init__(self, page, text="", button_text="", back_route="/", img=""):
        super().__init__()
        self.page = page
        self.back_route = back_route
        self.button_text = button_text
        self.text = text
        self.img = img

    def build(self):
        return Column(
            height=WINDOW_HEIGHT,
            controls=[
                Row(
                    controls=[
                        Container(
                            height=WINDOW_WIDTH,
                            width=WINDOW_WIDTH * 0.9,
                            content=Image(
                                src=self.img,
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        Text(
                            self.text,
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
                                text=self.button_text,
                                style=ButtonStyle(color=BTN_BASE_COLOR),
                                width=WINDOW_WIDTH * 0.6,
                                on_click=lambda _: self.page.go(self.back_route),
                            ),
                            padding=padding.only(top=WINDOW_HEIGHT * 0.05),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            spacing=50,
        )
