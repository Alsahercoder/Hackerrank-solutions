def push(arr):
	
	print("Enter the element:")
	num = int(input())
	arr.append(num)
	print(num, "is pushed into the stack")
	

def pop(arr):
	
	print(arr[-1], "is poped out of the stack")
	arr.pop()
	
	
def display(arr):
	
	print(arr)
	
if __name__ == "__main__":
	
	arr = []
	while True:
		
		choice = 0
		print("***Menu***")
		print("1. Push()")
		print("2. Pop()")
		print("3. Display()")
		
		print("Enter your choice:", end = "")
		choice = int(input())
		
		if choice == 1:
			push(arr)
		elif choice == 2:
			pop(arr)
		elif choice == 3:
			display(arr)
		else:
			break
