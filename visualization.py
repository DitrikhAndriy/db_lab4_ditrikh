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
        anim_studio.append(row[0])
        total.append(row[1])

    x_range = range(len(anim_studio))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, total, label='Total')
    bar_ax.bar_label(bar, label_type='center', fmt='%d', rotation=90)
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(anim_studio, rotation=27)
    bar_ax.set_xlabel('Студії анімації')
    bar_ax.set_yticks(bar_ax.get_yticks())
    bar_ax.set_yticklabels(str(int(float(label))) for label in bar_ax.get_yticks())
    bar_ax.set_ylabel('Фанати, осіб')
    bar_ax.set_title('Кількість фанатів аніме в залежності від студії')

    pie_ax.pie(total, labels=anim_studio, autopct='%1.01f%%')
    pie_ax.set_title('Частка фанатів кожної студії')

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
    graph_ax.set_title('Графік залежності рейтингу аніме від кількості його жанрів')


mng = plt.get_current_fig_manager()
mng.resize(1700, 900)

plt.show()