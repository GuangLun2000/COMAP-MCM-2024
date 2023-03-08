# This is the Python code for model testing (Page 20/25, part 1).
# Designed by Wenxuan Luo and commented by Hanlin Cai (Team #2316192).
# Github Page: https://github.com/GuangLun2000/MCM-2316192/

import random
import math

init_animal=100
init_capacity=1000
human_impact=0.01
sum_impact=0.01
init_income=10000


def restrict_hunting(animal_count,income):
    temp_animal_count = animal_count*random.uniform(0, 0.01) *(1-limit_hunting)
    new_animal_count=animal_count-temp_animal_count
    hunting_profit=1000*(1-limit_hunting)
    temp_imcome = temp_animal_count*hunting_profit*(1-random.uniform(0, 1.5))
    new_income=income+temp_imcome
    return new_animal_count ,new_income

def restrict_landing(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))
    landing_profit=1000*(1-COMPETITION_LIMIT)
    income += landing_profit*(1-random.uniform(0, 1.5))
    return new_animal_count, income

def restrict_tree(animal_count,income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))
    tree_profit=1000*(1-limit_tree)
    temp_income = tree_profit*(1-random.uniform(0, 1.5))
    income += temp_income
    return new_animal_count,income

def develop_tourism(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))
    tour_profit=1000*TOURISM_INCOME
    temp_income = tour_profit*(random.uniform(0,1.1))
    income+=temp_income
    return new_animal_count, income

def develop_agriculture(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))
    agri_profit=1000*AGRICULTURE_INCOME
    temp_income=agri_profit*(random.uniform(0,1.1))
    income += temp_income
    return new_animal_count, income

def develop_animal_husbandry(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))
    husb_profit=1000*ANIMAL_HUSBANDRY_INCOME
    temp_income=husb_profit*(random.uniform(0,1.1))
    income += temp_income
    return new_animal_count, income


def implement_policies(num_years,judge,initial_animals=init_animal, initial_income=init_income):
    animal_counts = [initial_animals]
    incomes = [initial_income]
    for i in range(num_years):
        animal_count = animal_counts[-1]
        income = incomes[-1]
        animal_grow = random.uniform(0.05,0.15)
        max_capacity = init_capacity*(1-random.uniform(-0.05,0.05))
        delta_animal = animal_grow*animal_count*(1-(animal_count/max_capacity))\
                       -animal_count*random.uniform(0, 0.1) *(1-limit_hunting)
        animal_count = animal_count+delta_animal

        if animal_count >= max_capacity:
            animal_count = max_capacity

        if judge=="A":
            # 1
            animal_count, income = restrict_hunting(animal_count, income)
            # 2
            animal_count, income = restrict_landing(animal_count, income)
            # 3
            animal_count, income = restrict_tree(animal_count, income)
        elif judge=="B":
            # 1
            animal_count, income = restrict_hunting(animal_count, income)
            # 2
            animal_count, income = restrict_landing(animal_count, income)
            # 3
            animal_count, income = restrict_tree(animal_count, income)
            # 4
            animal_count, income = develop_tourism(animal_count, income)
            # 5
            animal_count, income = develop_agriculture(animal_count, income)
            # 6
            animal_count, income = develop_animal_husbandry(animal_count, income)
        elif judge=="C":
            # 4
            animal_count, income = develop_tourism(animal_count, income)
            # 5
            animal_count, income = develop_agriculture(animal_count, income)
            # 6
            animal_count, income = develop_animal_husbandry(animal_count, income)


        animal_counts.append(animal_count)
        incomes.append(income)


    return animal_counts,incomes


def stand_sum(lst):

    temp_lst=lst
    res_sum=0
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]*lst[i]
    sq_sum=math.sqrt(sum)
    for i in range(len(temp_lst)):
        res_sum+=(temp_lst[i]/sq_sum)
    return res_sum

def final(aaa,f_judge):
    res_count,res_income=implement_policies(num_years=100,judge=f_judge)
    single_sum=math.sin(aaa)*stand_sum(res_income)+math.cos(aaa)*stand_sum(res_count)
    return single_sum

T=input("请输入控制量，A为前三，B为全部，C为后三")
#a为弧度

a_j=90
res_lst = []

for i in range(1,a_j):

    a = a_j * math.pi / 180

    limit_hunting = a
    COMPETITION_LIMIT = math.sin(a)
    limit_tree = 1 - math.cos(a)
    TOURISM_INCOME = math.cos(a)
    ANIMAL_HUSBANDRY_INCOME = 1 - math.sin(a)
    AGRICULTURE_INCOME = 1.5 - a

    init_animal = 100
    init_capacity = 1000
    human_impact = 0.01
    sum_impact = 0.01
    init_income = 10000

    res_lst.append(final(a_j,T))


print(res_lst)