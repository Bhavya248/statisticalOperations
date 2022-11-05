# This is the same code with functional and never ending approch 
def input_data():
    print('''Enter the format of data :
              RAW --> RAW data
              UGF --> Ungrouped Frequency Distribution
              GRF --> Grouped Frequency Distribution''')
    data_format = str(input())
    observation = []
    frequency = []
    lcf = []
    classmark = []
    N = int(input('Enter number of observation --> '))
    '''The section below will take data for observations'''
    if data_format == 'RAW' :
         for i in range(N):
              print('Enter the integral observation --> ')
              observation.append(int(input()))
         print('Your entered data')
         print(observation)
    '''End for Raw observations'''   
    '''Ungrouped frequency distribution'''
    if data_format == 'UGF' :
        for i in range(N):
         print('Enter the integral observation --> ')
         obs = int(input())
         observation.append(int(obs))
         print('Enter Frequency for observation --> ')
         freq = int(input())
         frequency.append(freq)
        print('Your entered data:')
        print('Observation | Frequency')
        for i in range(N):
            print(observation[i],'|',frequency[i])
    '''End for ungrouped frequency'''
    '''Grouped frequency distribution'''
    if data_format == 'GRF':
        print('Enter class interval in following format -->  obs-obs')
        print(' ')
        for p in range(N):
             print("Enter the class interval --> ")
             obs = str(input())
             occ = obs.index("-")
             ocp = occ+1
             l =   len(obs)+1
             a =( obs[:occ])
             b =(obs[ocp:l])
             obs_list = (a,b)
             observation.append(obs_list)
             classmark.append((int(observation[p][0])+int(observation[p][1]))/2)
             print('Enter frequency for observation --> ')
             frequency.append(int(input()))
             print(" ")
        print('Your entered data') 
        print('Observation | Frequency | Classmark')
        for i in range(N):
              print(observation[i][0],'-',observation[i][1],'    | ',frequency[i],'      | ',classmark[i])
              result = (classmark[i]*frequency[i])
        return data_format      
 
def operation(x,y) :
    if x == 'MEAN' and y == 'raw' :
        summation = 0
        for i in range(N):
            summation = summation + i
        print('Mean for given data is',summation/N)



continue_program = "Y"
while continue_program == "Y" :
    if continue_program == "N" :
        quit()
    elif continue_program == 'Y':
        f = input_data()
        print('''Enter the operation to be performed for the entered data :
             MEAN       --> for mean of data
             MEDIAN     --> for median of data
             MODE       --> for mode of data
             QUARTILE   --> for quartile of data
             DECILE     --> For Decile of data
             PERCENTILE -->for percentile of data''')
        operations_key = str(input())
        operation(operations_key,f)
