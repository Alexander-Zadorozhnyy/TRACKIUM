from pages.Congrats.add_congrats_abstract import AddCongratsAbstract


class AddCarCongrats(AddCongratsAbstract):
    def __init__(self, page):
        super().__init__(page)
        self.back_route = "/cars"
        self.button_text = "Мои машины"
        self.text = "Машина успешно добавлена"
        self.img = "assets/icons/congrats.svg"