# Homework Assignment Part 2

- Applicant: Kasra Azizbaigi
- email: kasra.azizbaigi@gmail.com

## Project Overview

The part 2 of the homework assignment is a Python application that simulates the operation of a pet shop. It includes two main classes, `Cat` and `Dog`, which represent cats and dogs that can be added to a database. The project also features a `Data` class responsible for managing database interactions, and a set of unit tests to ensure the functionality of the `Cat` and `Data` classes. It also features a sql file including SQL statement to create tables and sample insert statements.

## File Structure

The project directory is structured as follows:

- **main.py**: Contains the `Cat`, `Dog`, and `Data` classes, as well as the main logic for interacting with pets and the database.
- **petShop.py**: Provides functions for saving test data to the database and creating pets for the pet shop.
- **tests/test.py**: Includes unit tests for the `Cat` and `Data` classes. Same test cases could be replicated for the 'Dog' class.
- **database/homework.sql**: Defines the SQL schema for the database, including tables for cats, dogs, and name history. Also includes SQL insert statements.

## How to Run the Project

To run and test the project, follow these steps:

1. **Database Setup**: Ensure you have a database available (e.g., PostgreSQL, MySQL) and update the `main.py` and `petShop.py` files to provide the appropriate database connection details.

2. **Database Initialization**: Execute the SQL script in `database/homework.sql` to create the required tables and initial data.

3. **Running the Application**:
    - To test the code in `main.py`, execute it directly by running `python main.py`.
    - To run the `petShop.py` module and insert test data into the database, execute it directly with `python petShop.py`. It also checks whether the transactions were completed succesfully or they were rolled back.

4. **Running Unit Tests**:
    - To run unit tests, execute `python -m unittest tests/test.py`.

## Project Rationale

### Code Organization

- The project separates the core functionality into the `Cat` and `Data` classes. This promotes code modularity and reusability.
- The `petShop.py` module provides a way to save test data to the database and create pets for the pet shop.

### Database Structure

- The project employs a relational database structure with separate tables for cats, dogs, and name history. 
- It also includes sql insert statements to isnert cat and dog objects to the Cats and Dogs tables.

### Error Handling

- The code includes error handling to ensure that database transactions are correctly committed or rolled back in case of an exception during data insertion.

### Testing

- Unit tests in `tests/test.py` validate the functionality of the `Cat` and `Data` classes.
- the same test cases could be replicated for the `Dog` class.

## Future Improvements

- **Enhanced Inheritance**: Refactor the code to use a `Pet` class as the parent class for `Cat` and `Dog`. This approach allows for better code reuse and maintains a consistent structure for both types of pets.

    ```python
    from dataclasses import dataclass
    import random

    @dataclass
    class Pet:
        name: str
        age: int
        favorite_item: str = None
        name_history: list = None
        speak_count: int = 0

        def speak(self, message=""):
            print(message)
            self.speak_count += 1
            if this.speak_count % 5 == 0:
                self.age += 1

        def get_names(self):
            names = [name for name in this.name_history if name is not None]
            if this.name is not None:
                names.append(this.name)
            return names

        def get_average_name_length(this):
            filtered_names = [name for name in this.name_history if isinstance(name, str)]
            if this.name is not None and isinstance(this.name, str):
                filtered_names.append(this.name)

            if not filtered_names:
                return 0

            total_length = sum(len(name) for name in filtered_names)
            return total_length / len(filtered_names)

    @dataclass
    class Cat(Pet):
        favoriteFood: str = None

    @dataclass
    class Dog(Pet):
        favoriteToy: str = None
    ```
    Following this structure the pet databse could be updated as follows where we store all pets in the Pets table and use PetID as a foreign key in the Cats and Dogs tables:

    ```
    -- Table for Pets
    CREATE TABLE Pets (
        PetID INT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Age INT NOT NULL,
        FavoriteItem VARCHAR(255),
        SpeakCount INT NOT NULL
    );

    -- Table for Cats
    CREATE TABLE Cats (
        CatID INT PRIMARY KEY,
        PetID INT NOT NULL,
        FavoriteFood VARCHAR(255),
        FOREIGN KEY (PetID) REFERENCES Pets(PetID)
    );

    -- Table for Dogs
    CREATE TABLE Dogs (
        DogID INT PRIMARY KEY,
        PetID INT NOT NULL,
        FavoriteToy VARCHAR(255),
        FOREIGN KEY (PetID) REFERENCES Pets(PetID)
    );
    ```

- Version controll systems (e.g. Git) could be used to manage project's source code and promote collaboration. 
- Error handling in database interactions could be enhanced with more detailed error messages and logging.
- The project could benefit from a command-line interface (CLI) for user-friendly interaction.
- Support for different database engines and configurations could be added.

If you have any further questions or need assistance, please feel free to reach out.
