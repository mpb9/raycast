from applescript import run_applescript

focus_body = """tell application "System Events"
tell application process "Notes"
    tell window "Notes"
        tell splitter group 1
            tell splitter group 1
            tell group 2
                tell scroll area 1
                    tell text area 1
                        set focused to true
                    end tell
                end tell
            end tell
            end tell
        end tell
    end tell
end tell
end tell"""


def open(title="To-Do 🫡", folder="IMPORTANT 🫵🏻"):
    body = f'''tell application "Notes"
        show note "{title}"'''

    if folder != "":
        body += f''' of folder "{folder}"'''

    body += """
        activate
    end tell"""

    open_result = run_applescript(body)
    focus_result = run_applescript(focus_body)

    return focus_result.stdout
