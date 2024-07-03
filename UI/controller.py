import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        anni = self._model.listAnni
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))

    def handle_graph(self, e):
        try:
            giorni = int(self._view.txtGiorni.value)
        except ValueError:
            self._view.create_alert("Inserire un numer di giorni intero")
            return

        if self._view.ddyear.value is None:
            self._view.create_alert("Inserire un anno")
            return
        else:
            anno = self._view.ddyear.value

        self._model.buildGraph(anno, giorni)
        nN, nE = self._model.getGraphSize()
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato con {nN} vertici e {nE} archi"))
        adiacenze = self._model.getAdiacenti()
        for i in adiacenze:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {i[0].id}, somma dei pesi= {i[1]}"))
        self._view.update_page()

    def handle_path(self, e):
        pass