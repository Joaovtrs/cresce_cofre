import requests
import yfinance as yf
from loguru import logger
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from system import sistema


class NovaAcao(QWidget):

    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)
        logger.log('CLASS', 'Criando classe "NovaAcao"')

        self.func_atualizar = func_atualizar

        self.setFixedSize(500, 200)
        self.setWindowTitle('Adicionar nova ação')

        self.main_grid = QVBoxLayout(self)

        self.grid_1 = QHBoxLayout()
        self.grid_2 = QHBoxLayout()
        self.grid_3 = QHBoxLayout()
        self.grid_4 = QHBoxLayout()

        self.main_grid.addLayout(self.grid_1)
        self.main_grid.addLayout(self.grid_2)
        self.main_grid.addLayout(self.grid_3)

        self.spacer_1 = QSpacerItem(
            10, 10,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.main_grid.addItem(self.spacer_1)

        self.main_grid.addLayout(self.grid_4)

        self.lbl_nome = QLabel('Nome: ', self)
        self.lbl_nome.setMinimumHeight(40)
        self.grid_1.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self)
        self.grid_1.addWidget(self.txt_nome)

        self.lbl_key = QLabel('Chave: ', self)
        self.lbl_key.setMinimumHeight(40)
        self.grid_2.addWidget(self.lbl_key)

        self.txt_key = QLineEdit(self)
        self.grid_2.addWidget(self.txt_key)

        self.btn_verificacao = QPushButton('Verificar chave')
        self.grid_3.addWidget(self.btn_verificacao)

        self.lbl_verificacao = QLabel('Chave não verificada')
        self.lbl_verificacao.setMinimumHeight(40)
        self.grid_3.addWidget(self.lbl_verificacao)

        self.spacer_2 = QSpacerItem(
            10, 10,
            QSizePolicy.Expanding,
            QSizePolicy.Minimum
        )
        self.grid_4.addItem(self.spacer_2)

        self.btn_cancelar = QPushButton('Cancelar', self)
        self.grid_4.addWidget(self.btn_cancelar)

        self.btn_adicionar = QPushButton('Adicionar', self)
        self.grid_4.addWidget(self.btn_adicionar)

        self.btn_verificacao.clicked.connect(self.func_btn_verificar)
        self.btn_cancelar.clicked.connect(self.func_btn_cancelar)
        self.btn_adicionar.clicked.connect(self.func_btn_adicionar)

    def func_btn_verificar(self):
        logger.log('METHOD', 'Chamando função "NovaAcao.check_key_exist"')

        key = self.txt_key.text()

        if not key:
            self.lbl_verificacao.setText('Chave não verificada')
        else:
            self.lbl_verificacao.setText('Verificando ...')
            try:
                key = key + '.SA'
                ticker = yf.Ticker(key)
                info = ticker.info
                self.lbl_verificacao.setText('Chave existe')
                logger.debug('Varificação achou a ação')
            except requests.exceptions.HTTPError:
                self.lbl_verificacao.setText('Chave não existe')
                logger.debug('Varificação não achou a ação')
            except Exception as e:
                logger.critical(
                    f'Varificação de ação apresentou erro desconhecido: ' +
                    f'{type(e)}: {e}'
                )

    def func_btn_cancelar(self):
        logger.log('METHOD', 'Chamando função "NovaAcao.func_btn_cancelar"')

        self.close()

    def func_btn_adicionar(self):
        logger.log('METHOD', 'Chamando função "NovaAcao.func_btn_adicionar"')

        nome = self.txt_nome.text()
        key = self.txt_key.text().upper()

        if nome and key:
            sistema.add_acao(nome, key, 0, 0, 0)

            self.func_atualizar()

            self.close()
