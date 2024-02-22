import flet as ft
from flet_route import Routing,path
from views.index import IndexView
from views.add import AddView
from views.edit import EditView
from views.station import StationView
from views.choice import ChoiceView
from views.table import TableView


def main(page: ft.Page):
    app_routes = [
        path(url='/',clear=True,view=IndexView),
        path(url="/add/", clear=False, view=AddView),
        path(url='/table/', clear=False, view=TableView),
        path(url='/station/:my_id', clear=False, view=StationView),
        path(url='/edit/', clear=False, view=EditView),
        path(url='/choice/', clear=False, view=ChoiceView)
    ]

    Routing(
        page=page,
        app_routes=app_routes
        )
    page.go(page.route)

ft.app(target=main, upload_dir='/images/')