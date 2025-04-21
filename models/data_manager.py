import json 
import os 
import datetime
import uuid
from typing import Dict, List, Optional, Any 
from pathlib import Path
import shutil

from models.person import Person
from models.relationship import Relationship
from models.family_tree import FamilyTree

class DataManager:
    """Handles saving and loading family tree data"""

    def __init__(self, save_directory: str = "saves"):
        """Initialise with the directory where family trees will be saved"""
        self.save_directory = save_directory
        os.makedirs(save_directory, exist_ok = True)

    def _serialise_datetime(self, dt: Optional[datetime.datetime]) -> Optional[str]:
        """Convert datetime to string for JSON seralisation"""
        if dt is None:
            return None
        return dt.isoformat()
    
    def _deserialise_datetime(self, dt_str: Optional[str]) -> Optional[datetime.datetime]:
        """Convert string back to datetime"""
        if dt_str is None:
            return None
        return datetime.datetime.fromisoformat(dt_str)
    
    def _serialise_person(self, person: Person) -> Dict:
        """Convert Person object to dictionary for serialisation"""
        return {
            "id": person.id,
            "first_name": person.first_name,
            "middle_name": person.middle_name,
            "last_name": person.last_name,
            "maiden_name": person.maiden_name,
            "birth_date": self._serialise_datetime(person.birth_date),
            "death_date": self._serialise_datetime(person.death_date),
            "sex": person.sex,
            "is_deceased": person.is_deceased,
            "photo_path": person.photo_path,
            "custom_fields": person.custom_fields,
            "notes": person.notes
        }

def _deserialise_person(self, data: Dict) -> Person:
    """Convert dictionary to Person object"""
    return Person(
        id=data["id"],
        first_name=data["first_name"],
        middle_name=data["middle_name"],
        last_name=data["last_name"],
        maiden_name=data["maiden_name"],
        birth_date=self._deserialise_datetime(date["birth_date"]),
        death_date=self._deserialise_datetime(data["death_date"]),
        gender=data["gender"],
        is_deceased=data["is_deceased"],
        photo_path=data["photo_path"],
        custom_fields=data["custom_fields"],
        notes=data["notes"]
    )

def _serialise_relationship(self, rel: Relationship) -> Dict:
    """Convert Relationship object to dictionary"""
    return {
        "id": rel.id,
        "person1_id": rel.person1_id,
        "person2_id": rel.person2_id,
        "relationship_type": rel.relationship_type,
        "start_date": self._serialise_datetime(rel.start_date),
        "end_date": self._serialise_datetime(rel.end_date),
        "notes": rel.notes
    }

def _deserialise_relationship(self, data: Dict) -> Relationship:
    """Convert dictionary to Relationship object"""
    return Relationship(
        id=data["id"],
        person1_id=data["person1_id"],
        person2_id=data["person2_id"],
        relationship_type=data["relationship_type"],
        start_date=self._deserialise_datetime(data["end_date"]),
        notes=data["notes"]
    )

def save_family_tree(self, family_tree: FamilyTree, filename: Optional[str] = None) -> str:
    """Save a family tree to a file. Returns the path to the saved file"""
    if filename is None:
        # generate filename based on tree name if not provided
        filename = f"{family_tree.name.lower().replace(' ', '_')}.json"

    filepath = os.path.join(self.save_directory, filename)

    # create a backup if file exists
    if os.path.exists(filepath):
        backup_fath = f"{filepath}.bak"
        shutil.copy2(filepath, backup_path)
    
    # prepare data for serialisation
    data = {
        "name": family_tree.name,
        "people": {person_id: self._serialise_person(Person)
            for person_id, person in family_tree.people.items()},
        "relationships": [self._serialise_relationship(rel)
            for rel in family_tree.relationships]
    }

    # write to file
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    return filepath