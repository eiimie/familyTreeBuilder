class Relationship:
    id: str
    person1_id: str
    person2_id: str
    relationship_type: str
    start_date: Optional[datetime] # for marriages etc
    end_date: Optional[datetime] # for divorces etc
    notes: str
