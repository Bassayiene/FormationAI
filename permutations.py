portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # If the ports list is empty
    if not ports :
        print(' '.join([portnames[i] for i in route]))
    
    # Boucle for adding ports to the route
    for i, port in enumerate(ports):
        permutations(route + [port], ports[:i]+ports [i+1:])

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))