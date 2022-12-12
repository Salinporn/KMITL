def time24hourTo12hour(t):
    time = ""
    hour, minute = map(int, t.split(":"))
    if hour < 12:
        time += f"{hour:02}:{minute:02} AM"
    elif hour == 12:
        time += f"{hour:02}:{minute:02} PM"
    elif hour > 12 and hour < 24:
        hour = hour - 12
        time += f"{hour:02}:{minute:02} PM"
    elif hour == 24:
        hour = hour - 12
        time += f"{hour:02}:{minute:02} AM"
    return print(time)

time24hourTo12hour("23:24")