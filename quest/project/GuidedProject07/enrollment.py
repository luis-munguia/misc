if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_enrollment = data["total_enrollment"].sum()
    school_enroll = ["SCH_ENR_HI_M", "SCH_ENR_HI_F", "SCH_ENR_AM_M",
                     "SCH_ENR_AM_F", "SCH_ENR_AS_M", "SCH_ENR_AS_F",
                     "SCH_ENR_HP_M", "SCH_ENR_HP_F", "SCH_ENR_BL_M",
                     "SCH_ENR_BL_F", "SCH_ENR_WH_M", "SCH_ENR_WH_F",
                     "SCH_ENR_TR_M", "SCH_ENR_TR_F"]
    
    print("The following are the percentage of enrollment by race and gender:\n")
                     
    for i in school_enroll:
        x = data[i].sum()
        print("The percentage for " + i + " = " + str(x / all_enrollment))