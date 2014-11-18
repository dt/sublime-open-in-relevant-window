# Open File in Relevant Window

If you have multiple sublime windows open, attempt to open files in the right one.

If you open a file with sublime (eg `subl foo` or cmd-click in iTerm), it usually opens in the most-recently focused Sublime window.

When a file is loaded, this plugin checks each sublime window to see if the common prefix of its open directories is a prefix of the opened file.

If the file matches a window is not the window in which it was opened, it opens the file in that window, switches focus to the new window and closes the view in the old window.
