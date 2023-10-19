# Import required classes
from main import Cat, Dog, Data

def saveTest():
    # Connect to the petShop database
    data = Data("petShop")

    # Create a Cat with a name and insert it into the petShop database
    cat = Cat("Whiskers")  
    data.insert("Cat", cat)  

    # Create a Dog with a name and insert it into the petShop database
    dog = Dog("Buddy")
    data.insert("Dog", dog) 


def savePetShop():
    # Create three nameless cats and three nameless dogs
    cats = [Cat() for _ in range(3)]
    dogs = [Dog() for _ in range(3)]

    # Connect to the petShop database
    data = Data("petShop")

    try:
        # Insert all six pets into the database in a transaction
        data.beginTran()
        for cat in cats:
            data.insert("Cat", cat)
        for dog in dogs:
            data.insert("Dog", dog)
        data.commit()
    except Exception as e:
        # If an error occurs during insertion, roll back the transaction and shows the error message
        data.rollback()
        print(f"Error: Transaction rolled back due to {e}")
    else:
        # If successful, print a message showing the transaction was sucessfull
        print("All six pets have been successfully inserted.")

def logStats():
    # Log information about script execution
    print("Script execution completed successfully.")

    # Additional useful information:
    print("Number of cats in the petShop: X")   # Replace 'X' with the count of cats in the petShop
    print("Number of dogs in the petShop: Y")   # Replace 'Y' with the count of dogs in the petShop
    print("Total transactions: Z")              # Replace 'Z' with the number of transactions
    print("Total pets created: X + Y = Z")      # Calculate the total pets added to the petShop
    print("Average age of cats: A years")       # Calculate the average age of cats
    print("Average age of dogs: B years")       # Calculate the average age of dogs
    

if __name__ == "__main__":
    saveTest()
    savePetShop()
    logStats()