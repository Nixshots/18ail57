import ast

constants = ['cow','sheep']
predicates = {
    'mammal': 1,
    'animal': 1
}
assertions = [
    ('animal','cow'),
    ('mammal','cow')
]

def is_true(predicate, *args):
    return (predicate, *args) in assertions


query_predicate, query_constant = input("Enter the query ").split(',')

query = (query_predicate.strip(), query_constant.strip())

if is_true(*query):
    print("The query is entailed by the given assertions.")
else:
    print("The query is not entailed by the given assertions.")
