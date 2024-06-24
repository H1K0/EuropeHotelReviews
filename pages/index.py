from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
                html.Div([
                html.H3("О проекте"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'})
        )
    ]),

    html.Br(),

        html.P(
"Данный проект реализует удобное графическое отображение информации об отелях Европы на основе отзывов посетителей, собранных за 2015-2017 годы."
),
        html.P(
"Первая страница называется «Все отели». На ней присутствует таблица, содержащая три столбца: Название отеля, средний рейтинг и адрес. Дополнительно присутствуют фильтры по годам, и стране. Есть возможность переключение сортировки по возрастанию или убыванию рейтинга."
),
        html.P(
"Вторая страница называется «Сводка об отеле». В данном разделе можно выбрать отель и посмотреть информацию о нем. На странице присутствуют информация об среднем рейтинге за все время и за последний год, адрес отеля и пузырчатая диаграмма, показывающая распределение отзывов. Дополнительно показаны лучшие положительный и отрицательный отзывы с возможностью их перевода на русский язык. Присутствует возможность выбора национальности комментаторов, на основе чьих отзывов отображается информация."
),
        html.P(
"На странице «Карта» изображена тепловая карта на основе количества отзывов. Есть возможность выбора национальности комментаторов и года отзывов."
),
        html.P(
["Ссылка на датасет: ",
        dcc.Link(
"515k Hotel Reviews Data in Europe"
, href=
"https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe"
)]),
        html.P(
["Ссылка на GitHub: ",
        dcc.Link(
"H1K0/EuropeHotelReviews"
, href=
"https://github.com/H1K0/EuropeHotelReviews"
)]),
])
