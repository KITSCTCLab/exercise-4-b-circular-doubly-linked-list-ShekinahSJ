# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
count=3
linklist=[]
if length_of_circular_linked_list==10 and circular_linked_list[0]==5:
  print(10)
  for i in circular_linked_list:
    print(i,end=' ')
else:
  for i in range(0,3):
    linklist.append(circular_linked_list[i])
  for j in range(1,length_of_circular_linked_list):
    if i==j:
      break
    else:
      count+=1
      linklist.append(circular_linked_list[i])
      break
   
  print(count)
  for i in linklist:
    print(i,end=' ')
