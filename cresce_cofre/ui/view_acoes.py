from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout)
from system import sistema

from .main_menu_buttons import MainManuButton
from .nova_acao import NovaAcao


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

        self.opcoes = Opcoes(self.func_atualizar, self)
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
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)

        self.grid.addWidget(self.tabela)

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "ViewAcoes.View.atualizar"')

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
        logger.log('METHOD', 'Chamando função "ViewAcoes.View.add_item"')

        item = QTableWidgetItem(i)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tabela.setItem(coluna, linha, item)


class Opcoes(QFrame):
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "ViewAcoes.Opcoes"')

        self.func_atualizar = func_atualizar

        self.setFrameShape(QFrame.Panel)
        self.setMaximumWidth(100)
        self.setMinimumWidth(100)

        self.janela_nova_acao = None

        self.grid = QVBoxLayout(self)

        self.botao_mais = MainManuButton('', 'icons/add.png')
        self.botao_mais.clicked.connect(self.abrir_janela_nova_acao)
        self.grid.addWidget(self.botao_mais)

        self.botao_menos = MainManuButton('', 'icons/cancel.png')
        self.grid.addWidget(self.botao_menos)

        self.botao_ajuste = MainManuButton('', 'icons/wrench.png')
        self.grid.addWidget(self.botao_ajuste)

        self.spacer = QSpacerItem(
            10, 10,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.grid.addItem(self.spacer)

    def atualizar(self):
        logger.log('METHOD', 'Chamando função "ViewAcoes.Opcoes.atualizar"')

        if sistema.is_open:
            self.botao_mais.setDisabled(False)
            self.botao_menos.setDisabled(False)
            self.botao_ajuste.setDisabled(False)
        else:
            self.botao_mais.setDisabled(True)
            self.botao_menos.setDisabled(True)
            self.botao_ajuste.setDisabled(True)

    def abrir_janela_nova_acao(self):
        logger.log(
            'METHOD',
            'Chamando função "ViewAcoes.Opcoes.abrir_janela_nova_acao"'
        )

        self.janela_nova_acao = NovaAcao(self.func_atualizar)
        self.janela_nova_acao.show()
