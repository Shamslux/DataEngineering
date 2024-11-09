from dataclasses import dataclass
from typing import Dict, Optional, Union, NamedTuple

from dbt_common.dataclass_schema import dbtClassMixin
from dbt_common.utils.formatting import lowercase


@dataclass
class StatsItem(dbtClassMixin):
    id: str
    label: str
    value: Union[bool, str, float, None]
    include: bool
    description: Optional[str] = None


StatsDict = Dict[str, StatsItem]


@dataclass
class TableMetadata(dbtClassMixin):
    type: str
    schema: str
    name: str
    database: Optional[str] = None
    comment: Optional[str] = None
    owner: Optional[str] = None


CatalogKey = NamedTuple(
    "CatalogKey", [("database", Optional[str]), ("schema", str), ("name", str)]
)


@dataclass
class ColumnMetadata(dbtClassMixin):
    type: str
    index: int
    name: str
    comment: Optional[str] = None


ColumnMap = Dict[str, ColumnMetadata]


@dataclass
class CatalogTable(dbtClassMixin):
    metadata: TableMetadata
    columns: ColumnMap
    stats: StatsDict
    # the same table with two unique IDs will just be listed two times
    unique_id: Optional[str] = None

    def key(self) -> CatalogKey:
        return CatalogKey(
            lowercase(self.metadata.database),
            self.metadata.schema.lower(),
            self.metadata.name.lower(),
        )
