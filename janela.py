import tkinter as tk

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("600x500")
janela.configure(bg="white")

espaço = tk.Label(janela, bg="white", height=3) #espaço entre o título e o campo de e-mail
espaço.pack() 

email = tk.Entry(
    janela,
    font=("Arial", 12), # Fonte utilizada e tamanho
    bg='#ECE6E6', # Cor do background
    fg='#8D7B7B', # Cor do texto
    bd=0, # Borda
    justify="center" # Alinhamento do texto na horizontal
)
email.insert(0, "e-mail")  # Texto inicial (placeholder)
email.pack(ipadx=40, ipady=10, pady=8)

janela.mainloop()