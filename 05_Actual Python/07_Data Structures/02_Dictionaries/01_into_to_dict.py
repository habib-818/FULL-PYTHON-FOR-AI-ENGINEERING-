## WHAT IS DICTIONARY?
"""
 Dictionary is like Vocabulary which has key and value 
 Ex: "age" = 25
"""

## EXAMPLE 

student = {
    "name": "Habib",
    "age": 20,
    "country": "Bangladesh"
}

## METHODS OF DICT

# 1. get(key)
student.get("name")

# 2. keys()
student.keys()


"""
 * get()          -> Get value safely
 * keys()         -> Return all keys
 * values()       -> Return all values
 * items()        -> Return key-value pairs
 * update()       -> Add/update multiple items
 * pop()          -> Remove by key
 * popitem()      -> Remove last key-value pair
 * clear()        -> Remove everything
 * copy()         -> Copy dictionary
 * setdefault()   -> Get or create a key

 * student[key]   -> Access value
 * student[key] = value -> Add or update value
 * del student[key] -> Delete a key
 * in             -> Check if a key exists
"""