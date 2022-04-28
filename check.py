import os

# dir is your directory path as string
onlyfiles = next(os.walk('./data/predictions'))[2]
print(len(onlyfiles))
