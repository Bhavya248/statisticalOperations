#Statistics Solver
exit_program = "Y"
while True:
     if exit_program == ("N" or "n"):
        quit()
     else:      
        print('''Welcome to  statistics point
        You will find all modules for performing statistical operations...
        Just type the operation and module appears:
        MR   --> Mean For Raw data
        MU   --> Mean For Ungrouped frequency data
        MG   --> Mean For Grouped frequency data
        MIR  --> Median For Raw data
        MIU  --> Median For Ungrouped data
        MIG  --> Median For Grouped data
        MOR  --> Mode For Raw data
        MOU  --> Mode For Ungrouped data
        MOG  --> Mode For Grouped data
        ''')
        operation = str(input('Enter the operation from above list --> '))
        #Mean For Raw data
        if operation == 'MR':
            N = int(input('Enter number of observation --> '))
            observation = []
            for i in range(N):
                print('Enter the integral observation --> ')
                observation.append(int(input()))
            print('Your entered data:')
            print(observation)
            summation = 0
            for i in range(N):
                summation = summation + i
            print('Mean for given data is',summation/N)



        #Mean for Ungrouped frequency data   
        elif operation == 'MU' :
            print('Enter number of observation --> ')
            N = int(input())
            observation = []
            frequency = []
            for i in range(N):
                print('Enter the integral observation --> ')
                obs = int(input())
                observation.append(int(obs))
                print('Enter Frequency for observation --> ')
                freq = int(input())
                frequency.append(freq)
            print('Your entered data:')
            fx = 0
            print('Observation | Frequency')
            for i in range(N):
                print(observation[i],'|',frequency[i])
                fx = (observation[i]*frequency[i]) + fx
            print('Mean for the data is ',fx/N)


            
        #Mean For Grouped frequency data
        elif operation == 'MG' :
            N = int(input('Enter number of observation --> '))
            observation = []
            frequency =[]
            classmark =[]
            print('Enter class interval in following format -->  obs-obs')
            print(' ')
            for p in range(N):
                print("Enter the class interval --> ")
                obs = str(input())
                occ = obs.index("-")
                ocp = occ+1
                l = len(obs)+1
                a =(obs[:occ])
                b =(obs[ocp:l])
                obs_list = (a,b)
                observation.append(obs_list)
                classmark.append((int(observation[p][0])+int(observation[p][1]))/2)
                print('Enter frequency for observation --> ')
                frequency.append(int(input()))
                print(" ")
                result = 0
            print('Your entered data')
            print('Observation | Frequency | Classmark')
            for i in range(N):
                print(observation[i][0],'-',observation[i][1],'    | ',frequency[i],'      | ',classmark[i])
                result = (classmark[i]*frequency[i])
            print('Mean for the data is',round(result/sum(frequency)))



        #Median for raw data
        elif operation == 'MIR' :
            N = int(input("Enter number of observation --> "))
            observation = []
            for i in range(N):
                print("Enter value of ",i+1," observation -->")
                observation.append((input()))
            print("Data entered by you in sorted manner is: ")
            s_obs = sorted(observation)
            print(sorted(observation))
            median = 0
            median_value = 0
            if N%2 != 0 :
                median_value = (N+1)/2
                median = s_obs[int(median_value)-1]
                print("Median for the given data is ",median)
            else :
                a = int((N/2)-1)
                b = int(((N/2)+1)-1)
                median = (int(s_obs[a])+int(s_obs[b]))/2
                print("Median for the given data is ",median)


        #Median for ungrouped frequency distribution
        elif operation == "MIU" :
            N = int(input("Enter number of observation --> "))
            temp_observation = []
            observation = []
            frequency =[]
            count = 0
            for i in range(N):
                print("Enter value of ",i+1," observation -->")
                temp_observation.append((input()))
                print("Enter frequency for",temp_observation[i]," -->")
                frequency.append(int((input())))
                print(" ")
            for i in range(N):
                for j in range(int(frequency[i])):
                    observation.append(int(temp_observation[i]))
            sort_obs = sorted(observation)
            if len(sort_obs < 100):
                print("Data entered by you in sorted manner is: ")
                print(sort_obs)
            else :
                pass
            median = 0
            median_value = 0
            count = sum(frequency)
            if count%2 != 0 :
                median_value = (count+1)/2
                median = sort_obs[int(median_value)-1]
                print("Median for the given data is ",median)
            else :
                a = int((count/2)-1)
                b = int(((count/2)+1)-1)
                median = (int(sort_obs[a])+int(sort_obs[b]))/2
                print("Median for the given data is ",median)



        #Median for grouped freqquency distribution:
        elif operation == "MIG" :
            observation = []
            frequency = []
            lcf = []
            N = int(input('Enter the number of observations --> '))
            print('Enter class interval in following format -->  obs-obs')
            print(' ')
            lcfv = 0
            for p in range(N):
                print("Enter the class interval --> ")
                obs = str(input())
                occ = obs.index("-")
                ocp = occ+1
                l = len(obs)+1
                a =(obs[:occ])
                b =(obs[ocp:l])
                obs_list = (int(a),int(b))
                observation.append(obs_list)
                print('Enter the frequency for ',observation[p],' --> ')
                frequency.append(int(input()))
                lcfv = lcfv + frequency[p]
                lcf.append(lcfv)
            F = (sum(frequency))/2
            median_class = 0
            for i in range(N):
                if lcf[i] > F:
                    median_class = i
                    break
                else :
                    pass
            ll = observation[median_class][0]
            ul = observation[median_class][1]
            #n/2 = F
            cf = lcf[i-1]
            fr = frequency[i]
            median = ll + ((((F-cf)/fr))*(ul-ll))
            print('Data entered by you :')
            print('Observation | Frequency | LCF ')
            for i in range(N):
                print(observation[i][0],'-',observation[i][1],'       | ' ,frequency[i],'       | ',lcf[i])
            print('Median for the given data is ',round(median))
            
        #Mode for raw data
        elif operation == 'MOR' :
            N = int(input("Enter number of observation --> "))
            observation = []
            frequency =[]
            for i in range(N):
                print('Enter the ',i,' observation -->')
                observation.append(int(input()))
            max_occur = 0
            observation = sorted(observation)
            for i in observation :
                count = 0
                for p in observation:
                    if i == p :
                        count = count + 1
                frequency.append([i,count])
            frequency_obs = []
            for i in range(N):
                frequency_obs.append(frequency[i][1])
            print(frequency_obs)    
            mode_frequency = max(frequency_obs)
            #mode = list(frequency.keys())[list(frequency.values()).index(mode_frequency)]
            for i in range(len(frequency_obs)):
                if mode_frequency==frequency[i][1]:
                    mode=frequency[i][0]
                print('mode for given data is -->',mode)
            

            print("Continue program (Y/N) :")
            exit_program = input()    
    


     
     
         
     
    
   
         
    
    


            
                
        
    
    
    
        
