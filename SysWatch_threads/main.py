import tkinter as tk
import threading
import time

from monitor import coletar_dados
from interface import TelaMonitor


def main():
    raiz = tk.Tk()
    tela = TelaMonitor(raiz)

    dados_compartilhados = {"valor": None}

    def coletar_em_loop():
        while True:
            if not tela.pausado:
                dados_compartilhados["valor"] = coletar_dados()
            time.sleep(1)

    def atualizar_tela():
        dados = dados_compartilhados["valor"]
        if dados is not None:
            tela.atualizar(dados)
        raiz.after(1000, atualizar_tela)

    thread_coleta = threading.Thread(target=coletar_em_loop, daemon=True)
    thread_coleta.start()

    atualizar_tela()
    raiz.mainloop()


if __name__ == "__main__":
    main()
