#!/bin/bash
LANG=en_US.UTF-8

# You can get the info (and a lot more) from the command:
# xprop -id <window_id>
pid="$(xdotool getactivewindow)"
echo "$pid"



# The output will look like:
# _NET_WM_STATE(ATOM) = _NET_WM_STATE_MAXIMIZED_HORZ, _NET_WM_STATE_MAXIMIZED_VERT, _NET_WM_STATE_HIDDEN

STR="$(xprop -id $pid | grep '_NET_WM_STATE(ATOM)')"
SUB='_NET_WM_STATE_MAXIMIZED_VERT'
if [[ "$STR" == *"$SUB"* ]]; then
    #   The window is maximized Vertically
    xdotool key 'Super_L+F11'
  echo "It's there."
fi

