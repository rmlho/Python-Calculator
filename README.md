# 🧮 Python Calculator

Uma calculadora desktop com interface gráfica construída em Python usando Tkinter.

## 🚀 Tecnologias

- Python 3
- Tkinter (GUI)

## 📁 Estrutura do projeto

```
Python-Calculator/
├── main.py     # Interface gráfica e menu(Tkinter)
├── calculator.py    # Lógica das operações matemáticas
└── README.md
```

## ⚙️ Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/rmlho/Python-Calculator
cd Python-Calculator
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Instale a dependência do Tkinter** *(se necessário)*
```bash
# Arch/CachyOS
sudo pacman -S tk

# Debian/Ubuntu
sudo apt install python3-tk
```

**4. Execute**
```bash
python3 main.py
```

## 🔢 Operações suportadas

- Adição `+`
- Subtração `−`
- Multiplicação `×`
- Divisão `÷` (com tratamento de divisão por zero)

## 📌 Observações

- Projeto desenvolvido como exercício de programação durante a graduação em Ciência da Computação na UEPB.
