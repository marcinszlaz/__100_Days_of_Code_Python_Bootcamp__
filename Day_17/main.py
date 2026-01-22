class User:
    pass # mozna tez uzyc slowa kluczowego pass albo standardowo ...
    def __init__(self, sex, user_id): # ta metoda jest prosta, to jest inicjalizator zmiennych, działą przy użyciu konstruktora obiektu
        print('new user being created...') # ten tekst wydrukuje sie zawsze gdy zadziała obiekt stworzony przez konstruktor
        # np przy przypisaywaniu zmiennych albo przy drukowaniu chyba bardziej NIE DZIAŁA TYLKO PRZY KONSTRUKTORZE !!!
        self.sex = sex
        self.user_id = user_id
        self.atrybut_defaultowy = 0 # możesz dodawać defaultowe atrybuty ale nie wpisujesz ich do () w funkcji __init__
        # jak w standardowej funkcji, tylko jako self (obiekt konstruktor, to 'coś' bierze udział w konstruowaniu)
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('M',1) # tu zadziala ten print z __init__
# PascalCalse camelCase sanke_case, PascalCase -> class names , snake_case - reszta :), camelCase, rzadko widywane w
# python

user_1.name = 'Marcin'
user_1.id = '007'

print(user_1.name, user_1.id) # mozesz tak dodawać atrybuty do OBIEKTU klasy, nie samej klasy, bo klasa to blueprint
user_2 = User('F',2)
print(user_1.sex, user_2.sex)

user_2.follow(user_1)
print(user_1.followers, user_2.followers)
print(user_1.following , user_2.following)
user_1.follow(user_2)
print(user_1.followers, user_2.followers)
print(user_1.following , user_2.following)
