from random import randint, choice
from string import ascii_lowercase, digits

'''Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.'''


class EmailValidator:
    def __new__(cls):
        return None

    letters = ascii_lowercase + digits + "_" + "."

    @classmethod
    def get_random_email(cls):
        """для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com"""
        ln = randint(1, 101)
        d = choice(cls.letters)
        tem = 0
        while tem != ln:
            letter = choice(cls.letters)
            if letter == '.':
                if letter != d[-1]:
                    continue
                else:
                    break
            d += letter
            tem += 1
        d += '@gmail.com'
        return d

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True
        else:
            return False

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count('@') == 1:
            before, after = email.split('@')
        else:
            return False
        if len(before) > 100 or len(after) > 50:
            return False
        if '.' not in after:
            return False
        for i in range(len(before)):
            if before[i] == '.' and i != 0:
                if before[i] == before[i-1]:
                    return False
            if before[i] not in cls.letters:
                return False
        for y in range(len(after)):
            if after[y] == '.' and y != 0:
                if after[y] == after[y-1]:
                    return False
            if after[y] not in cls.letters:
                return False

        return True


assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False
assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email("sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email("sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email("sc.lib@listru") == False and EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"