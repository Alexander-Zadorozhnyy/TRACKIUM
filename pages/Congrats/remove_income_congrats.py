from pages.Congrats.add_congrats_abstract import AddCongratsAbstract


class RemoveIncomeCongrats(AddCongratsAbstract):
    def __init__(self, page, status):
        super().__init__(page)
        self.back_route = "/transactions" if status == 0 else "/finance"
        self.button_text = "Транзакции"  if status == 0 else "Финансы"
        self.text = "Выбранное поступление удалено"
        self.img = "assets/icons/delete.svg"