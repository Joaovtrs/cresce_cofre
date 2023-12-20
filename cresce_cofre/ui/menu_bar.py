from PySide6.QtWidgets import QFileDialog, QMenuBar


class MenuBar(QMenuBar):
    def __init__(self, sistema, func_atualizar, parent=None):
        super().__init__(parent)

        self.sistema = sistema
        self.func_atualizar = func_atualizar

        self.arquivo = self.addMenu('Arquivo')

        self.arquivo_criar = self.arquivo.addAction('Criar banco de dados')
        self.arquivo_criar.setShortcut('Ctrl+N')
        self.arquivo_criar.triggered.connect(self.criar_arquivo)

        self.arquivo_abrir = self.arquivo.addAction('Abrir banco de dados')
        self.arquivo_abrir.setShortcut('Ctrl+O')
        self.arquivo_abrir.triggered.connect(self.abrir_arquivo)

    def criar_arquivo(self):
        caminho = QFileDialog.getSaveFileName(
            parent=self,
            caption='Salvar como',
            filter='*.db'
        )
        if caminho[0]:
            self.sistema.criar_db(caminho[0])
            self.func_atualizar()

    def abrir_arquivo(self):
        caminho = QFileDialog.getOpenFileName(
            parent=self,
            caption='Abrir',
            filter='*.db'
        )
        if caminho[0]:
            self.sistema.abrir_db(caminho[0])
            self.func_atualizar()
