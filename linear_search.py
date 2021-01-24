def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i+1
   return -1
arr = [1,2,3,4,5,6,7,8,9,10]
x=int(input("Enter the number that you want to search: "))
index=linearsearch(arr,x)
if index>0:
    print("Element found at index "+str(index))
else:
    print(f"Element not found in the array {arr}")