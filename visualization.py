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
        anim_genre.append(row[0])
        total.append(row[1])

    x_range = range(len(anim_genre))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, total, label='Total')
    bar_ax.bar_label(bar, label_type='center', fmt='%d')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(anim_genre, rotation=90)
    bar_ax.set_xlabel('Назви жанрів')
    bar_ax.set_yticks(bar_ax.get_yticks())
    bar_ax.set_yticklabels(str(int(float(label))) for label in bar_ax.get_yticks())
    bar_ax.set_ylabel('Кількість, шт.')
    bar_ax.set_title('Кількість аніме, що належать до жанрів')

    pie_ax.pie(total, labels=anim_genre, autopct='%1.01f%%')
    pie_ax.set_title('Частка аніме кожного жанру')

    cur.execute(query_2)
    count = []
    rating = []

    for row in cur:
        count.append(row[1])
        rating.append(row[0])

    graph_ax.plot(count, rating, color='blue', marker='o')

    for cnt, rat in zip(count, rating):
        graph_ax.annotate(rat, xy=(cnt, rat), color='blue',
                           textcoords='offset points')

    graph_ax.set_xlabel('Кількість жанрів')
    graph_ax.set_ylabel('Рейтинг')
    graph_ax.set_title('Графік залежності середнього рейтингу аніме від кількості його жанрів')


mng = plt.get_current_fig_manager()
mng.resize(1700, 900)

plt.show()