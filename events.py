
def selectAllHandler(e):
    e.widget.select_range(0, 'end')
    e.widget.icursor('end')
    return 'break'