# This is the Python code for the Long-term Trend Prediction Models (Page 18/25).
# Designed by Wenxuan Luo and commented by Hanlin Cai (Team #2316192). Also inspried by chatGPT.
# Github Page: https://github.com/GuangLun2000/MCM-2316192/

import random
import math
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Coupling Degree Calculation  引入耦合度模型
a_j=int(input("Please input the value of coupling degree a: ")) # 输入模型耦合度
a=a_j*math.pi/180

# Set initial values
init_animal=100
#INITIAL_ANIMALS = 100
init_capacity=1000
#ANIMALS_MAX_CAPACITY = 1000
global delta_animal
global temp_animal_count
human_impact=0.01
sum_impact=0.01

init_income=10000
#INITIAL_INCOME = 10000

# Policy parameters
#HUNTING_LIMIT = 0.9
limit_hunting=a  # Policy 1: Livestock Industry (LI) 不能杀这么多的系数
COMPETITION_LIMIT = math.sin(a)  # Policy 2: Planting Industry (PI)
#limit_land=0.01
limit_tree=1-math.cos(a)   # Policy 3: Tourist Industry (TI)
TOURISM_INCOME = math.cos(a)  # Strategy 4: Animal Hunting (AH)
#init_tour=1500
ANIMAL_HUSBANDRY_INCOME = 1-math.sin(a)  # Strategy 5: Vegetation Felling (VF)
AGRICULTURE_INCOME = 1.5-a  # Strategy 6: Land Development (LD)

# ------------------------------------------------------------------------------

# 第三问函数
def restrict_hunting(animal_count,income):

    temp_animal_count = animal_count*random.uniform(0, 0.01) *(1-limit_hunting)
    new_animal_count=animal_count-temp_animal_count

    hunting_profit=1000*(1-limit_hunting)
    temp_imcome = temp_animal_count*hunting_profit*(1-random.uniform(0, 1.5))
    new_income=income+temp_imcome

    return new_animal_count ,new_income

# # Functions for each policy
# def restrict_hunting(animal_count, income):
#     new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))
#     income -= income * HUNTING_LIMIT
#     return new_animal_count, income

def restrict_landing(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))

    landing_profit=1000*(1-COMPETITION_LIMIT)
    # print("landing_pro:",landing_profit)
    income += landing_profit*(1-random.uniform(0, 1.5))
    # print("income_landing",income)

    return new_animal_count, income

def restrict_tree(animal_count,income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))

    tree_profit=1000*(1-limit_tree)
    # print("tree_pro: ",tree_profit)
    temp_income = tree_profit*(1-random.uniform(0, 1.5))
    # print("new_income: ",temp_income)
    income += temp_income
    return new_animal_count,income

def develop_tourism(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))

    tour_profit=1000*TOURISM_INCOME
    #(random.uniform(0,1.1))
    temp_income = tour_profit*(random.uniform(0,1.1))
    income+=temp_income
    return new_animal_count, income

def develop_agriculture(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))

    agri_profit=1000*AGRICULTURE_INCOME
    #(random.uniform(0,1.1))
    temp_income=agri_profit*(random.uniform(0,1.1))
    income += temp_income
    return new_animal_count, income

def develop_animal_husbandry(animal_count, income):
    new_animal_count = int(animal_count * (1 + random.uniform(0, 0.02)))

    husb_profit=1000*ANIMAL_HUSBANDRY_INCOME
    #(random.uniform(0,1.1))
    temp_income=husb_profit*(random.uniform(0,1.1))
    income += temp_income
    return new_animal_count, income

# ------------------------------------------------------------------------------

# Main function to control policy implementation 主函数
def implement_policies(num_years, initial_animals=init_animal, initial_income=init_income):
    animal_counts = [initial_animals]
    incomes = [initial_income]

    for i in range(num_years):
        animal_count = animal_counts[-1]
        income = incomes[-1]

        # Add natural animal growth
        animal_grow = random.uniform(0.05,0.15)
        max_capacity = init_capacity*(1-random.uniform(-0.05,0.05))
        # print("max_ca: ",max_capacity)

        delta_animal = animal_grow*animal_count*(1-(animal_count/max_capacity))\
                       -animal_count*random.uniform(0, 0.1) *(1-limit_hunting)
        # print("del_ani:",delta_animal)
        animal_count = animal_count+delta_animal
        # print("pre_ani: ",animal_count)

        # Check if animal count exceeds maximum capacity
        if animal_count >= max_capacity:
            animal_count = max_capacity

        # Implement each policy
        #1
        animal_count, income = restrict_hunting(animal_count, income)
        # print("income_1: ", income)
        #2
        animal_count, income = restrict_landing(animal_count, income)
        # print("income_2: ", income)
        #3
        animal_count,income=restrict_tree(animal_count, income)
        # print("income_3: ",income)
        #4
        animal_count, income = develop_tourism(animal_count, income)
        # print("income_4 ", incomes)
        #5
        animal_count, income = develop_agriculture(animal_count, income)
        # print("income_5: ", incomes)
        #6
        animal_count, income = develop_animal_husbandry(animal_count, income)
        # print("income_6: ", incomes)

        # Update lists with new values
        animal_counts.append(animal_count)
        incomes.append(income)

# ------------------------------------------------------------------------------

    # Plot results
    """ 
    ani————y1  income————y2   year————x
    """
    # Plot the first set of data on the left y-axis
    fig, ax1 = plt.subplots()

    # plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.rcParams['font.size'] = 14

# 蓝色 #003366  绿色 #006633  红色#990000
    ax2 = ax1.twinx()
    ax1.set_xlabel('Year', fontweight='bold', fontdict={'family': 'Times New Roman', 'size': 14})
    ax1.set_ylabel('Wildlife population (Unit:number)', fontweight='bold', fontdict={'family': 'Times New Roman', 'size': 14, 'color': '#003366'})
    ax2.set_ylabel('Local income (Unit:$)', fontweight='bold', fontdict={'family': 'Times New Roman', 'size': 14, 'color': '#990000'})

    ax1.plot(range(num_years + 1), animal_counts, color='#003366', marker='*', label='Wildlife population')
    ax1.tick_params(axis='y', labelcolor='#003366')
    ax2.plot(range(num_years + 1), incomes, color='#990000', marker='o', label='Local income',)
    ax2.tick_params(axis='y', labelcolor='#990000')

#    ax1.set_title('Double Y Axis Plot', fontdict={'family': 'Times New Roman', 'size': 16, 'fontweight': 'bold'})

    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    handles = handles1 + handles2
    labels = labels1 + labels2
    plt.legend(handles, labels, loc='upper left', prop={'family': 'Times New Roman', 'size': 12})

    # plt.savefig('figure_demo_1.png', dpi=300, bbox_inches='tight')
    plt.show()


# Example usage 设置预测年限
implement_policies(num_years=100)