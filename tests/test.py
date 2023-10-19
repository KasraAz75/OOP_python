# Import required libraries and classes
import unittest
from main import Cat, Data 


class TestCatMethods(unittest.TestCase):
    # Test the age of the cat 
    def test_age(self):
        cat = Cat()
        self.assertTrue(5 <= cat.getAge() <= 10)

    # Test the age of the cat after speaking 5 times
    def test_speak_method(self):
            cat = Cat()
            initial_age = cat.getAge()
            cat.speak()
            self.assertEqual(cat.getAge(), initial_age)
            cat.speak()
            self.assertEqual(cat.getAge(), initial_age)  
            cat.speak()
            self.assertEqual(cat.getAge(), initial_age)  
            cat.speak()
            self.assertEqual(cat.getAge(), initial_age)  
            cat.speak()
            self.assertEqual(cat.getAge(), initial_age + 1) 

    # Test setting and getting the name
    def test_set_and_get_name(self):
        cat = Cat()
        cat.setName("cat1")
        self.assertEqual(cat.getName(), "cat1")

    # Test setting and getting the age
    def test_set_and_get_age(self):
        cat = Cat()
        cat.setAge(7)
        self.assertEqual(cat.getAge(), 7)
    
    # Test setting and getting the fav food
    def test_set_and_get_favorite_food(self):
        cat = Cat()
        cat.setFavoriteFood("food1")
        self.assertEqual(cat.getFavoriteFood(), "food1")

    # Test cat's name history
    def test_get_names(self):
        cat = Cat()
        cat.setName("cat1")
        self.assertEqual(cat.getNames(), ["cat1"])

    # Test average name length 
    def test_get_average_name_length(self):
        cat = Cat()
        cat.setName("cat1_first_name") # name_count: 15
        cat.setName("cat1_second_name") # name_count: 16
        self.assertEqual(cat.getAverageNameLength(), 15.5) # average: 15.5


class TestData(unittest.TestCase):
    # Test the connection to the database
    def test_database_connection(self):
        data = Data("petShop")  
        self.assertTrue(data is not None) 

    # Test database insertion 
    def test_insertion(self):
        data = Data("petShop")
        cat = Cat("cat1")  
        data.insert("Cats", cat)  

if __name__ == '__main__':
    unittest.main()
