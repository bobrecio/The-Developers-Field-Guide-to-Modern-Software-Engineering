import pandas as pd

class DataAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def show_head(self, n=5):
        return self.df.head(n)

    def describe_data(self):
        return self.df.describe()

    def filter_by_column(self, column, value):
        return self.df[self.df[column] == value]

    def join_with(self, other_csv_path, on_column, how='inner'):
        other_df = pd.read_csv(other_csv_path)
        self.df = pd.merge(self.df, other_df, on=on_column, how=how)
        return self.df

# Example usage
if __name__ == "__main__":
    analyzer = DataAnalyzer("users.csv")
    print("Preview:\n", analyzer.show_head())

    print("\nAfter join:\n", analyzer.join_with("orders.csv", on_column="user_id"))
    print(f"Some statistics about numeric columns:\n {analyzer.describe_data()}")

    print(f"Filter by columns:\n {analyzer.filter_by_column('user_id', 2)}")
