# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
#count=0
linklist=[]
for i in range(0,length_of_circular_linked_list):
  linklist.append(circular_linked_list[i])
for i in range(length_of_circular_linked_list):
  if circular_linked_list[0]!=circular_linked_list[i]:
    #count+=1
    linklist.append(circular_linked_list[i])
  elif circular_linked_list[0]==circular_linked_list[i]:
    break
  for i in linkedlist:
    print(i,end=' ')
