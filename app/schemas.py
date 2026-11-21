from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)

from datetime import datetime, timezone

class TaskCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    title = Field(
        min_length=1
    )
    
    description = Field(
        default=None,
        max_length=2000
    )

class TaskUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    title = Field(
        min_length=1
    )
    
    description = Field(
        default=None,
        max_length=2000
    )
    
    is_completed = None
    
    @field_validator("description", "is_completed")
    @classmethod
    def not_null_if_provided(self, value):
        if value is None:
            raise ValueError("Поле не может быть пустым. Пропустите его если не меняете")
        return value
    
class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime
    
    @field_validator("created_at")
    @classmethod
    def normalize_utc(self, value):
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        
        return value.astimezone(timezone.utc)