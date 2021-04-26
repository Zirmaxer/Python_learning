'''Робочі взаємини

Реалізуйте 2 класи: Boss і Worker. Worker має властивість boss і його значення має бути
екземпляром класу Boss.
Ви можете переприсвоїти це значення, але слід перевіряти, чи є нове значення Boss.
Кожен Boss має список працівників. Потрібно реалізувати метод, який дозволить додавати працівників
до Boss.
Не можна додавати екземпляри класу Boss до списку працівників безпосередньо через доступ до
атрибутів. Замість цього, використовуйте геттери і сеттери.
Можна змінювати наявний код.
id_ – це просто випадкове унікальне ціле число.'''


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        if isinstance(id_, int):
            self.id_ = id_
        else:
            ValueError('id_ must be integer')
        if isinstance(name, str) or isinstance(company, str):
            self._name = name
            self._company = company
        else:
            ValueError('name and company must be string')
        self.workers = []

    def __eq__(self, other):
        return self.id_ == other.id_ and self._name == other._name and self._company == other._company

    @property
    def add_worker(self):
        return self.workers

    @add_worker.setter
    def add_worker(self, new_worker):
        if not isinstance(new_worker, Worker):
            raise ValueError('Worker mus be part of class Worker')
        if new_worker in self.workers:
            raise ValueError('Worker already in workers list')
        self.workers.append(new_worker)

    def del_worker(self, delete_worker):
        if delete_worker in self.workers:
            self.workers.remove(delete_worker)

    def __repr__(self):
        return f"boss {self._name}, ({self._company}) should have {self.workers} in workers"

    def __str__(self):
        return f"{self._name}, ({self._company}, {self.workers})"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        if isinstance(id_, int):
            self.id_ = id_
        else:
            ValueError('id_ must be integer')
        if isinstance(name, str) or isinstance(company, str):
            self._name = name
            self._company = company
        else:
            ValueError('name and company must be string')
        if isinstance(boss, Boss):
            self._boss = boss
        else:
            raise ValueError('boss is not a part of class Boss')
        boss.add_worker= self

    def __str__(self):
        return f"Worker id:{self.id_}, his name is {self._name} and it's work in {self._company} company, he had Boss: {self._boss._name}"

    def __eq__(self, other):
        return self.id_ == other.id_ and self._name == other._name and self._company == other._company

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        old_boss = self._boss
        if isinstance(new_boss, Boss):
            old_boss.del_worker(self)
            self._boss = new_boss
            new_boss.add_worker = self
        else:
            raise ValueError('New boss is not a part of class Boss')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def company(self):
        return self._name

    @company.setter
    def company(self, new_company):
        self._company = new_company


if __name__ == "__main__":
    Boss1 = Boss(1, 'Barabash', 'USB')
    Boss2 = Boss(2, 'LI', 'USB')
    print(Boss1)
    AK = Worker(1, 'Andrii', 'USB', Boss1)
    OV = Worker(2, 'Alex', 'USB', Boss1)
    print(Boss1)
    print(Boss2)
    print(AK)
    print(Boss1)
    AK.boss = Boss2
    print(AK)
    print(Boss1)
    print(Boss2)

    print('...........')
    boss1 = Boss(13246546, "Jack Daniels", "Coca-Cola")
    boss2 = Boss(132, "Samogon", "Coca-Cola")
    worker1 = Worker(131313, "Lu Pen", "Coca_Cola", boss1)
    print(worker1)
    worker1.name = "New name"
    worker1.company = "New company"
    worker1.boss = boss2
    print(worker1)

    print('........... test deleter')
    Boss3 = Boss(1, 'Barabash', 'USB')
    Boss4 = Boss(2, 'LI', 'USB')
    print(Boss3)
    print(Boss4)
    AK = Worker(1, 'Andrii', 'USB', Boss3)
    OV = Worker(2, 'Alex', 'USB', Boss3)
    print(Boss3)
    print(Boss4)
    AK.boss = Boss4
    print(Boss3)
    print(Boss4)
