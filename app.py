from flet import *
import psycopg2

from views import views_handler

from utils.config import DEVICE_HEIGHT, DEVICE_WIDTH

host = "dpg-cgt5rhl269vbmesuapn0-a.oregon-postgres.render.com"
user = "admin"
password = "JAxVoO3oYMC5681LPi3FXYUk96hZvcsj"
db_name = "db_truckium"


class TRUCKIUMDatabase:
    def __init__(self):
        self.conn = None

    @staticmethod
    def get_output(x):
        x = x.replace("(", "").replace(")", "")
        return x.split(",")

    def connect_to_database(self):
        try:
            self.conn = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )

            self.conn.autocommit = True

            with self.conn.cursor() as cur:
                cur.execute(open("TRUCKIUM.sql", "r").read())
                print("Work DONE")

                # cur.execute("""SELECT table_name FROM information_schema.tables
                #        WHERE table_schema = 'public'""")
                # for table in cur.fetchall():
                #     print(table)

        except Exception as ex:
            print(f"[INFO] {ex}")
        # finally:
        #     if conn:
        #         conn.close()
        #         print("[INFO] Connection closed!")

    def reset_database(self):
        try:
            with self.conn.cursor() as cur:
                request = """SELECT table_name FROM information_schema.tables
                       WHERE table_schema = 'public'"""
                cur.execute(request)
                for table in cur.fetchall():
                    req = f'''DROP TABLE "{table[0]}" CASCADE'''
                    cur.execute(req)

        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_user_data(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT ("Id", "UserName") FROM "User" WHERE "UserEmail" = '{values[0]}' 
                AND "UserPassword" = '{values[1]}'"""
                cur.execute(request, values)
                return cur.fetchone()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_user_name(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT "UserName" FROM "User" WHERE "Id" = '{values}'"""
                cur.execute(request, values)
                return cur.fetchone()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def insert_to_database(self, table, params, values):
        try:
            with self.conn.cursor() as cur:
                request_params = '"' + '", "'.join(params) + '"'
                reuest_values = ", ".join(['%s' for _ in range(len(params))])
                request = f"""INSERT INTO "{table}" ({request_params}) VALUES ({reuest_values})"""
                cur.execute(request, values)
                print(f"Element in table {table} added!")

        except Exception as ex:
            print(f"[INFO] {ex}")
            return False

        return True

    def delete_from_database(self, table, values):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"""DELETE FROM "{table}" WHERE "Id" = {values}""")
                print("Item was deleted!")

        except Exception as ex:
            print(f"[INFO] {ex}")
            return False

        return True

    def insert_user_to_database(self, values):
        return self.insert_to_database("User",
                                       ["UserName", "UserEmail", "UserPassword"],
                                       values)

    def delete_user_from_database(self, values):
        return self.delete_from_database("User", values)

    def insert_car_to_database(self, values):
        return self.insert_to_database("Car",
                                       ["User", "Driver", "Contact", "Date", "LicencePlate"],
                                       values)

    def get_cars(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT ("Id", "Driver", "LicencePlate", "Contact", "Date")
                 FROM "Car" 
                 WHERE "User" = '{values}'
                 ORDER BY "Date" DESC
"""
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_fin_cars(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT ("Id", "LicencePlate")
                 FROM "Car" 
                 WHERE "User" = '{values}'
                 ORDER BY "Date" DESC
"""
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_car_id(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT "Id" FROM "Car" WHERE "LicencePlate" = '{values}'"""
                cur.execute(request, values)
                return cur.fetchone()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_car_from_id(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT * FROM "Car" WHERE "Id" = '{values}'"""
                cur.execute(request, values)
                return cur.fetchone()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def delete_car_from_database(self, values):
        try:
            with self.conn.cursor() as cur:
                for table in ["Income", "Expense", "Deal"]:
                    cur.execute(f"""DELETE FROM "{table}" WHERE "Car" = {values}""")
                    print("Car was deleted!")
                return self.delete_from_database("Car", values)

        except Exception as ex:
            print(f"[INFO] {ex}")
            return False

    def insert_deal_to_database(self, values):
        return self.insert_to_database("Deal",
                                       ["User", "Car", "From", "To", "Company", "Sum", "Date"],
                                       values)

    def get_deals(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT *
                 FROM "Deal" 
                 WHERE "User" = '{values}'
                 ORDER BY "Date" DESC
"""
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_deal_from_car_id(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT * FROM "Deal" 
                WHERE "Car" = '{values}'
                ORDER BY "Date" DESC
"""
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def delete_deal_from_database(self, values):
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"""DELETE FROM "Income" WHERE "Deal" = {values}""")
                return self.delete_from_database("Deal", values)

        except Exception as ex:
            print(f"[INFO] {ex}")
            return False

    def insert_income_to_database(self, values):
        return self.insert_to_database("Income",
                                       ["User", "Car", "Deal", "Sender", "Sum", "Date", "IsCash"],
                                       values)

    def get_incomes(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT *
                         FROM "Income" 
                         WHERE "User" = '{values}'
                         ORDER BY "Date" DESC
        """
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_income_from_deal_id(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""
                SELECT * FROM "Income" 
                WHERE "Deal" = '{values}' 
                ORDER BY "Date" DESC
"""
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_income_from_car_id(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT * FROM "Income" 
                WHERE "Car" = '{values}'
                ORDER BY "Date" DESC
"""
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def delete_income_from_database(self, values):
        return self.delete_from_database("Income", values)

    def insert_expense_to_database(self, values):
        return self.insert_to_database("Expense",
                                       ["User", "Car", "Sum", "Date", "IsCash", "Description"],
                                       values)

    def get_expenses(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT *
                         FROM "Expense" 
                         WHERE "User" = '{values}'
                         ORDER BY "Date" DESC
        """
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def get_expense_from_car_id(self, values):
        try:
            with self.conn.cursor() as cur:
                request = f"""SELECT * FROM "Expense" 
                WHERE "Car" = '{values}'
                ORDER BY "Date" DESC
"""
                cur.execute(request, values)
                return cur.fetchall()
        except Exception as ex:
            print(f"[INFO] {ex}")
            return None

    def delete_expense_from_database(self, values):
        return self.delete_from_database("Expense", values)

    def test(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Income" """)
                for table in cur.fetchall():
                    print(table)
                cur.execute("""SELECT * FROM "Expense" """)
                for table in cur.fetchall():
                    print(table)
        except Exception as ex:
            print(f"[INFO] {ex}")
            return False

        return True

    # def UpdateDatabase(self, values):
    #     self.c.execute("UPDATE tasks SET Task = ? WHERE Task=?", values)
    #     self.db.commit()

    def close_database(self):
        self.conn.close()


class CurrentUser:
    def __init__(self, db, user_id=None, user_name=None, car=None, deal=None):
        self.db = db
        self.user_id = user_id
        self.user_name = user_name
        self.car = car
        self.deal = deal


class App(UserControl):
    def __init__(self, pg: Page):
        super().__init__()

        pg.window_title_bar_hidden = True
        pg.window_frameless = True
        pg.window_title_bar_buttons_hidden = True
        pg.window_movable = True
        pg.bgcolor = colors.TRANSPARENT
        pg.window_bgcolor = colors.TRANSPARENT
        pg.fonts = {
            "Poppins ThinItalic": "fonts/poppins/Poppins-ThinItalic.ttf",
            "Poppins Thin": "fonts/poppins/Poppins-Thin.ttf",
            "Poppins Semibold": "fonts/poppins/Poppins-Semibold.ttf",
            "Poppins SemiboldItalic": "fonts/poppins/Poppins-SemiboldItalic.ttf",
            "Poppins Regular": "fonts/poppins/Poppins-Regular.ttf",
            "Poppins MediumItalic": "fonts/poppins/Poppins-MediumItalic.ttf",
            "Poppins Medium": "fonts/poppins/Poppins-Medium.ttf",
            "Poppins LightItalic": "fonts/poppins/Poppins-LightItalic.ttf",
            "Poppins Light": "fonts/poppins/Poppins-Light.ttf",
            "Poppins Italic": "fonts/poppins/Poppins-Italic.ttf",
            "Poppins ExtraLightItalic": "fonts/poppins/Poppins-ExtraLightItalic.ttf",
            "Poppins ExtraLight": "fonts/poppins/Poppins-ExtraLight.ttf",
            "Poppins ExtraBold": "fonts/poppins/Poppins-ExtraBold.ttf",
            "Poppins ExtraBoldItalic": "fonts/poppins/Poppins-ExtraBoldItalic.ttf",
            "Poppins BoldItalic": "fonts/poppins/Poppins-BoldItalic.ttf",
            "Poppins Bold": "fonts/poppins/Poppins-Bold.ttf",
            "Poppins BlackItalic": "fonts/poppins/Poppins-BlackItalic.ttf",
            "Poppins Black": "fonts/poppins/Poppins-Black.ttf",
        }
        pg.window_min_height = DEVICE_HEIGHT
        pg.window_min_width = DEVICE_WIDTH
        pg.window_height = DEVICE_HEIGHT
        pg.window_width = DEVICE_WIDTH

        db = TRUCKIUMDatabase()
        db.connect_to_database()

        self.user = CurrentUser(db)

        pg.on_route_change = self.route_change

        self.pg = pg
        self.pg.go('/start_page' if self.user.user_id is None else '/home')

    def route_change(self, route):
        print(self.pg.route)
        self.pg.views.clear()
        self.pg.views.append(
            views_handler(self.pg, self.user)[self.pg.route]
        )


# def main(page: Page):
#     def route_change(route):
#         print(page.route)
#         page.views.clear()
#         page.views.append(
#             views_handler(page)[page.route]
#         )
#
#     page.on_route_change = route_change
#     page.go('/start_page')


if __name__ == "__main__":
    app(target=App, assets_dir='assets', host='0.0.0.0')
