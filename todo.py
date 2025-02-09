#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title To-Do List
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName Utils

# Documentation:
# @raycast.description Open To-Do List - Notes
# @raycast.author michael_beebe
# @raycast.authorURL https://raycast.com/michael_beebe

import apps.notes.open_note as open_note
import apps.notes.get_note as get_note

folder = "IMPORTANT 🫵🏻"
title = "To-Do 🫡"

body = get_note.get_body(title, folder)

# ! Convert to try/except block
# ! Make sure to log errors, find where logs are stored

# ! Doesn't complete when ran immediately after Notes - set timeout?
# ! Focus doesnt shift from Raycast->Notes when focused on Notes prior to running script

open_note.open(title, folder)
