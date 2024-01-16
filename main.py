import flet as ft

def main(page: ft.Page):
    page.title = "Дипломная работа, первая версия"

    def route_change(route):
        fp = ft.FilePicker()
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                
                [
                    
                    ft.AppBar(title=ft.Text("Добавление нового объекта"), bgcolor=ft.colors.SURFACE_VARIANT),
                    # ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                    ft.ElevatedButton("Загрузите фотографии", on_click=lambda _: fp.pick_files(allow_multiple=True)),
                    ft.TextField(label="Название", width=300),
                    ft.ResponsiveRow([
                        ft.Column(col=3, controls=[ft.TextField(label="Мощность", width=300)]),
                        ft.Column(col=3, controls=[ft.TextField(label="Напряжение", width=300)])
                ]),
                ft.ResponsiveRow([
                        ft.Column(col=3, controls=[ft.TextField(label="Площадь", width=300)]),
                        ft.Column(col=3, controls=[ft.TextField(label="Координаты", width=300)])
                ]),
                ft.ResponsiveRow([
                        ft.Column(col=3, controls=[ft.TextField(label="Охват населения", width=300)]),
                        ft.Column(col=3, controls=[ft.Dropdown(
                        label ='Тип объекта:',
                        width=200,
                        options=[
                            ft.dropdown.Option("ТЭЦ"),
                            ft.dropdown.Option("ГЭС"),
                            ft.dropdown.Option("АЭС "),
                        ],
                    )])
                ]),
                ft.ResponsiveRow([
                        ft.Column(col=3, controls=[ft.TextField(label="Количество связей", width=300)]),
                        ft.Column(col=3, controls=[ft.TextField(label="Способ подключения к сети", width=300)])
                ]),
                ft.ElevatedButton("Добавить новый объект")
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)