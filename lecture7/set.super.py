# Define two sets
set_a = {1, 2, 3, 4}
set_b = {2, 3}
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 4, 5}

# Superset and Subset
print("Is set_a a superset of set_b?:", set_a >= set_b)  # Output: True
print("Is set_b a subset of set_a?:", set_b <= set_a)    # Output: True

# Proper Superset and Proper Subset
print("Is set_a a proper superset of set_b?:", set_a > set_b)  # Output: True
print("Is set_b a proper subset of set_a?:", set_b < set_a)    # Output: True

# Equal Sets
print("Are set_a and set_c equal?:", set_a == set_c)  # Output: True

# Related but not equal (one is a subset but not equal)
print("Is set_b a subset of set_d and not equal?:", set_b <= set_d and set_b != set_d)  # Output: True
