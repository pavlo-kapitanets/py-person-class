class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        human_name = Person.people[human["name"]]
        if "wife" in human and human["wife"] is not None:
            human_name.wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"] is not None:
            human_name.husband = Person.people[human["husband"]]
    return new_list
