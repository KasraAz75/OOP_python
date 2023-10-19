# Import required libraries
import random 

class Cat:
    def __init__(self, initial_name=None):
        """
        Initialize a Cat object with optional initial name.
        randomly assign an age between 5 to 10 to the cat.
        """
        self.name = initial_name
        self.age = random.randint(5, 10)
        self.favoriteFood = None
        self.name_history = []
        self.speak_count = 0

    def getName(self):
        """
        Get the name of the cat.
        """
        return self.name

    def getAge(self):
        """
        Get the age of the cat.
        """
        return self.age

    def getFavoriteFood(self):
        """
        Get the cat's favorite food.
        """
        return self.favoriteFood

    def setName(self, newName):
        """
        Set a new name for the cat and add the previous name to the name history.
        :param newName: The new name for the cat.
        """
        self.name_history.append(self.name)
        self.name = newName

    def setAge(self, newAge):
        """
        Set the age of the cat.
        :param newAge: The new age for the cat.
        """
        self.age = newAge

    def setFavoriteFood(self, newFavoriteFood):
        """
        Set the cat's favorite food.
        :param newFavoriteFood: The new favorite food for the cat.
        """
        self.favoriteFood = newFavoriteFood
    
    def speak(self, catMessage="meow"):
        """
        Make the cat speak with the given message. Increment speak count and age if necessary.
        :param catMessage: The message of the cat.
        """
        print(catMessage)
        self.speak_count += 1
        if self.speak_count % 5 == 0:
            self.age += 1
    
    def getNames(self):
        """
        Get a list of names in the cat's name history.
        """
        names = [name for name in self.name_history if name is not None]
        if self.name is not None:
            names.append(self.name)
        return names
    
    def getAverageNameLength(self):
        """
        Calculate and return the average length of names in the name history.
        """
        filtered_names = [name for name in self.name_history if isinstance(name, str)]
        if self.name is not None and isinstance(self.name, str):
            filtered_names.append(self.name)

        if not filtered_names:
            return 0

        total_length = sum(len(name) for name in filtered_names)
        return total_length / len(filtered_names)
    

class Dog:
    def __init__(self, initial_name=None):
        """
        Initialize a Dog object with optional initial name.
        randomly assign an age between 5 to 10 to the dog.
        """
        self.name = initial_name
        self.age = random.randint(5, 10)
        self.favoriteToy = None
        self.name_history = []
        self.bark_count = 0

    def getName(self):
        """
        Get the name of the dog.
        """
        return self.name

    def getAge(self):
        """
        Get the age of the dog.
        """
        return self.age

    def getFavoriteToy(self):
        """
        Set the dog's favorite toy.
        """
        return self.favoriteToy

    def setName(self, newName):
        """
        Set a new name for the dog and add the previous name to the name history.
        :param newName: The new name for the dog.
        """
        self.name_history.append(self.name)
        self.name = newName

    def setAge(self, newAge):
        """
        Set the age of the dog.
        :param newAge: The new age for the dog.
        """
        self.age = newAge

    def setFavoriteToy(self, newFavoriteToy):
        """
        Set the dog's favorite toy.
        :param newFavoriteToy: The new toy for the dog.
        """
        self.favoriteToy = newFavoriteToy

    def bark(self, dogMessage="woof"):
        """
        Make the dog bark with the given message. Increment bark count and age if necessary.
        :param dogMessage: The message of the dog.
        """
        print(dogMessage)
        self.bark_count += 1
        if self.bark_count % 5 == 0:
            self.age += 1

    def getNames(self):
        """
        Get a list of names in the dog's name history.
        """
        names = [name for name in self.name_history if name is not None]
        if self.name is not None:
            names.append(self.name)
        return names

    def getAverageNameLength(self):
        """
        Calculate and return the average length of names in the name history.
        """
        filtered_names = [name for name in self.name_history if isinstance(name, str)]
        if self.name is not None and isinstance(self.name, str):
            filtered_names.append(self.name)

        if not filtered_names:
            return 0

        total_length = sum(len(name) for name in filtered_names)
        return total_length / len(filtered_names)
    

class Data:
    def __init__(self, database):
        """
        Connect to the database.
        :param database: The name or connection details of the database.
        """
        print("Connecting to database")

    def beginTran(self):
        """
        Begin the transaction.
        """
        print("Beginning a transaction")

    def commit(self):
        """
        Commit the current database transaction.
        """
        print("Committing transaction")

    def rollback(self):
        """
        Roll back the current database transaction in case of an error.
        """
        print("Rolling back transaction")

    def insert(self, table, object):
        """
        Insert the object (e.g. cat) to the table (e.g. Cats) in the database.
        """
        print("Inserting " + object.getName() + " into table " + table)


def main():

    # Create a Cat instance
    cat = Cat()
    
    # Display the current name of the cat
    print("Name is currently " + str(cat.getName()))

    # Set the name of the cat to "Garfield"
    cat.setName("Garfield")

    # Display the updated name of the cat
    print("Name has been changed to " + str(cat.getName()))

    # Create a Data instance and connect to the database
    data = Data("database")
    
    # Insert the cat's name into the "Cat" table
    data.insert("Cat", cat)


if __name__ == "__main__":
    main()