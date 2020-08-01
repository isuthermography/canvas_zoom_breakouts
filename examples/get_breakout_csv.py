from canvasapi import Canvas
from canvas_zoom_breakouts.canvas_zoom_breakouts import canvas_zoom_breakouts

CANVAS_API_URL="https://canvas.iastate.edu"
# See: https://canvasapi.readthedocs.io/en/stable/

# Obtain CANVAS_API_KEY by going to your Canvas
# account settings, scrolling to "Approved Integrations"
# and selecting "New Access Token" These tokens will last
# according to the expiration selected when you create
# them. 
CANVAS_API_KEY="INSERT_CANVAS_API_KEY_HERE"


course_name="Enter Course Name Here"

canvas = Canvas(CANVAS_API_URL,CANVAS_API_KEY)
(course,
 canvpart_by_netid,
 groups_by_name,
 zoom_csvfile_string) = canvas_zoom_breakouts(canvas,course_name,course_name+"_zoom_breakouts.csv")

