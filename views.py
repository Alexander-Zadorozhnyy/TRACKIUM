from flet import *

from pages.AddPages.add_car import AddCar
from pages.Congrats.add_car_congrats import AddCarCongrats
from pages.AddPages.add_deal import AddDeal
from pages.AddPages.add_expense import AddExpense
from pages.AddPages.add_income import AddIncome
from pages.Car.cars import Cars
from pages.Car.history import History
from pages.Car.single_car import SingleCar
from pages.Congrats.add_deal_congrats import AddDealCongrats
from pages.Congrats.add_expense_congrats import AddExpenseCongrats
from pages.Congrats.add_income_congrats import AddIncomeCongrats
from pages.Congrats.remove_car_congrats import RemoveCarCongrats
from pages.Congrats.remove_deal_congrats import RemoveDealCongrats
from pages.Congrats.remove_expense_congrats import RemoveExpenseCongrats
from pages.Congrats.remove_income_congrats import RemoveIncomeCongrats
from pages.Login.start_page import StartPage
from pages.Login.login import Login
from pages.Login.register import Register
from pages.Congrats.congrats import Congrats
from pages.deals import Deals
from pages.finance import Finance
from pages.profile import Profile
from pages.transactions import Transactions
from pages.home import Home


def views_handler(page, user=None):
    return {
        '/start_page': View(
            route='/start_page',
            controls=[
                StartPage(page, user)
            ]
        ),
        '/register': View(
            route='/register',
            controls=[
                Register(page, user, 0)
            ]
        ),
        '/register_fail': View(
            route='/',
            controls=[
                Register(page, user, 1)
            ]
        ),
        '/login': View(
            route='/login',
            controls=[
                Login(page, user, 0)
            ]
        ),
        '/login_fail': View(
            route='/login',
            controls=[
                Login(page, user, 1)
            ]
        ),
        '/home': View(
            route='/',
            controls=[
                Home(page, user)
            ]
        ),
        '/congrats': View(
            route='/congrats',
            controls=[
                Congrats(page, user)
            ]
        ),
        '/add_car_congrats': View(
            route='/add_car_congrats',
            controls=[
                AddCarCongrats(page)
            ]
        ),
        f'/cars': View(
            route='/cars',
            controls=[
                Cars(page, user)
            ]
        ),
        '/single_car': View(
            route='/single_car',
            controls=[
                SingleCar(page, user)
            ]
        ),
        '/history': View(
            route='/history',
            controls=[
                History(page, user)
            ]
        ),
        '/add_car': View(
            route='/add_car',
            controls=[
                AddCar(page, user, 0)
            ]
        ),
        '/add_car_fail': View(
            route='/add_car',
            controls=[
                AddCar(page, user, 1)
            ]
        ),
        '/remove_car_congrats': View(
            route='/remove_car_congrats',
            controls=[
                RemoveCarCongrats(page)
            ]
        ),
        '/finance': View(
            route='/finance',
            controls=[
                Finance(page, user)
            ]
        ),
        '/transactions': View(
            route='/transactions',
            controls=[
                Transactions(page)
            ]
        ),
        '/add_income': View(
            route='/add_income',
            controls=[
                AddIncome(page, user, 0)
            ]
        ),
        '/add_income_congrats': View(
            route='/add_income_congrats',
            controls=[
                AddIncomeCongrats(page)
            ]
        ),
        '/add_income_fail': View(
            route='/add_income',
            controls=[
                AddIncome(page, user, 1)
            ]
        ),
        '/remove_income_congrats': View(
            route='/remove_income_congrats',
            controls=[
                RemoveIncomeCongrats(page, 0)
            ]
        ),
        '/remove_income_congrats_fin': View(
            route='/remove_income_congrats',
            controls=[
                RemoveIncomeCongrats(page, 1)
            ]
        ),
        '/add_expense': View(
            route='/add_expense',
            controls=[
                AddExpense(page, user, 0)
            ]
        ),
        '/add_expense_congrats': View(
            route='/add_expense_congrats',
            controls=[
                AddExpenseCongrats(page)
            ]
        ),
        '/add_expense_fail': View(
            route='/add_expense',
            controls=[
                AddExpense(page, user, 1)
            ]
        ),
        '/remove_expense_congrats': View(
            route='/remove_expense_congrats',
            controls=[
                RemoveExpenseCongrats(page, 0)
            ]
        ),
        '/remove_expense_congrats_fin': View(
            route='/remove_expense_congrats',
            controls=[
                RemoveExpenseCongrats(page, 1)
            ]
        ),
        '/deals': View(
            route='/deals',
            controls=[
                Deals(page, user)
            ]
        ),
        '/add_deal': View(
            route='/add_deal',
            controls=[
                AddDeal(page, user, 0)
            ]
        ),
        '/add_deal_congrats': View(
            route='/add_deal_congrats',
            controls=[
                AddDealCongrats(page)
            ]
        ),
        '/add_deal_fail': View(
            route='/add_deal',
            controls=[
                AddDeal(page, user, 1)
            ]
        ),
        '/remove_deal_congrats': View(
            route='/remove_deal_congrats',
            controls=[
                RemoveDealCongrats(page)
            ]
        ),
        '/profile': View(
            route='/profile',
            controls=[
                Profile(page, user)
            ]
        ),
    }
