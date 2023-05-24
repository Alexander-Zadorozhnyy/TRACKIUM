from flet import *

from utils.config import *


class StartPage(UserControl):
    def __init__(self, page, user):
        super().__init__()
        self.page = page
        self.user = user

    def build(self):
        return Column(
            height=WINDOW_HEIGHT,
            controls=[
                Row(
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    height=100,
                                    width=200,
                                    content=Image(
                                        src="assets/images/logo.svg",
                                        scale=1.7,
                                    ),
                                ),
                                Container(
                                    height=30,
                                    width=200,
                                    content=Image(
                                        src="assets/images/name.svg",
                                        scale=1.2,
                                    ),
                                ),
                            ],
                            spacing=10,
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        Container(
                            on_click=lambda _: self.page.go('/register'),
                            content=Text(f"Регистрация",
                                         size=BASE_FONT_SIZE,
                                         color=TEXT_COLOR,
                                         text_align=TextAlign.CENTER,
                                         font_family='poppins regular'
                                         )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        Container(
                            on_click=lambda _: self.page.go('/login'),
                            content=Text(f"Авторизация",
                                         size=BASE_FONT_SIZE,
                                         color=TEXT_COLOR,
                                         font_family='poppins regular'
                                         )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            spacing=50,
        )

# Container(
#     height=WINDOW_HEIGHT, width=WINDOW_WIDTH,
#     bgcolor=BG_COLOR,
#     content=Column(
#         controls=[
#             Text('Welcome back \n This is the register pages'),
#             Container(
#                 on_click=lambda _: self.page.go('/'),
#                 content=Text('Goto Home', size=25, color='black')
#             )
#         ]
#     )
# )
