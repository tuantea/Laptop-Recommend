import numpy as np
import pandas as pd
import re

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

# csv into pd data frame (chuyển csv thành pd data frame)
study_df = pd.read_csv('study_laptops_raw.csv', sep=',')

# temporarily fill all N/A with -1 (tạm thời điền tất cả N/A với -1)
study_df = study_df.fillna(-1)

# turn all prices into floats (biến tất cả giá thành dạng float)
def clean_prices(d):
    for i in range(len(study_df['price'])):
        if type(study_df.loc[i, 'price']) == str:
            study_df.loc[i, 'price'] = float(study_df.loc[i, 'price'].replace(',', ''))

    return study_df

# remove strings from cpu_speed, leave only GHz, turn into floats (xóa chuỗi khỏi cpu_speed, chỉ để lại GHz, biến thành float)
def clean_cpu_speed(study_df):
    for i in range(len(study_df['cpu_speed'])):
        # missing values (các giá trị còn thiếu)
        if study_df.loc[i, 'cpu_speed'] == -1:
            pass

        # case with extra words at beginning (trường hợp có thêm từ ở đầu) 
        elif '(' in study_df.loc[i, 'cpu_speed']:
            study_df.loc[i, 'cpu_speed'] = float(study_df.loc[i,'cpu_speed'].split('(')[1].replace(')', '').split(' ')[0])

        # when GHz is at the end (khi mà GHz ở cuối cùng)
        elif study_df.loc[i, 'cpu_speed'].split(' ')[1] == 'GHz':
            study_df.loc[i, 'cpu_speed'] = float(study_df.loc[i, 'cpu_speed'].split(' ')[0])

    return study_df

# convert cores into integer values ( chuyển cores thành giá trị số nguyên)
def clean_cores(study_df):
    for i in range(len(study_df['cores'])):
        if study_df.loc[i, 'cores'] == -1:
            pass
        elif 'Dual' in study_df.loc[i, 'cores']:
            study_df.loc[i, 'cores'] = 2
        elif 'Quad' in study_df.loc[i, 'cores']:
            study_df.loc[i, 'cores'] = 4
        elif '6' in study_df.loc[i, 'cores']:
            study_df.loc[i, 'cores'] = 6

    return study_df

# leave only GB in storage, convert to int (chỉ để lại GB trong bộ nhớ, chuyển đổi thành int)
# create a new column called cpu_type that = SSD or HDD (tạo một cột mới gọi là cpu_type = SSD hoặc HDD)
def clean_storage(study_df):
    for i in range(len(study_df['storage'])):
        if study_df.loc[i, 'storage'] != -1:
            # study_df.loc[i, 'storage'] = re.split('[A-z]|,', study_df.loc[i, 'storage'])[0]
            study_df.loc[i, 'storage'] = study_df.loc[i, 'storage'].replace('+', ',')
            storage_split_list = re.split('[A-z]|,', study_df.loc[i, 'storage'])

            # retrieve integer values from raw data (truy xuất các giá trị số nguyên từ dữ liệu thô)
            storage_int = 0
            for n in range(len(storage_split_list)):
                # add up all the integers in the split up string (cộng tất cả các số nguyên trong chuỗi chia nhỏ)
                try:
                    val = int(storage_split_list[n])
                    if val == 1:
                        val = 1000
                    elif val == 2:
                        val = 2000
                    storage_int += int(val)
                except ValueError:
                    pass

            # assign new value to storage column ( gán giá trị mới cho cột lưu trữ)
            study_df.loc[i, 'storage'] = storage_int

    return study_df

def clean_memory(study_df):
    # retrieve GB ints from raw data (# truy xuất số nguyên GB từ dữ liệu thô)
    for i in range(len(study_df['memory'])):
        study_df.loc[i, 'memory'] = int(study_df.loc[i, 'memory'].split(' ')[0])

    return study_df


def clean_screen_sizes(study_df):
    # turn all screen sizes into floats (# biến tất cả các kích thước màn hình thành float)
    for i in range(len(study_df['screen'])):
        if study_df.loc[i, 'screen'] == 'No':
            study_df.loc[i, 'screen'] = -1
        if type(study_df.loc[i, 'screen']) == str:
            study_df.loc[i, 'screen'] = float(study_df.loc[i, 'screen'].replace('"', ''))

    return study_df


## MAIN ##
clean_prices(study_study_df)
clean_cpu_speed(study_study_df)
clean_cores(study_study_df)
clean_storage(study_study_df)
clean_memory(study_study_df)
clean_screen_sizes(study_study_df)

# write to csv (ghi vào file csv)

