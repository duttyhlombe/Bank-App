class bank:
    print("Welcome to the South African Bank of Rands")


    def __init__(self, inamount=100.00):
        self.balance = inamount
        print("Total Balance Amount is:", self.balance)

    def custdep(self,custamt):
        custamt=float(custamt)
        self.balance = self.balance + custamt
        self.logtrans(f"Deposit :{custamt}")

    def logtrans(self,trans):
        with open("Transaction Log.txt", "a") as file:
            file.write(f"{trans} \t\t\t Balance: {self.balance}\n")

    def custwith(self,custamt):
        custamt=float(custamt)
        self.balance = self.balance-custamt
        self.logtrans(f"Withdraw :{custamt}")

    def action(self):
        while True:
            print("withdrawal money or deposit money from bank??")

            ans=input("Enter w for Withdrawal and Enter d for Deposit: ")
            if ans=='w':
                withans=input("enter amount for withdrawal..")
                bankk.custwith(withans)

            elif ans=='d':
                withans = input("enter amount for deposit..")
                bankk.custdep(withans)
            else:
                print("you enter wrong keyword..")

            yes=input("continue....(y/n) :")
            if yes=='y':
                continue
            elif yes=='n':
                break
            else:
                print("you enter wrong keyword..End Process...try again later")
                break

    def dispcust(self):
        print("Your Updated bank amount is :", self.balance)
        with open("Transaction Log.txt", "r") as file:
            print(file.read())

bankk = bank()
bankk.action()
bankk.dispcust()
            
