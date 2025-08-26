from utils.preprocessing import prepare_data

if __name__ == "__main__":
    data = prepare_data("data/bank_client.csv")
    print(data.head())