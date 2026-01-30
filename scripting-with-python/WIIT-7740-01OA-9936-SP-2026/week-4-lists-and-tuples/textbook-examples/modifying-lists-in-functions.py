def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left unprinted.
    'pop' last item in list and move to completed_models after 'printing'.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Print model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    #for loop - performs the same action (print item name) on every item in the list
    for completed_model in completed_models:
        print(completed_model)

#set up: create two lists (unprinted and printed)
unprinted = ['phone case', 'robot pendant', 'dodecahedron']
printed = []

#run print function with lists we set up
print_models(unprinted, printed)
#run show completed function with final 'printed' list
show_completed_models(printed)