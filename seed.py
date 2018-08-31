import math
import random
def sum(list):
    total = 0.0
    for line in list:
        total += line
    return total
def rand(a, b):
    number =  random.uniform(a,b)
    return math.floor(number*100)/100
PI = math.pi
def fitness(x1,x2):
    return 2*(x1-3)*math.sin(8*PI*x2)+(x2-4)*math.cos(13*PI*x1)
def todecimal(str):
    parta = str[0:4]
    partb = str[4:]
    numerical = int(parta,2)
    partb = partb[::-1]
    for i in range(len(partb)):
        numerical += int(partb[i])*math.pow(0.5,(i+1))
    return numerical
def tobinarystring(numerical):
    numa = math.floor(numerical)
    numb = numerical - numa
    bina = bin(numa)
    bina = bina[2:]
    result = "0"*(4-len(bina))
    result += bina
    for i in range(7):
        numb *= 2
        result += str(math.floor(numb))
        numb = numb - math.floor(numb)
    return result
class Population:
    def __init__(self):
        self.pop_size = 500     # 设定种群个体数为500
        self.population = [[]]    # 种群个体的二进制字符串集合，每个个体的字符串由一个列表组成[x1,x2]
        self.individual_fitness = []    # 种群个体的适应度集合
        self.chrom_length = 22  # 一个染色体22位
        self.results = [[]]     # 记录每一代最优个体，是一个三元组(value,x1_str,x2_str)
        self.pc = 0.6           # 交配概率
        self.pm = 0.01          # 变异概率
        self.distribution = []  # 用于种群选择时的轮盘
    def initial(self):
        for i in range(self.pop_size):
            x1 = rand(0,10)
            x2 = rand(0,14)
            x1_str = tobinarystring(x1)
            x2_str = tobinarystring(x2)
            self.population.append([x1_str,x2_str]) # 添加一个个体
            fitness_value = fitness(x1,x2)
            self.individual_fitness.append(fitness_value)   # 记录该个体的适应度
        self.population = self.population[1:]
        self.results = self.results[1:]
    def eliminate(self):
        for i in range(self.pop_size):
            if self.individual_fitness[i]<0:
                self.individual_fitness[i] = 0.0
    def getbest(self):
        "取得当前种群中的一个最有个体加入results集合"
        index = self.individual_fitness.index(max(self.individual_fitness))
        x1_str = self.population[index][0]
        x2_str = self.population[index][1]
        value = self.individual_fitness[index]
        self.results.append((value,x1_str,x2_str,))
    def select(self):
        "轮盘算法，用随机数做个体选择，选择之后会更新individual_fitness对应的数值"
        "第一步先要初始化轮盘"
        "选出新种群之后更新individual_fitness"
        total = sum(self.individual_fitness)
        begin = 0
        for i in range(self.pop_size):
            temp = self.individual_fitness[i]/total+begin
            self.distribution.append(temp)
            begin = temp
        new_population = []
        new_individual_fitness = []
        for i in range(self.pop_size):
            num = random.random()   # 生成一个0~1之间的浮点数
            j = 0
            for j in range(self.pop_size):
                if self.distribution[j]<num:
                    continue
                else:
                    break
            index = j if j!=0 else (self.pop_size-1)
            new_population.append(self.population[index])
            new_individual_fitness.append(self.individual_fitness[index])
        self.population = new_population
        self.individual_fitness = new_individual_fitness
    def crossover(self):
        "选择好新种群之后要进行交配"
        "注意这只是一次种群交配，种群每一次交配过程，会让每两个相邻的染色体进行信息交配"
        for i in range(self.pop_size-1):
            if random.random()<self.pc:
                cross_position = random.randint(1,self.chrom_length-1)
                i_x1x2_str = self.population[i][0]+self.population[i][1]    # 拼接起第i个染色体的两个二进制字符串
                i1_x1x2_str = self.population[i+1][0]+self.population[i+1][1]    # 拼接起第i+1个染色体的两个二进制字符串
                str1_part1 = i_x1x2_str[:cross_position]
                str1_part2 = i_x1x2_str[cross_position:]
                str2_part1 = i1_x1x2_str[:cross_position]
                str2_part2 = i1_x1x2_str[cross_position:]
                str1 = str1_part1+str2_part2
                str2 = str2_part1+str1_part2
                self.population[i] = [str1[:11],str1[11:]]
                self.population[i+1] = [str2[:11],str2[11:]]
        "然后更新individual_fitness"
        for i in range(self.pop_size):
            x1_str = self.population[i][0]
            x2_str = self.population[i][1]
            x1 = todecimal(x1_str)
            x2 = todecimal(x2_str)
            self.individual_fitness[i] = fitness(x1,x2)
    def mutation(self):
        "个体基因变异"
        for i in range(self.pop_size):
            if random.random()<self.pm:
                x1x2_str = self.population[i][0]+self.population[i][1]
                pos = random.randint(0,self.chrom_length-1)
                bit = "1" if x1x2_str[pos]=="0" else "0"
                x1x2_str = x1x2_str[:pos]+bit+x1x2_str[pos+1:]
                self.population[i][0] = x1x2_str[:11]
                self.population[i][1] = x1x2_str[11:]
        "然后更新individual_fitness"
        for i in range(self.pop_size):
            x1_str = self.population[i][0]
            x2_str = self.population[i][1]
            x1 = todecimal(x1_str)
            x2 = todecimal(x2_str)
            self.individual_fitness[i] = fitness(x1, x2)
    def solving(self,times):
        "进行times次数的整个种群交配变异"
        "先获得初代的最优个体"
        self.getbest()
        for i in range(times):
            "每一代的染色体个体和适应值，需要先淘汰，然后选择，再交配、变异，最后获取最优个体。然后进入下一代"
            self.eliminate()
            self.select()
            self.crossover()
            self.mutation()
            self.getbest()
    def returnbest(self):
        self.results.sort()
        return self.results[len(self.results)-1]
if __name__ == '__main__':
    demo = Population()
    demo.initial()
    demo.solving(100)
    answer = demo.returnbest()
    value = answer[0]
    x1 = todecimal(answer[1])
    x2 = todecimal(answer[2])
    print(x1,x2,value)