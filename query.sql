-- 1, 2. Вивести назви жанрів аніме, й кількість аніме що до них належать
select Anime_genre.genre, count(Anime.anime_id) as anim_count from Anime_genre
join Anime on Anime_genre.anime_id = Anime.anime_id
group by Anime_genre.genre
order by anim_count desc;

-- 3. Вивести середній рейтинг аніме, й кількість жанрів що відносяться до цього рейтингу
select avg(rating), genre_count
from
(select Anime.rating, count(Anime_genre.genre) as genre_count from Anime
join Anime_genre on Anime.anime_id = Anime_genre.anime_id
group by Anime.rating
order by genre_count desc) as subquery
group by genre_count
order by genre_count;