import os

# dir is your directory path as string
onlyfiles = next(os.walk('./data/predict_phase_2'))[2]
print(len(onlyfiles))
