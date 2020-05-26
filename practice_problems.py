'''
1. How many different ways can you rearrange the letters in the word "prepare"?
'''

# word = list('prepare')

# word_set = list(set(word))

# words_lst = []

# for i in word_set:
#     for j in word_set:
#         for k in word_set:
#             for l in word_set:
#                 for m in word_set:
#                     for n in word_set:
#                         for o in word_set:
#                             potential = ''.join([i,j,k,l,m,n,o])
#                             if sorted(potential) == sorted(word):
#                                 if potential not in words_lst:
#                                     words_lst.append(potential)

# for word in words_lst:
#     print(word)

# print(len(words_lst))


# # 'prepare'
# # p*2
# # e*2
# # r*2

# # 7!
# # --------
# # 2!*2!*2!



'''
2. Given two 6-sided dice, what is the probability of rolling the same number of pips on both dice?
'''

# dice_roll = [1,2,3,4,5,6]
# possibilities = []

# for roll1 in dice_roll:
#     for roll2 in dice_roll:
#         possibilities.append([roll1, roll2])

# # for roll in possibilities:
# #     print(roll)

# identicals =  []
# for lst in possibilities:
#     if lst[0] == lst[1]:
#         identicals.append(lst)

# print(len(identicals) / len(possibilities))



'''
3. You plan on flipping a coin 6 times. How many total outcomes of the 6 coin flips can you have with exactly 2 tails?
'''
# binary = [0, 1]

# heads_2_list = []
# for i in binary:
#     for j in binary:
#         for k in binary:
#             for l in binary:
#                 for m in binary:
#                     for n in binary:
#                         if [i,j,k,l,m,n].count(1) == 2:
#                             heads_2_list.append([i,j,k,l,m,n])

# for result in heads_2_list:
#     print(result)

# print(len(heads_2_list))



'''
4. How many ways can you award an identical award to 3 of 11 people?
'''

outcome = [0,1]
lst = []
for i in outcome:
    for j in outcome:
        for k in outcome:
            for l in outcome:
                for m in outcome:
                    for n in outcome:
                        for o in outcome:
                            for p in outcome:
                                for q in outcome:
                                    for r in outcome:
                                        for s in outcome:
                                            if [i,j,k,l,m,n,o,p,q,r,s].count(1)==3:
                                                lst.append([i,j,k,l,m,n,o,p,q,r,s])

for item in lst:
    print(item)

print(len(lst))







'''
5. If the chance of winning the lottery is 1/100, and a person plays the lottery every day for 100 days, what is the probability of winning within those 100 days?
'''


'''
6. You will roll a 5-sided die 10 times. What is the probability that the sum of the dice will equal 25?
'''


'''
7. Suppose on average that there are 25 dust particles in a droplet of rain in a given region. What is the probability that there 50 dust particles in 3 droplets of rain?
'''


'''
8. Suppose a circuit is designed with 20 redundant components, of which 7 must be functioning for the circuit to perform as expected. At any given time, there is a 0.05 probability that one of the components will have failed. What is the probability that, at any given time, the circuit is functioning?
'''


'''
9. A canvasser is going door to door to collect donations. On average, 20% of people whose door the canvasser knocks on will give the requested donation of $20. On a given day, the canvasser will knock on 20 doors. What is the probability the canvasser will make at least $100?
'''


'''
10. A door to door salesperson is selling really nice vacuums. One in 20 people will buy this vacuum. Each house visited takes about 30 minutes. The goal is to sell 1 vacuum a day. What is the probability of a vacuum being sold in under 8 hours?
'''


'''
11. On average, a plumber fixes 7 broken pipes a day. What is the probability that the plumber will fix 15 pipes on a given day?
'''


'''
12. 
'''