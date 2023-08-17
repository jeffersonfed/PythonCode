import matplotlib.pyplot as py
import matplotlib.patches as patch 
# import matplotlib.patches as fig 
                                            
u = patch.Rectangle((0,1), width=6, height=2, facecolor="#FFFFFF", edgecolor="black")
d = patch.Rectangle((0,3), width=6, height=2, facecolor="#ff0000", edgecolor="black")

# for Flags with three colors example

# d = patch.Rectangle((0,1), width=10, height=2, facecolor="#ff0000", edgecolor="black")
# d = patch.Rectangle((0,3), width=10, height=2, facecolor="#FFFFFF", edgecolor="black")
# d = patch.Rectangle((0,5), width=10, height=2, facecolor="#ff0000", edgecolor="black")

m,n = py.subplots()

n.add_patch(u)
n.add_patch(d)

py.axis('equal')
# displaying the title
py.title("Happy Independence Day")

py.show()