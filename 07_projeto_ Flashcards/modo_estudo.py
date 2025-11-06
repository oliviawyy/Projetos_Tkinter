import tkinter as tk
from flashcards import FlashcardC
from tkinter import Tk

class Estudo():
    def __init__(self):
        # criando a janela
        self.janela = tk.Tk()
        self.janela.title("Modo Estudo")
        self.janela.geometry("800x700")
        self.janela.resizable(False, False)

        self.botao_estudo = tk.Button(self.janela, text="Inicar Modo Estudo")


#Desafio Extra:
#Implementar um 'Modo Estudo'. Numa nova janela (`Toplevel`), o sistema mostra a *pergunta* de um cartão aleatório. O usuário clica num botão 'Revelar Resposta' para ver a resposta.
        
    # Função para iniciar o modo de estudo
    
    
    
    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Estudo()
    app.run()
