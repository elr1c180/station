import flet as ft
from flet_route import Params,Basket
from database.core import *

def IndexView(page:ft.Page, params:Params, basket:Basket):

    with engine.connect() as conn:
        query = select(station)
        res = conn.execute(query)

        stations = res.fetchall()

    table_data = ft.DataTable(
            width=300,
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
        

    return ft.View(
        '/',
        controls=[
            ft.AppBar(title=ft.Text("Главное меню"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Column(
            [
                table_data[0],
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