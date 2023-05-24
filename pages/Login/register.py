from flet import *

from utils.config import *


class Register(UserControl):
    def __init__(self, page, user, status):
        super().__init__()
        self.page = page
        self.user = user
        self.status = status

        self.password_box = TextField(
            password=True,

            hint_text='Введите ваш пароль',
            hint_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=HINT_COLOR,
            ),
            text_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=TEXT_COLOR,
            ),
            border=InputBorder.NONE,
        )

        self.name_box = TextField(
            capitalization=TextCapitalization.WORDS,
            keyboard_type=KeyboardType.NAME,
            hint_text='Введите ваше имя',
            hint_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=HINT_COLOR,
            ),
            text_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=TEXT_COLOR,
            ),
            border=InputBorder.NONE,
        )

        self.email_box = TextField(
            keyboard_type=KeyboardType.EMAIL,
            hint_text='Введите ваш email',
            hint_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=HINT_COLOR,
            ),
            text_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=TEXT_COLOR,
            ),
            border=InputBorder.NONE,
        )

        self.error = Text(
            value="Пользователь с таким Email же существует!",
            color='red',
            font_family='poppins regular'

        ) if status == 1 else Container()

    def check(self):
        if self.user.db.insert_user_to_database((self.name_box.value,
                                                 self.email_box.value,
                                                 self.password_box.value)
                                                ):
            data = self.user.db.get_user_data((self.email_box.value, self.password_box.value))
            data = self.user.db.get_output(data[0])
            # print(data)

            self.user.user_id = data[0]
            self.user.user_name = data[1]
            self.page.go('/congrats')
        else:
            self.page.go('/register_fail')

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
                                                        on_click=lambda _: self.page.go('/start_page'),
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                            Column(
                                                controls=[
                                                    Container(
                                                        content=Text(
                                                            "Регистрация",
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
                Row(
                    controls=[
                        Container(
                            height=WINDOW_HEIGHT * 0.12,
                            width=WINDOW_WIDTH * 0.85,
                            padding=padding.only(left=WINDOW_WIDTH * 0.05),
                            content=Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Container(
                                                height=WINDOW_WIDTH * 0.115,
                                                width=WINDOW_WIDTH * 0.115,
                                                border_radius=BORDER_RADIUS,
                                                bgcolor=DEAL_CIRCLE_COLOR,
                                                content=Image(
                                                    # height=40,
                                                    # width=40,
                                                    # scale=0.9,
                                                    src="assets/icons/pen.svg",
                                                ),
                                                alignment=alignment.center,
                                            ),
                                        ],
                                        alignment=MainAxisAlignment.CENTER,
                                    ),
                                    Column(
                                        controls=[
                                            self.name_box,
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
                        Container(
                            height=WINDOW_HEIGHT * 0.12,
                            width=WINDOW_WIDTH * 0.85,
                            padding=padding.only(left=WINDOW_WIDTH * 0.05),
                            content=Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Container(
                                                height=WINDOW_WIDTH * 0.115,
                                                width=WINDOW_WIDTH * 0.115,
                                                border_radius=BORDER_RADIUS,
                                                bgcolor=DEAL_CIRCLE_COLOR,
                                                content=Image(
                                                    # height=40,
                                                    # width=40,
                                                    # scale=0.9,
                                                    src="assets/icons/pen.svg",
                                                ),
                                                alignment=alignment.center,
                                            ),
                                        ],
                                        alignment=MainAxisAlignment.CENTER,
                                    ),
                                    Column(
                                        controls=[
                                            self.email_box,
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
                                    height=WINDOW_HEIGHT * 0.12,
                                    width=WINDOW_WIDTH * 0.85,
                                    padding=padding.only(left=WINDOW_WIDTH * 0.05),
                                    content=Row(
                                        controls=[
                                            Column(
                                                controls=[
                                                    Container(
                                                        height=WINDOW_WIDTH * 0.115,
                                                        width=WINDOW_WIDTH * 0.115,
                                                        border_radius=BORDER_RADIUS,
                                                        bgcolor=DEAL_CIRCLE_COLOR,
                                                        content=Image(
                                                            # height=40,
                                                            # width=40,
                                                            # scale=0.9,
                                                            src="assets/icons/pen.svg",
                                                        ),
                                                        alignment=alignment.center,
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                            Column(
                                                controls=[
                                                    self.password_box,
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
                                ),
                                Container(
                                    content=self.error,
                                )
                            ],
                        ),

                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        Container(
                            content=FilledTonalButton(
                                text="Начать",
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
            spacing=50,
        )
