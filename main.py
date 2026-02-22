import pandas as pd 
import glob 
import os


def CalculateRevenue(row):
    return float(row["price"].replace('$', '')) * row["quantity"]


def main():
    path = "./data/"
    all_files = glob.glob(os.path.join(path, "daily_sales_data_*.csv"))

    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    print(df["price"].dtype)
    df.drop(df[df["product"] != "pink morsel"].index,inplace=True)
    df["revenue"] = df.apply(CalculateRevenue, axis=1)
    print(df.head())

    daily_revenue = df.groupby("date")["revenue"].sum().reset_index()
    daily_revenue.columns = ["date", "total_revenue"]
    
    daily_regional_revenue = df.groupby(["date", "region"])["revenue"].sum().reset_index()
    daily_regional_revenue.columns = ["date", "region", "sales"]
    
    # Export to single CSV file with sales, date, region columns
    output_df = daily_regional_revenue[["sales", "date", "region"]]
    output_df.to_csv("./data/sales_summary.csv", index=False)
    
    print("\nSales Summary:")
    print(output_df)
    

if __name__ == "__main__":    
    main()