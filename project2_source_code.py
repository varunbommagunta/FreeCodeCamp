import pandas as pd   #Importing the module


def calculate_demographic_data(print_data=True):
    # Read data from file
    df=pd.read_csv("adult.data.csv")
    df.rename(columns={"hours-per-week":"hours","native-country":"country"},inplace=True)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    #To get shape of original dataframe
    R,C=df.shape

    # What is the average age of men?
    average_age_men = round(df["age"][df["sex"]=="Male"].mean(),1)


    # What is the percentage of people who have a Bachelor's degree?
    bach =df[df["education"]=="Bachelors"]
    Total=df[["education"]]
    r1,c1=Total.shape
    r,c=bach.shape
    percentage_bachelors=(round(r*100/R,1))
  
    #Highest_Education_rich
    Advanced_Education = df[(df["education"]=="Bachelors") | (df["education"]=="Masters") | (df["education"]=="Doctorate")]
    AE_Row,_=Advanced_Education.shape
    AEA50K=Advanced_Education[Advanced_Education["salary"]=='>50K']
    AEA50K_Row,_=AEA50K.shape
    x=AEA50K_Row*100/AE_Row
    higher_education_rich=(round(x,1))
    
    #Lower_education_rich
    NAE=df[~(df["education"]=="Bachelors") & ~(df["education"]=="Masters") & ~(df["education"]=="Doctorate")]
    NAE_Row,_=NAE.shape
    NAEA50K=NAE[NAE["salary"]==">50K"]
    NAEA50K_Row,_=NAEA50K.shape
    y=NAEA50K_Row*100/NAE_Row
    lower_education_rich=(round(y,1))
  

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours"].min()

    
    #Min hour working rich_percentage
    Min_hour_working=df[df["hours"]==1]
    MHW_r,_=Min_hour_working.shape
    MHW50K=Min_hour_working[Min_hour_working["salary"]==">50K"]
    r,c=MHW50K.shape
    z=r*100/MHW_r
    rich_percentage=(int(z))

    # What country has the highest percentage of people that earn >50K?
    #highest_earning_country
    def cal_per(l1,l2):
      dic={}
      for i,j in zip(l1,l2):
       a=i[1]
       b=j[1]
       cal=b*100/a
       dic[i[0]]=cal
      return sorted(dic.items(),key=lambda x:x[1],reverse=True)[0][0]

    a=df["country"].value_counts()
    b=df["country"][df["salary"]==">50K"].value_counts()
    l1=[]
    l2=[]
    for i,j in a.items():
     l1.append([i,j])
    for i,j in b.items():
     l2.append([i,j])
    l1=sorted(l1,key=lambda x:x[1],reverse=True)
    l2=sorted(l2,key=lambda x:x[1],reverse=True)
    l3=[]
    for i in l1:
      for j in l2:
        if i[0]==j[0]:
          l3.append(j)
    highest_earning_country =cal_per(l1,l3)

    #highest_earning_country_percentage
    a=df["country"].value_counts()
    for i,j in a.items():
      if i==highest_earning_country:
        k=i
        z=j

    df[["country"]][(df["salary"]==">50K")]
    c=0
    for i in df["country"][(df["salary"]==">50K")]:
      if i==k:
        c+=1
    highest_earning_country_percentage = (round(c*100/z,1))

    # Identify the most popular occupation for those who earn >50K in India.
    
    k=df["occupation"][(df["salary"]==">50K") & (df["country"]=="India")].mode()
    for i in k:
      top_IN_occupation=i

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
