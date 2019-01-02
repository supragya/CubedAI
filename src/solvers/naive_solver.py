from r_cube import draw
from r_cube.cube import rubiks_cube

def up_cross_place_edges(rb):

    # Edges
    # edges are arranged as a list of 2-tuples (unordered set of colors of edges)
    # First 4 elements of list are tuples representing the edges on the up
    # surface of the cube (unordered) starting from sticker 7 rotating clockwise
    # to find 5, 1, 3 stickers
    # Next 4 elements of the list are tuples representing the edges on the lateral surface
    # in clockwise ordering starting from back-right piece
    # Last 4 elements of the list are tuples representing the edges on the down surface
    # of the cube (similar to how the up surface edges are represented)

    edges_up = [(7, 7), (5, 7), (1, 7), (3, 7)]
    edges_mid = [(3, 5), (3, 5), (3, 5), (3, 5)]
    edges_down = [(7, 1), (5, 1), (1, 1), (3, 1)]

    color_order = [rb.facecolor[x] for x in rb.facelist]

    edges = []
    for x in range(4):
        color_0 = rb.cubeconfig[rb.faceslist.index('up')][edges_up[0]]
        color_1 = rb.cubeconfig[rb.faceslist.index(rb.ordering['up'][x])][edges_up[1]]
        if (color_order[color_0] < color_order[color_1]):
            edges.append((color_0, color_1))
        else:
            edges.append((color_1, color_0))
    for x in range(4):
        color_0 = rb.cubeconfig[rb.faceslist.index(rb.ordering['up'][x])][edges_mid[0]]
        color_1 = rb.cubeconfig[rb.faceslist.index(rb.ordering['up'][(x + 1) % 4])][edges_mid[1]]
        if (color_order[color_0] < color_order[color_1]):
            edges.append((color_0, color_1))
        else:
            edges.append((color_1, color_0))
    for x in range(4):
        color_0 = rb.cubeconfig[rb.faceslist.index('down')][edges_down[0]]
        color_1 = rb.cubeconfig[rb.faceslist.index(rb.ordering['down'][x])][edges_down[1]]
        if (color_order[color_0] < color_order[color_1]):
            edges.append((color_0, color_1))
        else:
            edges.append((color_1, color_0))

    moves_list = ['B', 'R', 'F', 'L']

    edges_to_find = []
    for f in rb.ordering['up']:
        color_0 = rb.facecolor['up']
        color_1 = rb.facecolor[f]
        if (color_order[color_0] < color_order[color_1]):
            edges_to_find.append((color_0, color_1))
        else:
            edges_to_find.append((color_1, color_0))

    for x in range(4):
        location = edges.index(edges_to_find[x])
            

    # up_index = rb.faceslist.index('up')
    # up_neighbors = [rb.faceslist.index(x) for x in rb.ordering['up']]
    # up_neighbors_colors = [rb.facecolor[rb.ordering['up'][x]] for x in range(4)]
    # on_edges = [7, 5, 1, 3]
    # up_edges = [rb.faceneighbors['up'][x] for x in [1, 4, 7, 10]]
    
    # edge_to_opposite_surface = [rb.move_B, rb.move_R, rb.move_F, rb.move_L]
    # for x in range(4):
    #     color = [rb.cubeconfig[up_index][on_edges[x]],
    #             rb.cubeconfig[up_neighbors[x]][around_edges[x]]]
    #     if (color[0] == rb.facecolor['up'] and color[1] in up_neighbors_colors) or \
    #         (color[0] in up_neighbors_colors and color[1] == rb.facecolor['up']):
    #         print("we found an edge at {}".format(x))
            
    #         edge_to_opposite_surface[x]()
    #         edge_to_opposite_surface[x]()
    #         non_up_color = color[0] if color[0] != rb.facecolor['up'] else color[1]
    #         print(non_up_color)
    #         quarter_moves = (up_neighbors_colors.index(non_up_color) - x) % 4
            
    #         for x in range(quarter_moves):
    #             rb.move_DI()
            
    #         edge_to_opposite_surface[(x - quarter_moves) % 4]()
    #         edge_to_opposite_surface[(x - quarter_moves) % 4]()



    print('done test')


def up_cross_align_edges(rb):
    pass

if __name__ == "__main__":
    rb = rubiks_cube()
    rb.move_U()
    # print(rb.scramble())
    up_cross_place_edges(rb)
    up_cross_align_edges(rb)
    draw.draw_cube(rb)
