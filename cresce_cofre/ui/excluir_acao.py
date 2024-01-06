from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel, QMessageBox,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from system import sistema


class ExcluirAcao(QWidget):

    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "ExcluirAcao"')

        self.func_atualizar = func_atualizar

        self.setFixedSize(450, 200)
        self.setWindowTitle('Romover ação')
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        self.main_grid = QVBoxLayout(self)

        self.grid_1 = QHBoxLayout()
        self.grid_2 = QHBoxLayout()

        self.main_grid.addLayout(self.grid_1)

        self.spacer_1 = QSpacerItem(
            10, 10,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.main_grid.addItem(self.spacer_1)

        self.main_grid.addLayout(self.grid_2)

        self.lbl_nome = QLabel('Ação: ')
        self.lbl_nome.setMinimumHeight(40)
        self.grid_1.addWidget(self.lbl_nome)

        self.box_nome = QComboBox(self)
        self.box_nome.setMinimumWidth(350)
        self.grid_1.addWidget(self.box_nome)

        self.spacer_2 = QSpacerItem(
            10, 10,
            QSizePolicy.Expanding,
            QSizePolicy.Minimum
        )
        self.grid_2.addItem(self.spacer_2)

        self.btn_cancelar = QPushButton('Cancelar', self)
        self.btn_cancelar.setMinimumWidth(100)
        self.grid_2.addWidget(self.btn_cancelar)

        self.btn_excluir = QPushButton('Excluir', self)
        self.btn_excluir.setMinimumWidth(100)
        self.grid_2.addWidget(self.btn_excluir)

        self.add_itens_box()

        self.btn_cancelar.clicked.connect(self.func_btn_cancelar)
        self.btn_excluir.clicked.connect(self.func_btn_excluir)

    def add_itens_box(self):
        for item in sistema.get_acoes():
            self.box_nome.addItem(item['key'])

    def func_btn_cancelar(self):
        logger.log('METHOD', 'Chamando função "ExcluirAcao.func_btn_cancelar"')

        self.close()

    def func_btn_excluir(self):
        logger.log('METHOD', 'Chamando função "ExcluirAcao.func_btn_excluir"')

        item = self.box_nome.currentText()

        if item:
            pop_up_excluir = QMessageBox(self)
            pop_up_excluir.setWindowTitle('Aviso')
            pop_up_excluir.setText('Deseja excluir o ação?')
            pop_up_excluir.setIcon(QMessageBox.Critical)
            pop_up_excluir.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            pop_up_excluir.setDefaultButton(QMessageBox.No)
            x = pop_up_excluir.exec()
            if x == QMessageBox.Yes:
                sistema.excluir_acao(item)
                self.func_atualizar()
                self.close()
