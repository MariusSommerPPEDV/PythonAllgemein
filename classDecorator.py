import datetime


class Fahrzeug:
    def __init__(self, cylinders):
        self.cylinders = cylinders

    @property
    def cylinders(self):
        print("Getting cylinders")
        return self._cylinders

    @cylinders.setter
    def cylinders(self, count):
        print("Setting cylinders")
        self._cylinders = count



Lambo = Fahrzeug(8)
print(Lambo.cylinders)
Lambo.cylinders = 4


class Customer:
    bonuscode = "ABC"

    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    @property
    def firstName(self):
        # Ist der Getter
        print("Getting Firstname")
        return self._FirstName

    @firstName.setter
    def firstName(self, name):
        print("Setting Firstname")
        self._FirstName = name

    @firstName.deleter
    def firstName(self):
        print("Deleteing FirstName")
        del self._FirstName

    @property
    def lastName(self):
        print("Getting Firstname")
        return self._LastName

    @lastName.setter
    def lastName(self, name):
        print("Setting Firstname")
        self._LastName = name

    @classmethod
    def set_bonuscode(cls, code):
        cls.bonuscode = code

    @classmethod
    def test_customer(cls):
        return cls("Max", "Mustermann")

    @staticmethod
    def calc_age(birthyear):
        return datetime.datetime.now().year - datetime.datetime(birthyear, 1, 1).year


print(Fahrzeug(Customer.calc_age(2000)).cylinders)


customer1 = Customer("John", "Doe")
customer2 = Customer("Melina", "Melior")

customer1.firstName = "Jürgen"
print(customer1.firstName)

print(customer1.bonuscode)
print(customer2.bonuscode)
Customer.set_bonuscode("JOL")
print(customer1.bonuscode)
print(customer2.bonuscode)
customer1.bonuscode = "Dol"
print(customer1.bonuscode)
Customer.bonuscode = "ÖLLÖL"
print(customer2.bonuscode)

test = Customer.test_customer()
print(test.firstName)
print(customer1.calc_age(2000))
print(Customer.calc_age(1995))
# del customer1.firstName
# print(customer1.firstName)


class NoCoffee(Exception):
    def __init__(self):
        super(NoCoffee, self).__init__("Ohne Kaffe geht nix!")


x = 5

if x < 200:
    raise NoCoffee
    print("NO!")
