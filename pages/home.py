import math
from datetime import datetime

from flet import *
from utils.config import *


class Home(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

        incomes = list(map(lambda x: (x[5], True, x[6]),
                           self.user.db.get_incomes(self.user.user_id) if self.user.user_id is not None else []))
        expenses = list(map(lambda x: (x[3], False, x[4]),
                            self.user.db.get_expenses(self.user.user_id) if self.user.user_id is not None else []))

        transactions = sorted(incomes + expenses, key=lambda x: x[-1])[::-1]

        self.transactions = [self.create_card(*x[:-1]) for x in transactions]

        cur_year = datetime.now().year
        self.graph = {i: sum(list(
            map(lambda y: y[0] if y[1] else -y[0],
                list(filter(lambda x: x[-1].year == cur_year and x[-1].month - 1 == i, transactions)))))
            for i in range(12)}
        self.months = ["Янв", "Февр", "Март", "Апр", "Май", "Июнь", "Июль", "Авг", "Сент", "Окт", "Нояб", "Дек"]

    @staticmethod
    def create_card(sym, type):
        return Row(
            width=WINDOW_WIDTH * 0.7,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Container(
                    padding=padding.only(left=WINDOW_WIDTH * 0.05, right=WINDOW_WIDTH * 0.05),
                    content=Row(
                        width=WINDOW_WIDTH * 0.7,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Column(
                                controls=[
                                    Text(
                                        f"{sym}",
                                        size=DEAL_FONT_SIZE,
                                        font_family='Poppins Bold',
                                        color=TEXT_COLOR,
                                        text_align=TextAlign.CENTER,
                                    ),
                                ]
                            ),
                            Column(
                                controls=[
                                    Container(
                                        border_radius=10,
                                        width=WINDOW_WIDTH * 0.25,
                                        bgcolor=GREEN_COLOR if type else BTN_DELETE_COLOR,
                                        content=Text(
                                            f"{'Прибыль' if type else 'Расходы'}",
                                            size=DEAL_FONT_SIZE,
                                            font_family='Poppins Bold',
                                            color=TEXT_FIELD_COLOR if type else RED_COLOR,
                                            text_align=TextAlign.CENTER,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        )

    def create_bar_chart_group(self, x, y, tooltip, color):
        return BarChartGroup(
            x=x,
            bar_rods=[
                BarChartRod(
                    from_y=0,
                    to_y=y,
                    width=10,
                    color=color,
                    tooltip=tooltip,
                    border_radius=0,
                ),
            ],
        )

    def get_chart(self):
        return BarChart(
            scale=0.8,
            bar_groups=[
                *[self.create_bar_chart_group(30 * i, self.graph[i], self.months[i], GRAPH_COLORS[i]) for i in
                  list(self.graph.keys())]  #
            ],
            border=border.all(1, colors.GREY_400),
            left_axis=ChartAxis(
                labels_interval=30000,
                labels_size=50, title=Text("Доходы"), title_size=20
            ),
            bottom_axis=ChartAxis(
                labels=[
                    *[ChartAxisLabel(
                        value=30 * i, label=Container(Text(self.months[i]), padding=10)
                    ) for i in range(0, 12, 2)]
                ],
                labels_size=50,
            ),
            horizontal_grid_lines=ChartGridLines(
                color=colors.GREY_300,
                width=1,
                # dash_pattern=[3, 3],
                interval=15000
            ),
            # tooltip_bgcolor=colors.with_opacity(0.5, colors.GREY_300),
            max_y=max(self.graph.values()),
            # interactive=True,
            expand=True,
        )

    def build(self):
        return Column(
            height=WINDOW_HEIGHT,
            # spacing=30,
            # scroll=ScrollMode.HIDDEN,
            controls=[
                Column(
                    height=WINDOW_HEIGHT * 0.85,
                    controls=[
                        Container(
                            padding=padding.only(top=WINDOW_HEIGHT * 0.02, bottom=WINDOW_HEIGHT * 0.02),
                            content=Column(
                                controls=[
                                    Container(
                                        width=WINDOW_WIDTH * 0.95,
                                        height=WINDOW_HEIGHT * 0.15,
                                        content=Row(
                                            controls=[
                                                Container(
                                                    # padding=padding.only(left=WINDOW_WIDTH * 0.05),
                                                    content=Row(
                                                        controls=[
                                                            Column(
                                                                height=WINDOW_HEIGHT * 0.15,
                                                                width=WINDOW_WIDTH * 0.12,
                                                                controls=[
                                                                    Container(
                                                                        height=WINDOW_HEIGHT * 0.15,
                                                                        width=WINDOW_WIDTH * 0.15,
                                                                        content=Image(
                                                                            src="assets/icons/profile.svg",
                                                                            scale=1,
                                                                        ),
                                                                    ),
                                                                ],
                                                                alignment=MainAxisAlignment.CENTER,
                                                            ),
                                                            Column(
                                                                height=WINDOW_HEIGHT * 0.15,
                                                                width=WINDOW_WIDTH * 0.3,
                                                                controls=[
                                                                    Row(
                                                                        controls=[
                                                                            Column(
                                                                                controls=[
                                                                                    Row(
                                                                                        controls=[
                                                                                            Text(
                                                                                                "Добро пожаловать,",
                                                                                                size=DEAL_FONT_SIZE - 4,
                                                                                                color=TEXT_COLOR,
                                                                                                font_family='poppins regular'
                                                                                            )
                                                                                        ],
                                                                                    ),
                                                                                    Row(
                                                                                        controls=[
                                                                                            Text(
                                                                                                f"{self.user.user_name}!",
                                                                                                size=DEAL_FONT_SIZE + 2,
                                                                                                color=TEXT_COLOR,
                                                                                                font_family='poppins regular'
                                                                                            )
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ],
                                                                alignment=MainAxisAlignment.CENTER,
                                                            ),
                                                        ],
                                                        # spacing=10,
                                                    )
                                                ),
                                                Column(
                                                    controls=[
                                                        Container(
                                                            height=WINDOW_WIDTH * 0.15,
                                                            width=WINDOW_WIDTH * 0.4,
                                                            content=Image(
                                                                src="assets/icons/name.svg",
                                                                scale=0.9,
                                                            ),
                                                        ),
                                                    ],
                                                    alignment=MainAxisAlignment.CENTER,
                                                ),
                                            ],
                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        ),
                                    ),
                                    Row(
                                        controls=[
                                            Container(
                                                height=WINDOW_HEIGHT * 0.5,
                                                width=WINDOW_WIDTH * 0.85,
                                                content=self.get_chart(),
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
                                                        height=WINDOW_HEIGHT * 0.3 + WINDOW_HEIGHT * 0.05 * (
                                                                len(self.transactions) - 2),
                                                        width=WINDOW_WIDTH * 0.85,
                                                        padding=padding.only(left=WINDOW_WIDTH * 0.03,
                                                                             right=WINDOW_WIDTH * 0.03,
                                                                             top=WINDOW_WIDTH * 0.03),
                                                        content=Column(
                                                            controls=[
                                                                Row(
                                                                    controls=[
                                                                        Column(
                                                                            controls=[
                                                                                Container(
                                                                                    height=WINDOW_WIDTH * 0.12,
                                                                                    width=WINDOW_WIDTH * 0.12,
                                                                                    border_radius=10,
                                                                                    bgcolor=LIGHT_GREEN_COLOR,
                                                                                    content=Image(
                                                                                        # height=40,
                                                                                        # width=40,
                                                                                        scale=1,
                                                                                        src="assets/icons/money.svg",
                                                                                        color=GREEN_COLOR,
                                                                                    ),
                                                                                    alignment=alignment.center,
                                                                                ),
                                                                            ],
                                                                        ),

                                                                        Column(
                                                                            controls=[
                                                                                Container(
                                                                                    on_click=lambda _: self.page.go(
                                                                                        '/transactions'),
                                                                                    height=WINDOW_WIDTH * 0.12,
                                                                                    width=WINDOW_WIDTH * 0.12,
                                                                                    border_radius=10,
                                                                                    bgcolor=DEAL_CIRCLE_COLOR,
                                                                                    content=Image(
                                                                                        # height=40,
                                                                                        # width=40,
                                                                                        scale=1,
                                                                                        src="assets/icons/plus.svg",
                                                                                        color=TEXT_FIELD_COLOR,
                                                                                    ),
                                                                                    alignment=alignment.center,
                                                                                ),
                                                                            ],
                                                                        ),

                                                                    ],
                                                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                                ),
                                                                Row(
                                                                    controls=[
                                                                        Container(
                                                                            padding=padding.only(
                                                                                left=WINDOW_WIDTH * 0.01),
                                                                            content=Text(
                                                                                "Банковская история",
                                                                                size=DEAL_FONT_SIZE,
                                                                                font_family='Poppins Bold',
                                                                                color=TEXT_COLOR,
                                                                                text_align=TextAlign.CENTER,
                                                                            ),
                                                                        ),

                                                                    ],
                                                                    alignment=MainAxisAlignment.START,
                                                                ),
                                                                *self.transactions,
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
                            ),
                        ),
                    ],
                    scroll=ScrollMode.HIDDEN,
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
        )
