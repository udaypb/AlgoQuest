
'''
return random task given weights of the tasks.
tags: random, weighted
complexity: Time:O(n), Space:O(n)
company: Uber
'''
import random
def random_task(tasks, weights): # len(tasks) == len(weights)
   dictt = {}
   #get sum of all weights
   weightSum = sum(weights)
   #build dictionary with task as key and a range of weights as value
   start = 0
   for i in range(len(tasks)):

       dictt[tasks[i]] = [start + 1, start + weights[i]]
       start += weights[i]
   random_num = random.randint(1, weightSum)
   for k, v in dictt.items():
       if v[0] <= random_num <= v[1]:
           return k
