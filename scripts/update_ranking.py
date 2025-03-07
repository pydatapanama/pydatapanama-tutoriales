import os
import json
import collections

# 📌 Points configuration
POINTS_CREATION = 20
POINTS_CORRECTION = 10

# 📌 Files
RANKING_FILE = "RANKING.md"
PROCESSED_FILE = "processed_tutorials.json"

# 📌 Directories where tutorials are stored
CATEGORIES = ["01_Numpy", "02_Pandas", "03_Matplotlib", "04_Seaborn"]

# 📌 Get the GitHub actor (user who made the PR)
GITHUB_ACTOR = os.getenv("GITHUB_ACTOR", "").strip()

# Load previously processed tutorials
if os.path.exists(PROCESSED_FILE):
    with open(PROCESSED_FILE, "r") as f:
        processed_tutorials = set(json.load(f))
else:
    processed_tutorials = set()

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

# 📌 Ranking storage
ranking = collections.defaultdict(int)

# 📌 Detect new and modified tutorial directories
new_tutorials = set()
modified_tutorials = set()

for category in CATEGORIES:
    category_path = os.path.join(os.getcwd(), category)

    if os.path.exists(category_path):
        for tutorial in os.listdir(category_path):
            tutorial_path = os.path.join(category_path, tutorial)

            # Ignore template folders
            if os.path.isdir(tutorial_path) and "-" in tutorial and not tutorial.startswith("template-"):
                tutorial_parts = tutorial.rsplit("-", 1)

                if len(tutorial_parts) == 2:
                    _, user = tutorial_parts
                    user = user.strip()

                    # Ensure valid GitHub username
                    if user.replace("-", "").isalnum():
                        tutorial_id = f"{category}/{tutorial}"

                        # 📌 New tutorial detection
                        if tutorial_id not in processed_tutorials:
                            print(f"✅ DEBUG: New tutorial '{tutorial}' detected by user '{user}'")
                            new_tutorials.add(tutorial_id)
                            ranking[user] += POINTS_CREATION
                            processed_tutorials.add(tutorial_id)

                        # 📌 Modified tutorial detection
                        elif tutorial_id in processed_tutorials:
                            print(f"🔄 DEBUG: Modified tutorial '{tutorial}' by user '{user}'")
                            modified_tutorials.add(tutorial_id)
                            ranking[user] += POINTS_CORRECTION

# Save processed tutorials
with open(PROCESSED_FILE, "w") as f:
    json.dump(list(processed_tutorials), f, indent=4)

# 📌 Merge new points with existing ranking
for user, points in ranking_current.items():
    ranking[user] += points

# 📌 Sort and write the new ranking
sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

with open(RANKING_FILE, "w") as f:
    f.write("# 🏆 PyData Panama Contributors Ranking\n\n")
    f.write("| User | Points |\n")
    f.write("|---------|--------|\n")
    for user, points in sorted_ranking:
        f.write(f"| {user} | {points} |\n")
    f.write("\n🚀 **Keep contributing to climb up the ranking!**\n")

print("✅ Ranking successfully updated.")