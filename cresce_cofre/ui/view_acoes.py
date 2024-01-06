from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QFrame, QHBoxLayout,
                               QMessageBox, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout)
from system import sistema

from .main_menu_buttons import MainManuButton


class ViewAcoes(QFrame):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "ViewAcoes"')

        self.func_atualizar = func_atualizar

        self.setFrameShape(QFrame.Panel)

        self.grid = QHBoxLayout(self)

        self.view = View(self)
        self.grid.addWidget(self.view)

        self.separdor = QFrame(self)
        self.separdor.setFrameShape(QFrame.VLine)
        self.grid.addWidget(self.separdor)

        self.opcoes = Opcoes(self.func_atualizar, self.view.tabela, self)
        self.grid.addWidget(self.opcoes)

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "ViewAcoes.atualizar"')

        self.view.atualizar()
        self.opcoes.atualizar()


class View(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "ViewAcoes.View"')

        self.setFrameShape(QFrame.Panel)
        self.grid = QVBoxLayout(self)

        self.tabela = QTableWidget(self)
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.verticalHeader().setVisible(False)
        self.atualizar()

        self.grid.addWidget(self.tabela)

        self.acoes = None

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "ViewAcoes.View.atualizar"')

        self.tabela.clear()
        self.tabela.setColumnHidden(0, True)
        self.acoes = None

        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels([
            'ID', 'Nome', 'Chave', 'Quantidade', 'Valor médio', 'Valor total'
        ])
        self.tabela.setColumnWidth(0, 150)
        self.tabela.setColumnWidth(1, 300)
        self.tabela.setColumnWidth(2, 300)
        self.tabela.setColumnWidth(3, 300)
        self.tabela.setColumnWidth(4, 300)
        self.tabela.setColumnWidth(5, 300)

        if sistema.is_open:
            self.acoes = sistema.get_acoes()
            self.tabela.setRowCount(len(self.acoes))
            for i, a in enumerate(self.acoes):
                self.add_item(i, 0, str(a['id']))
                self.add_item(i, 1, str(a['nome']))
                self.add_item(i, 2, str(a['key']))
                self.add_item(i, 3, str(a['quantidade']))
                self.add_item(i, 4, str(a['valor_medio']))
                self.add_item(i, 5, str(a['valor_total']))

    def add_item(self, coluna, linha, i):
        logger.log('METHOD', 'Chamando função "ViewAcoes.View.add_item"')

        item = QTableWidgetItem(i)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tabela.setItem(coluna, linha, item)


class Opcoes(QFrame):
    def __init__(self, func_atualizar, tabela, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "ViewAcoes.Opcoes"')

        self.func_atualizar = func_atualizar
        self.tabela = tabela

        self.setFrameShape(QFrame.Panel)
        self.setMaximumWidth(100)
        self.setMinimumWidth(100)

        self.grid = QVBoxLayout(self)

        self.btn_mais = MainManuButton('', 'icons/add.png')
        self.grid.addWidget(self.btn_mais)

        self.btn_menos = MainManuButton('', 'icons/cancel.png')
        self.grid.addWidget(self.btn_menos)

        self.spacer = QSpacerItem(
            10, 10,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.grid.addItem(self.spacer)

        self.btn_mais.clicked.connect(self.func_btn_mais)
        self.btn_menos.clicked.connect(self.func_btn_menos)

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "ViewAcoes.Opcoes.atualizar"')

        if sistema.is_open:
            self.btn_mais.setDisabled(False)
            self.btn_menos.setDisabled(False)
        else:
            self.btn_mais.setDisabled(True)
            self.btn_menos.setDisabled(True)

    def func_btn_mais(self):
        logger.log(
            'METHOD',
            'Chamando função "ViewAcoes.Opcoes.abrir_janela_nova_acao"'
        )

        sistema.add_acao('', '', 0, 0, 0)
        self.func_atualizar()

    def func_btn_menos(self):
        logger.log(
            'METHOD',
            'Chamando função "ViewAcoes.Opcoes.abrir_janela_excluir_acao"'
        )

        selecionado = self.tabela.currentRow()
        nome = self.tabela.item(selecionado, 1).text()
        id_ = self.tabela.item(selecionado, 0).text()

        pop_up_excluir = QMessageBox(self)
        pop_up_excluir.setWindowTitle('Aviso')
        pop_up_excluir.setText(f'Deseja excluir o ação "{nome}"?')
        pop_up_excluir.setIcon(QMessageBox.Critical)
        pop_up_excluir.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        pop_up_excluir.setDefaultButton(QMessageBox.No)
        x = pop_up_excluir.exec()

        if x == QMessageBox.Yes:
            sistema.excluir_acao(id_)
            self.func_atualizar()

