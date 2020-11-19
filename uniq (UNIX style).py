# Implement a function which behaves like the uniq command in UNIX.

# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

# Example:

# ["a", "a", "b", "b", "c", "a", "b", "c"]  =>  ["a", "b", "c", "a", "b", "c"]

def uniq(seq): 
    return [seq[i] for i in range(len(seq)) if seq[i] != seq[i-1] or i == 0]


print(uniq(["a", "a", "b", "b", "c", "a", "b", "c"]))