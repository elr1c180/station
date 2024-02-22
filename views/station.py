import flet as ft
from flet_route import Params,Basket
from database.core import *

def StationView(page:ft.Page, params:Params, basket:Basket):
    with engine.connect() as conn:
        
        title_query = (
            select(station)
            .where(station.c.id == int(params.get('my_id')))
        )
        title_res = conn.execute(title_query).fetchall()[0][2]

        query = select(station)
        res = conn.execute(query)

        stations = res.fetchall()

    table_data = ft.DataTable(
            width=250,
            columns=[
                ft.DataColumn(ft.Text("Название объекта")),
            ],

            rows=[
                
                
            ],
        ),
    
    for data in stations:
        table_data[0].rows.append(ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.ElevatedButton(str(data[2]), on_click=lambda e, id=data[0]: page.go(f"/station/{id}"))
                                ),
                        ],
                    ),)
    
    table_data_one = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Название объекта")),
                ft.DataColumn(ft.Text("Тип объекта")),
                ft.DataColumn(ft.Text("Площадь")),
                ft.DataColumn(ft.Text("Мощность")),
                ft.DataColumn(ft.Text("Напряжение")),
                ft.DataColumn(ft.Text("Охват населения")),
                ft.DataColumn(ft.Text("Количество подключений")),
                ft.DataColumn(ft.Text("Тип подключения")),
                ft.DataColumn(ft.Text('Наличие объектов военного назначения'))
            ],

            rows=[
                
                
            ],
        ),
    with engine.connect() as conn:
        station_one = conn.execute(title_query).fetchall()[0]
    print(station_one)
    photo = station_one[1]
    table_data_one[0].rows.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(station_one[2]))),
                        ft.DataCell(ft.Text(str(station_one[4]))),
                        ft.DataCell(ft.Text(str(station_one[3]))),
                        ft.DataCell(ft.Text(str(station_one[5]))),
                        ft.DataCell(ft.Text(str(station_one[6]))),
                        ft.DataCell(ft.Text(str(station_one[7]))),
                        ft.DataCell(ft.Text(str(station_one[8]))),
                        ft.DataCell(ft.Text(str(station_one[9]))),
                        ft.DataCell(ft.Text(str(station_one[10])))
                    ],
                ),)

    return ft.View(
        '/station/:my_id',
        controls=[
            ft.AppBar(title=ft.Text(title_res), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Column(
            [
                ft.Row(
                    [
                        table_data[0],
                        
                
                ft.Container(
                            content=ft.Column(
                                [
                                ft.Text(f"Название: {str(station_one[2])}"),
                                ft.Text(f"Тип станции: {str(station_one[4])}"),
                                ft.Text(f"Площадь: {str(station_one[3])}"),
                                ft.Text(f"Мощность: {str(station_one[5])}"),
                                ft.Text(f"Напряжение: {str(station_one[6])}"),
                                ft.Text(f"Охват населения: {str(station_one[7])}"),
                                ft.Text(f"Количество подключений: {str(station_one[8])}"),
                                ft.Text(f"Тип подключения: {str(station_one[9])}"),
                                ft.Text(f"Наличие объектов военного назначения: {str(station_one[10])}"),
                                ]
                                )
                        ),
                        
                ft.Image(
                    src=photo,
                   
                    fit=ft.ImageFit.CONTAIN,
                    ),
                ],
                ),
                ft.Divider(height=9, thickness=2),
                ft.ElevatedButton(
                    "Добавить объект",
                    style=ft.ButtonStyle(
                        color=ft.colors.BLACK87,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ), 
                    on_click=lambda _: page.go("/add/")
                    ),
                # ft.ElevatedButton(
                #     "Таблица обектов",
                #     style=ft.ButtonStyle(
                #         color=ft.colors.BLACK87,
                #         shape=ft.RoundedRectangleBorder(radius=10)
                #     ),
                #     on_click=lambda _: page.go("/table/")
                #     ),
                ft.ElevatedButton(
                    "Изменить вес коэфициентов",
                    style=ft.ButtonStyle(
                        color=ft.colors.BLACK87,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    on_click=lambda _: page.go("/edit/")
                    ),
                ft.ElevatedButton(
                    "Выбрать элементы и создать таблицу",
                    style=ft.ButtonStyle(
                        color=ft.colors.BLACK87,
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    on_click=lambda _: page.go("/choice/")
                    ),
            ],
             ),
        ]
    )