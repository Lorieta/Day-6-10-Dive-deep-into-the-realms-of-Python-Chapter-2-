with open("story.txt", "r") as file:
    story = file.readlines()
    count = 0
    for line in story:
        count += 1
print(story)
print(f"Total line in the file: {count}")
