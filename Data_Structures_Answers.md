Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method? 
O(1)

2. What is the space complexity of your ring buffer's `append` function? 
I use the attributes given on the class, so no new memory is used.

3. What is the runtime complexity of your ring buffer's `get` method?
O(n)

4. What is the space complexity of your ring buffer's `get` method?
An array is declared and filled with non-None values each time the get method is called. This could be optimized further. 

5. What is the runtime complexity of the provided code in `names.py`?
O(n^2)

6. What is the space complexity of the provided code in `names.py`?
The names_1 and names_2 variables use memory and can be cumbersome on certain machines. The duplicates array is another declared piece of memory.

7. What is the runtime complexity of your optimized code in `names.py`?
O(n)

8. What is the space complexity of your optimized code in `names.py`?
Similar to the provided code except for a few extra variables (i, j).