CREATE TABLE Animation_studio
(
  studio_id INT NOT NULL,
  founded DATE NOT NULL,
  country VARCHAR(200) NOT NULL,
  name VARCHAR(200) NOT NULL,
  PRIMARY KEY (studio_id)
);

CREATE TABLE Anime
(
  name VARCHAR(200) NOT NULL,
  type VARCHAR(200) NOT NULL,
  episodes INT NOT NULL,
  rating FLOAT NOT NULL,
  members INT NOT NULL,
  anime_id INT NOT NULL,
  studio_id INT NOT NULL,
  PRIMARY KEY (anime_id),
  FOREIGN KEY (studio_id) REFERENCES Animation_studio(studio_id)
);

CREATE TABLE Anime_genre
(
  genre VARCHAR(200) NOT NULL,
  anime_id INT NOT NULL,
  PRIMARY KEY (genre, anime_id),
  FOREIGN KEY (anime_id) REFERENCES Anime(anime_id)
);