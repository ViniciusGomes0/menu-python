import tkinter as tk
from tkinter import messagebox, simpledialog

def menu():
    messagebox.showinfo("Menu", "Escolha uma das opções:\n1 - Login\n2 - Cadastro\n3 - Sair")

def executar_escolha():
    escolha = escolha_var.get()

    if escolha == "1":
        messagebox.showinfo("Login", "Bem-vindo de volta! Estamos prontos para te ajudar a alcançar seus objetivos.")

    elif escolha == "2":
        nome = simpledialog.askstring("Cadastro", "Digite seu nome:")
        if not nome:
            return
        try:
            idade = int(simpledialog.askstring("Cadastro", "Digite sua idade:"))
            cpf = simpledialog.askstring("Cadastro", "Digite seu CPF (com pontos):")
            if not cpf:
                raise ValueError
            messagebox.showinfo("Cadastro", f"Prazer {nome}, sua idade é {idade} e seu CPF é {cpf}")
        except:
            messagebox.showerror("Erro", "Preencha os dados corretamente.")

    elif escolha == "3":
        voltar = messagebox.askyesno("Sair", "Agradecemos seu contato. Deseja voltar?")
        if voltar:
            menu()
        else:
            messagebox.showinfo("Até mais", "Certo, qualquer coisa estamos por aqui.")
            root.quit()
    else:
        messagebox.showwarning("Inválido", "Digite uma opção válida.")

root = tk.Tk()
root.title("Sistema Interativo")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Digite uma opção (1, 2 ou 3):", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

escolha_var = tk.StringVar()
entry = tk.Entry(root, textvariable=escolha_var, font=("Arial", 12), width=5, justify="center")
entry.pack(pady=5)

button = tk.Button(root, text="Confirmar", font=("Arial", 12), command=executar_escolha, bg="#4caf50", fg="white", width=15)
button.pack(pady=20)

menu()
root.mainloop()
