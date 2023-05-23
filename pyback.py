# elso feladat

import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


names = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

users = []
for name in names:
    lastname, firstname = name
    email = f"{remove_accents(lastname.lower())}.{remove_accents(firstname.lower())}@company.hu"
    password = f"{lastname}123Start"
    user = {
        'name': name,
        'email': email,
        'password': password,
    }
    users.append(user)

with open('nevek.txt', 'w') as f:
    for user in sorted(users, key=lambda x: x['name']):
        f.write(
            f"{remove_accents(user['name'][0])} {remove_accents(user['name'][1])} {user['email']} {remove_accents(user['password'])}\n")

print(users)


# második feladat 2.1

class Counter:
    def __init__(self, value, step=1):
        self.value = value
        self.step = step

    def increment(self):
        self.value += self.step

    def decrement(self):
        self.value -= self.step

    def set_value(self, new_value):
        self.value = new_value

    def set_step(self, new_step):
        self.step = new_step

    def get_value(self):
        return self.value


myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
print(myCounter.get_value())
myCounter.set_step(5)
myCounter.decrement()
print(myCounter.get_value())
myCounter.set_value(100)
myCounter.increment()
print(myCounter.get_value())


# második feladat 2.2

class ScoreCounter(Counter):
    def __init__(self, value, name, age, step=1):
        super().__init__(value, step)
        self.name = name
        self.age = age
        self.winner = False

    def increment(self):
        super().increment()
        if self.value >= 12:
            self.winner = True


myScoreCounter = ScoreCounter(10, 'Zsolt', 34)
myScoreCounter.increment()
print(myScoreCounter.get_value())
myScoreCounter.increment()
print(myScoreCounter.get_value())
print(myScoreCounter.winner)
