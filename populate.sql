INSERT INTO Animation_studio (studio_id, name, country, founded)
VALUES
	(71203, 'Nippon Television', 'Japan', '1990.10.03'),
	(17421, 'David Production', 'Japan', '2007.09.21'),
	(80900, 'Madhouse', 'Japan', '1972.10.17'),
	(46711, 'Toei Animation', 'Japan', '1948.01.23'),
	(83910, 'White Fox', 'Japan', '2007.04.05'),
	(23410, 'Bones', 'Japan', '1998.10.01'),
	(53490, 'Madhouse', 'Japan', '1972.10.17');

INSERT INTO Anime (anime_id, name, type, episodes, rating, members, studio_id)
VALUES
	(33, 'Berserk', 'TV', 25, 8.40, 226430, 71203),
	(14719, 'JoJo no Kimyou na Bouken', 'TV', 26, 8.51, 190197, 17421),
	(1535, 'Death Note', 'TV', 37, 8.71, 1013917, 80900),
	(21, 'One Piece', 'TV', 1081, 8.58, 504862, 46711),
	(9253, 'Steins;Gate', 'TV', 24, 9.17, 673572, 83910),
	(5114, 'Fullmetal Alchemist: Brotherhood', 'TV', 64, 9.26, 793665, 23410),
	(11061, 'Hunter x Hunter (2011)', 'TV', 148, 9.13, 425855, 53490);

INSERT INTO Anime_genre (anime_id, genre)
VALUES
	(33, 'Action'),
	(33, 'Adventure'),
	(33, 'Demons'),
	(33, 'Drama'),
	(33, 'Fantasy'),
	(33, 'Horror'),
	(33, 'Military'),
	(33, 'Romance'),
	(33, 'Seinen'),
	(33, 'Supernatural'),
	(14719, 'Action'),
	(14719, 'Adventure'),
	(14719, 'Shounen'),
	(14719, 'Supernatural'),
	(14719, 'Vampire'),
	(1535, 'Mystery'),
	(1535, 'Police'),
	(1535, 'Psychological'),
	(1535, 'Supernatural'),
	(1535, 'Thriller'),
	(21, 'Action'),
	(21, 'Adventure'),
	(21, 'Comedy'),
	(21, 'Drama'),
	(21, 'Fantasy'),
	(21, 'Shounen'),
	(21, 'Super Power'),
	(9253, 'Sci-Fi'),
	(9253, 'Thriller'),
	(5114, 'Action'),
	(5114, 'Adventure'),
	(5114, 'Drama'),
	(5114, 'Fantasy'),
	(5114, 'Magic'),
	(5114, 'Military'),
	(5114, 'Shounen'),
  	(11061, 'Action'),
  	(11061, 'Adventure'),
  	(11061, 'Shounen'),
  	(11061, 'Super_Power');
	
