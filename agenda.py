import pandas as pd

# Criando a estrutura de dados
dados = [
    ["Segunda-feira", "13:50 - 14:30", "Física II"],
    ["Segunda-feira", "20:45 - 22:25", "Álgebra Linear"],
    
    ["Terça-feira", "09:50 - 11:30", "Estruturas de Dados"],
    ["Terça-feira", "13:00 - 14:40", "Física II"],
    ["Terça-feira", "16:40 - 18:20", "Matemática Discreta"],
    
    ["Quarta-feira", "09:50 - 11:30", "Sistemas Operacionais"],
    ["Quarta-feira", "13:00 - 14:00", "Estruturas de Dados"],
    ["Quarta-feira", "16:40 - 18:30", "Introdução à Extensão"],
    ["Quarta-feira", "18:50 - 20:30", "Álgebra Linear"],
    ["Quarta-feira", "20:45 - 22:25", "Cálculo II"],
    
    ["Quinta-feira", "07:00 - 08:40", "Sistemas Operacionais"],
    ["Quinta-feira", "13:00 - 14:40", "Probabilidade Computacional"],
    ["Quinta-feira", "14:40 - 18:20", "Eletrônica Digital"],
    ["Quinta-feira", "20:45 - 22:25", "Cálculo II"],
    
    ["Sexta-feira", "-", "Sem aulas confirmadas"]
]

# Criando um DataFrame
df = pd.DataFrame(dados, columns=["Dia", "Horário", "Disciplina"])

# Salvando a planilha
df.to_excel("Horario_Faculdade.xlsx", index=False)

print("Planilha 'Horario_Faculdade.xlsx' criada com sucesso!")
