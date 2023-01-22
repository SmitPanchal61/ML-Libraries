import pandas as pd

#? dataframe is the data type in which pandas manipulates and interacts with its data

#? delimiter is used to identify that where the data is being seperated in the txt file
# df_txt = pd.read_csv('pokemon_data.txt', delimiter="\t") 
# print(df_txt)

#? reading excel files
# df_xls = pd.read_excel('pokemon_data.xlsx')
# print(df_xls.head(5))

#? reading .csv files

df = pd.read_csv('pokemon_data.csv')

# print(df.head(5))

#? read data

# read headers
# print(df.columns)

# read columns
# print(df['Name']) -> printing just one column
# print(df['Name'][0:4]) -> printing a specific number of columns by slicing it
# print(df[['Name', 'Type 1', 'Attack']]) -> printing multiple columns

# read each row
# print(df.iloc[0:4]) -> prints each row using the .iloc function with some slicing

# read a specific location (R,C)
# print(df.iloc[2,1]) -> gives a specific location

#? iterate throug rows

# for index, row in df.iterrows(): -> .iterrows() function is used
#     print(index, row['Name']) -> can access anything inside the row eg. Name

#? get rows using a specific condition

# print(df.loc[df["Type 1"]=="Fire"])

#? sorting / describing

# print(df.describe())

# print(df.sort_values(['HP']))
# print(df.sort_values(['HP'], ascending=False))
# print(df.sort_values(['HP', 'Attack'], ascending=[0,1]))

#? make changes to the data

# creating total column containing sum of other columns
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df.sort_values(['Total'], ascending=False))
# df = df.drop(columns=['Total'])

# creating total column containing sum of other columns ( way 2 )
# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df)

# re arranging the columns
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df)

#? saving the modified data

# df.to_csv('modified_pokemon_data.csv', index=False) -> index=false is given so that it does not add a seperate index
# df.to_excel('modified_pokemon_data.xlsx', index=False) 
# df.to_csv('modified_pokemon_data.txt', index=False, sep='\t') -> sep='\t' is used to seperate the data with tabs

#? Additional filtering
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] -> additional filtering conditions

# new_df.reset_index(drop=True, inplace=True) -> reset the original index and start from 0, inplace is used to replace the original df so no need to create new variable

# new_df -> printing

# new_df.to_csv('filtered.csv') -> saving the file

