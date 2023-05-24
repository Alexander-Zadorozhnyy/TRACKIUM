import datetime

import deal as deal
from flet import *

from pages.AddPages.add_abstruct import AddAbstract
from utils.config import *


class AddIncome(AddAbstract):
    def __init__(self, page, user, status):
        super().__init__(page, user, status)
        self.title = "Добавить поступление"
        self.back_route = "/transactions"

        cars = [self.user.db.get_output(i[0]) for i in
                self.user.db.get_cars(self.user.user_id)] if self.user.user_id is not None else []
        # print(cars[0] if cars != [] else "")
        deals = [i for i in
                 self.user.db.get_deals(self.user.user_id)] if self.user.user_id is not None else []
        formated_deals = list(map(lambda x: f'Направление: {x[2]}-{x[3]}. \n'
                                            f"Дата: {x[-1].strftime('%d.%m.%Y')}.\n"
                                            f'Машины: {", ".join([y[2] for y in cars if int(y[0]) == x[1]])}.', deals
                                  )
                              )

        self.sender = TextField(
            keyboard_type=KeyboardType.NUMBER,
            hint_text='Отправитель',
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

        self.is_cash = Dropdown(
            border=InputBorder.NONE,
            hint_text='Наличные',
            hint_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=HINT_COLOR,
            ),
            width=WINDOW_WIDTH * 0.7,
            options=[
                dropdown.Option(key=True,
                                text="Да"),
                dropdown.Option(key=False,
                                text="Нет"),
            ],
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

        self.deal = Dropdown(
            border=InputBorder.NONE,
            hint_text='Сделка',
            hint_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=HINT_COLOR,
            ),
            width=WINDOW_WIDTH * 0.7,
            options=[
                *[dropdown.Option(
                    key=deals[i][0],
                    text=formated_deals[i]
                ) for i in range(len(deals))]
            ],
        )

        self.values = [
            self.sender,
            self.sum,
            self.is_cash,
            self.date,
            self.car,
            self.deal,
        ]

        self.error = [Container() for _ in range(5)] + [Text(
            value="Проверьте корректность введенных данных!",
            color='red',
            font_family='poppins regular'

        ) if status == 1 else Container()]

    def check(self):
        try:
            date = datetime.date(*list(map(int, self.date.value.split(".")))[::-1])
            car_id = self.user.db.get_car_id(self.car.value)[0]
            if self.user.db.insert_income_to_database((self.user.user_id,
                                                       car_id,
                                                       self.deal.value,
                                                       self.sender.value,
                                                       self.sum.value,
                                                       date,
                                                       self.is_cash.value,)
                                                      ):
                self.page.go('/add_income_congrats')
            else:
                self.page.go('/add_income_fail')
        except Exception as ex:
            print(f"[Add] {ex}")
            self.page.go('/add_income_fail')
