import flet as ft

from flet_route import Params,Basket
from database.core import *

def ChoiceView(page: ft.Page, params: Params, basket: Basket):

    with engine.connect() as conn:

        query = (
            select(station.columns.name).order_by(desc(station.c.k))
            )
        
        res = conn.execute(query).fetchall()
    
    central_row = ft.Column(
        [

        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

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
                ft.DataColumn(ft.Text("Наличие объектов военного назначения")),
                ft.DataColumn(ft.Text('Коэффициент k'))
        ],

        rows = [

        ],
    ),

    
    stations_res = []
    def check(e):
        for item in central_row.controls:
            try:
                if item.value:
                    with engine.connect() as conn:
                        print(item.label)
                        query = (
                            select(station).
                            where(station.c.name == item.label)
                        )

                        result = conn.execute(query).fetchall()

                        stations_res.append(result)
            
            except Exception as e:
                print(e)
        print(stations_res)
        for res in stations_res:
            print(res)
            table_data[0].columns.append(ft.DataRow(
                            cells = [
                            ft.DataCell(ft.Text(str(res[0][2]))),
                            ft.DataCell(ft.Text(str(res[0][4]))),
                            ft.DataCell(ft.Text(str(res[0][3]))),
                            ft.DataCell(ft.Text(str(res[0][5]))),
                            ft.DataCell(ft.Text(str(res[0][6]))),
                            ft.DataCell(ft.Text(str(res[0][7]))),
                            ft.DataCell(ft.Text(str(res[0][8]))),
                            ft.DataCell(ft.Text(str(res[0][9]))),
                            ft.DataCell(ft.Text(str(res[0][10]))),
                            ft.DataCell(ft.Text(str(res[0][11]))),
                            ]
                            ))
        central_row.clean()
        central_row.update()
        central_row.controls.append(ft.Row([table_data[0]]))
        central_row.controls.append(ft.Row(
            [
            ft.ElevatedButton(
                'Назад',
                on_click= lambda _: page.go('/')
            )
            ]
        ))
        central_row.update()

    for item in res:
        central_row.controls.append(ft.Checkbox(
            label=item[0]
            ))
    central_row.controls.append(
        ft.ElevatedButton(
            text='Составить таблицу',
            on_click= check
        )
    )

    pg = ft.View(
        '/choice/',
        [
            central_row
        ]
    )
    return pg