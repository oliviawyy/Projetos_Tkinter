import tkinter as tk
from tkinter import ttk
from modo_estudo import Estudo
from tkinter import messagebox
import sqlite3


class FlashcardC():
    def __init__(self):
        # criando a janela
        self.janela = tk.Tk()
        self.janela.title("Flashcards")
        self.janela.geometry("800x700")
        self.janela.resizable(False, False)

        # self.janela.iconbitmap("genio.ico")
        

        self.rotulo = ttk.Label(self.janela,
                        text="Gerenciar cartões de estudo ┆⤿💌⌗",
                        background="lightskyblue",
                        foreground="navy",
                        font=("Kristen ITC", 20))
        self.rotulo.pack(pady=30)

        # Campo para disciplina
        disciplina_label = ttk.Label(self.janela, 
                                     text="Disciplina:", 
                                     font=("Kristen ITC", 12),
                                     foreground="lightskyblue",
                                       )
        disciplina_label.pack(pady=(10, 0))

        self.disciplina_entry = ttk.Entry(self.janela, 
                                          width=50, 
                                          foreground="blue",
                                          )
        self.disciplina_entry.pack(pady=(0, 10))

        # Campo para pergunta
        pergunta_label = ttk.Label(self.janela, 
                                   text="Pergunta:", 
                                   font=("Kristen ITC", 12), 
                                   foreground="lightskyblue")
        pergunta_label.pack(pady=(10, 0))
# relief="solid",
        self.pergunta_text = tk.Text(self.janela, 
                                     height=2, 
                                     width=50, 
                                     wrap="word", 
                                     borderwidth=1, 
                                     foreground="blue")
        self.pergunta_text.pack(pady=(0, 10))

        # Campo para resposta
        resposta_label = ttk.Label(self.janela, 
                                   text="Resposta:", 
                                   font=("Kristen ITC", 12), 
                                   foreground="lightskyblue")
        resposta_label.pack(pady=(10, 0))

        self.resposta_text = tk.Text(self.janela, 
                                     height=2, 
                                     width=50, 
                                     wrap="word",
                                     borderwidth=1, 
                                     foreground="blue",
                                     )
        self.resposta_text.pack(pady=(0, 10))

        # Botão para salvar
        salvar_button = ttk.Button(self.janela, 
                                   text="Salvar Cartão", 
                                   command=self.salvar_cartao)
        salvar_button.pack(pady=10)

        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom", 
                         expand=True)

        botao_excluir = ttk.Button(frame_botao,
                                   command=self.excluir_cartao ,
                                   text="Excluir", 
                                   width=20) 
        botao_excluir.pack(side="left",padx=10)


        # Criando o Treeview (apenas uma vez)
        self.treeview = ttk.Treeview(self.janela, columns=("disciplina", "pergunta", "resposta"), show="headings")
        self.treeview.pack(pady=20)

        # Configurando as colunas do Treeview
        self.treeview.heading("disciplina", text="Disciplina")
        self.treeview.heading("pergunta", text="Pergunta")
        self.treeview.heading("resposta", text="Resposta")

        self.treeview.column("disciplina", anchor="center", width=150)
        self.treeview.column("pergunta", anchor="center", width=300)
        self.treeview.column("resposta", anchor="center", width=300)

    def salvar_cartao(self):
        # Obtendo os valores dos campos de texto
        disciplina = self.disciplina_entry.get().strip()
        pergunta = self.pergunta_text.get("1.0", tk.END).strip()
        resposta = self.resposta_text.get("1.0", tk.END).strip()

        # Adicionando os dados ao Treeview
        if disciplina and pergunta and resposta:
            self.treeview.insert("", "end", values=(disciplina, pergunta, resposta))

            # Limpando os campos de texto
            self.disciplina_entry.delete(0, tk.END)
            self.pergunta_text.delete("1.0", tk.END)
            self.resposta_text.delete("1.0", tk.END)

        # excluir carta
    def excluir_cartao(self):
        excluir_dados = self.lista.curselection()

        if excluir_dados:
                texto_tarefa = self.lista.get(excluir_dados[0])  # Obter o texto da tarefa
                self.lista.delete(excluir_dados)

                conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")
                cursor = conexao.cursor()

                sql_delete = """
                                DELETE FROM tarefa WHERE descricao_tarefa = ?;
                            """
                cursor.execute(sql_delete, (texto_tarefa,))  # Corrigido
                conexao.commit()

                cursor.close()
                conexao.close()
        else:
                messagebox.showerror(message="Selecione um item antes de excluir")

    def banco_dados(self):
        conexao = sqlite3.connect("./bd_projeto_flashcards.sqlite3")

        cursor = conexao.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXIST disciplina(
                        disciplina VARCHAR(50) ,
                        pergunta VARCHAR(50) ,
                        resposta VARCHAR(50) PRIMARY KEY
                       
                       )             
        """)



        

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = FlashcardC()
    app.run()
