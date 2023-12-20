class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})"

    def __lt__(self, other):
        if self.age == other.age:
            return self.name < other.name
        return self.age > other.age

class AgeGroup:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.respondents = []

    def add_respondent(self, respondent):
        self.respondents.append(respondent)

    def is_in_range(self, age):
        return self.lower_bound <= age <= self.upper_bound

    def get_formatted_group(self):
        respondents_str = ", ".join(str(respondent) for respondent in self.respondents)
        return f"{self.lower_bound}-{self.upper_bound}: {respondents_str}"

def main():
    #создаём массив и заполняем его данными
    groups = []
    ages = list(map(int, input().split()))
    #создание возрастных групп
    for i in range(len(ages) - 1):
        group = AgeGroup(ages[i] + 1, ages[i + 1])
        groups.append(group)

    oldest_group = AgeGroup(ages[-1] + 1, 123)
    groups.append(oldest_group)
    #ввод данных респондентов
    respondents = []
    while True:
        data = input()
        if data == "END":
            break
        name, age = data.split(",")
        respondent = Respondent(name, int(age))
        respondents.append(respondent)
    #распределение по группам
    for respondent in respondents:
        for group in groups:
            if group.is_in_range(respondent.age):
                group.add_respondent(respondent)
                break
    #вывод данных
    for group in groups[::-1]:
        if group.respondents:
            print(group.get_formatted_group())

if __name__ == "__main__":
    main()