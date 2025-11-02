class BankAccount():

    BANK_MONEY = 1000000 # Stała klasy, wspólna dla wszystkich obiektów tej klasy

    def __init__(self, account_number):
        self._balance = 0 # Prywatny atrybut oznaczamy podkreśleniem _ na początku nazwy jest to tylko konwencja
        self._account_number = account_number

    @property # '@' Dekorator gettera - (wproperty właściwość)
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

    @balance.setter # Dekorator settera
    def balance(self, value):
        if value < 0:
            print("Nie możnaesz wypłwięcej niż posiadasz na koncie!")
            return
        self._balance = value

    @balance.deleter
    def balance(self):
        print("nie możesz usunąć atrybutu balance")

my_account = BankAccount(58758759)
my_account.balance += 500  # Użycie settera do ustawienia wartości
my_account.balance -= 5000
print(my_account.account_number)
my_account.account_number += 7777777777
del my_account.account_number

print(my_account.balance)