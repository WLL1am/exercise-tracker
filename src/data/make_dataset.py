import pandas as pd
from glob import glob

# Read single CSV file
file_acc = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv"
)

single_file_gyr = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv"
)


# List all data in data/raw/MetaMotion
files = glob("../../data/raw/MetaMotion/*.csv")
len(files)


# Extract features from filename
data_path = "../../data/raw/MetaMotion/"
f = files[0]

participant = f.split("-")[0].replace(data_path, "")
exercise_label = f.split("-")[1]
intensity_category = f.split("-")[2].rstrip("123")

df = pd.read_csv(f)

df["participant"] = participant
df["exercise"] = exercise_label
df["intensity"] = intensity_category
