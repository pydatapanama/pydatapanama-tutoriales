import os
import collections
import json

# 📌 Points configuration
POINTS_CREATION = 20
POINTS_CORRECTION = 10

# 📌 Ranking file
RANKING_FILE = "RANKING.md"
ranking = collections.defaultdict(int)

# 📌 Directories where tutorials are stored
CATEGORIES = ["01_Numpy", "02_Pandas", "03_Matplotlib", "04_Seaborn"]

# 📌 Get the GitHub actor (user who made the PR)
GITHUB_ACTOR = os.getenv('GITHUB_ACTOR', '').strip()  # This gets the PR author's GitHub username

# 📌 Read current ranking if it exists
ranking_current = {}
if os.path.exists(RANKING_FILE):
    with open(RANKING_FILE, "r") as f:
        for line in f.readlines():
            if "|" in line and "Points" not in line:
                parts = line.split("|")
                user = parts[1].strip()
                points = parts[2].strip()
                if user.isalnum() and points.isdigit():
                    ranking_current[user] = int(points)

# 📌 Detect new and modified tutorial directories
for category in CATEGORIES:
    category_path = os.path.join(os.getcwd(), category)  # Full path to category

    if os.path.exists(category_path):  
        for tutorial in os.listdir(category_path):  # Iterate over tutorial folders
            tutorial_path = os.path.join(category_path, tutorial)

            # 📌 Ignore template folders
            if os.path.isdir(tutorial_path) and not tutorial.startswith("template-") and "-" in tutorial:
                tutorial_parts = tutorial.rsplit("-", 1)  # Extract user from folder name
                
                if len(tutorial_parts) == 2:
                    _, user = tutorial_parts
                    user = user.strip()

                    # Ensure valid GitHub username (alphanumeric + hyphens)
                    if user.replace("-", "").isalnum():
                        print(f"✅ DEBUG: Valid tutorial '{tutorial}' detected with user '{user}'")

                        # Only assign points if the user is the PR author
                        if user == GITHUB_ACTOR:
                            if user not in ranking_current:
                                ranking[user] += POINTS_CREATION
                            else:
                                ranking[user] += POINTS_CORRECTION  # Existing tutorial, assume modification

# 📌 Merge new points with existing ranking
for user, points in ranking_current.items():
    ranking[user] += points  # Accumulate instead of overwriting

# 📌 Sort and write the new ranking
sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

with open(RANKING_FILE, "w") as f:
    f.write("# 🏆 PyData Panama Contributors Ranking\n\n")
    f.write("| User | Points |\n")
    f.write("|---------|--------|\n")
    for user, points in sorted_ranking:
        f.write(f"| {user} | {points} |\n")
    f.write("\n🚀 **Keep contributing to climb up the ranking!**\n")

print(f"✅ Ranking successfully updated. User {GITHUB_ACTOR} received points.")