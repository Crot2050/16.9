class Client:
    def __init__(self, name, client_balans):
        self.name = name
        self.client_balans = client_balans

    def get_info(self):
        return f"Клиент: {self.name}, Баланс:{self.client_balans},руб."

client_1 = Client("Иван Петров", 50)
print(client_1.get_info())
