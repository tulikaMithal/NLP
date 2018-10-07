# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:07:05 2018

@author: lenovo
"""

import sys
import numpy as np


# opening file content
file =  open(sys.argv[1], 'r', encoding='latin')


#reading file content
content=""
for line in file:
    content = content + line
    
#tokenizing the contents of file
tokens = content.split()

#declaring dictionary for bigrams present in file
bigramMap = {}

#declaring dictionary for frequency of each word in file
countMap = {}

#No. of words in file
length = len(tokens)

#forming bigram map
for i in range(length-1):
    bigram = tokens[i]+" "+tokens[i+1]
    
    if bigram in bigramMap:
        bigramMap[bigram] = bigramMap[bigram]+1
    else:
        bigramMap[bigram] = 1
        
        
#forming tokens map
for i in range(length):
    if tokens[i] in countMap:
        countMap[tokens[i]] += 1
    else:
        countMap[tokens[i]] = 1
    

# reading sentences from command line arguments  
sentence1 = sys.argv[2]
sentence2 = sys.argv[3]


#finding number of tokens in sentences
l1 = len(sentence1.split())
l2 = len(sentence2.split())


#declaring bigram count table for sentence 1 with no smoothing
table1_sent1_nosmooth = np.zeros((l1,l1))

#declaring bigram count table for sentence 2 with no smoothing
table2_sent2_nosmooth = np.zeros((l2,l2))

#declaring bigram probability table for sentence 1 with no smoothing
table1_prob_sent1_nosmooth = np.zeros((l1,l1))

#declaring bigram probability table for sentence 2 with no smoothing
table2_prob_sent2_nosmooth = np.zeros((l2,l2))


# filling bigram count table for sentence 1 without smoothing
for i in range(l1):
    for j in range(l1):
        
        word1 = sentence1.split()[i]
        word2 = sentence1.split()[j]
        
        bigram = word1+" "+word2
        
        if bigram in bigramMap:
            table1_sent1_nosmooth[i][j] = bigramMap[bigram]
        else:
            table1_sent1_nosmooth[i][j] = 0
            
            
print("\n#######################################################################################\n")            
print("\nBigram count table for Sentence 1 without smoothing\n")           
print(table1_sent1_nosmooth)
print("\n#######################################################################################\n")    
 
# filling bigram count table for sentence 2 without smoothing       
for i in range(l2):
    for j in range(l2):
        
        word1 = sentence2.split()[i]
        word2 = sentence2.split()[j]
        
        bigram = word1+" "+word2
        
        if bigram in bigramMap:
            table2_sent2_nosmooth[i][j] = bigramMap[bigram]
        else:
            table2_sent2_nosmooth[i][j] = 0
 
print("\n#######################################################################################\n")              
print("\nBigram count table for Sentence 2 without smoothing\n")           
print(table2_sent2_nosmooth)
print("\n#######################################################################################\n")   
            
# probability table for sentence1 without smoothing       
for i in range(l1):
    for j in range(l1):
        
        word1 = sentence1.split()[i]
        word2 = sentence1.split()[j]
        
        bigram = word1+" "+word2
        
        if word1 in countMap:
            cnt = countMap[word1]
        else:
            cnt=1
        table1_prob_sent1_nosmooth[i][j] = (table1_sent1_nosmooth[i][j])/cnt
  
print("\n#######################################################################################\n")         
print("\nBigram probability table for Sentence 1  without smoothing\n")        
print(table1_prob_sent1_nosmooth) 
print("\n#######################################################################################\n")          
        
# probability table for sentence2 without smoothing  
for i in range(l2):
    for j in range(l2):
        
        word1 = sentence2.split()[i]
        word2 = sentence2.split()[j]
        
        bigram = word1+" "+word2
        
        if word1 in countMap:
            cnt = countMap[word1]
        else:
            cnt=1
        table2_prob_sent2_nosmooth[i][j] = (table2_sent2_nosmooth[i][j])/cnt

print("\n#######################################################################################\n")           
print("\nBigram probability table for Sentence 2  without smoothing\n")        
print(table2_prob_sent2_nosmooth) 
print("\n#######################################################################################\n")          
        
# finding probability of sentence 1 without smoothing        
        
prob_sent1 = 1

for i in range(l1-1):
    prob_sent1 *= table1_prob_sent1_nosmooth[i][i+1]

prob_sent1 = prob_sent1 * ((countMap[(sentence1.split())[0]])/length)

print("\n#######################################################################################\n")   
print("\nProbability of Sentence 1 without smoothing\n")
print(prob_sent1)
print("\n#######################################################################################\n")   

# finding probability of sentence 2 without smoothing   
 
prob_sent2 = 1

for i in range(l2-1):
    prob_sent2 *= table2_prob_sent2_nosmooth[i][i+1]

prob_sent2 = prob_sent2 * ((countMap[(sentence2.split())[0]])/length)


print("\n#######################################################################################\n")   
print("\nProbability of Sentence 2 without smoothing\n")
print(prob_sent2)
print("\n#######################################################################################\n")      
    
#######################################################################################################################################################
# with smoothing
######################################################################################################################################################

#declaring bigram count table for sentence 1 with  smoothing
table1_sent1_smooth = np.zeros((l1,l1))

#declaring bigram count table for sentence 2 with  smoothing
table2_sent2_smooth = np.zeros((l2,l2))

#declaring bigram probability table for sentence 1 with  smoothing
table1_prob_sent1_smooth = np.zeros((l1,l1))

#declaring bigram probability table for sentence 2 with  smoothing
table2_prob_sent2_smooth = np.zeros((l2,l2))


# filling bigram count table for sentence 1 with smoothing
for i in range(l1):
    for j in range(l1):
        
        word1 = sentence1.split()[i]
        word2 = sentence1.split()[j]
        
        bigram = word1+" "+word2
        
        if bigram in bigramMap:
            table1_sent1_smooth[i][j] = bigramMap[bigram]+1
        else:
            table1_sent1_smooth[i][j] = 1

print("\n#######################################################################################\n")               
print("\nBigram count table for Sentence 1 with smoothing\n")
print(table1_sent1_smooth) 
print("\n#######################################################################################\n")              
            
# filling bigram count table for sentence 2 with smoothing        
for i in range(l2):
    for j in range(l2):
        
        word1 = sentence2.split()[i]
        word2 = sentence2.split()[j]
        
        bigram = word1+" "+word2
        
        if bigram in bigramMap:
            table2_sent2_smooth[i][j] = bigramMap[bigram]+1
        else:
            table2_sent2_smooth[i][j] = 1
 

print("\n#######################################################################################\n")              
print("\nBigram count table for Sentence 2 with smoothing\n")           
print(table2_sent2_smooth)            
print("\n#######################################################################################\n")   

         
# probability table for sentence1 with smoothing          
for i in range(l1):
    for j in range(l1):
        
        word1 = sentence1.split()[i]
        word2 = sentence1.split()[j]
        
        bigram = word1+" "+word2
        
        if word1 in countMap:
            cnt = countMap[word1]+ len(countMap)
        else:
            cnt=len(countMap)
        table1_prob_sent1_smooth[i][j] = (table1_sent1_smooth[i][j])/cnt
        
print("\n#######################################################################################\n")          
print("\nBigram probability table for Sentence 1 with smoothing\n")
print(table1_prob_sent1_smooth)        
print("\n#######################################################################################\n")   

       
# probability table for sentence2 with smoothing           
for i in range(l2):
    for j in range(l2):
        
        word1 = sentence2.split()[i]
        word2 = sentence2.split()[j]
        
        bigram = word1+" "+word2
        
        if word1 in countMap:
            cnt = countMap[word1]+len(countMap)
        else:
            cnt=len(countMap)
        table2_prob_sent2_smooth[i][j] = (table2_sent2_smooth[i][j])/cnt
  

print("\n#######################################################################################\n")         
print("\nBigram probability table for Sentence 2  with smoothing\n")        
print(table2_prob_sent2_smooth)        
print("\n#######################################################################################\n")          
        
# finding probability of sentence 1 with smoothing        
prob_sent1 = 1

for i in range(l1-1):
    prob_sent1 *= table1_prob_sent1_smooth[i][i+1]

prob_sent1 = prob_sent1 * ((countMap[(sentence1.split())[0]]+1)/(length+len(countMap)))

print("\n#######################################################################################\n")   
print("\nProbability of Sentence 1 with smoothing\n")
print(prob_sent1)
print("\n#######################################################################################\n")   

# finding probability of sentence 2 with smoothing
prob_sent2 = 1

for i in range(l2-1):
    prob_sent2 *= table2_prob_sent2_smooth[i][i+1]

prob_sent2 = prob_sent2 * ((countMap[(sentence2.split())[0]]+1)/(length+len(countMap)))

print("\n#######################################################################################\n")   
print("\nProbability of Sentence 2 with smoothing\n")
print(prob_sent2)
print("\n#######################################################################################\n")   
        
        
        

        
    
        
        
        
        



