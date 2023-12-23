import os

from logs import logger
from PySide6.QtWidgets import QFileDialog, QMenuBar
from system import sistema

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                       'OneDrive\\Área de Trabalho')


class MainMenuBar(QMenuBar):
    @logger.class_init
    def __init__(self, func_atualizar, parent=None):
        super().__init__(parent)

        self.func_atualizar = func_atualizar

        self.arquivo = self.addMenu('Arquivo')

        self.arquivo_criar = self.arquivo.addAction('Criar banco de dados')
        self.arquivo_criar.setShortcut('Ctrl+N')
        self.arquivo_criar.triggered.connect(self.criar_arquivo)

        self.arquivo_abrir = self.arquivo.addAction('Abrir banco de dados')
        self.arquivo_abrir.setShortcut('Ctrl+O')
        self.arquivo_abrir.triggered.connect(self.abrir_arquivo)

    @logger.class_method_init
    def atualizar(self):
        pass

    @logger.class_method_init
    def criar_arquivo(self):
        caminho = QFileDialog.getSaveFileName(
            parent=self,
            caption='Salvar como',
            filter='*.db',
            dir=desktop
        )

        if caminho[0]:
            sistema.criar_db(caminho[0])
            self.func_atualizar()
        else:
            logger.warning('Caminho não encontrado')

    @logger.class_method_init
    def abrir_arquivo(self):
        caminho = QFileDialog.getOpenFileName(
            parent=self,
            caption='Abrir',
            filter='*.db',
            dir=desktop
        )

        if caminho[0]:
            sistema.abrir_db(caminho[0])
            self.func_atualizar()
        else:
            logger.warning('Caminho não encontrado')