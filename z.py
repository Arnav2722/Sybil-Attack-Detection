import matplotlib.pyplot as plt

# Data
models = [
    "RandomForestClassifier",
    "LogisticRegression",
    "SVC",
    "DecisionTreeClassifier",
]
accuracies = [98.08, 83.68, 60.41, 97.99]

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(models, accuracies, color=["blue", "green", "red", "purple"])

# Labels and title
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")
plt.title("Model Accuracy Comparison")
plt.ylim(0, 100)  # Set y-axis limit from 0 to 100
plt.xticks(rotation=25)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show values on top of bars
for i, v in enumerate(accuracies):
    plt.text(i, v + 1, f"{v:.2f}%", ha="center", fontsize=10)

# Show plot
plt.show()
