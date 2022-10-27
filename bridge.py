#chunk - dł. płyty
#goal - dł. mostu

def build_bridge(chunk,goal):
    return print("mozna budowac most") if goal == chunk + chunk/2 else print("nie mozna budowac mostu")

build_bridge(10,15)
