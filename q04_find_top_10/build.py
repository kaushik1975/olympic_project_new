# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df,Total_Summer, Total_Winter,Total):
    df.drop(df.tail(1).index,inplace=True)

    df_1 = df[['Country Name','Total_Summer']].sort_values(by='Total_Summer', ascending=False)
    SummerList = df_1[0:10]
    
    df_1 = df[['Country Name','Total_Winter']].sort_values(by='Total_Winter', ascending=False)
    WinterList = df_1[0:10]
    
    df_1 = df[['Country Name','Total']].sort_values(by='Total', ascending=False)
    Top = df_1[0:10]
        
    s1 = pd.merge(SummerList, WinterList, how='inner', on=['Country Name'])
    s2 = pd.merge(SummerList, Top, how='inner', on=['Country Name'])
    s3 = pd.merge(s1, s2, how='inner', on=['Country Name'])
    SummerList = SummerList['Country Name'].tolist()
    WinterList = WinterList['Country Name'].tolist()
    Top = Top['Country Name'].tolist()
    CommonElements = s3['Country Name'].tolist()
    
    return SummerList,WinterList,Top,CommonElements




