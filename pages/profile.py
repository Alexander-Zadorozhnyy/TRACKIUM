from flet import *
from utils.config import *


class Profile(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

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
                                                        content=Text(
                                                            "Профиль",
                                                            size=HEADER_FONT_SIZE + 5,
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
                        Column(
                            controls=[
                                Container(
                                    height=WINDOW_WIDTH * 0.6,
                                    width=WINDOW_WIDTH * 0.6,
                                    content=Image(
                                        src="assets/icons/profile.svg"
                                    ),
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
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
                Container(
                    height=WINDOW_HEIGHT * 0.2,
                ),
                Row(
                    controls=[
                        NavigationBar(
                            width=WINDOW_WIDTH * 0.95,
                            destinations=[
                                NavigationDestination(
                                    label="Главная",
                                    icon_content=Container(
                                        content=Icon(
                                            name=icons.HOME,
                                            color=TEXT_COLOR,
                                        ),
                                        on_click=lambda _: self.page.go('/home'),
                                    ),
                                ),
                                NavigationDestination(
                                    label="Машины",
                                    icon_content=Container(
                                        content=Icon(
                                            name=icons.FIRE_TRUCK,
                                            color=TEXT_COLOR,
                                        ),
                                        on_click=lambda _: self.page.go('/cars'),
                                    ),
                                ),
                                NavigationDestination(
                                    label="Финансы",
                                    icon_content=Container(
                                        content=Icon(
                                            name=icons.ATTACH_MONEY,
                                            color=TEXT_COLOR,
                                        ),
                                        on_click=lambda _: self.page.go('/finance'),
                                    ),
                                ),
                                NavigationDestination(
                                    label="Сделки",
                                    icon_content=Container(
                                        content=Icon(
                                            name=icons.WORK_HISTORY,
                                            color=TEXT_COLOR,
                                        ),
                                        on_click=lambda _: self.page.go('/deals'),
                                    ),
                                ),
                                NavigationDestination(
                                    label="Профиль",
                                    icon_content=Container(
                                        content=Icon(
                                            name=icons.LOCATION_HISTORY,
                                            color=TEXT_COLOR,
                                        ),
                                        on_click=lambda _: self.page.go('/profile'),
                                    ),
                                ),
                            ]
                        ),
                    ],
                    alignment=MainAxisAlignment.START,
                ),
            ],
            spacing=25,
        )
