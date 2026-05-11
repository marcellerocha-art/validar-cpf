# Validador de CPF

Sistema completo para validação de CPF (Cadastro de Pessoa Física) em Python. Este projeto oferece várias implementações, desde a mais simples até interfaces gráficas, para entender e validar CPFs brasileiros.

## 📋 O que é CPF?

O **CPF (Cadastro de Pessoa Física)** é um número de identificação única emitido pela Receita Federal do Brasil para pessoas físicas residentes no país.

### 📌 Estrutura do CPF

```
┌─────────────────────────────────────────────────────┐
│                      CPF BRASIL                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│   Número: 1 2 3 . 4 5 6 . 7 8 9 - 1 0              │
│            └─┬─┘ └─┬─┘ └─┬─┘   └┬─┘                │
│              │     │     │       │                  │
│         Sequência Sequência Sequência Verificadores│
│         (Grupo 1) (Grupo 2) (Grupo 3) (Check digit)│
│                                                     │
│   Total: 11 dígitos                                │
│   Formato: XXX.XXX.XXX-XX                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 🔍 Componentes:

- **Primeiros 3 dígitos**: Sequência numérica (000-999)
- **Próximos 3 dígitos**: Sequência numérica (000-999)
- **Próximos 3 dígitos**: Sequência numérica (000-999)
- **Últimos 2 dígitos**: Dígitos verificadores (calculados via algoritmo)

### ✅ Validação do CPF

O CPF é validado através de um algoritmo que calcula dois dígitos verificadores:

1. **Primeiro dígito verificador**: Multiplica os 9 primeiros dígitos por uma sequência decrescente (10, 9, 8, ..., 2) e valida o resultado
2. **Segundo dígito verificador**: Multiplica os 10 primeiros dígitos por uma sequência decrescente (11, 10, 9, ..., 2) e valida o resultado

## 📚 Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| **validar_cpf.py** | Validador básico de CPF (função simples) |
| **validar_cpf_explicação.py** | Validador com explicação passo a passo |
| **validar_cpf_interface.py** | Validador com interface de menu |
| **validar_cpf_interface_explicação.py** | Interface completa com explicações detalhadas |

## 🚀 Como Usar

### 1. Validador Básico
```bash
python3 validar_cpf.py
```

### 2. Validador com Explicação
```bash
python3 validar_cpf_explicação.py
```

### 3. Interface de Menu
```bash
python3 validar_cpf_interface.py
```

### 4. Interface Completa
```bash
python3 validar_cpf_interface_explicação.py
```

## 💻 Requisitos

- Python 3.6 ou superior
- Terminal/Prompt de comando

## 📝 Exemplo de Uso

```python
Digite um CPF: 123.456.789-10

CPF: 123.456.789-10
Status: ❌ INVÁLIDO
Motivo: Falha na validação do dígito verificador
```

## 🎯 Conceitos Abordados

- ✅ Manipulação de strings
- ✅ Loops e iterações
- ✅ Operações matemáticas (módulo)
- ✅ Validação de dados
- ✅ Algoritmos de verificação
- ✅ Interfaces de usuário
- ✅ Tratamento de erros

## 📖 Algoritmo de Validação

### Cálculo do Primeiro Dígito Verificador:
```
1. Multiplicar cada um dos 9 primeiros dígitos por 10, 9, 8, 7, 6, 5, 4, 3, 2
2. Somar todos os resultados
3. Dividir por 11 e pegar o resto
4. Se resto < 2: dígito = 0, senão: dígito = 11 - resto
```

### Cálculo do Segundo Dígito Verificador:
```
1. Multiplicar cada um dos 10 primeiros dígitos por 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
2. Somar todos os resultados
3. Dividir por 11 e pegar o resto
4. Se resto < 2: dígito = 0, senão: dígito = 11 - resto
```

## ⚠️ CPFs Inválidos Conhecidos

Alguns CPFs são considerados inválidos mesmo que passem no algoritmo:
- `000.000.000-00`
- `111.111.111-11`
- `222.222.222-22`
- ... (todos os dígitos iguais)

## 👤 Autor

[marcellerocha-art](https://github.com/marcellerocha-art)

## 📄 Licença

Este repositório é de código aberto e disponível para fins educacionais.

---

**Nota**: Este projeto foi desenvolvido para fins educacionais. Para validações em produção, use bibliotecas especializadas e sempre valide com os servidores da Receita Federal.
