'''
Валідація email-адреси
1 можливий бал (оцінюється)
Адреса електронної пошти визначає скриньку електронної пошти, на яку доставляються повідомлення.
Ви можете прочитати докладний опис цієї теми у відповідній статті у Вікіпедії:
https://en.wikipedia.org/wiki/Email_address.

У цьому завданні вам потрібно буде створити клас Email зі спеціальним захищеним методом з
ім'ям _validate, який слід викликати з email property setter для перевірки переданого параметра
email_str, який представляє певну адресу електронної пошти. Логіка всередині методу _validate може
полягати в тому, щоб перевірити, чи є переданий параметр електронної пошти допустимим рядком
електронної пошти, та викликати виняток, якщо електронна пошта недійсна. Таким чином, вам потрібно
буде визначити property getters and setters в email і перевірити переданий параметр до property
setter перед призначенням атрибута екземпляра класу Email. Крім того, вам потрібно буде визначити
відповідні методи __init__ і __str__.

Щоб спростити завдання та не дотримуватися всіх вимог до адреси електронної пошти, визначених у
відповідних RFC специфікаціях, ми визначимо такі вимоги до рядка адреси електронної пошти:

- загальні: формат адреси електронної пошти – local-part@domain, де локальна частина може мати
довжину до 64 символів, а домен – максимум 255 символів;

- локальна частина: символи ASCII – латинські літери від A до Z і від a до z ; цифри від 0 до 9 ;
друковані символи ! # $% (амперсанд) '* + - / =? ^ _ `{|} ~ ; крапка . , за умови, що це не перший
і не останній символ, а також за умови, що він не з'являється послідовно; пробіли та спеціальні
символи "(),:; (математичний знак менше ніж)> @ [\] "(),:; (математичний знак менше ніж)> @ [\] не
допускаються;

- частина домену: символи ASCII: латинські літери від A до Z і від a до z ; цифри від 0 до 9 ;
дефіс – за умови, що це не перший і не останній символ.
'''


class Email:

    def __init__(self):
        self._email = None

    def __str__(self):
        if self._email == None:
            return f''
        else:
            return f'{self._email}'

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email_str):
        self._validate(email_str)
        self._email = email_str

    def _validate(self, email):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%'*+-/=?^_`{|}~;."
        domain_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
        simbols = "'*+-/=?^_`{|}~;."
        if not isinstance(email, str):
            raise TypeError
        if '@' not in email:
            raise ValueError
        if '.' not in email:
            raise ValueError
        name, next_part = email.split('@')
        domain, subdomain = next_part.split('.')
        # Проверяем длину имени и домена
        if len(name) < 1 or len(name) > 64:
            raise ValueError
        if len(domain) < 1 or len(domain) > 255:
            raise ValueError
        # Проверяем локальное имя на доступные символы
        for item in name:
            if item not in alphabet:
                raise ValueError
        if name[0] in simbols or name[-1] in simbols:
            raise ValueError
        # Проверяем домен на доступные символы
        for item in domain:
            if item not in domain_alphabet:
                raise ValueError
        if domain[0] == '-' or domain[-1] == '-':
            raise ValueError


if __name__ == "__main__":
    email_instance = Email()
    email_instance.email = "hello@email.com"
    print(email_instance)


