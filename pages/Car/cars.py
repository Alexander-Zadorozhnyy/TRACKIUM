from flet import *
from utils.config import *


class Cars(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

        cars = [self.user.db.get_output(i[0]) for i in
                self.user.db.get_cars(self.user.user_id)] if self.user.user_id is not None else []

        self.cars = list(map(
            lambda x: x[:3],
            cars)
        )

        # self.values = self.create_truck(0, "Max", "FFFFFFFFFF", RED_COLOR)

        self.values = [self.create_truck(*self.cars[i], TRUCK_COLORS[i % 3]) for i in range(len(self.cars))]

    def redirect(self, id):
        self.user.car = id
        self.page.go('/single_car')

    def create_truck(self, id, name, lp, color):
        return Row(
            controls=[
                Container(
                    on_click=lambda _: self.redirect(id),
                    height=WINDOW_HEIGHT * 0.12,
                    width=WINDOW_WIDTH * 0.85,
                    padding=padding.only(left=WINDOW_WIDTH * 0.05),
                    content=Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        height=WINDOW_WIDTH * 0.117,
                                        width=WINDOW_WIDTH * 0.117,
                                        content=Image(
                                            # height=40,
                                            # width=40,
                                            # scale=0.9,
                                            src="assets/icons/truck.svg",
                                            color=color,
                                            # scale=1.1,
                                        ),
                                        alignment=alignment.center,
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            ),
                            Column(
                                controls=[
                                    Text(
                                        f"{name} - {lp}",
                                        size=BASE_FONT_SIZE - 5,
                                        font_family='Poppins Regular',
                                        color=TEXT_COLOR,
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            ),
                            Column(
                                controls=[
                                    Container(
                                        height=WINDOW_WIDTH / 15,
                                        width=WINDOW_WIDTH / 15,
                                        content=Image(
                                            src="assets/icons/right_arrow.svg",
                                            color=color,
                                        ),
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            ),

                        ],
                    ),
                    bgcolor=TEXT_FIELD_COLOR,
                    border=Border(*[BorderSide(1, color=color) for _ in range(4)]),
                    border_radius=BORDER_RADIUS,
                    shadow=BoxShadow(spread_radius=0.5,
                                     blur_radius=10,
                                     offset=Offset(1, 1),
                                     color=color,
                                     # blur_style=ShadowBlurStyle.OUTER,
                                     )
                )
            ],
            alignment=MainAxisAlignment.CENTER,
        )

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
                                                            f"Мои машины",
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
                Container(
                    height=WINDOW_HEIGHT * 0.5,
                    padding=padding.only(top=WINDOW_HEIGHT * 0.05, ),
                    content=Column(
                        scroll=ScrollMode.AUTO,
                        controls=[
                            *self.values,
                        ],
                        spacing=WINDOW_HEIGHT * 0.05,
                    ),
                ),
                Row(
                    controls=[
                        Container(
                            content=FilledTonalButton(
                                text="Добавить машину",
                                style=ButtonStyle(color=BTN_BASE_COLOR),
                                width=WINDOW_WIDTH * 0.6,
                                on_click=lambda _: self.page.go('/add_car'),
                            ),
                            padding=padding.only(top=WINDOW_HEIGHT * 0.05),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
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
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            # spacing=50,
        )
