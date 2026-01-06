# 📊 Desafio de Análise de Dados com Pandas

Este repositório contém a solução para um **desafio de análise de dados em Python**, desenvolvido como parte da trilha de estudos na comunidade **@Hashtag**.

O objetivo do desafio é analisar dados corporativos relacionados a **funcionários, clientes e serviços prestados**, utilizando a biblioteca **Pandas**, e gerar indicadores relevantes para tomada de decisão.

---

## 🎯 Objetivos do Desafio

A partir de três bases de dados distintas, o script calcula os seguintes indicadores:

1. **Valor total da folha salarial**
2. **Valor total do faturamento**
3. **Porcentagem de funcionários que fecharam contratos**
4. **Total de contratos por área**
5. **Total de funcionários por área**
6. **Ticket médio dos contratos**

---

## 🗂️ Bases de Dados Utilizadas

- `CadastroFuncionarios.csv`  
  Contém informações de funcionários, como área e custos (salário, impostos, benefícios etc).

- `CadastroClientes.csv`  
  Contém dados dos clientes e o valor mensal dos contratos.

- `BaseServiçosPrestados.xlsx`  
  Relaciona funcionários aos contratos e informa o tempo total de cada contrato.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- openpyxl

---

## ⚙️ Lógica da Solução

- Leitura de arquivos CSV e Excel com Pandas
- Uso de operações vetorizadas, filtros e merges entre DataFrames
- Cálculo de métricas financeiras e percentuais
- Organização dos resultados em variáveis claras
- Escrita do output final em um arquivo `.txt`, já que o formato de saída não foi definido no desafio

---

## 📄 Output

Os resultados são armazenados no arquivo:

```txt
pandas_desafio_analise_dados.txt
```

---

## ▶️ Como Executar

Ajuste os caminhos dos arquivos de entrada no código:

```python
pd.read_csv("caminho/do/arquivo.csv")
pd.read_excel("caminho/do/arquivo.xlsx")
```

Execute o script:

```bash
python M6A13_desafio_pandas_analise_dados.py
```

Verifique o arquivo de saída gerado no diretório do projeto.

---

## 🧠 Observações

- O desafio não utiliza bibliotecas externas além do Pandas
- O foco está na lógica de negócio, clareza do código e manipulação de dados
- O exercício simula cenários reais de análise em ambiente corporativo

---

## 👤 Autor

Matheus Alexandre
Engenheiro de Dados


