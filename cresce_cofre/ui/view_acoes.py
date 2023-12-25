from loguru import logger
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QTableWidget,
                               QTableWidgetItem, QVBoxLayout)
from PySide6.QtCore import Qt
from system import sistema


class ViewAcoes(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)

        self.grid = QHBoxLayout(self)

        self.view = View(self)
        self.grid.addWidget(self.view)

        self.separdor = QFrame(self)
        self.separdor.setFrameShape(QFrame.VLine)
        self.grid.addWidget(self.separdor)

        self.opcoes = Opcoes(self)
        self.grid.addWidget(self.opcoes)

    def atualizar(self):
        self.view.atualizar()


class View(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)
        self.grid = QVBoxLayout(self)

        self.tabela = QTableWidget(self)

        self.grid.addWidget(self.tabela)

    def atualizar(self):
        self.tabela.clear()

        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels([
            'Nome', 'Chave', 'Quantidade', 'Valor médio', 'Valor total'
        ])
        self.tabela.setColumnWidth(0, 300)
        self.tabela.setColumnWidth(1, 300)
        self.tabela.setColumnWidth(2, 300)
        self.tabela.setColumnWidth(3, 300)
        self.tabela.setColumnWidth(4, 300)

        if sistema.is_open:
            acoes = sistema.get_acoes()
            self.tabela.setRowCount(len(acoes))
            for i, a in enumerate(acoes):
                self.add_item(i, 0, str(a['nome']))
                self.add_item(i, 1, str(a['key']))
                self.add_item(i, 2, str(a['quantidade']))
                self.add_item(i, 3, str(a['valor_medio']))
                self.add_item(i, 4, str(a['valor_total']))

    def add_item(self, coluna, linha, i):
        item = QTableWidgetItem(i)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tabela.setItem(coluna, linha, item)


class Opcoes(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)
        self.setMaximumWidth(100)
        self.setMinimumWidth(100)
