from polars.dataframe.frame import DataFrame
from polars.lazyframe.frame import LazyFrame

def read_parquet(
    source: object,
    *,
    columns: object = None,
    schema: object = None,
    row_index_name: str | None = None,
    hive_partitioning: bool | None = None,
    hive_schema: object = None,
    include_file_paths: str | None = None,
    **kwargs: object,
) -> DataFrame: ...
def scan_parquet(
    source: object,
    *,
    schema: object = None,
    row_index_name: str | None = None,
    hive_partitioning: bool | None = None,
    hive_schema: object = None,
    include_file_paths: str | None = None,
    cast_options: object = None,
    **kwargs: object,
) -> LazyFrame: ...
