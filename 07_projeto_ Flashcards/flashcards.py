import tkinter as tk
from tkinter import ttk
from modo_estudo import Estudo
from tkinter import messagebox
import sqlite3


class FlashcardC():
    def __init__(self, JanelaPai):
        self.janelapai = JanelaPai
        # criando a janela
        self.janela = tk.Toplevel(JanelaPai)
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
        self.pergunta_text = tk.Entry(self.janela, 
                                      
                                     width=50, 
                                      
                                     borderwidth=1, 
                                     foreground="blue")
        self.pergunta_text.pack(pady=(0, 10))

        # Campo para resposta
        resposta_label = ttk.Label(self.janela, 
                                   text="Resposta:", 
                                   font=("Kristen ITC", 12), 
                                   foreground="lightskyblue")
        resposta_label.pack(pady=(10, 0))

        self.resposta_text = tk.Entry(self.janela, 
                                      
                                     width=50, 
                                     
                                     borderwidth=1, 
                                     foreground="blue",
                                     )
        self.resposta_text.pack(pady=(0, 10))

        # Botão para salvar
        salvar_button = ttk.Button(self.janela, 
                                   text="Adicionar Cartao", 
                                   command=self.inserir_disciplina)
        salvar_button.pack(pady=10)

        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom", 
                         expand=True)

        botao_excluir = ttk.Button(frame_botao,
                                   command=self.excluir_cartao ,
                                   text="Excluir", 
                                   width=20) 
        botao_excluir.pack(side="left",padx=10)

        # botao para ir para o modo estudo
        botao_estudo = ttk.Button(self.janela,
                                  text="Modo Estudo",
                                  command=self.modo_estudo
                                  )

    def modo_estudo(self):
        
             

        # Criando o Treeview (apenas uma vez)
        self.treeview = ttk.Treeview(self.janela, columns=("codigo", "disciplina", "pergunta", "resposta"), show="headings")
        self.treeview.pack(pady=20)

        # Configurando as colunas do Treeview
        self.treeview.heading("codigo", text="Codigo")
        self.treeview.heading("disciplina", text="Disciplina")
        self.treeview.heading("pergunta", text="Pergunta")
        self.treeview.heading("resposta", text="Resposta")

        self.treeview.column("codigo", anchor="center", width=150)
        self.treeview.column("disciplina", anchor="center", width=150)
        self.treeview.column("pergunta", anchor="center", width=200)
        self.treeview.column("resposta", anchor="center", width=200)

    # criando banco de dados
        conexao = sqlite3.connect("./bd_projeto_flashcards.sqlite3")

        cursor = conexao.cursor()

       

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS disciplina(
                        codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        disciplina VARCHAR(50) ,
                        pergunta VARCHAR(50) ,
                        resposta VARCHAR(50)
                       
                       
                       )             
        """)

        # INTEGER ARMAZENAR NUMEROS INTEIROS

        # atualizando lista aqui
        self.atualizar_tabela()
        # inicio a conexao
        conexao.commit()

        # encerro a conexão
        conexao.close()

    def atualizar_tabela(self):
        #  vai ver todos os itens da treeview e deletar um por um
        for item in self.treeview.get_children():
              self.treeview.delete(item)

        conexao = sqlite3.connect("bd_projeto_flashcards.sqlite3")

        cursor = conexao.cursor()

        sql_atualizar = """
                        SELECT codigo, disciplina, pergunta, resposta FROM disciplina;
                        """
        
        cursor.execute(sql_atualizar)

        # fetchall - para pegar todos os itens da consulta
        disciplinas = cursor.fetchall()
        cursor.close()
        conexao.close()

        # add no treeview
        for linha in disciplinas:
             self.treeview.insert("", "end", values=linha)


    def salvar_cartao(self):
        # Obtendo os valores dos campos de texto
        disciplina = self.disciplina_entry.get().strip()
        pergunta = self.pergunta_text.get().strip()
        resposta = self.resposta_text.get().strip()

        # Adicionando os dados ao Treeview
        if disciplina and pergunta and resposta:
            self.treeview.insert("", "end", values=(disciplina, pergunta, resposta))

            # Limpando os campos de texto
            self.disciplina_entry.delete(0, "end")
            self.pergunta_text.delete(0, "end")
            self.resposta_text.delete(0, "end")

        # excluir carta
    def excluir_cartao(self):
        excluir_dados = self.treeview.selection()

        if excluir_dados:
                codigo_disciplina = self.treeview.item(excluir_dados)["values"][0]
                
                self.treeview.delete(excluir_dados)

                conexao = sqlite3.connect("bd_projeto_flashcards.sqlite3")
                cursor = conexao.cursor()

                sql_delete = """
                                DELETE FROM disciplina WHERE codigo = ?;
                            """
                cursor.execute(sql_delete, (codigo_disciplina,))  # Corrigido
                conexao.commit()

                cursor.close()
                conexao.close()
        else:
                messagebox.showerror(message="Adicione um item antes de salvar")

   
    def inserir_disciplina(self):

        disciplina = self.disciplina_entry.get()
        pergunta = self.pergunta_text.get()
        resposta = self.resposta_text.get()

        # criar conexao
        conexao = sqlite3.connect("./bd_projeto_flashcards.sqlite3")

        # criar cursor
        cursor =  conexao.cursor()

        # executar

        sql_insert = f""" 
                        INSERT INTO disciplina
                            (disciplina,
                            pergunta,
                            resposta)
                            VALUES
                            (?,
                            ?,
                            ?);
                        """
        valores = [disciplina, pergunta, resposta]

        cursor.execute(sql_insert, valores)

        self.atualizar_tabela()
        
    
        # comitar
        conexao.commit()

            # fechar conexão
        conexao.close()

        novo_id = cursor.lastrowid
                
        self.treeview.insert("","end", values=[novo_id, disciplina, pergunta, resposta])


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = FlashcardC()
    app.run()
