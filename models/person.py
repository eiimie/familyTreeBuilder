class Person:
    id: str
    first_name: str
    middle_name: str
    last_name: str
    maiden_name: str
    birth_date: datetime
    death_date: Optional[datetime]
    sex: str
    is_deceased: bool
    photo_path: str
    custom_fields: Dict[str, Any]
    notes: str
