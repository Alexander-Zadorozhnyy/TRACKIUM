import datetime

from flet import *

from pages.AddPages.add_abstruct import AddAbstract
from utils.config import *


class AddExpense(AddAbstract):
    def __init__(self, page, user, status):
        super().__init__(page, user, status)
        self.title = "Добавить платеж"
        self.back_route = "/transactions"

        cars = [self.user.db.get_output(i[0]) for i in
                self.user.db.get_cars(self.user.user_id)] if self.user.user_id is not None else []  # 39

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

        self.description = TextField(
            keyboard_type=KeyboardType.TEXT,
            hint_text='Описание',
            hint_style=TextStyle(
                size=BASE_FONT_SIZE,
                font_family='Poppins Regular',
                color=HINT_COLOR,
            ),
            max_length=15,
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

        self.values = [
            self.car,
            self.sum,
            self.is_cash,
            self.description,
            self.date,
        ]

        self.error = [Container() for _ in range(4)] + [Text(
            value="Проверьте корректность введенных данных!",
            color='red',
            font_family='poppins regular'

        ) if status == 1 else Container()]

    def check(self):
        try:
            date = datetime.date(*list(map(int, self.date.value.split(".")))[::-1])
            car_id = self.user.db.get_car_id(self.car.value)[0]
            if self.user.db.insert_expense_to_database((self.user.user_id,
                                                        car_id,
                                                        self.sum.value,
                                                        date,
                                                        self.is_cash.value,
                                                        self.description.value,)
                                                       ):
                self.page.go('/add_expense_congrats')
            else:
                self.page.go('/add_expense_fail')
        except Exception as ex:
            print(f"[Add] {ex}")
            self.page.go('/add_expense_fail')
