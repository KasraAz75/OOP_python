-- Table for Cats
CREATE TABLE Cats (
    CatID INT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    FavoriteFood VARCHAR(255),
    SpeakCount INT
);

-- Table for Dogs
CREATE TABLE Dogs (
    DogID INT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    FavoriteToy VARCHAR(255),
    BarkCount INT
);

-- Table for Name History
CREATE TABLE NameHistory (
    HistoryID INT PRIMARY KEY,
    AnimalID INT, -- Foreign key to Cats or Dogs table
    Name VARCHAR(255),
    HistoryDate TIMESTAMP -- Date or timestamp when the name was changed
);

-- Sample Insert Statements for Cats
INSERT INTO Cats (CatID, Name, Age, FavoriteFood, SpeakCount)
VALUES (1, 'cat1', 8, 'food1', 0);

INSERT INTO Cats (CatID, Name, Age, FavoriteFood, SpeakCount)
VALUES (2, 'cat2', 6, 'food2', 0);

-- Sample Insert Statements for Dogs
INSERT INTO Dogs (DogID, Name, Age, FavoriteToy, BarkCount)
VALUES (1, 'dog1', 7, 'toy1', 0);

INSERT INTO Dogs (DogID, Name, Age, FavoriteToy, BarkCount)
VALUES (2, 'dog2', 5, 'toy2', 0);