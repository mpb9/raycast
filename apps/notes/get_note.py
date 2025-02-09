from applescript import run_applescript


def get_body(title="To-Do 🫡", folder="IMPORTANT 🫵🏻"):
    body = f'''tell Application "Notes"
        activate
        tell account "iCloud"
            get body of note "{title}"'''

    if folder != "":
        body += f''' of folder "{folder}"'''

    body += """
        end tell 
    end tell"""

    result = run_applescript(body, True)
    return result.stdout
