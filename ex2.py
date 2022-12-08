def main():

   print("Enter the start and end of the range")
   
   start = int(input("The beginning: "))
   end = int(input("The end: "))
  
   print("All numbers in the range: ")
   for i in range(start, end + 1):
       print(i, end=" ")
   print()
   print("All numbers in the range are in descending order: ")
   for i in range(end, start - 1, -1):
       print(i, end=" ")
   print()
   print("All numbers are multiples of 7: ")
   for i in range(start, end + 1):
       if i % 7 == 0:
           print(i, end=" ")
   print()
   print("The number of numbers that are multiples of 5: ")
   count = 0
   for i in range(start, end + 1):
       if i % 5 == 0:
           count += 1
   print(count)

if __name__ == "__main__":
   main()
