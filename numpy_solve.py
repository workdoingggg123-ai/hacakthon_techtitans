import numpy as np

class shopkeeper:

    def __init__(self):
        self.username = "meet"
        self.password = "1707007"

        self.product_name = []
        self.product_price = []

        self.sales = None
        self.profit = None


    # ---------------- LOGIN SYSTEM ----------------
    def login_system(self):

        user_name = input("GIVE THE USER NAME : ")
        password = input("GIVE THE PASSWORD TO LOGIN : ")

        if user_name == self.username and password == self.password:
            print("LOGIN SUCCESSFULLY DONE\n")
            return True

        else:
            print("INVALID LOGIN!")
            return False


    # ---------------- ITEM INPUT ----------------
    def item_input(self):

        num_product = int(input("Give The Number Of Product In Shop : "))
        num_days = int(input("Give The Number Of Days Of Sales : "))

        pro_total = []
        total_price = []

        self.product_name.clear()
        self.product_price.clear()

        for i in range(num_product):

            pro_name = input(f"\nGive The Name Of Product {i+1} : ")
            price = int(input(f"Give price of {pro_name} : "))

            self.product_name.append(pro_name)
            self.product_price.append(price)

            print(f"\nEnter the sales of {pro_name}")

            pro_list = []
            pro_money = []

            for j in range(num_days):

                pro_sales = int(input(f"Day {j+1} sales : "))
                pro_list.append(pro_sales)

                money = price * pro_sales
                pro_money.append(money)

            pro_total.append(pro_list)
            total_price.append(pro_money)

        self.sales = np.array(pro_total)
        self.profit = np.array(total_price)

        print("\nProduct Names :")
        print(self.product_name)

        print("\nSales Matrix :")
        print(self.sales)

        print("\nProfit Matrix :")
        print(self.profit)

        print("\nTOTAL PROFIT =", self.profit.sum())


    # ---------------- PROFIT PER ITEM ----------------
    def profit_peritem(self):

        if self.profit is None:
            print("PLEASE ENTER PRODUCT DATA FIRST")
            return

        total_profit_product = self.profit.sum(axis=1)

        print("\nProfit Per Product\n")

        for i in range(len(self.product_name)):

            print(self.product_name[i], "=", total_profit_product[i])


    # ---------------- STORE DATA ----------------
    def num_item(self):

        if self.sales is None:
            print("ENTER PRODUCT DATA FIRST")
            return

        print("TO SEE STORE DATA ENTER PASSWORD")

        password = input("PASSWORD : ")

        if password == self.password:

            print("\nSTORE DATA\n")

            for name, sale, price in zip(self.product_name, self.sales, self.product_price): 
                print(name , price , sale )
                print("Product Name :", name)
                print("Price :", price)
                print("Sales per day :", sale)
                print("Total Profit :", (sale * price).sum())
                print()

        else:
            print("WRONG PASSWORD")


    # ---------------- MENU ----------------
    def menu(self):

        while True:

            print("\n===== STORE MANAGEMENT SYSTEM =====")
            print("1. ITEM INPUT")
            print("2. PROFIT PER ITEM")
            print("3. STORE DATA")
            print("4. EXIT")

            choice = input("ENTER YOUR CHOICE : ")

            if choice == "1":
                self.item_input()

            elif choice == "2":
                self.profit_peritem()

            elif choice == "3":
                self.num_item()

            elif choice == "4":
                print("EXITING SYSTEM...")
                break

            else:
                print("INVALID OPTION")


# ---------------- MAIN PROGRAM ----------------

system = shopkeeper()

if system.login_system():
    system.menu()