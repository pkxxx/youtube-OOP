class BankAccount():
    def __init__(self, account_number):
        self._balance = 0  # Prywatny atrybut oznaczamy podkreśleniem _ na początku nazwy jest to tylko konwencja
        self._account_number = account_number

    @classmethod  # Dekorator metody klasowej
    def create_with_balance(cls, account_number,
                            initial_balance):  # 'cls' odnosi się do klasy BankAccount nie ma self bo self odnosie się do instancji oniektu
        account = cls(account_number)  #odwołanie się do
        account.balance = initial_balance
        return account

    @property  # '@' Dekorator gettera - (wproperty właściwość)
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        print("Nie możesz zmieniać numeru konta!")

    @account_number.deleter
    def account_number(self):
        print("Nie możesz usunąć atrybutu account_number")

    @balance.setter  # Dekorator settera
    def balance(self, value):
        if value < 0:
            print("Nie możnaesz wypłwięcej niż posiadasz na koncie!")
            return
        self._balance = value

    @balance.deleter
    def balance(self):
        print("nie możesz usunąć atrybutu balance")

    @staticmethod
    def convert(amount):
        return round(amount / 4.20, 2)  # Przykład statycznej metody do konwersji waluty

    @staticmethod
    def transfer(sender, recipient, amount):
        if sender.balance >= amount:
            sender.balance -= amount
            recipient.balance += amount
            print("Przelew na konto: ", recipient.account_number, "w kwocie:", amount, "został wykonany.")
        else:
            print("Masz zamało środków na dokonanie tego przelewu.")


f_account = BankAccount.create_with_balance(111111, 111)
s_account = BankAccount(222222)
BankAccount.transfer(f_account, s_account, 222)

print("Po przelewie:")
print("Konto nadawcy:", f_account.balance)
print("Konto odbiorcy:", s_account.balance)

my_account = BankAccount(58758759)
my_account.balance = my_account.convert(5)
print(my_account.balance)
my_account.balance += 500  # Użycie settera do ustawienia wartości
my_account.balance -= 5000
print(my_account.account_number)
# my_account.account_number += 7777777777
# del my_account.account_number

print(my_account.balance)
###
my_account_with_balance = BankAccount.create_with_balance(12345678, 1000)
print(my_account_with_balance.balance)
