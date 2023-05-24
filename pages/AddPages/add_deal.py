import datetime

from flet import *

from pages.AddPages.add_abstruct import AddAbstract
from utils.config import *


class AddDeal(AddAbstract):
    def __init__(self, page, user, status):
        super().__init__(page, user, status)
        self.title = "Добавить сделку"
        self.back_route = "/deals"

        cars = [self.user.db.get_output(i[0]) for i in
                self.user.db.get_cars(self.user.user_id)] if self.user.user_id is not None else []  # 39

        self.A = TextField(
            keyboard_type=KeyboardType.NUMBER,
            hint_text='Откуда',
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

        self.B = TextField(
            keyboard_type=KeyboardType.NUMBER,
            hint_text='Куда',
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

        self.company = TextField(
            keyboard_type=KeyboardType.NUMBER,
            hint_text='Компания',
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

        self.sum = TextField(
            keyboard_type=KeyboardType.NUMBER,
            hint_text='Сумма',
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

        self.date = TextField(
            keyboard_type=KeyboardType.DATETIME,
            hint_text='Дата - dd.mm.yyyy',
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

        self.car = Dropdown(
            border=InputBorder.NONE,
            hint_text='Машина',
            hint_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=HINT_COLOR,
            ),
            width=WINDOW_WIDTH * 0.7,
            options=[
                *[dropdown.Option(car[2]) for car in cars]
            ],
        )

        self.error = [Container() for _ in range(5)] + [Text(
            value="Проверьте корректность введенных данных!",
            color='red',
            font_family='poppins regular'

        ) if status == 1 else Container()]
        self.values = [
            self.A,
            self.B,
            self.company,
            self.date,
            self.sum,
            self.car,
        ]

    def check(self):
        try:
            date = datetime.date(*list(map(int, self.date.value.split(".")))[::-1])
            car_id = self.user.db.get_car_id(self.car.value)[0]

            if self.user.db.insert_deal_to_database((self.user.user_id,
                                                     car_id,
                                                     self.A.value,
                                                     self.B.value,
                                                     self.company.value,
                                                     self.sum.value,
                                                     date,
                                                     )):
                self.page.go('/add_deal_congrats')
            else:
                self.page.go('/add_deal_fail')
        except Exception as ex:
            print(f"[Deal] {ex}")
            self.page.go('/add_deal_fail')
