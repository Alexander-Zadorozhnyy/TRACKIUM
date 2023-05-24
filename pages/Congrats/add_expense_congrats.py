from pages.Congrats.add_congrats_abstract import AddCongratsAbstract


class AddExpenseCongrats(AddCongratsAbstract):
    def __init__(self, page):
        super().__init__(page)
        self.back_route = "/transactions"
        self.button_text = "Транзакции"
        self.text = "Платеж успешно добавлен"
        self.img = "assets/icons/congrats.svg"