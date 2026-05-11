# Validador de CPF

Projeto educacional com múltiplas implementações de um validador de CPF (Cadastro de Pessoa Física). Inclui versão simples, versão com explicações detalhadas e versão com interface gráfica.

## 📚 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| **validar_cpf.py** | Implementação simples e direta do validador de CPF |
| **validar_cpf_explicação.py** | Versão com comentários explicativos sobre o algoritmo |
| **validar_cpf_interface.py** | Versão com interface gráfica (tkinter) |
| **validar_cpf_interface_explicação.py** | Versão gráfica com explicações detalhadas |

## 🚀 Como Usar

### Versão Simples (Terminal)
```bash
python3 validar_cpf.py
```

### Versão com Explicações
```bash
python3 validar_cpf_explicação.py
```

### Versão com Interface Gráfica
```bash
python3 validar_cpf_interface.py
```

### Versão Gráfica com Explicações
```bash
python3 validar_cpf_interface_explicação.py
```

## 💻 Requisitos

- Python 3.6 ou superior
- Tkinter (geralmente incluído no Python)
- Terminal/Prompt de comando ou ambiente gráfico

## 📝 Sobre o CPF

O CPF (Cadastro de Pessoa Física) é um número de identificação brasileiro com 11 dígitos. Os dois últimos dígitos são verificadores calculados através de um algoritmo específico.

**Formato:** XXX.XXX.XXX-XX

## 🔍 Como Funciona a Validação

1. **Primeiro Dígito Verificador:**
   - Multiplica cada um dos 9 primeiros dígitos por 10, 9, 8, 7, 6, 5, 4, 3, 2 respectivamente
   - Soma todos os resultados
   - Calcula o resto da divisão por 11
   - Se resto < 2, dígito = 0, senão dígito = 11 - resto

2. **Segundo Dígito Verificador:**
   - Multiplica cada um dos 10 primeiros dígitos por 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 respectivamente
   - Repete o processo anterior

3. **Validação:**
   - Compara os dígitos calculados com os dígitos informados

## 📌 Conceitos Abordados

- ✅ Manipulação de strings
- ✅ Loops e iterações
- ✅ Operações matemáticas
- ✅ Validação de dados
- ✅ Interface gráfica com tkinter
- ✅ Funções e modularização
- ✅ Tratamento de exceções

## 🎯 Objetivo

Compreender como funcionam os algoritmos de validação, especificamente o do CPF, através de implementações progressivas que começam simples e evoluem para versões com interface visual.

## 👤 Autor

[marcellerocha-art](https://github.com/marcellerocha-art)

## 📄 Licença

Este repositório é de código aberto e disponível para fins educacionais.

## 📚 Referências

- Mais informações sobre CPF: [Wikipedia](https://pt.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas)
- Documentação Tkinter: [Python Docs](https://docs.python.org/3/library/tkinter.html)
