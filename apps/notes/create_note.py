from applescript import run_applescript
from datetime import date, time

# ! Not currently used

# MARK: AppleScript body
as_body = """tell application "Notes"
    activate
    tell account "iCloud"
        make new note at folder "{}" with properties {{body:"{}"}}
    end tell
end tell"""

# MARK: HTML Templates
title_today = '<div><b><h1>To-Do Test</h1></b><font face=".AppleSystemUIFont"><h1>🫡</h1></font><b><h1><br></h1></b></div>'
blank_line = "<div><br></div>"
title_template = r"<div><b><span style=\"font-size: 24px\">{}</span></b></div>"
last_updated_template = r"<div><b>Last update: {}</b></div>"
item_template = r"<div><b><font color=\"#31B6E6\"><span style=\"font-size: 18px\">{}</span></font></b><br></div>"
time_template = r"<div><b><i><font color=\"#7531A9\">{}</font></i></b><br></div>"
list_template = r"<ul>{}</ul>"
list_item_template = r"<li>{}</li>"


# MARK: Formats Note HTML
def to_html(title=title_today, items=[""]) -> str:
    curr_date = date.today().isoformat()
    curr_time = f"{time.hour}:{time.minute}"

    if (title is title_today) | (title == "") | (title is None):
        text = title_today
    else:
        text = title_template.format(f"{title}")

    for item in items:
        text += item_template.format(f"{item}")

    text += blank_line + last_updated_template.format(f"{curr_date} {curr_time}")
    return text


def create_note(title="", items=[""], folder=""):
    note_html = to_html(title=title, items=items)
    print(note_html)

    if folder == "":
        folder = "Notes"
    cmd = as_body.format(folder, note_html)

    result = run_applescript(cmd.encode())
    return result.stdout
