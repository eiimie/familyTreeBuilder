class FamilyTree:
    name: str
    people: Dict[str, Person] # id -> Person mapping
    relationships: List[Relationship]

    # methods for tree manipulation & querying 
    add_person(person: Person) -> str
    remove_person(person_id: str) -> bool
    add_relationship(rel: Relationship) -> str
    find_relatives(person_id, str, rel_type: str) -> List[str]
    calculate_relationship(person1_id: str, person2_id: str) -> str