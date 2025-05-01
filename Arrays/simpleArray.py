class SimpleArray:
    def __init__(self, size):
        """
        Initialize a simple array with a fixed size.
        
        Key concepts:
        1. Fixed Size: Arrays have a predetermined size that cannot be changed after creation
        2. Contiguous Memory: Elements are stored in consecutive memory locations
        3. Index-based Access: Elements can be accessed using indices (0 to size-1)
        
        Parameters:
        - size: The maximum number of elements the array can hold
        
        Implementation details:
        - We use a Python list to simulate the array behavior
        - All elements are initially set to None to represent empty slots
        - We track the actual number of elements separately from the size
        """
        self.size = size        # Maximum capacity of the array
        self.array = [None] * size  # Create array with all None values
        self.length = 0         # Current number of elements in the array

    # How to insert values into the array
    def insert(self, value):
        if self.length>=self.size:
            print("Array is full")
            return
        self.array[self.length]=value
        self.length+=1
    # How to delete first instance of values from the array
    def delete(self,value):
        for i in range(self.length):
            if self.array[i]==value:
                self.array[i]=None
                self.length-=1
                return
    # How to find the index of the first instance of a value in the array
    def findIndex(self,value):
        for i in range(self.length):
            if self.array[i]==value:
                return i
            


# Example usage
if __name__ == "__main__":
    # Create an array that can hold 5 elements
    my_array = SimpleArray(5)
    
    # Print the initial state
    print("Array size:", my_array.size)
    print("Current length:", my_array.length)
    print("Array contents:", my_array.array) 

    # Insert some values
    my_array.insert(10)
    my_array.insert(20)
    my_array.insert(30)
    my_array.insert(30)
    print("Array Contents: After Inserting values",my_array.array)
    # delete some values 
    my_array.delete(10)
    my_array.delete(30)
    print("Array Contents: After Deleting values",my_array.array)
    # finding the index of a value
    print("what is the index of the value in my array:",my_array.findIndex(20))