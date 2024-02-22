import flet as ft
from flet_route import Params,Basket
from database.core import *

def TableView(page:ft.Page,params:Params,basket:Basket):

    with engine.connect() as conn:
        query = select(station).order_by(desc(station.c.k))
        res = conn.execute(query)

        stations = res.fetchall()
    
    print(stations)

    table_data = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Название объекта")),
                ft.DataColumn(ft.Text("Тип объекта")),
                ft.DataColumn(ft.Text("Площадь")),
                ft.DataColumn(ft.Text("Мощность")),
                ft.DataColumn(ft.Text("Напряжение")),
                ft.DataColumn(ft.Text("Охват населения")),
                ft.DataColumn(ft.Text("Количество подключений")),
                ft.DataColumn(ft.Text("Тип подключения")),
                ft.DataColumn(ft.Text('Коэффициент k'))
            ],

            rows=[
                
                
            ],
        ),
    
    for data in stations:
        table_data[0].rows.append(ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(data[2]))),
                            ft.DataCell(ft.Text(str(data[4]))),
                            ft.DataCell(ft.Text(str(data[3]))),
                            ft.DataCell(ft.Text(str(data[5]))),
                            ft.DataCell(ft.Text(str(data[6]))),
                            ft.DataCell(ft.Text(str(data[7]))),
                            ft.DataCell(ft.Text(str(data[8]))),
                            ft.DataCell(ft.Text(str(data[9]))),
                            ft.DataCell(ft.Text(str(data[10])))
                        ],
                    ),)
    return ft.View(
        '/',
        controls=[
            ft.AppBar(title=ft.Text('Ранжированная таблица'), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Row(
            [
                table_data[0]
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ]
    )