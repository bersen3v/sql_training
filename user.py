from datetime import datetime 
import random

users = []
surnames = ["Ivanov", "Petrov", "Sidorov", "Афанасьев"]
names = ["Ivan", "Stepan", "Oleg"]
patronymics = ["Ivanovich", "Stepanovich", "Olegovich"]
sex = ["male", "female"]
groups = [156, 157, 158]
adresses = ["alekseeva 33", "gagarina 19", "lenina 19"]
number = 0

def random_element(list):
        return list[random.randint(0, len(list)-1)]


class User:
    def __init__(self):
        global number
        self.number = int(f"{number}")
        self.surname = random_element(surnames)
        self.name = random_element(names)
        self.patronymic = random_element(patronymics)
        self.sex = random_element(sex)
        self.birthday = datetime.now().date()
        self.group_name = random_element(groups)
        self.adress = random_element(adresses)
        self.mark1 = random.randint(5,5),
        self.mark2 = random.randint(2,5),
        self.mark3 = random.randint(5,5),
        self.mark4 = random.randint(5,5),
        self.result = "Otl",
    
    def to_string_view(self):
        global number
        number+=1
        return f"('{self.number}','{self.surname}','{self.name}','{self.patronymic}','{self.sex}','{self.birthday}','{self.group_name}','{self.adress}')"
    
    def for_session(self):
         marks = [self.mark1[0], self.mark2[0], self.mark3[0], self.mark4[0]]
         self.result = "Otl"
         if(marks.count(4) == 1): self.result = "Hor1"
         if (marks.count(4) > 1): self.result = "Hor"
         if(3 in marks): self.result = "Ud"
         if(2 in marks): self.result = "Neud"


         return f"('{self.number}', '{self.mark1[0]}', '{self.mark2[0]}', '{self.mark3[0]}', '{self.mark4[0]}', '{self.result}')"

