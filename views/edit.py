import flet as ft
from flet_route import Params,Basket
from database.core import *

def EditView(page:ft.Page,params:Params,basket:Basket):

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Успех!"),
        content=ft.Text("Изменения вступили в силу"),
        actions=[
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    

    with engine.connect() as conn:
        query = select(k)
        res = conn.execute(query)
        
        data = []
        for i in res.all()[0]:
            data.append(i)
        
        count_connect_value = data[1]
        station_type_value = data[2]
        population_value = data[3]
        power_value = data[4]
        voltage_value = data[5]
        square_value = data[6]
        is_military_value = data[7]

    power =  ft.TextField(label="Мощность", width=200, value=power_value)
    voltage = ft.TextField(label="Напряжение", width=200, value=voltage_value)
    square = ft.TextField(label='Площадь', width=200, value=square_value)
    #
    population = ft.TextField(label="Охват населения", width=200, value=population_value)
    count_connect = ft.TextField(label="Количество связей", width=200, value=count_connect_value)
    station_type = ft.TextField(label="Тип станции", width=200, value=station_type_value)
    #
    is_military = ft.TextField(label='Наличие объектов военного назначения', width=200, value=is_military_value)
    def save_button(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

        with engine.connect() as conn:
            query = (
                update(k)
                .values(
                    count_connect = str(count_connect.value),
                    station_type = str(station_type.value),
                    population = str(population.value),
                    power = str(power.value),
                    voltage = str(voltage.value),
                    square = str(square.value)
                )
                .where(k.c.id == 1)
            )
            conn.execute(query)
            conn.commit()
    return ft.View(
        '/',
        controls=[
            ft.AppBar(title=ft.Text('Редактировать коэффициенты'), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Row(
            [       
                    square,
                    power,
                    voltage
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                   population,
                   count_connect,
                   station_type
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                is_military
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
            ft.ElevatedButton('Сохранить', on_click=save_button)
            ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ]
    )