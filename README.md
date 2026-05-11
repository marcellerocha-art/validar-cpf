# Validador de CPF

## 📋 O que é CPF?

O **CPF (Cadastro de Pessoa Física)** é um número de identificação utilizado no Brasil para registrar pessoas físicas junto à Receita Federal. É um documento essencial para qualquer transação financeira, fiscal ou administrativa.

### Estrutura do CPF

```
┌─────────────────────────────────────────────────┐
│          DOCUMENTO DE IDENTIFICAÇÃO              │
│                                                  │
│                                                  │
│  Nome: João da Silva                            │
│  CPF:  123.456.789-09                          │
│        └─┬──┘ └─┬──┘ └──┬──┘ └──┬──┘          │
│          │      │       │       └─ Dígito 2   │
│          │      │       └────── Dígito 1      │
│          │      └───────────── Sequencial     │
│          └────────────────── Origem/Região    │
│                                                  │
│  Data de Nascimento: 15/03/1990                │
│  Naturalidade: São Paulo                       │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Formatação padrão:** XXX.XXX.XXX-XX

- **Primeiros 8 números:** Identificação sequencial
- **9º número:** Dígito que identifica região/origem
- **10º e 11º números:** Dígitos verificadores (calculados via algoritmo)

---

## 🎯 O Projeto

Este repositório contém soluções para **validar CPF** usando diferentes abordagens em Python. O projeto demonstra desde a validação simples até interfaces gráficas.

## 📁 Arquivos e Como Funcionam

### 1️⃣ **validar_cpf.py** - Versão Console Simples

**O que faz:**
- Recebe um CPF do usuário via terminal
- Remove pontos e hífens da formatação
- Valida usando o algoritmo oficial do CPF
- Exibe se é válido ou inválido

**Como funciona:**

```python
# Remove formatação (123.456.789-09 → 12345678909)
cpf = cpf.replace(".", "").replace("-", "")

# Verifica tamanho e repetição (11111111111 é inválido)
if len(cpf) != 11 or cpf == cpf[0] * 11:
    return False

# Calcula 1º dígito verificador
soma = 0
for i in range(9):
    soma += int(cpf[i]) * (10 - i)  # Multiplica cada dígito pelo peso decrescente
resto = (soma * 10) % 11
if resto == 10:
    resto = 0  # Se resto for 10, substitui por 0

# Calcula 2º dígito verificador (mesmo processo)
# E compara com os dígitos finais do CPF
```

**Execução:**
```bash
python3 validar_cpf.py
```

**Exemplo:**
```
Digite o CPF: 123.456.789-09
CPF válido!
```

---

### 2️⃣ **validar_cpf_explicação.py** - Versão com Detalhes

**O que faz:**
- Valida o CPF como a versão anterior
- Mostra passo a passo do cálculo dos dígitos
- Explica cada etapa do algoritmo

**Como funciona:**
- Mesmo algoritmo da versão simples
- Adiciona prints mostrando:
  - Soma de cada multiplicação
  - Resto da divisão por 11
  - Valor esperado vs valor recebido

**Execução:**
```bash
python3 validar_cpf_explicação.py
```

---

### 3️⃣ **validar_cpf_interface.py** - Versão com Interface Gráfica

**O que faz:**
- Interface gráfica usando **Tkinter**
- Campo de entrada para digitar o CPF
- Botão para validar
- Janela popup com resultado

**Como funciona:**
```python
# Cria janela de interface gráfica
janela = tk.Tk()
janela.title("Validador de CPF")

# Cria campo de entrada
entrada = tk.Entry(janela)

# Cria botão que chama função de validação
botao = tk.Button(janela, text="Validar", command=verificar)

# Mostra popup com resultado
messagebox.showinfo("Resultado", "CPF válido!")
```

**Execução:**
```bash
python3 validar_cpf_interface.py
```

**Vantagem:** Interface visual mais amigável para usuários

---

### 4️⃣ **validar_cpf_interface_explicação.py** - Versão Completa

**O que faz:**
- Interface gráfica avançada
- Mostra detalhes da validação na interface
- Explica o algoritmo durante o processo
- Design melhorado

**Como funciona:**
- Combina a explicação completa com interface gráfica
- Mostra em tempo real:
  - Limpeza de formatação
  - Cálculo dos dígitos verificadores
  - Comparação dos resultados
  - Status final

**Execução:**
```bash
python3 validar_cpf_interface_explicação.py
```

---

## 🔍 Algoritmo de Validação do CPF

### Passo 1: Remover Formatação
```
123.456.789-09 → 12345678909
```

### Passo 2: Verificar Tamanho e Repetição
- Deve ter 11 dígitos
- Não pode ser 11111111111, 22222222222, etc.

### Passo 3: Calcular 1º Dígito Verificador
```
Números: 1 2 3 4 5 6 7 8 9
Pesos:   10 9 8 7 6 5 4 3 2

Soma = (1×10) + (2×9) + (3×8) + (4×7) + (5×6) + (6×5) + (7×4) + (8×3) + (9×2)
Soma = 10 + 18 + 24 + 28 + 30 + 30 + 28 + 24 + 18 = 210

Resto = (210 × 10) % 11 = 2100 % 11 = 1
```

### Passo 4: Calcular 2º Dígito Verificador
```
Números: 1 2 3 4 5 6 7 8 9 [dígito1]
Pesos:   11 10 9 8 7 6 5 4 3 2

Soma = (1×11) + (2×10) + ... + ([dígito1]×2)

Resto = (Soma × 10) % 11
```

---

## 💻 Requisitos

- Python 3.6 ou superior
- Tkinter (incluído no Python padrão)

## 🚀 Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/marcellerocha-art/validar-cpf.git
cd validar-cpf
```

2. Escolha a versão desejada e execute:
```bash
python3 validar_cpf.py                              # Console
python3 validar_cpf_explicação.py                   # Console com detalhes
python3 validar_cpf_interface.py                    # Interface gráfica
python3 validar_cpf_interface_explicação.py         # Interface completa
```

## ✅ Exemplos de CPF

**CPF Válido:**
- 123.456.789-09 ✓
- 111.444.777-35 ✓

**CPF Inválido:**
- 111.111.111-11 ✗
- 123.456.789-10 ✗

## 📝 Conceitos Abordados

- ✅ Manipulação de strings
- ✅ Loops e iterações
- ✅ Operações matemáticas
- ✅ Validação de dados
- ✅ Interface gráfica (Tkinter)
- ✅ Algoritmos de verificação

## 🎯 Objetivo

Entender como funcionam os algoritmos de validação utilizados em documentos brasileiros, aplicando conceitos de lógica de programação em Python.

## 👤 Autor

[marcellerocha-art](https://github.com/marcellerocha-art)

## 📄 Licença

Este repositório é de código aberto e disponível para fins educacionais.
