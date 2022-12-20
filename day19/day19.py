""" Advent of Code Day 19

Robot rock! This takes long....

Author: Huub Donkers
Date: 19-12-2022
"""

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]
     
#Get instructions
blueprints = []
for d in data[:3]:
    bp, costs = d.split(":")
    instr = costs.strip().split(". ")
    #print(costs)
    bot_costs = {'ore':{}, 'clay':{}, 'obsidian':{}, 'geode':{}}
    for i, bot in enumerate(bot_costs.keys()):
        if 'and' in instr[i]:
            cost0, cost1 = instr[i].split('costs')[1].strip().split("and")
            
            bot_costs[bot][cost0.strip().split(" ")[1]] = int(cost0.strip().split(" ")[0])
            bot_costs[bot][cost1.strip().split(" ")[1].replace(".", "")] = int(cost1.strip().split(" ")[0]) 
        else:
            cost = instr[i].split('costs')[1].strip().split(" ")
            bot_costs[bot][cost[1]] = int(cost[0]) 

    #print(bot_costs)        
    blueprints.append(bot_costs)    

# Starting inventory
robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
minerals = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}

def check_minerals(costs, materials):
    have_materials = True
    for k, v in costs.items():
        #print(requirements)
        if materials[k] < v:
            have_materials = False
    return have_materials
    

it = 0
def round(robots, minerals, time_left, rests, max_ore):

    #global it
    #Copy input
    robots_cpy = robots.copy()
    minerals_cpy = minerals.copy()
    #it += 1
    #print(it)
    #print(robots, minerals_cpy, time_left)

    #Limit amount of bots
    #print(robots)
    
    if robots['ore'] > max_ore or robots['clay'] > 20 or robots['obsidian'] > 20:
        return minerals['geode']

    if rests > max_ore:
        return minerals['geode']
  
    if time_left > 0:

        # Build ore bot
        n1 = minerals['geode']+robots['geode']
        if check_minerals(bot_costs['ore'], minerals_cpy):
            next_robots = robots_cpy.copy()
            next_robots['ore'] += 1

            next_minerals = minerals_cpy.copy()
            for k, v in bot_costs['ore'].items():
                next_minerals[k] -= v

            #All robots mine their mineral
            for robot, amount in robots_cpy.items():
                next_minerals[robot] += amount

            n1 = round(next_robots, next_minerals, time_left-1,0, max_ore)   

        # Build other bots
        order=['geode', 'obsidian', 'clay']
        n2 = minerals['geode']+robots['geode']
        for bot in order:            
            if check_minerals(bot_costs[bot], minerals_cpy):
                next_robots = robots_cpy.copy()
                next_robots[bot] += 1

                next_minerals = minerals_cpy.copy()
                for k, v in bot_costs[bot].items():
                    next_minerals[k] -= v

                #All robots mine their mineral
                for robot, amount in robots_cpy.items():
                    next_minerals[robot] += amount

                n2 = round(next_robots, next_minerals, time_left-1,0, max_ore)         
                break

        #Do nothing
        #All robots mine their mineral
        for robot, amount in robots_cpy.items():
            minerals_cpy[robot] += amount
        n3 = round(robots_cpy, minerals_cpy, time_left-1,rests+1, max_ore)  
        
        return max(n1,n2,n3)

    else:
        return minerals['geode']

#max_geodes = round(robots, minerals, 24)
#print(max_geodes)

quality_lvl = 0    
for i, bot_costs in enumerate(blueprints):
    print("Checking blueprint", i+1)
    max_ore = max(bot_costs['ore']['ore'], bot_costs['clay']['ore'],bot_costs['obsidian']['ore'],bot_costs['geode']['ore'], )
    print("Max ore", max_ore)
    max_geodes = round(robots, minerals, 32, 0, max_ore)
    print("Max geodes:", max_geodes)
    quality_lvl += (i+1)*max_geodes
    
print('Quality lvl:', quality_lvl)

#1630 Too low

#Part 2
#4712 Too low
