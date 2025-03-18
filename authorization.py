#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Authorization
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName Utils

# Documentation:
# @raycast.description Open auth -> passwords - Notes
# @raycast.author michael_beebe
# @raycast.authorURL https://raycast.com/michael_beebe

import apps.notes.get_note as get_note
import apps.notes.open_note as open_note

folder = "auth 🔐"
title = "PASSWORDS"

body = get_note.get_body(title=title, folder=folder)

open_note.open(title=title, folder=folder)
