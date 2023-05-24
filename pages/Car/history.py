from flet import *
from utils.config import *


class History(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

        incomes = self.user.db.get_income_from_deal_id(
            self.user.deal) if self.user.user_id is not None and self.user.deal is not None else []

        incomes_print = []

        for income in incomes:
            sender = f"От: {income[4]}"
            date = f"Дата: {income[6].strftime('%d.%m.%Y')}"
            sym_int = f"Сумма: {income[5]}"
            is_cash = f"Наличные: {'да' if income[7] else 'нет'}"

            incomes_print += [(income[0], sender, date, sym_int, is_cash)]

        self.incomes = [self.create_card(income) for income in incomes_print]

    def delete(self, id):
        self.user.db.delete_income_from_database(id)
        self.page.go('/single_car')

    def delete_deal(self):
        self.user.db.delete_car_from_database(self.user.car)
        self.user.car = None
        self.page.go('/remove_car_congrats')

    def create_card(self, values):
        return Row(
            controls=[
                Container(
                    height=WINDOW_HEIGHT * 0.18,
                    width=WINDOW_WIDTH * 0.85,
                    padding=padding.only(left=WINDOW_WIDTH * 0.05, right=WINDOW_WIDTH * 0.05),
                    content=Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
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
                                                size=DEAL_FONT_SIZE - 3,
                                                font_family='Poppins Regular',
                                                color=TEXT_COLOR,
                                            ),
                                            Text(
                                                values[4],
                                                size=DEAL_FONT_SIZE - 3,
                                                font_family='Poppins Regular',
                                                color=TEXT_COLOR,
                                            ),
                                        ],
                                        alignment=MainAxisAlignment.START,
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                spacing=2,
                            ),
                            Container(
                                on_click=lambda _: self.delete(values[0]),
                                content=Column(
                                    controls=[
                                        Container(
                                            height=WINDOW_WIDTH * 0.115,
                                            width=WINDOW_WIDTH * 0.115,
                                            border_radius=BORDER_RADIUS,
                                            bgcolor=BTN_DELETE_COLOR,
                                            content=Image(
                                                # height=40,
                                                # width=40,
                                                scale=1.2,
                                                src="assets/icons/cross.svg",
                                                color=TEXT_COLOR,
                                            ),
                                            alignment=alignment.center,
                                        ),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
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
                                                        on_click=lambda _: self.page.go('/single_car'),
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.CENTER,
                                            ),
                                            Column(
                                                controls=[
                                                    Container(
                                                        content=Text(
                                                            f"История сделки",
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
                                    "Транзакции",
                                    size=BASE_FONT_SIZE,
                                    color=HINT_COLOR,
                                    font_family='poppins regular'
                                ),
                            ),
                            *self.incomes,
                            Container(
                                height=WINDOW_HEIGHT * 0.015
                            ),
                        ],
                        spacing=WINDOW_HEIGHT * 0.05,
                    ),
                ),
                Container(
                    height=WINDOW_HEIGHT * (0 if len(self.incomes) >= 4
                                            else 0.125 * (4 - len(self.incomes)))
                ),
                Row(
                    controls=[
                        Container(
                            content=ElevatedButton(
                                text="Удалить сделку",
                                style=ButtonStyle(
                                    bgcolor={
                                        MaterialState.HOVERED: RED_COLOR,
                                        "": BTN_DELETE_COLOR
                                    },
                                    color=TEXT_COLOR,
                                ),
                                width=WINDOW_WIDTH * 0.6,
                                on_click=lambda _: self.delete_deal(),
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
