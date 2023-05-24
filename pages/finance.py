from flet import *
from flet.plotly_chart import PlotlyChart
from utils.config import *

import plotly.graph_objects as go


class Finance(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

        cars = [self.user.db.get_output(i[0]) for i in
                self.user.db.get_fin_cars(self.user.user_id)] if self.user.user_id is not None else []
        cars = [(int(x[0]), x[1]) for x in cars]

        incomes = list(map(lambda x: (x[0], x[2], x[5], True, x[4], x[7], x[6]),
                           self.user.db.get_incomes(self.user.user_id) if self.user.user_id is not None else []))
        expenses = list(map(lambda x: (x[0], x[2], x[3], False, x[6], x[5], x[4]),
                            self.user.db.get_expenses(self.user.user_id) if self.user.user_id is not None else []))

        transactions = sorted(incomes + expenses, key=lambda x: x[-1])[::-1]

        transactions_print = []

        for tr in transactions:
            data = f"{'От' if tr[3] else 'Описание'}: {tr[4]}"
            date = f"Дата: {tr[-1].strftime('%d.%m.%Y')}"
            sym_int = f"Сумма: {tr[2]}"
            is_cash = f"Наличные: {'да' if tr[5] else 'нет'}"

            transactions_print += [(tr[0], tr[3], data, date, sym_int, is_cash)]

        self.transactions = [self.create_card(income) for income in transactions_print]

        self.graph = {car[1]: sum(list(
            map(lambda y: y[2] if y[3] else -y[2],
                list(filter(lambda x: x[1] == car[0], transactions)))))
            for car in cars}

    def get_plotly_chart(self):
        # layout = go.Layout(paper_bgcolor=BG_COLOR)
        fig = go.Figure(data=[go.Pie(labels=list(self.graph.keys()), values=list(self.graph.values()))],
                        # layout=layout
                        )
        return PlotlyChart(fig, expand=True)

    def delete_income(self, id):
        self.user.db.delete_income_from_database(id)
        self.page.go('/remove_income_congrats_fin')

    def delete_expense(self, id):
        self.user.db.delete_expense_from_database(id)
        self.page.go('/remove_expense_congrats_fin')

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
                                        width=WINDOW_WIDTH * 0.6,
                                        controls=[
                                            Text(
                                                values[2],
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
                                            Text(
                                                values[4],
                                                size=DEAL_FONT_SIZE - 3,
                                                font_family='Poppins Regular',
                                                color=TEXT_COLOR,
                                            ),
                                            Text(
                                                values[5],
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
                                on_click=lambda _: self.delete_income(values[0]) if values[1] else self.delete_expense(
                                    values[0]),
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
            scroll=ScrollMode.HIDDEN,
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
                                                            "Финансы",
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
                        Column(
                            controls=[
                                Container(
                                    height=WINDOW_HEIGHT * 0.6,
                                    width=WINDOW_WIDTH,
                                    padding=padding.only(left=-WINDOW_WIDTH * 0.2, ),
                                    scale=1,
                                    content=self.get_plotly_chart(),
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
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
                            *self.transactions,
                            Container(
                                height=WINDOW_HEIGHT * 0.015
                            ),
                        ],
                        spacing=WINDOW_HEIGHT * 0.05,
                    ),
                ),
            ],
        )
