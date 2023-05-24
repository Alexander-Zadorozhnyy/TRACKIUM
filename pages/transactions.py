from flet import *
from utils.config import *


class Transactions(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            height=WINDOW_HEIGHT,
            controls=[
                Row(
                    controls=[
                        Row(
                            controls=[
                                Container(
                                    padding=padding.only(left=WINDOW_WIDTH * 0.05, top=WINDOW_HEIGHT * 0.05),
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
                                                        on_click=lambda _: self.page.go('/home'),
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                            Column(
                                                controls=[
                                                    Container(
                                                        content=Text(
                                                            "Транзакции",
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
                Container(),
                Row(
                    controls=[
                        Container(
                            on_click=lambda _: self.page.go('/add_income'),
                            height=WINDOW_HEIGHT * 0.2,
                            width=WINDOW_WIDTH * 0.85,
                            padding=padding.only(left=WINDOW_WIDTH * 0.05),
                            content=Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Container(
                                                height=WINDOW_WIDTH * 0.15,
                                                width=WINDOW_WIDTH * 0.15,
                                                border_radius=BORDER_RADIUS,
                                                bgcolor=DEAL_CIRCLE_COLOR,
                                                content=Image(
                                                    # height=40,
                                                    # width=40,
                                                    scale=1.4,
                                                    src="assets/icons/income.svg",
                                                ),
                                                alignment=alignment.center,
                                            ),
                                        ],
                                        alignment=MainAxisAlignment.CENTER,
                                    ),
                                    Column(
                                        width=WINDOW_WIDTH * 0.6,
                                        controls=[
                                            Container(
                                                Text(
                                                    "Добавить поступление",
                                                    size=HEADER_FONT_SIZE,
                                                    font_family='Poppins Regular',
                                                    color=TEXT_COLOR,
                                                    text_align=TextAlign.CENTER,
                                                ),
                                                padding=padding.only(left=15),
                                            ),
                                        ],
                                        alignment=MainAxisAlignment.CENTER,
                                    ),

                                ],
                            ),
                            bgcolor=TEXT_FIELD_COLOR,
                            border_radius=BORDER_RADIUS,
                            shadow=BoxShadow(spread_radius=1,
                                             blur_radius=15,
                                             offset=Offset(5, 5),
                                             color=SHADOW_COLOR,
                                             # blur_style=ShadowBlurStyle.OUTER,
                                             )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    on_click=lambda _: self.page.go('/add_expense'),
                                    height=WINDOW_HEIGHT * 0.2,
                                    width=WINDOW_WIDTH * 0.85,
                                    padding=padding.only(left=WINDOW_WIDTH * 0.05),
                                    content=Row(
                                        controls=[
                                            Column(
                                                controls=[
                                                    Container(
                                                        height=WINDOW_WIDTH * 0.15,
                                                        width=WINDOW_WIDTH * 0.15,
                                                        border_radius=BORDER_RADIUS,
                                                        bgcolor=DEAL_CIRCLE_COLOR,
                                                        content=Image(
                                                            # height=40,
                                                            # width=40,
                                                            scale=0.8,
                                                            src="assets/icons/expense.svg",
                                                        ),
                                                        alignment=alignment.center,
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                            Column(
                                                width=WINDOW_WIDTH * 0.6,
                                                controls=[
                                                    Container(
                                                        Text(
                                                            "Добавить платеж",
                                                            size=HEADER_FONT_SIZE,
                                                            font_family='Poppins Bold',
                                                            color=TEXT_COLOR,
                                                            text_align=TextAlign.CENTER,
                                                        ),
                                                        padding=padding.only(left=15),
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),

                                        ],
                                    ),
                                    bgcolor=TEXT_FIELD_COLOR,
                                    border_radius=BORDER_RADIUS,
                                    shadow=BoxShadow(spread_radius=1,
                                                     blur_radius=15,
                                                     offset=Offset(5, 5),
                                                     color=SHADOW_COLOR,
                                                     # blur_style=ShadowBlurStyle.OUTER,
                                                     )
                                )
                            ],
                        ),

                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            spacing=50,
        )
