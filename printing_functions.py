def print_models(unprinted_designs):
    
    completed_models=[]
    while unprinted_designs:
        design =unprinted_designs.pop()
        print(f"Printing Design: {design}")
        completed_models.append(design)
    return completed_models

def print_completed_models(completed_models):
    print("\n The following models are completed: \n")
    while completed_models:
        print(completed_models.pop().title())

