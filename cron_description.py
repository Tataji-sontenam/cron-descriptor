from cron_descriptor import get_description

with open("crons.txt") as f:
    crons = [line.strip() for line in f if line.strip()]

print("Cron Expression -> Description")
print("--------------------------------")

for cron in crons:
    description = get_description(cron)
    print(f"{cron} -> {description}")
