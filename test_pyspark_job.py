"""Clean invalid records and calculate tax-inclusive amounts."""
import pytest
from pyspark.sql import SparkSession

from pyspark_job import clean_data


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("PySparkCleanDataTests")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    yield spark

    spark.stop()


def test_valid_records_are_kept(spark):
    input_df = spark.createDataFrame(
        [
            ("Alice", 100.0),
            ("Bob", 50.0),
        ],
        ["name", "amount"],
    )

    result = clean_data(input_df).orderBy("name").collect()

    assert [(row.name, row.amount) for row in result] == [
        ("Alice", 100.0),
        ("Bob", 50.0),
    ]


def test_records_with_non_positive_amount_are_removed(spark):
    input_df = spark.createDataFrame(
        [
            ("Positive", 10.0),
            ("Zero", 0.0),
            ("Negative", -5.0),
        ],
        ["name", "amount"],
    )

    result = (
        clean_data(input_df)
        .select("name")
        .orderBy("name")
        .rdd
        .flatMap(lambda row: row)
        .collect()
    )

    assert result == ["Positive"]


def test_records_with_null_names_are_removed(spark):
    input_df = spark.createDataFrame(
        [
            ("Named", 25.0),
            (None, 30.0),
        ],
        ["name", "amount"],
    )

    result = clean_data(input_df).select("name").collect()

    assert result == [("Named",)]


def test_amount_with_tax_is_calculated_correctly(spark):
    input_df = spark.createDataFrame(
        [
            ("Product", 100.0),
        ],
        ["name", "amount"],
    )

    result = clean_data(input_df).first()

    assert "amount_with_tax" in clean_data(input_df).columns
    assert result.amount_with_tax == pytest.approx(120.0)
