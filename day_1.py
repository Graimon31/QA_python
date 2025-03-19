class Smartwatch:
    def __init__(self, brand, battery, is_on):
        self.brand = brand
        self.battery = battery
        self.is_on = is_on

    def show_time(self):
        if self.is_on == False:
            print("Часы выключены, включите их!")
        else:
            print("Текущее время")

    def power_on(self):
        if self.battery > 0:
            self.is_on = True
            print("Часы включены!")
        else:
            self.is_on = False

    def power_off(self):
        self.is_on = False
        print("Часы выключены.")

    def use(self):
        if self.battery >= 10:
            self.battery = self.battery - 10
            print(f"{'Используем часы, заряд:'} {self.battery} {'%'}")
        else:
            self.is_on = False
            print('Часы выключены')


my_watch = Smartwatch("Apple Watch", 100, False)
my_watch.show_time()  # Часы выключены, включите их!
my_watch.power_on()  # Часы включены!
my_watch.show_time()  # Текущее время: 12:34  (пример)
my_watch.use()  # Используем часы, заряд: 90%
my_watch.use()  # Используем часы, заряд: 80%
my_watch.power_off()  # Часы выключены.