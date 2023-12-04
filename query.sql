-- 1. Вивести кількість фанатів кожного аніме в залежності від студії анімації
-- 2. Вивести розподіл частки фанатів кожної студії
select Animation_studio.name, sum(Anime.members) as mem_sum
from Animation_studio join Anime on Animation_studio.studio_id = Anime.studio_id
group by Animation_studio.name;

-- 3. Вивести графік залежності рейтингу аніме від кількості його жанрів
select Anime.rating, count(Anime_genre.genre) as genre_count from Anime
join Anime_genre on Anime.anime_id = Anime_genre.anime_id
group by Anime.rating
order by genre_count desc;