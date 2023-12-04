-- 1, 2. Вивести назви жанрів аніме, й кількість аніме що до них належать
select Anime_genre.genre, count(Anime.anime_id) as anim_count from Anime_genre
join Anime on Anime_genre.anime_id = Anime.anime_id
group by Anime_genre.genre
order by anim_count desc;

-- 3. Вивести рейтинг аніме, й кількість жанрів що має аніме з таким рейтингом
select Anime.rating, count(Anime_genre.genre) as genre_count from Anime
join Anime_genre on Anime.anime_id = Anime_genre.anime_id
group by Anime.rating
order by genre_count desc;