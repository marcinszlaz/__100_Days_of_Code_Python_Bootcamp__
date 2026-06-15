class bankAccount:
  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.__balance = balance # Private Attribute

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount

  def get_balance(self):
    return self.__balance

#Creating an account
account = bankAccount("John",1000)
account.deposit(500)
#Normal way
print(f'account balance: {account.get_balance()}')
#Abnormal way xD
try:
  print(f'account balance: {account.__balance}')
except AttributeError as ae:
  print(f'You can\'t do this {str(ae)}')
#Tricky way xD
print(f'Tricky way to get private attribute from\n'
      f'class: {account._bankAccount__balance}')
#This language mechanism is called Name Mangling (Mielenie Nazw [PL])
