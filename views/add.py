import flet as ft 
from flet import FilePickerUploadFile
from flet_route import Params,Basket
from database import core
import shutil
import os

def AddView(page:ft.Page,params:Params,basket:Basket):

    photo_path = []

    def on_dialog_result(e: ft.FilePickerResultEvent):
        upload_list = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                photo_path.append(os.path.join('images', f.name))
                shutil.move(f.path, os.path.join('images', f.name))
            file_picker.upload(upload_list)
            
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Успех!"),
        content=ft.Text("Вы добавили новую станцию"),
        actions=[
            ft.TextButton("Закрыть", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    upload_photo_btn = ft.ElevatedButton(
        'Выберите фотографию',
        on_click=lambda _:file_picker.pick_files(allow_multiple=False)
    )
    #
    name = ft.TextField(hint_text="Название", width=200)
    station_type = ft.Dropdown(
                        label ='Тип объекта:',
                        width=200,
                        options=[
                            ft.dropdown.Option("ТЭЦ"),
                            ft.dropdown.Option("ГЭС"),
                            ft.dropdown.Option("АЭС"),
                            ft.dropdown.Option("Подстанция"),
                        ],
                    )
    square = ft.TextField(
        hint_text='Площадь', width=200
    )
    #
    power =  ft.TextField(hint_text="Мощность", width=200)
    voltage = ft.TextField(hint_text="Напряжение", width=200)
    #
    population = ft.TextField(hint_text="Охват населения", width=200,)
    count_connect = ft.TextField(hint_text="Количество связей", width=200)
    connect_type = ft.Dropdown(
                        label ='Тип подключения',
                        width=200,
                        options=[
                            ft.dropdown.Option("Параллельный"),
                            ft.dropdown.Option("Последовательный"),
                        ],
                    )
    #
    is_military = ft.Dropdown(
        label='Наличие объектов военного назначения',
        width=200,
        options=[
            ft.dropdown.Option('Да'),
            ft.dropdown.Option('Нет')
        ]
    )
    def save_button(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

        k_num = core.k_find(
            count_connect = count_connect.value,
            population = population.value,
            power = power.value,
            volatge = voltage.value,
            square = square.value,
        )  

        print(k_num)
        print(photo_path)
        core.add_station(
            image=photo_path[0],
            name = name.value,
            square = square.value,
            station_type = station_type.value,
            power = power.value,
            voltage = voltage.value,
            population = population.value,
            count_connect = count_connect.value,
            connect_type = connect_type.value,
            is_military = is_military.value,
            k = float(k_num)
        )

    photo_row = ft.Row([],alignment=ft.MainAxisAlignment.CENTER)

    pg = ft.View(
        '/',
        controls=[
            ft.AppBar(title=ft.Text("Добавление объекта"), bgcolor=ft.colors.SURFACE_VARIANT),
            photo_row,
            ft.Row(
            [       
                    name,
                    station_type
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
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
                   connect_type
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [is_military],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
            ft.ElevatedButton('Сохранить', on_click=save_button)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        )
        ]
        
    )

    photo_row.controls.append(upload_photo_btn)
    photo_row.controls.append(file_picker)
    return pg