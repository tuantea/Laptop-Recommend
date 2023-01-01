import csv
import pandas as pd
from User import user

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

study_df = pd.read_csv('../data/study_laptops_cleaned.csv', sep=',', encoding='latin')
gaming_df = pd.read_csv('../data/gaming_laptops_cleaned.csv', sep=',', encoding='latin')

def create_new_columns(df):
    df['price_score'] = 0
    df['rating_score'] = 0
    df['cpu_speed_score'] = 0
    df['core_score'] = 0
    df['storage_score'] = 0
    df['memory_score'] = 0
    df['screen_score'] = 0
    df['total_score'] = 0
    return df

def get_price_score(df, row, budget,priority):
    # get budget from matt's end
    # s(p) = ((b - p) / b) * (1/7)
    return ((budget - df.loc[row, 'price']) / budget) * (priority/28)
def get_rating_score(df, row,priority):
    rating = df.loc[row, 'rating']
    if rating != -1:
        return (rating / 5) * (priority/28)
    else:
        return 0

def get_cpu_speed_score(df, row,priority):
    max_cpu_speed = 3.1
    return (df.loc[row, 'cpu_speed'] / max_cpu_speed) * (priority/28)

def get_core_score(df, row,priority):
    max_cores = 6
    return (df.loc[row, 'cores'] / max_cores) * (priority/28)

def get_storage_score(df, row,priority):
    max_storage = 3024
    return (df.loc[row, 'storage'] / max_storage) * (priority/28)

def get_memory_score(df, row,priority):
    max_memory = 32
    return (df.loc[row, 'memory'] / max_memory) * (priority/28)

def get_screen_score(df, row,priority):
    max_screen = 17.3
    return (df.loc[row, 'screen'] / max_screen) * (priority/28)

def get_top_10(df):
    budget_bool = df.price <= user.budget
    storage_bool = (df.storage >= user.storage_range[0]) \
                   & (df.storage <= user.storage_range[1])
    screen_bool = (df.screen >= user.screen_range[0]) \
                  & (df.screen <= user.screen_range[1])
    ram_bool = df.memory == user.ram
    return df[budget_bool & storage_bool & screen_bool & ram_bool].sort_values('total_score',ascending=False).head(10)
def get_top_10_weight(df):
    budget_bool = df.price <= user.budget
    storage_bool = (df.storage >= user.storage_range[0]) \
                   & (df.storage <= user.storage_range[1])
    screen_bool = (df.screen >= user.screen_range[0]) \
                  & (df.screen <= user.screen_range[1])
    ram_bool = df.memory == user.ram
    return df[budget_bool & storage_bool & screen_bool & ram_bool].sort_values('total_score',ascending=False).head(10).sort_values('weight',ascending=True).head(10)

## MAIN
# create new columns for scores
study_df = create_new_columns(study_df)
for r in list(study_df.index):
     study_df.loc[r, 'price_score'] = get_price_score(study_df, r, user.budget,6)
     study_df.loc[r, 'rating_score'] = get_rating_score(study_df, r,5)
     study_df.loc[r, 'cpu_speed_score'] = get_cpu_speed_score(study_df, r,4)
     study_df.loc[r, 'core_score'] = get_core_score(study_df, r,1)
     study_df.loc[r, 'storage_score'] = get_storage_score(study_df, r,2)
     study_df.loc[r, 'memory_score'] = get_memory_score(study_df, r,3)
     study_df.loc[r, 'screen_score'] = get_screen_score(study_df, r,7)
     study_df.loc[r, 'total_score'] = sum(study_df.loc[r, 'price_score':'screen_score'])
gaming_df = create_new_columns(gaming_df)
for r in list(gaming_df.index):
     gaming_df.loc[r, 'price_score'] = get_price_score(gaming_df, r, user.budget,3)
     gaming_df.loc[r, 'rating_score'] = get_rating_score(gaming_df, r,1)
     gaming_df.loc[r, 'cpu_speed_score'] = get_cpu_speed_score(gaming_df, r,7)
     gaming_df.loc[r, 'core_score'] = get_core_score(gaming_df, r,5)
     gaming_df.loc[r, 'storage_score'] = get_storage_score(gaming_df, r,4)
     gaming_df.loc[r, 'memory_score'] = get_memory_score(gaming_df, r,6)
     gaming_df.loc[r, 'screen_score'] = get_screen_score(gaming_df, r,2)
     gaming_df.loc[r, 'total_score'] = sum(gaming_df.loc[r, 'price_score':'screen_score'])
combined_df = pd.concat([study_df, gaming_df]).reset_index(drop=True)

# do this for each data point - loop thru everything
subset = combined_df[combined_df.price <= user.budget + 50]
# for r in list(subset.index):
#      subset.loc[r, 'price_score'] = get_price_score(subset, r, user.budget)
#      subset.loc[r, 'rating_score'] = get_rating_score(subset, r)
#      subset.loc[r, 'cpu_speed_score'] = get_cpu_speed_score(subset, r)
#      subset.loc[r, 'core_score'] = get_core_score(subset, r)
#      subset.loc[r, 'storage_score'] = get_storage_score(subset, r)
#      subset.loc[r, 'memory_score'] = get_memory_score(subset, r)
#      subset.loc[r, 'screen_score'] = get_screen_score(subset, r)
#      subset.loc[r, 'total_score'] = sum(subset.loc[r, 'price_score':'screen_score'])
# output the results
top_10 = get_top_10(subset)
top_10_weight=get_top_10_weight(subset)
if user.sex==1:
   if len(top_10) == 0:
      print("Sorry, we do not have any products that match up to what you are looking for :c")
   else:
      print("Alright, after considering all the factors that you answered for us, we decided on this list of the top " + str(len(top_10)) + " laptops best suited for you!\n")
      top_10.to_csv('../data/nam.csv')
      n = 1
      for i in top_10.index:
         print(str(n) + ' - ' + '$' + str(top_10.price[i]) + ' - ' + top_10.name[i])
         n += 1
else:
    if len(top_10_weight) == 0:
      print("Sorry, we do not have any products that match up to what you are looking for :c")
    else:
      print("Alright, after considering all the factors that you answered for us, we decided on this list of the top " + str(len(top_10_weight)) + " laptops best suited for you!\n")
      top_10_weight.to_csv('../data/nu.csv')
      n = 1
      for i in top_10_weight.index:
         print(str(n) + ' - ' + '$' + str(top_10_weight.price[i]) + ' - ' + top_10_weight.name[i])
         n += 1