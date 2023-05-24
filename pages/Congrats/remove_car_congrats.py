from pages.Congrats.add_congrats_abstract import AddCongratsAbstract


class RemoveCarCongrats(AddCongratsAbstract):
    def __init__(self, page):
        super().__init__(page)
        self.back_route = "/cars"
        self.button_text = "Машины"
        self.text = "Выбранная машина удалена"
        self.img = "assets/icons/delete.svg"