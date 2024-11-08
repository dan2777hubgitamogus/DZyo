class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False
    def __str__(self):
        return f"{self.title} - {self.deadline} - {'Виконано' if self.completed else 'Не виконано'}"


class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, title, description, deadline):
        self.tasks.append(Task(title, description, deadline))
    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
    def mark_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
    def show_tasks(self):
        for task in self.tasks:
            print(task)


task=Task()
manager = TaskManager()




class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        target.take_damage(10)

    def take_damage(self, damage):
        self.health = damage


class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self, target):
        target.take_damage(15)
class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def attack(self, target):
        target.take_damage(self.damage)

hero = Hero("Герой", 100, "Меч")
enemy = Enemy("Ворог", 80, 12)

hero.attack(enemy)
enemy.attack(hero)