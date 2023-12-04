import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '3421'
database = 'lab3_DB'
host = 'localhost'
port = '5432'

query_1 = '''
select Animation_studio.name, sum(Anime.members) as mem_sum
from Animation_studio join Anime on Animation_studio.studio_id = Anime.studio_id
group by Animation_studio.name;
'''
query_2 = '''
select Anime.rating, count(Anime_genre.genre) as genre_count from Anime
join Anime_genre on Anime.anime_id = Anime_genre.anime_id
group by Anime.rating
order by genre_count desc;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    anim_studio = []
    total = []

    for row in cur:
        print(row)
        anim_studio.append(row[0])
        total.append(row[1])

    print()
    for i in range(len(anim_studio)):
        print(f"{anim_studio[i]} {100*total[i]/sum(total):1.01f}%")

    cur.execute(query_2)
    count = []
    rating = []

    print()
    for row in cur:
        print(row)
        count.append(row[1])
        rating.append(row[0])