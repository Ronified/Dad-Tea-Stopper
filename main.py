# save as tea_taper.py and run: python tea_taper.py
import datetime, json, os

START_CUPS = 8  # change to his baseline (6-8)
TARGET_CUPS = 1
DAYS_PER_STEP = 3  # remove 1 cup every 3 days

def make_schedule(start, target, days_per_step):
    steps = start - target
    total_days = steps * days_per_step
    schedule = []
    day = 1
    current = start
    for s in range(steps):
        for _ in range(days_per_step):
            schedule.append((day, current))
            day += 1
        current -= 1
    # fill final day(s) with target for clarity (1 day)
    schedule.append((day, target))
    return schedule

def print_schedule(schedule):
    today = datetime.date.today()
    for daynum, cups in schedule:
        date = today + datetime.timedelta(days=daynum-1)
        print(f"Day {daynum:2d} | {date.isoformat()} | target cups: {cups}")

def log_progress(day, actual_cups):
    fname = "tea_log.txt"
    entry = {"date": str(datetime.date.today()), "day": day, "cups": actual_cups}
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf8") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(fname, "w", encoding="utf8") as f:
        json.dump(data, f, indent=2)
    print("Logged.")

if __name__ == "__main__":
    sched = make_schedule(START_CUPS, TARGET_CUPS, DAYS_PER_STEP)
    print("\n=== 21-day Taper Schedule (example) ===\n")
    print_schedule(sched)
    print("\nTo log today's cups: import this script and call log_progress(day_number, actual_cups) OR modify and rerun.")
