def compare_numerics_sql(table_1, table_2, numerical_cols, indexes) -> str:
    return f"""
    WITH

    t1 AS (
        SELECT *
        FROM {table_1}
    ),

    t2 AS (
        SELECT *
        FROM {table_2}
    ),

    joined AS (
        SELECT
            {",".join([f"t1.{col} AS t1_{col}" for col in numerical_cols])},
            {",".join([f"t2.{col} AS t2_{col}" for col in numerical_cols])}
        FROM t1
        INNER JOIN t2 USING({",".join(indexes)})
    ),

    diff AS (
        SELECT
            {",".join([f"t1_{col} - t2_{col} AS {col}_diff" for col in numerical_cols])}
        FROM joined
    ),

    avg_diff AS (
        SELECT
            {",".join([f"AVG({col}_diff) AS {col}_avg_diff" for col in numerical_cols])}
        FROM diff
    )

    SELECT * FROM avg_diff

    """
