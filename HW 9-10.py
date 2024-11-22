class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__energy = 100
        self.__weapon = "Without weapon"
    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"{self.name} Attacks with weapon {self.__weapon}")
        else:
            print("Not enough energy for attack")
    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            print(f"Character {self.name} Dead")
        else:
            print(f"{self.name} Damage taken: {damage}, Health now: {self.__health}")
    def equip_weapon(self, weapon):
        self.__weapon = weapon
        print(f"{self.name} сменил оружие на {self.__weapon}")
    def get_status(self):
        return f"Здоровье: {self.__health}, Энергия: {self.__energy}, Оружие: {self.__weapon}"
character = Character("Alex")
print(character.get_status())
character.equip_weapon("Sword")
character.attack()
character.take_damage(60)
character.take_damage(60)




import requests


class SiteManager:
    def __init__(self):
        self.sites = []

    def add_site(self, url):
        self.sites.append(url)

    def get_sites(self):
        return self.sites


class SiteParser:
    def __init__(self, site_manager):
        self.site_manager = site_manager

    def content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            return ""

    def search(self, query):
        query = query.lower()
        results = {}
        for site in self.site_manager.get_sites():
            content = self.content(site)
            matches = content.lower().count(query)
            if matches > 0:
                results[site] = matches
        return results


class UserInterface:
    def __init__(self):
        self.site_manager = SiteManager()
        self.site_parser = SiteParser(self.site_manager)

    def start(self):
        while True:
            print("1. Add site")
            print("2. Search query")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_site()
            elif choice == '2':
                self.search_query()
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")

    def add_site(self):
        url = input("Enter site URL: ")
        self.site_manager.add_site(url)
        print(f"Site {url} added.")

    def search_query(self):
        query = input("Enter search query: ")
        results = self.site_parser.search(query)
        sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
        print("\nSearch Results:")
        for site, count in sorted_results:
            print(f"{site}: {count} matches")


class SearchApp:
    def run(self):
        ui = UserInterface()
        ui.start()


if __name__ == "__main__":
    app = SearchApp()
    app.run()
