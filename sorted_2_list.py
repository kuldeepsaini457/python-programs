lt1=[int(i) for i in input("Enter the list one: ").split()]
lt2=[int(i) for i in input("Enter the list two: ").split()]
merge=lt1[1:]+lt2[1:]
for i in range(len(lt1)):
    min=merge[i]
    for j in range(len(lt2)):
        if min>merge[j]:
            min=merge[j]
            merge[j]=merge[i]
            merge[i]=min
print("Combined sorted list is: ",merge)