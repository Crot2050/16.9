class Customers:
    def __init__(self, first_name,last_name,city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.city = city

    def __str__(self):
        return f'''"{self.first_name} {self.last_name}". {self.city}. Баланс: {self.balance} руб.'''

    def guest(self):
        return f'{self.first_name} {self.last_name},г. {self.city}'


costomer_1 = Customers('Мария','Соловьева','Казань',100)
costomer_2 = Customers('Светлана','Казакова','Санкт-Петербург',80)
costomer_3 = Customers('Вероника','Стеблецова','Сочи',300)

guest_list = [costomer_1, costomer_2, costomer_3]


for guest in guest_list:
    print(guest.guest())
