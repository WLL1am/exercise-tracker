import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import display


# Load data
df = pd.read_pickle("../../data/interim/01_data_processed.pkl")


# Plot single columns
set_df = df[df["set"] == 1]
plt.plot(set_df["acc_y"])

plt.plot(set_df["acc_y"].reset_index(drop=True))


# Plot all exercises
for exercise in df["exercise"].unique():
    subset = df[df["exercise"] == exercise]
    fig, ax = plt.subplots()
    plt.plot(subset["acc_y"].reset_index(drop=True), label=exercise)
    plt.legend()
    plt.show()
    
for exercise in df["exercise"].unique():
    subset = df[df["exercise"] == exercise]
    fig, ax = plt.subplots()
    plt.plot(subset[:100]["acc_y"].reset_index(drop=True), label=exercise)
    plt.legend()
    plt.show()
    
    
# Adjust plot settings
mpl.style.use("seaborn-v0_8-deep")
mpl.rcParams["figure.figsize"] = (20, 5)
mpl.rcParams["figure.dpi"] = 100


# Compare medium vs. heavy sets
intensity_df = df.query("exercise == 'squat'").query("participant == 'A'").reset_index()

fig, ax = plt.subplots()
intensity_df.groupby(["intensity"])["acc_y"].plot()
ax.set_ylabel("acc_y")
ax.set_xlabel("samples")
plt.legend()


# Compare participants
participant_df = df.query("exercise == 'bench'").sort_values("participant").reset_index()

fig, ax = plt.subplots()
participant_df.groupby(["participant"])["acc_y"].plot()
ax.set_ylabel("acc_y")
ax.set_xlabel("samples")
plt.legend()