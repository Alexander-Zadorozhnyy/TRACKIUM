from pages.Congrats.add_congrats_abstract import AddCongratsAbstract


class AddDealCongrats(AddCongratsAbstract):
    def __init__(self, page):
        super().__init__(page)
        self.back_route = "/deals"
        self.button_text = "Сделки"
        self.text = "Сделка успешно добавлена"
        self.img = "assets/icons/congrats.svg"