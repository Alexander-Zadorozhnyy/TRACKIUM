from pages.Congrats.add_congrats_abstract import AddCongratsAbstract


class RemoveDealCongrats(AddCongratsAbstract):
    def __init__(self, page):
        super().__init__(page)
        self.back_route = "/deals"
        self.button_text = "Сделки"
        self.text = "Выбранная сделка удалена"
        self.img = "assets/icons/delete.svg"