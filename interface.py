import tkinter as tk
from tkinter import messagebox
import numpy as np
import random as rd
from mochila import Gerar_Problema, Solucao_Inicial, Avalia

# Variáveis globais para armazenar os dados gerados
tempo = None
prior = None
solucao_inicial = None

# Função para gerar o problema
def gerar_problema():
    try:
        N = int(entry_N.get())
        MIN_TP = int(entry_MIN_TP.get())
        MAX_TP = int(entry_MAX_TP.get())
        MIN_PRI = int(entry_MIN_PRI.get())
        MAX_PRI = int(entry_MAX_PRI.get())
        
        global tempo, prior
        tempo, prior = Gerar_Problema(N, MIN_TP, MAX_TP, MIN_PRI, MAX_PRI)
        
        # Limpar o histórico de resultados antes de exibir novos dados
        result_text.set("")  # Limpar o texto existente
        
        # Exibir novos resultados
        new_text = f"Problema gerado:\nTempos: {tempo}\nPrioridades: {prior}\n\n"
        result_text.set(new_text)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para gerar a solução inicial
def gerar_solucao_inicial():
    try:
        if tempo is None or prior is None:
            raise ValueError("Primeiro, gere o problema.")
        
        N = int(entry_N.get())
        CAPACIDADE = int(entry_CAPACIDADE.get())
        
        global solucao_inicial
        solucao_inicial = Solucao_Inicial(N, CAPACIDADE, tempo)
        
        # Concatenar resultados ao texto existente
        current_text = result_text.get()
        new_text = f"Solução inicial gerada:\n{solucao_inicial}\n\n"
        result_text.set(current_text + new_text)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para avaliar a solução
def avaliar_solucao():
    try:
        if solucao_inicial is None:
            raise ValueError("Primeiro, gere a solução inicial.")
        
        N = int(entry_N.get())
        valor = Avalia(N, solucao_inicial, tempo, prior)
        
        # Concatenar resultados ao texto existente
        current_text = result_text.get()
        new_text = f"Avaliação da solução:\nValor: {valor}\n\n"
        result_text.set(current_text + new_text)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Configurar interface
root = tk.Tk()
root.title("Problema da Mochila")
root.geometry("500x500")

# Widgets da interface
tk.Label(root, text="Total de clientes:").pack()
entry_N = tk.Entry(root)
entry_N.pack()

tk.Label(root, text="Tempo total de atendimento:").pack()
entry_CAPACIDADE = tk.Entry(root)
entry_CAPACIDADE.pack()

tk.Label(root, text="Tempo mínimo para um atendimento:").pack()
entry_MIN_TP = tk.Entry(root)
entry_MIN_TP.pack()

tk.Label(root, text="Tempo máximo para um atendimento:").pack()
entry_MAX_TP = tk.Entry(root)
entry_MAX_TP.pack()

tk.Label(root, text="Valor mínimo de prioridade:").pack()
entry_MIN_PRI = tk.Entry(root)
entry_MIN_PRI.insert(0, "1")  # Definir valor padrão como 1
entry_MIN_PRI.pack()

tk.Label(root, text="Valor máximo de prioridade:").pack()
entry_MAX_PRI = tk.Entry(root)
entry_MAX_PRI.insert(0, "10")  # Definir valor padrão como 10
entry_MAX_PRI.pack()

# Botões para gerar problema, solução inicial e avaliar
btn_gerar_problema = tk.Button(root, text="Gerar Problema", command=gerar_problema)
btn_gerar_problema.pack()

btn_gerar_solucao = tk.Button(root, text="Gerar Solução Inicial", command=gerar_solucao_inicial)
btn_gerar_solucao.pack()

btn_avaliar = tk.Button(root, text="Avaliar Solução", command=avaliar_solucao)
btn_avaliar.pack()

# Área para exibir resultados
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=300, justify="left")
result_label.pack()

# Iniciar o loop da interface
root.mainloop()
