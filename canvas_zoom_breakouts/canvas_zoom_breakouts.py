from canvasapi import Canvas

from . import canvas_groups

def canvas_zoom_breakouts(canvas,course_name,csvfile_name):
    course = [c for c in canvas.get_courses() if c.name==course_name][0]

    (canvpart_by_netid,
     canvpart_by_canvasid,
     canvpart_by_sortablename
    ) = canvas_groups.canvas_participants(canvas,course)
    

    groups_by_name=canvas_groups.canvas_groups(canvas,course,canvpart_by_canvasid)

    zoom_csvfile_lines = []
    zoom_csvfile_lines.append("Pre-assign Room Name,Email Address")
    
    for group_name in groups_by_name:
        for participant_netid in groups_by_name[group_name].part_by_netid:
            zoom_csvfile_lines.append("%s,%s@iastate.edu" % (group_name,participant_netid))
            pass
        pass
    zoom_csvfile_string="\n".join(zoom_csvfile_lines)

    if not csvfile_name.endswith(".csv"):
        raise ValueError("CSV file name \"%s\" does not end with \".csv\"" % (csvfile_name))

    fh=open(csvfile_name,"w")
    fh.write(zoom_csvfile_string)
    fh.close()

    return (course,
            canvpart_by_netid,
            groups_by_name,
            zoom_csvfile_string)
            

    
