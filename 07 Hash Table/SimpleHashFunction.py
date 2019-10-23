def hashFunc(string, lstrange):
    total = 0
    weird_prime = 31
    for i in string[:100]:
        total += ord(i) - 96
        total = (total * weird_prime) % lstrange
    return total

# Collisions
# 1 . Separate Chaining
# 2. Linear Probing

print(hashFunc('Pranav',11))
print(hashFunc('Pink',11))
print(hashFunc('Green',11))
print(hashFunc('green',11))
print(hashFunc('orange',11))
print(hashFunc('Orange',11))
print(hashFunc('Red', 11))
print(hashFunc('red', 11))




