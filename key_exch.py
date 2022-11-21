p=71
p_prim_root = 7

class Alice:
    x = 5

class Bob:
    x = 12

def alice_key_gen(p, g):
    alice = Alice()
    return bob_public_key(p, g)**alice.x % p
    
def bob_key_gen(p, g):
    bob = Bob()
    return alice_public_key(p, g)**bob.x % p

def alice_public_key(p, g):
    alice = Alice()
    y = g**alice.x % p
    print("Alice Public Key: "+str(y))
    return y

def bob_public_key(p, g):
    bob = Bob()
    y = g**bob.x % p
    print("Bob Public Key: "+str(y))
    return y

print("Alice Symmetric Key: "+ str(alice_key_gen(p, p_prim_root)))
print("Bob Symmetric Key: "+ str(bob_key_gen(p, p_prim_root)))
