keywords = ["ERROR", "FAIL","UNAUTHORIZED"]
suspiciouns_lines = []

with open("sample_log.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    for keyword in keywords:
        if keyword in line.upper():
            print(f"Suspicious line found: {line.strip()}")
            suspiciouns_lines.append(line)
with open("alerts.txt", "w") as output_file:
    for entry in suspiciouns_lines:
        output_file.write(entry)


