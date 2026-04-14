import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_vector_pair(ax, x_offset, y_offset, vec1, vec2, title):
    
    cell_width = 1.0
    cell_height = 1.0
    gap = 0.2
    
    ax.text(x_offset + cell_width + gap/2, y_offset + len(vec1) * cell_height + 0.5, 
            title, fontsize=24, ha='center', va='center')
    
    for i, (v1, v2) in enumerate(zip(vec1, vec2)):
        y = y_offset + (len(vec1) - 1 - i) * cell_height
        
        ax.add_patch(patches.Rectangle((x_offset, y), cell_width, cell_height, fill=False))
        ax.text(x_offset + cell_width/2, y + cell_height/2, str(v1), 
                fontsize=16, ha='center', va='center')
        
        x_right = x_offset + cell_width + gap
        ax.add_patch(patches.Rectangle((x_right, y), cell_width, cell_height, fill=False))
        ax.text(x_right + cell_width/2, y + cell_height/2, str(v2), 
                fontsize=16, ha='center', va='center')

# Log vectors
r = [1, 2, 15, 4, 8, 4, 12]
A_row0 = [0, 1, 0, 0, 0, 0, 0]
B_row0 = [0, 1, 0, 0, 0, 0, 0]
C_row0 = [0, 0, 0, 1, 0, 0, 0]

val_A = sum(x * y for x, y in zip(r, A_row0))
val_B = sum(x * y for x, y in zip(r, B_row0))
val_C = sum(x * y for x, y in zip(r, C_row0))

fig, ax = plt.subplots(figsize=(10, 8))

draw_vector_pair(ax, 0, 3, r, A_row0, 'A')
draw_vector_pair(ax, 4, 3, r, B_row0, 'B')
draw_vector_pair(ax, 8, 3, r, C_row0, 'C')

eq_y = 1.5
fontsize_eq = 28
ax.text(1.1, eq_y, str(val_A), fontsize=fontsize_eq, ha='center', va='center')
ax.text(2.6, eq_y, '*', fontsize=fontsize_eq, ha='center', va='center')
ax.text(5.1, eq_y, str(val_B), fontsize=fontsize_eq, ha='center', va='center')
ax.text(6.6, eq_y, '-', fontsize=fontsize_eq, ha='center', va='center')
ax.text(9.1, eq_y, str(val_C), fontsize=fontsize_eq, ha='center', va='center')
ax.text(10.6, eq_y, '=', fontsize=fontsize_eq, ha='center', va='center')
ax.text(11.6, eq_y, '0', fontsize=fontsize_eq, ha='center', va='center')

ax.set_xlim(-1, 13)
ax.set_ylim(0, 4 + len(r))
ax.axis('off')

plt.tight_layout()
plt.show()