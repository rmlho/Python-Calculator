from calculator import expressao_completa, formatacao
import tkinter as tk

# --- Estado da calculadora ---
primeiro_numero = None
operacao_atual = None
novo_numero = True  # flag: próximo dígito começa número novo

# --- Funções de lógica da interface ---

def atualizar_display(valor):
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, valor)
    display.config(state="readonly")

def pressionar_numero(n):
    global novo_numero
    atual = display.get()

    if novo_numero:
        atualizar_display(n)
        novo_numero = False
    else:
        if atual == "0":
            atualizar_display(n)
        else:
            atualizar_display(atual + n)

def pressionar_operacao(op):
    global primeiro_numero, operacao_atual, novo_numero
    try:
        primeiro_numero = float(display.get())
        operacao_atual = op
        novo_numero = True
        label_operacao.config(text=op)
    except ValueError:
        atualizar_display("Erro")

def pressionar_igual():
    global primeiro_numero, operacao_atual, novo_numero
    if primeiro_numero is None or operacao_atual is None:
        return
    try:
        segundo_numero = float(display.get())
        resultado = expressao_completa(primeiro_numero, segundo_numero, operacao_atual)
        if isinstance(resultado, str):
            atualizar_display(resultado)
        else:
            atualizar_display(formatacao(float(resultado)))
        primeiro_numero = None
        operacao_atual = None
        novo_numero = True
        label_operacao.config(text="")
    except Exception as e:
        atualizar_display("Erro")

def pressionar_ponto():
    atual = display.get()
    if novo_numero:
        atualizar_display("0.")
    elif "." not in atual:
        atualizar_display(atual + ".")

def limpar():
    global primeiro_numero, operacao_atual, novo_numero
    primeiro_numero = None
    operacao_atual = None
    novo_numero = True
    atualizar_display("0")
    label_operacao.config(text="")

def apagar():
    global novo_numero
    atual = display.get()
    if len(atual) <= 1 or (len(atual) == 2 and atual[0] == "-"):
        atualizar_display("0")
        novo_numero = True
    else:
        atualizar_display(atual[:-1])

# --- Janela principal ---
root = tk.Tk()
root.title("Calculadora")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

FONTE_DISPLAY = ("Courier New", 28, "bold")
FONTE_BTN     = ("Courier New", 16, "bold")

COR_BG       = "#1e1e2e"
COR_DISPLAY  = "#181825"
COR_NUM      = "#313244"
COR_OP       = "#89b4fa"
COR_IGUAL    = "#a6e3a1"
COR_CLEAR    = "#f38ba8"
COR_TEXT     = "#cdd6f4"
COR_OP_TEXT  = "#1e1e2e"

# --- Display ---
frame_display = tk.Frame(root, bg=COR_BG, pady=10, padx=10)
frame_display.grid(row=0, column=0, columnspan=4, sticky="ew")

label_operacao = tk.Label(frame_display, text="", font=("Courier New", 12),
                          bg=COR_BG, fg=COR_OP, anchor="e")
label_operacao.pack(fill="x", padx=4)

display = tk.Entry(frame_display, font=FONTE_DISPLAY, bg=COR_DISPLAY, fg=COR_TEXT,
                   bd=0, justify="right", readonlybackground=COR_DISPLAY,
                   insertbackground=COR_TEXT)
display.pack(fill="x", ipady=10, padx=4)
display.insert(0, "0")
display.config(state="readonly")

# --- Helper para criar botões ---
def criar_botao(parent, texto, comando, cor_bg, cor_fg=COR_TEXT, colspan=1):
    btn = tk.Button(
        parent, text=texto, command=comando,
        font=FONTE_BTN, bg=cor_bg, fg=cor_fg,
        activebackground=cor_fg, activeforeground=cor_bg,
        bd=0, cursor="hand2", padx=10, pady=18,
        relief="flat"
    )
    return btn

# --- Grade de botões ---
frame_botoes = tk.Frame(root, bg=COR_BG, padx=10, pady=4)
frame_botoes.grid(row=1, column=0, columnspan=4)

layout = [
    [("C", limpar, COR_CLEAR, COR_OP_TEXT),
     ("⌫", apagar, COR_NUM, COR_TEXT),
     ("%", lambda: None, COR_NUM, COR_TEXT),   # placeholder
     ("÷", lambda: pressionar_operacao("/"), COR_OP, COR_OP_TEXT)],

    [("7", lambda: pressionar_numero("7"), COR_NUM, COR_TEXT),
     ("8", lambda: pressionar_numero("8"), COR_NUM, COR_TEXT),
     ("9", lambda: pressionar_numero("9"), COR_NUM, COR_TEXT),
     ("×", lambda: pressionar_operacao("x"), COR_OP, COR_OP_TEXT)],

    [("4", lambda: pressionar_numero("4"), COR_NUM, COR_TEXT),
     ("5", lambda: pressionar_numero("5"), COR_NUM, COR_TEXT),
     ("6", lambda: pressionar_numero("6"), COR_NUM, COR_TEXT),
     ("−", lambda: pressionar_operacao("-"), COR_OP, COR_OP_TEXT)],

    [("1", lambda: pressionar_numero("1"), COR_NUM, COR_TEXT),
     ("2", lambda: pressionar_numero("2"), COR_NUM, COR_TEXT),
     ("3", lambda: pressionar_numero("3"), COR_NUM, COR_TEXT),
     ("+", lambda: pressionar_operacao("+"), COR_OP, COR_OP_TEXT)],

    [("0", lambda: pressionar_numero("0"), COR_NUM, COR_TEXT),
     (".", pressionar_ponto, COR_NUM, COR_TEXT),
     ("=", pressionar_igual, COR_IGUAL, COR_OP_TEXT, 2)],
]

for r, linha in enumerate(layout):
    c = 0
    for item in linha:
        texto, cmd, bg, fg = item[0], item[1], item[2], item[3]
        span = item[4] if len(item) > 4 else 1
        btn = criar_botao(frame_botoes, texto, cmd, bg, fg)
        btn.grid(row=r, column=c, columnspan=span,
                 sticky="nsew", padx=3, pady=3, ipadx=4)
        c += span

for i in range(4):
    frame_botoes.columnconfigure(i, weight=1)

root.mainloop()