import tkinter as tk

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("800x600")
janela.configure(bg="white")

espaçamento = tk.Label(janela, text="", bg="white")  # Cria um rótulo vazio para espaçamento
espaçamento.pack(ipady=20)  # Adiciona o rótulo à janela com um espaçamento vertical

image_logo = tk.PhotoImage(file="logo.png")  # Carrega a imagem do logo
logo_label = tk.Label(janela, image=image_logo, bg="white")  # Cria um rótulo para exibir a imagem do logo
logo_label.pack(ipady=15, ipadx=15)  # Adiciona o rótulo à janela com um espaçamento vertical

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

senha = tk.Entry(
    janela,
    font= ("Arial", 12), # Fonte
    bg='#ECE6E6', # Cor do background
    fg='#8D7B7B', # Cor do texto
    bd=0, # Borda
    justify="center", # Alinhamento do texto na horizontal
    show = "*" # Oculta o texto digitado
    )
senha.insert(0, "senha")  # Texto inicial (placeholder)
senha.pack(ipadx=40, ipady=10, pady=8)

botao_login = tk.Button(
    janela,
    text="Login", # Texto do botão
    font= ("Arial", 10, "bold"), # Fonte
    bg='#2B96C7', # Cor do background
    fg='white', # Cor do texto
    bd=0, # Borda
    )
botao_login.pack(ipadx=40, ipady=10, pady=8)


janela.mainloop()