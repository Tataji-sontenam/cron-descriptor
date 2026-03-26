import sys
from cron_descriptor import get_description

cron_input = sys.argv[1]

# Split by ;
cron_list = [cron.strip() for cron in cron_input.split(";") if cron.strip()]

print("\nCron Expression -> Description")
print("-----------------------------------")

for cron in cron_list:
    try:
        description = get_description(cron)
        print(f"{cron} -> {description}")
    except Exception as e:
        print(f"{cron} -> Invalid cron expression")
