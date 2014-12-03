# Copyright 2014 Foursquare Labs Inc. All Rights Reserved.

import os
import sublime, sublime_plugin

def window_for_file(filename):
  workspaces = {}
  for w in sublime.windows():
    workspace = os.path.commonprefix(w.folders())
    if workspace in workspaces: # non-unique workspaces. bail out.
      del workspaces[workspace]
    else:
      workspaces[workspace] = w
  for workspace in workspaces:
    if os.path.abspath(filename).startswith(os.path.abspath(workspace)):
      return workspaces[workspace]
  return None

class OpenFileInCorrectWindow(sublime_plugin.EventListener):
  def on_load(self, view):
    if not view.window():
      return

    filename = view.file_name()
    if filename:
      for folder in view.window().folders():
        if filename.startswith(folder):
          print("file {} exists in {}".format(filename, folder))
          return
      window = window_for_file(filename)
    if window != view.window():
      line = None
      sel = view.sel()
      if len(sel) > 0:
        pos = view.rowcol(view.sel()[0].begin())
        if pos:
          line = pos[0] + 1
      spec = filename
      if line > 1:
        spec = spec + ":" + str(line)
      window.open_file(spec, sublime.ENCODED_POSITION)
      new_view = window.active_view()
      window.run_command('focus_neighboring_group')
      window.focus_view(new_view)
      view.close()
      sublime.status_message("Switched opened file to matching window...")
