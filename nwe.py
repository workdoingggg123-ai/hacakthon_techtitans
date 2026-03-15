import numpy as np

class ShopKeeper:

    def __init__(self):
        self.username = "meet"
        self.password = "1707007"
        self.sales = None
        self.profit = None
        self.product_name = []

    # Login System
    def login_system(self):
        user_name = input("GIVE THE USER NAME : ")
        password = input("GIVE THE PASSWORD TO LOGIN : ")

        if user_name == self.username and password == self.password:
            print("LOGIN SUCCESSFULLY DONE")
            return True
        else:
            print("INVALID LOGIN!")
            return False

    # Input Product Data
    def item_input(self):

        self.product_name = []

        with open ("shopkeeper.txt" ,"a") as file:
         num_product = int(input("Give The Number Of Product In Shop : "))
         num_days = int(input("Give The Number Of Days Of Sales : "))

         sales_data = []
         profit_data = []

        for i in range(num_product):

            name = input(f"\nGive The Name Of Product {i+1} : ")
            price = int(input(f"Give price of {name} : "))

            self.product_name.append(name)

            print(f"Enter the sales of {name}")

            day_sales = []
            day_profit = []

            for j in range(num_days):

                sales = int(input(f"Day {j+1} : "))
                day_sales.append(sales)
                day_profit.append(price * sales)

            sales_data.append(day_sales)
            profit_data.append(day_profit)

        self.sales = np.array(sales_data)
        self.profit = np.array(profit_data)

        print("\nThe Name Of Product")
        print(self.product_name)

        print("\nSales Matrix:")
        print(self.sales)

        print("\nProfit Matrix:")
        print(self.profit)

        print(f"\nThe Total Profit Is {self.profit.sum()}")

        with open("shopkeeper.txt", "w") as file:

          for i in range(len(self.product_name)):

            file.write(f"\nProduct: {self.product_name[i]}\n")

            total_profit = 0

            for j in range(len(self.sales[i])):

               sale = self.sales[i][j]
               profit = self.profit[i][j]

               total_profit += profit

               file.write(f"Day {j+1}: Sold {sale} | Profit {profit}\n")

               file.write(f"Total Profit: {total_profit}\n")













    # Profit Per Product
    def profit_peritem(self):

        if self.profit is None:
            print("PLSS ENTER THE DATA FIRST !!")
            return

        total_profit_product = self.profit.sum(axis=1)

        print("\nProfit Per Product:")

        for name, profit in zip(self.product_name, total_profit_product):
            print(f"{name} : {profit}")

    # Menu
    def menu(self):

        while True:

            print("\n===== STORE MANAGEMENT =====")
            print("1. ITEM INPUT")
            print("2. PROFIT PER ITEM")
            print("3. EXIT")

            choice = input("Enter choice: ")

            if choice == "1":
                self.item_input()

            elif choice == "2":
                self.profit_peritem()

            elif choice == "3":
                print("EXITING PROGRAM...")
                break

            else:
                print("Invalid option")


# Run Program
system = ShopKeeper()

if system.login_system():
    system.menu()