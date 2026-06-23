import matplotlib.pyplot as plt 
from core.stats import get_dataset_stats

#data sapration for chart
def chart_data():
    
    chart_data = get_dataset_stats()
    data_keys = chart_data.keys()
    data_values = chart_data.values()
    return data_keys, data_values


# chart visualization
def visualize_data(data_keys, data_values):

    fig, ax = plt.subplots(figsize=(8, 5))

    # Dark background
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")

    bars = ax.bar(data_keys, data_values)

    # White text
    ax.set_title("Dataset Category Distribution", color="white")
    ax.set_xlabel("Categories", color="white")
    ax.set_ylabel("Number of Images", color="white")

    # White axis labels
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")

    # White border
    for spine in ax.spines.values():
        spine.set_color("white")

    # White values on bars
    for i, v in enumerate(data_values):
        ax.text(i, v + 2, str(v), ha="center", color="white")

    plt.tight_layout()

    return fig