with open("data/data.txt", "r") as infile:
    content = infile.read()

processed_content = content.upper()

with open("data/processed.txt", "w") as outfile:
    outfile.write(processed_content)

print("Preprocessing completed. Output saved to data/processed.txt")