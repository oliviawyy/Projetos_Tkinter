import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class Estudo():
    
    def __init__(self):
        # criando a janela
        self.janela = tk.Tk()
        self.janela.title("Modo Estudo")
        self.janela.geometry("800x500")
        self.janela.resizable(False, False)

#Desafio Extra:
#Implementar um 'Modo Estudo'. Numa nova janela (`Toplevel`), o sistema mostra a *pergunta* de um cartão aleatório. O usuário clica num botão 'Revelar Resposta' para ver a resposta.
        #criando um rótulo

        self.rotulo = tk.Label(self.janela,
                        text="Modo Estudo  ๋࣭ ࣪ ˖🎐",
                        background="lightskyblue",
                        foreground="navy",
                        font=("Kristen ITC", 20))
        self.rotulo.pack(pady=30)

        # Campo para pergunta
        pergunta_label = tk.Label(self.janela, 
                                   text="Pergunta:", 
                                   font=("Kristen ITC", 12), 
                                   foreground="lightskyblue")
        pergunta_label.pack(pady=(10, 0))
# relief="solid",
        self.pergunta_text = tk.Label(self.janela, 
                                     width=50,
                                     borderwidth=1, 
                                     foreground="blue",
                                     relief="solid")
        self.pergunta_text.pack(pady=(20, 0))



        frame_botoes = ttk.Frame(self.janela)
        frame_botoes.pack()

        botao_revelar = ttk.Button(frame_botoes,command=self.resposta ,text="Revelar Resposta")
        botao_revelar.pack(side="right", padx=5, pady=5)

        botao_aleatorio = ttk.Button(frame_botoes,command=self.alterar_pergunta ,text="Pergunta Aleatória")
        botao_aleatorio.pack(side="left",padx=5, pady=5)

        # Campo para resposta
        resposta_label = tk.Label(self.janela, 
                                   text="Resposta:", 
                                   font=("Kristen ITC", 12), 
                                   foreground="lightskyblue")
        resposta_label.pack(pady=(20, 0))

        self.respondida = ttk.Label(self.janela,
                               width=50,
                               borderwidth=1, 
                               relief="solid",
                               )
        self.respondida.pack(pady=(20, 0))

    def alterar_pergunta(self):
        conexao = sqlite3.connect("bd_projeto_flashcards.sqlite3")

        cursor = conexao.cursor()

        sql_alterar = """
                        SELECT pergunta FROM disciplina
                        ORDER BY RANDOM()

                        """
        cursor.execute(sql_alterar)
        self.perguntas = cursor.fetchone()

        conexao.commit()
        cursor.close()
        conexao.close()
        

        self.pergunta_text.configure(text=f"{self.perguntas}")

    def resposta(self):
        conexao = sqlite3.connect("bd_projeto_flashcards.sqlite3")

        cursor = conexao.cursor()

        sql_alterar = """
                        SELECT resposta FROM disciplina
                        WHERE pergunta = ?;

                        """
        valores = self.perguntas
        cursor.execute(sql_alterar, valores)
        self.respostas = cursor.fetchone()

        conexao.commit()
        cursor.close()
        conexao.close()

        self.respondida.configure(text=f"{self.respostas}")
    
    
    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Estudo()
    app.run()
