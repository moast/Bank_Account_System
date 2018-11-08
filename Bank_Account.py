

class Account(object):

    #constructor
	def __init__(self,initialBalance):
		if initialBalance>0.0:
			self.balance = initialBalance
		else:
			self.balance = 0
			print("Debit amount exceeded account balance")
    #credit(add) an amount ti the account
	def credit(self,amount):
		self.balance = self.balance+amount
	#return the account balacne
	def getBalance(self):
	    return self.balance #give the value of the balance to the calling method

	#withdraw money from account
	def debit(self,withdrawalAmount):
		if withdrawalAmount > 0:
		    if self.balance < withdrawalAmount:
		        print("Not enough money to withdraw")
		    else:
		        self.balance = self.balance - withdrawalAmount
		else:
		    print("withdrawal amount must be grater than 0")

		           

class AccountTest(object):
    def main(self):
        account1 = Account(50.00)
        account2 = Account(-7.53)
        print("account1 balance:$ "+ str(account1.getBalance()))
        print("account2 balance:$ "+ str(account2.getBalance()))

        withdrawFromAccount1 = float(input("Enter withdrawal amount for account1: "))
        print("")
        print("subtracting "+ str(withdrawFromAccount1) + " from account1")
        account1.debit(withdrawFromAccount1)
        print("account1 balance:$ "+ str(account1.getBalance()))
        print("")

        withdrawFromAccount2 = float(input("Enter withdrawal amount for account2: "))
        print("")
        print("subtracting "+ str(withdrawFromAccount2) + " from account1")
        account2.debit(withdrawFromAccount2)
        print("account2 balance:$ "+ str(account2.getBalance()))
        print("")

        print("Summary")
        print("account1 balance:$ "+ str(account1.getBalance()))
        print("account2 balance:$ "+ str(account2.getBalance()))
        	    



# account = Account(20)
# account.credit(10)
# print(account.balance)

accountTest = AccountTest()
accountTest.main()

