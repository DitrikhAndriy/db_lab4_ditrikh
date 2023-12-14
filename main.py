import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '3421'
database = 'lab3_DB'
host = 'localhost'
port = '5432'

query_1 = '''
select Anime_genre.genre, count(Anime.anime_id) as anim_count from Anime_genre
join Anime on Anime_genre.anime_id = Anime.anime_id
group by Anime_genre.genre
order by anim_count desc;
'''
query_2 = '''
select avg(rating), genre_count
from
(select Anime.rating, count(Anime_genre.genre) as genre_count from Anime
join Anime_genre on Anime.anime_id = Anime_genre.anime_id
group by Anime.rating
order by genre_count desc) as subquery
group by genre_count
order by genre_count;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    anim_genre = []
    total = []

    for row in cur:
        print(row)
        anim_genre.append(row[0])
        total.append(row[1])

    print()
    for i in range(len(anim_genre)):
        print(f"{anim_genre[i]} {100*total[i]/sum(total):1.01f}%")

    cur.execute(query_2)
    count = []
    rating = []

    print()
    for row in cur:
        print(row)
        count.append(row[1])
        rating.append(row[0])