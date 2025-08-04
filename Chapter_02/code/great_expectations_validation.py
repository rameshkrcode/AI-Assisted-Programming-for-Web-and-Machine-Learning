
from great_expectations.dataset import PandasDataset

dataset = PandasDataset(df)
dataset.expect_column_values_to_be_in_set("category", ["A", "B", "C"])
