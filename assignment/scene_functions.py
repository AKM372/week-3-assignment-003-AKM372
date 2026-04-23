import maya.cmds as cmds
import math
cmds.file(new=True, force=True)

def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a fence
    Args:
        height: How tall each post is
        length: Length of fence
        post_count: How many posts there are on the fence
        position: where the fence is

    Returns: name of created fence (grouped)"""
    
    spacing = length / (post_count - 1)
    post_list = []
    for i in range(post_count):
        post_name = f"post_{i+1}"
        cmds.polyCube(width=0.2, height=height, depth=0.2,name=post_name)
        x_pos = position[0] + spacing * i
        y_pos = height / 2.0
        cmds.move(x_pos, y_pos, position[2], post_name)
        post_list.append(post_name)
    rail = cmds.polyCube(width=length, height=0.2, depth=0.2,name="rail")
    cmds.move(position[0]+length/2, height/2.0, position[2], rail)
    fence = cmds.group(rail, post_list)
    cmds.move(position[0],position[1],position[2], fence)
    return fence
    

create_fence()


def create_building(width=2.0, height=5.0, depth=2.0, position=(0,0,0)):
    """Create a building
    Args:
        height, width, depth: Building size
        position: where the building is

    Returns: name of created building"""
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
    cmds.move(position[0], height / 2.0, position[2], building)
    return building

create_building()

def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    """Create a lamp post
    Args:
        height: height of pole
        light radius: radius of light sphere
        position: where the lamp post is

    Returns: name of created lamp post (grouped)"""
    pole = cmds.polyCylinder(radius=0.1, height=pole_height)[0]
    cmds.move(position[0], pole_height / 2.0, position[2],pole)
    lamp = cmds.polySphere(radius=0.25)[0]
    cmds.move(position[0], pole_height + 0.25, position[2], lamp)
    lamp_post=cmds.group(pole, lamp)
    cmds.move(position[0],position[1],position[2],lamp_post)
    return lamp_post

create_lamp_post()


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2, position=(0,0,0)):
    """Create a tree
    Args:
        trunk height: height of tree trunk
        canopy radius: radius of canopy sphere
        position: where the tree is

    Returns: name of created tree (grouped)"""
    trunk_radius = 0.3
    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(position[0], trunk_height / 2.0, trunk)
    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = trunk_height + canopy_radius * 0.6
    cmds.move(position[0], canopy_y, canopy)
    tree = cmds.group(trunk, canopy)
    cmds.move(position[0],position[1],position[2],tree)
    return tree

create_tree()


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0), **kwargs):
    """Call create_func repeatedly, placing results in a circle.
    Args:
        create_func = function being called
        count: how many of each object are created
        center: psoition of the center of the circle
        kwargs = key word arguements
    Returns: name of created list of objects"""
    results = []
    for i in range(count):
        angle = (2 * math.pi * i / count)
        x = center[0] + math.cos(angle) * radius
        z = center[2] + math.sin(angle) * radius
        result = create_building(position=(x, center[1], z))
        results.append(result)
    return results

cmds.viewFit(all=True)
place_in_circle(create_building)

