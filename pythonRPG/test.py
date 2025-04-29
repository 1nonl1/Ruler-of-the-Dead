import Armory
def create_dynamic_variables(base_name, num_variables, object_type):
    variables = {}
    for i in range(1, num_variables + 1):
        variable_name = f"{base_name}{i}"
        obj = object_type()
        obj.name = variable_name
        variables[variable_name] = obj
    return variables



if __name__ == "__main__":
    dynamic_swords = create_dynamic_variables("sword", 5, Armory.Weapon.Common.WoodSword)
    for name, obj in dynamic_swords.items():
        print(f"Variable Name: {name}, Object Name: {obj.name}")