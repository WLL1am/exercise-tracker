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


# Plot multiple axis
exercise = "squat"
participant = "A"
all_axis_df = df.query(f"exercise == '{exercise}'").query(f"participant == '{participant}'").reset_index()

fig, ax = plt.subplots()
all_axis_df[["acc_x", "acc_y", "acc_z"]].plot(ax=ax)
ax.set_ylabel("acc_y")
ax.set_xlabel("samples")
plt.legend()


# Create a loop to plot all combinations per sensor
exercises = df["exercise"].unique()
participants = df["participant"].unique()

for exercise in exercises:
    for participant in participants:
        all_axis_df = (
            df.query(f"exercise == '{exercise}'")
            .query(f"participant == '{participant}'")
            .reset_index()
        )
        
        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["gyr_x", "gyr_y", "gyr_z"]].plot(ax=ax)
            ax.set_ylabel("gyr_y")
            ax.set_xlabel("samples")
            plt.title(f"{exercise} ({participant})".title())
            plt.legend()

# Combine plots in one figure
exercise = "row"
participant = "A"
combined_plot_df = (
    df.query(f"exercise == '{exercise}'")
    .query(f"participant == '{participant}'")
    .reset_index(drop=True)
)

fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(20,10))
combined_plot_df[["acc_x", "acc_y", "acc_z"]].plot(ax=ax[0])
combined_plot_df[["gyr_x", "gyr_y", "gyr_z"]].plot(ax=ax[1])

ax[0].legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)
ax[1].legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)
ax[1].set_xlabel("samples")


# Loop over all combinations and export for both sensors
for exercise in exercises:
    for participant in participants:
        combined_plot_df = (
            df.query(f"exercise == '{exercise}'")
            .query(f"participant == '{participant}'")
            .reset_index()
        )
        
        if len(combined_plot_df) > 0:
            fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(20,10))
            combined_plot_df[["acc_x", "acc_y", "acc_z"]].plot(ax=ax[0])
            combined_plot_df[["gyr_x", "gyr_y", "gyr_z"]].plot(ax=ax[1])

            ax[0].legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)
            ax[1].legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)
            ax[1].set_xlabel("samples")
            
            plt.savefig(f"../../reports/figures/{exercise.title()} ({participant}).png")
            plt.show()
