class Student:
    def __init__(self, first_name, last_name, grades):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__grades = grades

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def average(self):
        return sum(self.__grades) / len(self.__grades)

    def __str__(self) -> str:
        return self.full_name

csaba = Student("Kiss", "Csaba", [1, 1, 5, 5, 5, 5, 5])
print(csaba.full_name, csaba.average)