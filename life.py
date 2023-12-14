import os
from dotenv.main import load_dotenv
from datetime import datetime
import matplotlib.pyplot as plt

# --- 2. Load the contents of the .env file as environment variables:
load_dotenv(dotenv_path=".env", verbose=True)

# --- 3. Print out the value of MY_VAR:
print(os.getenv("birth_date", "Default Date"))

# Define the birthdate and calculate the age based on today's date

birthdate =  datetime.strptime(os.getenv("birth_date"), '%Y-%m-%d')
today = datetime.today()

# Calculate full weeks lived

# full_weeks_lived = (today - birthdate).days // 7

# print(full_weeks_lived)

# Calculate the full years and weeks lived as of today
years_lived = (today - birthdate).days // 365  # Approximate full years lived
weeks_lived_since_last_birthday = (today - birthdate).days % 365 // 7  # Weeks lived after the last birthday

print(f"Life Lived So Far: {years_lived} Years - {weeks_lived_since_last_birthday} Weeks")

# Parameters
total_years = 82  # Total years in a lifetime
weeks_per_year = 52  # Weeks in a year
total_weeks = total_years * weeks_per_year  # Total weeks in a lifetime
margin = 0.1  # This is an example value; you can adjust it as needed
border_color = 'black'  # This sets the border color to black; you can choose any color you prefer
border_width = 0.1  # This is an example value; you can adjust it as needed
chart_title = "Life Lived So Far: " + str(years_lived) + " Years - " + str(weeks_lived_since_last_birthday) + " Weeks"
full_weeks_lived = (years_lived * 52) + weeks_lived_since_last_birthday
#full_weeks_lived = (today - birthdate).days // 7
# Update weeks lived so far with the actual number

weeks_lived = min(full_weeks_lived, total_weeks)  # Cannot exceed total weeks in 82 years

# Create an array representing each week of life

life_array = ['black' if i < weeks_lived else 'white' for i in range(total_weeks)]

# Create a grid for the visualization

fig, ax = plt.subplots(figsize=(10, 15))

ax.set_xlim(0, weeks_per_year)

ax.set_ylim(0, total_years)

ax.set_aspect('equal')

# Remove axes

ax.axis('off')

# Plot each week as a square in the grid

for i in range(total_years):

    for j in range(weeks_per_year):

        idx = i * weeks_per_year + j

        ax.add_patch(plt.Rectangle((j, total_years - i), 1, 1, color=life_array[idx]))

plt.show()

# Update the life_array to reflect the actual number of weeks lived
life_array = ['black' if i < full_weeks_lived else 'white' for i in range(total_weeks)]

# Create the visualization with the updated life_array
fig, ax = plt.subplots(figsize=(12, 18))
ax.set_xlim(0, weeks_per_year)
ax.set_ylim(0, total_years)
ax.set_aspect('equal')
ax.set_title(chart_title, fontsize=14)
ax.set_xlabel("Weeks", fontsize=12)
ax.set_ylabel("Years", fontsize=12)

# Set the tick labels for the axes
ax.set_xticks([i + 0.5 for i in range(weeks_per_year)])
ax.set_yticks([i + 0.5 for i in range(total_years)])
ax.set_xticklabels([str(i) for i in range(weeks_per_year)], fontsize=9)
ax.set_yticklabels([str(i) for i in range(0, total_years)], fontsize=9)

# Create each square with a border
for i in range(total_years):
    for j in range(weeks_per_year):
        idx = i * weeks_per_year + j
        ax.add_patch(plt.Rectangle((j + margin, i + margin),
                                   1 - margin*2, 1 - margin*2,
                                   edgecolor=border_color, facecolor=life_array[idx],
                                   linewidth=border_width))

# Hide the spines and the ticks
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=True, bottom=True)

# Invert the y-axis
ax.invert_yaxis()

plt.show()

# Save the figure as a PNG file
plt.savefig("life_lived_so_far.png")