import pickle


class User:
    def __init__(self, username, preferences):
        self.username = username
        self.preferences = preferences

    def __repr__(self):
        return f'User: {self.username}, \nPreferences: \nTheme: {self.preferences.get("theme")}\nLanguage: {self.preferences.get("language")}\nIDE: {self.preferences.get("ide")}'


user1 = User('Giorgi', {"theme": "Dark", "language": "Python", "ide": "Visual Studio"})


def save_preferences(obj, filename="data.pickle"):
    with open(filename, "wb") as file:
        pickle.dump(obj, file)
    print(f"Successfully saved!")


save_preferences(user1)


def load_preferences(filename="data.pickle"):
    with open(filename, "rb") as file:
        return pickle.load(file)
    print(f"Successfully loaded!")


loaded_preferences = load_preferences(filename="data.pickle")
print(loaded_preferences)