if __name__ == "__main__":
    import read
    df = read.load_data() #read data from read.py
    
    total_string = "" #this is where i'll store the headlines
    for i in df["headline"]: #don't forget to use quotes
        total_string += str(i)
        total_string += " "
    
    total_string = total_string.lower()
    total_list = total_string.split(" ")
    
    from collections import Counter #collections is a new library
    
    total_dict = Counter(total_list)
    
    print(Counter(total_list).most_common(100))