import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime


class TelaMonitor:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("SysWatch - Monitor de Sistema")
        self.raiz.geometry("650x500")

        self.dados_atuais = None
        self.pausado = False

        # Frame dos indicadores
        quadro_indicadores = tk.Frame(raiz, padx=10, pady=10)
        quadro_indicadores.pack(fill="x")

        self.rotulo_cpu = tk.Label(quadro_indicadores, text="CPU: --%", font=("Arial", 12, "bold"))
        self.rotulo_cpu.grid(row=0, column=0, padx=10)

        self.rotulo_memoria = tk.Label(quadro_indicadores, text="Memória: --%", font=("Arial", 12, "bold"))
        self.rotulo_memoria.grid(row=0, column=1, padx=10)

        self.rotulo_disco = tk.Label(quadro_indicadores, text="Disco: --%", font=("Arial", 12, "bold"))
        self.rotulo_disco.grid(row=0, column=2, padx=10)

        # Botões
        quadro_botoes = tk.Frame(raiz, padx=10, pady=5)
        quadro_botoes.pack(fill="x")

        self.botao_pausar = tk.Button(quadro_botoes, text="Pausar", command=self.alternar_pausa)
        self.botao_pausar.pack(side="left", padx=5)

        tk.Button(quadro_botoes, text="Exportar .txt", command=self.exportar).pack(side="left", padx=5)

        # Lista de processos
        tk.Label(raiz, text="Processos (PID | Memória MB | Memória % | Nome)", anchor="w").pack(fill="x", padx=10)

        self.lista_processos = tk.Listbox(raiz, font=("Courier", 10))
        self.lista_processos.pack(fill="both", expand=True, padx=10, pady=5)

        # Barra de rolagem
        barra = tk.Scrollbar(self.lista_processos)
        self.lista_processos.config(yscrollcommand=barra.set)
        barra.config(command=self.lista_processos.yview)
        barra.pack(side="right", fill="y")

    def alternar_pausa(self):
        self.pausado = not self.pausado
        self.botao_pausar.config(text="Retomar" if self.pausado else "Pausar")

    def atualizar(self, dados):
        self.dados_atuais = dados

        self.rotulo_cpu.config(text=f"CPU: {dados['cpu_pct']:.1f}%")
        self.rotulo_memoria.config(text=f"Memória: {dados['memoria_pct']:.1f}%")
        self.rotulo_disco.config(text=f"Disco: {dados['disco_pct']:.1f}%")

        self.lista_processos.delete(0, "end")
        for proc in dados["processos"]:
            linha = f"{proc['pid']:>6}  {proc['memoria_mb']:>8.1f} MB  {proc['memoria_pct']:>6.1f}%  {proc['nome']}"
            self.lista_processos.insert("end", linha)

    def exportar(self):
        if self.dados_atuais is None:
            messagebox.showwarning("Aviso", "Nenhum dado disponível para exportar.")
            return

        caminho = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivo de texto", "*.txt")],
            initialfile="relatorio_syswatch.txt"
        )

        if not caminho:
            return

        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATÓRIO SYSWATCH\n")
            arquivo.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            arquivo.write(f"CPU: {self.dados_atuais['cpu_pct']:.1f}%\n")
            arquivo.write(f"Memória total: {self.dados_atuais['memoria_total_gb']} GB\n")
            arquivo.write(f"Memória usada: {self.dados_atuais['memoria_pct']:.1f}%\n")
            arquivo.write(f"Disco total: {self.dados_atuais['disco_total_gb']} GB\n")
            arquivo.write(f"Disco usado: {self.dados_atuais['disco_pct']:.1f}%\n\n")
            arquivo.write("Processos:\n")
            arquivo.write(f"{'PID':>6}  {'MEM(MB)':>8}  {'MEM%':>6}  NOME\n")

            for proc in self.dados_atuais["processos"]:
                arquivo.write(f"{proc['pid']:>6}  {proc['memoria_mb']:>8.1f}  {proc['memoria_pct']:>6.1f}  {proc['nome']}\n")

        messagebox.showinfo("Sucesso", f"Relatório salvo em:\n{caminho}")
