import pandas as pd

df_employee = pd.read_csv(r"...\CadastroFuncionarios.csv", sep=';', decimal=',', encoding='utf-8')
df_lead = pd.read_csv(r"...\CadastroClientes.csv", sep=';', decimal=',', encoding='utf-8')
df_service = pd.read_excel(r"...\BaseServiçosPrestados.xlsx", engine='openpyxl')

### 1
total_folha = sum([sum([salario, impostos, beneficios, vt, vr]) for salario, impostos, beneficios, vt, vr in df_employee.iloc[::, 3:8].values])

# print(f'### 1. Valor Total da Folha Salarial: {total_folha}\n\n')

### 2
df_fatu_service = df_service.loc[:, ["ID Cliente", "Tempo Total de Contrato (Meses)"]]
df_fatu_lead = df_lead.loc[:, ["ID Cliente", "Valor Contrato Mensal"]]

df_fatu = df_fatu_service.merge(
    df_fatu_lead,
    how='left',
    left_on=["ID Cliente"],
    right_on=["ID Cliente"]
).fillna(1)

df_fatu["Valor Total de Contrato"] = [valor_mes * qtd_mes for lead, valor_mes, qtd_mes in df_fatu.values]
total_fatu = round(df_fatu["Valor Total de Contrato"].sum(), 2)

# print(f'### 2. Valor Total do Faturamento: {total_fatu}\n\n')

### 3
df_contracts_employee = df_employee.loc[:, ["ID Funcionário", "Nome Completo", "Area"]]
df_contracts = df_contracts_employee[df_contracts_employee.iloc[::, 0].isin(df_service["ID Funcionário"])]
perc_contracts = round(len(df_contracts) * 100 / len(df_contracts_employee), 2)

# print(f'### 3. Porcentagem de Funcionários que fecharam contratos: {perc_contracts}%\n\n')

### 4
df_area_employee = df_employee.loc[:, ["ID Funcionário", "Area"]]

df_area_contracts = df_area_employee.merge(
    df_service.loc[:, ["ID Funcionário"]],
    how='left',
    left_on=["ID Funcionário"],
    right_on=["ID Funcionário"]
).fillna('')
# print(df_area_employee["Area"].unique()) # Quais áreas existem

contracts_financeiro = (df_area_contracts["Area"] == 'Financeiro').sum()
contracts_administrativo = (df_area_contracts["Area"] == 'Administrativo').sum()
contracts_logistica = (df_area_contracts["Area"] == 'Logística').sum()
contracts_operacoes = (df_area_contracts["Area"] == 'Operações').sum()
contracts_comercial = (df_area_contracts["Area"] == 'Comercial').sum()

# print(f'### 4. Total de Contratos por Área:\n  Administrativo: {contracts_administrativo}\n  Financeiro: {contracts_financeiro}\n  Logística: {contracts_logistica}\n  Operações: {contracts_operacoes}\n  Comercial: {contracts_comercial}\n\n')

### 5
employee_financeiro = (df_area_employee["Area"] == 'Financeiro').sum()
employee_administrativo = (df_area_employee["Area"] == 'Administrativo').sum()
employee_logistica = (df_area_employee["Area"] == 'Logística').sum()
employee_operacoes = (df_area_employee["Area"] == 'Operações').sum()
employee_comercial = (df_area_employee["Area"] == 'Comercial').sum()

# print(f'### 5. Total de Funcionários por Área:\n  Administrativo: {employee_administrativo}\n  Financeiro: {employee_financeiro}\n  Logística: {employee_logistica}\n  Operações: {employee_operacoes}\n  Comercial: {employee_comercial}\n\n')


### 6
mean_ticket = round(df_lead["Valor Contrato Mensal"].mean(), 2)

# print(f'### 6. Ticket Médio dos Contratos: {mean_ticket}\n')

with open('pandas_desafio_analise_dados.txt', 'w', encoding='utf-8') as w:
    w.write(f'### 1. Valor Total da Folha Salarial: {total_folha}\n\n')
    w.write(f'### 2. Valor Total do Faturamento: {total_fatu}\n\n')
    w.write(f'### 3. Porcentagem de Funcionários que fecharam contratos: {perc_contracts}%\n\n')
    w.write(f'### 4. Total de Contratos por Área:\n  Administrativo: {contracts_administrativo}\n  Financeiro: {contracts_financeiro}\n  Logística: {contracts_logistica}\n  Operações: {contracts_operacoes}\n  Comercial: {contracts_comercial}\n\n')
    w.write(f'### 5. Total de Funcionários por Área:\n  Administrativo: {employee_administrativo}\n  Financeiro: {employee_financeiro}\n  Logística: {employee_logistica}\n  Operações: {employee_operacoes}\n  Comercial: {employee_comercial}\n\n')
    w.write(f'### 6. Ticket Médio dos Contratos: {mean_ticket}\n')



