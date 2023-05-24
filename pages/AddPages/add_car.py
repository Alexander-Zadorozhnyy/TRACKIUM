import datetime

from flet import *

from pages.AddPages.add_abstruct import AddAbstract
from utils.config import *


class AddCar(AddAbstract):
    def __init__(self, page, user, status):
        super().__init__(page, user, status)
        self.title = "Добавить машину"
        self.back_route = "/cars"

        self.driver = TextField(
            keyboard_type=KeyboardType.NAME,
            hint_text='Имя водителя',
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

        self.contact = TextField(
            keyboard_type=KeyboardType.PHONE,
            hint_text='Контакт',
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

        self.licence_plate = TextField(
            keyboard_type=KeyboardType.TEXT,
            hint_text='Номер машины',
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
            self.driver,
            self.contact,
            self.date,
            self.licence_plate,
        ]

        self.error = [Container() for _ in range(3)] + [Text(
            value="Проверьте корректность введенных данных!",
            color='red',
            font_family='poppins regular'

        ) if status == 1 else Container()]

    def check(self):
        try:
            date = datetime.date(*list(map(int, self.date.value.split(".")))[::-1])
            print(f"LP: {self.licence_plate.value}")
            if self.user.db.insert_car_to_database((self.user.user_id,
                                                    self.driver.value,
                                                    self.contact.value,
                                                    date,
                                                    "".join(self.licence_plate.value.split()))
                                                   ):
                self.page.go('/add_car_congrats')
            else:
                self.page.go('/add_car_fail')
        except Exception as ex:
            print(f"[Add] {ex}")
            self.page.go('/add_car_fail')
