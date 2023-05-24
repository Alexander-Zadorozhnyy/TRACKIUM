from flet import *
from utils.config import *


class AddAbstract(UserControl):
    def __init__(self, page, user, title="", values=[], error=[]):
        super().__init__()
        self.page = page
        self.title = title
        self.values = values
        self.user = user

        self.error = error

    def check(self):
        return None

    def build(self):
        return Column(
            height=WINDOW_HEIGHT,
            scroll=ScrollMode.AUTO,
            spacing=30,
            controls=[
                Row(
                    controls=[
                        Row(
                            controls=[
                                Container(
                                    padding=padding.only(left=WINDOW_WIDTH * 0.05, top=WINDOW_HEIGHT * 0.05, bottom=WINDOW_HEIGHT * 0.05),
                                    content=Row(
                                        controls=[
                                            Column(
                                                controls=[
                                                    Container(
                                                        height=WINDOW_WIDTH / 15,
                                                        width=WINDOW_WIDTH / 15,
                                                        content=Image(
                                                            src="assets/icons/left_arrow.svg",
                                                        ),
                                                        on_click=lambda _: self.page.go(self.back_route),
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                            Column(
                                                controls=[
                                                    Container(
                                                        content=Text(
                                                            self.title,
                                                            size=HEADER_FONT_SIZE,
                                                            color=TEXT_COLOR,
                                                            font_family='poppins regular'

                                                        )
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                        ],
                                        spacing=10,
                                    )
                                ),
                            ],

                        )
                    ],
                    alignment=MainAxisAlignment.START,
                ),
                *[Row(
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    height=WINDOW_HEIGHT * 0.12,
                                    width=WINDOW_WIDTH * 0.85,
                                    padding=padding.only(left=WINDOW_WIDTH * 0.05),
                                    content=Column(
                                        controls=[
                                            self.values[i],
                                        ],
                                        alignment=MainAxisAlignment.CENTER,
                                    ),
                                    bgcolor=TEXT_FIELD_COLOR,
                                    border_radius=BORDER_RADIUS,
                                    shadow=BoxShadow(spread_radius=1,
                                                     blur_radius=15,
                                                     offset=Offset(5, 5),
                                                     color=SHADOW_COLOR,
                                                     # blur_style=ShadowBlurStyle.OUTER,
                                                     )
                                ),
                                Container(
                                    content=self.error[i],
                                )
                            ],
                        ),

                    ],
                    alignment=MainAxisAlignment.CENTER,
                ) for i in range(len(self.values))],
                Row(
                    controls=[
                        Container(
                            content=FilledTonalButton(
                                text="Добавить",
                                style=ButtonStyle(color=BTN_BASE_COLOR),
                                width=WINDOW_WIDTH * 0.6,
                                on_click=lambda _: self.check(),
                            ),
                            padding=padding.only(top=WINDOW_HEIGHT * 0.05),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
        )
