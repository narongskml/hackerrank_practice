def permutationEquation(p):   #Deep Seek
    # Create a dictionary to map each value to its index (1-based)
    value_to_index = {value: idx + 1 for idx, value in enumerate(p)}
    
    result = []
    
    # Iterate through each x from 1 to n
    for x in range(1, len(p) + 1):
        # Find y such that p(y) = x
        y = value_to_index[x]
        
        # Find z such that p(z) = y
        z = value_to_index[y]
        
        # Append z to the result
        result.append(z)
    
    return result

# Example usage:
p = [2, 3, 1]
print(permutationEquation(p))  # Output: [2, 3, 1] 


def permutationEquation1(p):  #Chat GPT
    index_map = {value: idx + 1 for idx, value in enumerate(p)}  # Store indices of each value in p
    result = []

    for x in range(1, len(p) + 1):  # Iterate over 1 to n
        y = index_map[index_map[x]]  # Find y such that p(p(y)) = x
        result.append(y)

    return result

# Example usage:
p = [5, 2, 1, 3, 4]
print(permutationEquation1(p))  # Output: [4, 2, 5, 1, 3]