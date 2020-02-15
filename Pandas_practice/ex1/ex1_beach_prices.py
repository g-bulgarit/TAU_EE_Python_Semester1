import pandas as pd

def analyze_beach_prices(beach_names):
    for beach in beach_names:
        print(beach)
        df = pd.read_csv(beach)
        # To combine same products together, we can use groupby, and then do anything
        avg_prices_df = df.groupby('Product').mean()
        print (avg_prices_df)

def merge_files(beach_names):
    # concatenate into one df
    dataframes = []
    for beach in beach_names:
        df = pd.read_csv(beach)
        df["Beach_Name"] = beach[:-4]
        dataframes.append(df)

    output_df = pd.concat(dataframes, ignore_index=True)
    return output_df


if __name__ == "__main__":
    beach_names = ['Gordon.csv', 'Frishman.csv', 'Bugrashov.csv']
    product_names = ['Water', 'Coffee', 'Coke', 'Watermelon', 'Ice Cream']
    df = merge_files(beach_names)
    # Where can you get cheapest water?
    # 1. Get all rows where Product is Water
    water_df = df.loc[df["Product"] == "Water"]
    # 2. Get the index of the row with the cheapest price,
    target = water_df["Price"].idxmin()
    # 3. Print the value at "target_row", "Beach_Name" column.
    print(water_df.loc[target, "Beach_Name"])

    # Where can you get the most expensive coffee?
    df = merge_files(beach_names)
    # Get a list of only coffees
    df_coffee = df.loc[df["Product"] == "Coffee"]
    # now find most expensive coffee
    coffee_beach_name = df_coffee.loc[df_coffee["Price"].idxmax(), "Beach_Name"]
    coffee_beach_price =  df_coffee.loc[df_coffee["Price"].idxmax(), "Price"]
    print(f"The most expensive coffee is in {coffee_beach_name}, where it costs {coffee_beach_price}")




