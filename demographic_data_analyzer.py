import pandas as pd # Importa a biblioteca Pandas para manipulação de dados


def calculate_demographic_data(print_data=True):
    # Lê os dados de um arquivo
    df = None

    # Quantas pessoas de cada raça estão representadas no dataset
    race_count = None

    # Qual é a idade média dos homens
    average_age_men = None

     # Qual é a porcentagem de pessoas que têm um diploma de bacharel
    percentage_bachelors = None

    # Pessoas com e sem educação avançada
    higher_education = None
    lower_education = None

     # Porcentagem de pessoas com salário maior de 50 mil
    higher_education_rich = None
    lower_education_rich = None

     # Qual é o número mínimo de horas que uma pessoa trabalha por semana
    min_work_hours = None

    # Porcentagem de pessoas que trabalham o número mínimo de horas por semana e têm um salário maior que 50 mil
    num_min_workers = None

    rich_percentage = None

    # Qual país tem a maior porcentagem de pessoas que ganham mais de 50 mil
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Qual a ocupação mais popular para aqueles que ganham mais de 50 mil na Índia
    top_IN_occupation = None

    # Se `print_data` for True, imprime os resultados calculados acima
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Retorna um dicionário contendo todas as métricas calculadas
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
