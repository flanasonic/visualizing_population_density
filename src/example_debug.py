import pandas as pd
#
# Demonstration of what inplace does - specifically what 
# the return value of DataFrame.rename is when inplace is
# either True or False
#
data = [[0, 0], [1, 1], [2, 2]]

df_original = pd.DataFrame.from_records(data, columns=["Dumb Name 1", "Dumb Name 2"])

df_renamed = df_original.rename(columns={"Dumb Name 1":"First Col", "Dumb Name 2":"Second Col"})

print("\n\nThe original is left untouched because inplace=False (either by default or if you specify it so")
print("Original:")
print(df_original)

print("\n\nWe said df_renamed = df_original.rename(...) inplace is False by default so it will return a copy of the df with new column names")
print("df_renamed - not inplace:")
print(df_renamed)

print("\n -------------------------------------------------- \n")

# now let's call rename with inplace=True!
#
df_renamed = df_original.rename(columns={"Dumb Name 1":"First Col", "Dumb Name 2":"Second Col"}, inplace=True)

print("\ndf_original after rename when inplace=True")
print("Columns have been changed in place in the original dataframe (no copy / doesn't look like a copy)")
print(df_original)

print("...BUT!!!...")
print("we still said ndf_renamed = df_original.rename(..., inplace=True) so we're setting df_rename to the return value of rename")
print("But the return value of rename when inplace=True is None - so df_renamed is now None")
print("\ndf_rnamed after calling rename with inplace=True:")
print(df_renamed)
