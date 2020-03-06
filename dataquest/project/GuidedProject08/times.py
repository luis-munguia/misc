def extract_hour(series):
    from dateutil.parser import parse
    import datetime
    time_object = parse(series)
    return time_object.hour #change this to choose between month, year and so on
    


if __name__ == "__main__":
    import read
    df = read.load_data() #read data from read.py
    df["hour"] = df["submission_time"].apply(extract_hour)
    print(df["hour"].value_counts().head(10))