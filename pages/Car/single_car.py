from flet import *
from utils.config import *


class SingleCar(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

        self.car = self.user.db.get_car_from_id(
            self.user.car)[-1] if self.user.user_id is not None and self.user.car is not None else []

        deals = self.user.db.get_deal_from_car_id(
            self.user.car) if self.user.user_id is not None and self.user.car is not None else []

        incomes = {deal[0]: sum(
            list(
                map(
                    lambda x: x[5],
                    self.user.db.get_income_from_deal_id(deal[0])
                )
            )
        ) for deal in deals}

        # print(deals)
        active = []
        done = []

        for deal in deals:
            name = f"{deal[3]} - {deal[4]}"
            date = f"Дата: {deal[7].strftime('%d.%m.%Y')}"
            sym_int = deal[6]
            inc = incomes[deal[0]]
            sym_str = f"Получено: {inc} / {sym_int}"
            if inc < sym_int:
                active += [(deal[0], name, date, sym_str, inc / sym_int)]
            else:
                done += [(deal[0], name, date, sym_str, 1)]

        self.active = [self.create_card("assets/icons/play.svg", deal) for deal in active]
        # print(active)
        self.done = [self.create_card("assets/icons/done.svg", deal) for deal in done]
        # print(incomes)

        # self.values = [self.create_active(*self.cars[i], TRUCK_COLORS[i % 3]) for i in range(len(self.cars))]

    def redirect(self, id):
        self.user.deal = id
        self.page.go('/history')

    def delete(self):
        self.user.db.delete_car_from_database(self.user.car)
        self.user.car = None
        self.page.go('/remove_car_congrats')

    def create_card(self, img, values):
        return Row(
            controls=[
                Container(
                    on_click=lambda _: self.redirect(values[0]),
                    height=WINDOW_HEIGHT * 0.18,
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
                                            scale=1.2,
                                            src=img,
                                            color=TEXT_COLOR,
                                        ),
                                        alignment=alignment.center,
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            ),
                            Column(
                                controls=[
                                    Row(
                                        scroll=ScrollMode.AUTO,
                                        controls=[
                                            Text(
                                                values[1],
                                                size=DEAL_FONT_SIZE,
                                                font_family='Poppins Regular',
                                                color=TEXT_COLOR,
                                            ),

                                        ],
                                        alignment=MainAxisAlignment.START,
                                    ),
                                    Row(
                                        scroll=ScrollMode.AUTO,
                                        controls=[
                                            Text(
                                                values[2],
                                                size=DEAL_FONT_SIZE - 2,
                                                font_family='Poppins Regular',
                                                color=TEXT_COLOR,
                                            ),

                                        ],
                                        alignment=MainAxisAlignment.START,
                                    ),
                                    Row(
                                        scroll=ScrollMode.AUTO,
                                        controls=[
                                            Text(
                                                values[3],
                                                size=DEAL_FONT_SIZE - 2,
                                                font_family='Poppins Regular',
                                                color=TEXT_COLOR,
                                            ),

                                        ],
                                        alignment=MainAxisAlignment.START,
                                    ),
                                    Row(
                                        scroll=ScrollMode.AUTO,
                                        controls=[
                                            Stack(
                                                controls=[
                                                    Container(
                                                        height=WINDOW_HEIGHT * 0.015,
                                                        width=WINDOW_WIDTH * 0.6,
                                                        bgcolor=NEGATIVE_PROGRESS_BAR_COLOR,
                                                        border_radius=BORDER_RADIUS,
                                                    ),
                                                    Container(
                                                        height=WINDOW_HEIGHT * 0.015,
                                                        width=WINDOW_WIDTH * 0.6 * values[-1],
                                                        bgcolor=ACTIVE_PROGRESS_BAR_COLOR,
                                                        border_radius=BORDER_RADIUS,
                                                    ),
                                                ],

                                            ),
                                        ],
                                        alignment=MainAxisAlignment.START,
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                spacing=2,
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
        )

    def build(self):
        return Column(
            height=WINDOW_HEIGHT,
            scroll=ScrollMode.AUTO,
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
                                                        on_click=lambda _: self.page.go('/cars'),
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                            Column(
                                                controls=[
                                                    Container(
                                                        content=Text(
                                                            f"{self.car}",
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
                    # height=WINDOW_HEIGHT * 0.3,
                    padding=padding.only(top=WINDOW_HEIGHT * 0.02, ),
                    content=Column(
                        controls=[
                            Container(
                                padding=padding.only(left=WINDOW_WIDTH * 0.05),
                                content=Text(
                                    "Активные",
                                    size=BASE_FONT_SIZE,
                                    color=HINT_COLOR,
                                    font_family='poppins regular'
                                ),
                            ),
                            *self.active,
                            Container(
                                height=WINDOW_HEIGHT * 0.015
                            ),
                        ],
                        spacing=WINDOW_HEIGHT * 0.05,
                    ),
                ),
                Container(
                    padding=padding.only(top=WINDOW_HEIGHT * 0.02, ),
                    content=Column(
                        controls=[
                            Container(
                                padding=padding.only(left=WINDOW_WIDTH * 0.05),
                                content=Text(
                                    "Завершенные",
                                    size=BASE_FONT_SIZE,
                                    color=HINT_COLOR,
                                    font_family='poppins regular'
                                ),
                            ),
                            *self.done,
                            Container(
                                height=WINDOW_HEIGHT * 0.015
                            ),
                        ],
                        spacing=WINDOW_HEIGHT * 0.05,
                    ),
                ),
                Container(
                    height=WINDOW_HEIGHT * (0 if (len(self.active) + len(self.done)) >= 3
                                            else 0.125 * (3 - (len(self.active) + len(self.done))))
                ),
                Row(
                    controls=[
                        Container(
                            content=ElevatedButton(
                                text="Удалить машину",
                                style=ButtonStyle(
                                    bgcolor={
                                        MaterialState.HOVERED: RED_COLOR,
                                        "": BTN_DELETE_COLOR
                                    },
                                    color=TEXT_COLOR,
                                ),
                                width=WINDOW_WIDTH * 0.6,
                                on_click=lambda _: self.delete(),
                            ),
                            # padding=padding.only(top=WINDOW_HEIGHT * 0.1),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            spacing=80,
        )
