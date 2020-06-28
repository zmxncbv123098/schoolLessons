class Country:
    name = ""
    capital = ""
    gcd = 0
    head = None
    next = None

    def __init__(self, name, capital, gcd):
        self.name = name
        self.capital = capital
        self.gcd = gcd

    def election(self, name):
        self.head = name

    def change_GCD(self, newGcd):
        self.gcd = newGcd

    def show(self):
        print('Country - ' + self.name + ',', end=' ')
        print('Capital - ' + self.capital + ',', end=' ')
        print('GCD is ' + str(self.gcd) + ',', end=" ")
        if self.head is not None:
            print("Leader - " + self.head)
        else:
            print('No Leader')

    def show_next(self):
        self.next.show()

    def set_next(m, n):
        m.next = n
        n.next = m

    def return_(self):
        x = str(self.name) + ' ' + str(self.capital) + ' ' + str(self.gcd) + ' ' + str(self.head) + '\n'
        x += str(self.next.name) + ' ' + str(self.next.capital) + ' ' + str(self.next.gcd) + ' ' + str(self.next.head)
        print(x)


usa = Country('USA', 'Washington', 16)
eng = Country('England', 'London', 2)
rus = Country('Russia', 'Moscow', 20)
fra = Country('France', 'Paris', 10)

usa.election('TRUMP')
rus.election('PUTIN')
eng.election('Elizabeth I')
dic = {usa.name: usa, rus.name: rus, eng.name: eng, fra.name: fra}
Country.set_next(rus, usa)

name = input("Input Country:")
if name in dic:
    dic[name].show()
    if dic[name].next is not None:
        dic[name].next.show()
    else:
        print("No opponent in The 2018 FIFA World Cup")
else:
    print("No such country in Data Base")

dic[name].return_()
