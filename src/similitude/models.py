import pydantic
import abc


class Table(abc.ABC):
    """ Abstract representation of a table """
    """ TODO: Require schema field and implement it as propery in Table implementations """


class Field(pydantic.BaseModel):
    """
    Simple representation of a field.
    Centralized as model to unify across different databases.
    """

    name: str
    field_type: str  # Should be checked against central enum of types.
    is_nullable: bool

    def __eq__(self, other):
        if not isinstance(other, Field):
            # don't attempt to compare against unrelated types
            return NotImplemented

        name_equal = self.name == other.name
        type_equal = self.field_type == other.field_type
        contraints_equal = self.is_nullable == other.is_nullable
        return name_equal and type_equal and contraints_equal

    def __hash__(self):
        return hash(str(self.name))
