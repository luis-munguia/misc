if __name__ == "__main__":
    import read
    df = read.load_data() #read data from read.py
    domains = df["url"].value_counts().head(100)
    
    for name, row in domains.items():
        print("{0}: {1}".format(name,row))
        