from applescript import run_applescript

# ! Not currently used


def delete_note(title="", folder=""):
    body = f"""tell application "Notes"
        tell account "iCloud"
            delete note "{title}" of folder "{folder}"
        end tell
    end tell"""
    result = run_applescript(body)
    return result.stdout
