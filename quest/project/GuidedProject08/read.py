def load_data():
    import pandas as pd
    hackers = pd.read_csv("hn_stories.csv", header=None)
    hackers.columns = ["submission_time", "upvotes", "url", "headline"]
    return hackers
    
if __name__ == "__main__":
    load_data()