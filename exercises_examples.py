
####
# Support for ISART 2021-2022 Scripting Courses.
# Module 001 : Renaming Tool for Maya objects
####

import maya.cmds as mc

# I define constant variables, which can be used everywhere in the code
DEFAULT_SUFFIX = '_obj'
LIGHT_SUFFIX = '_lgt'
MESH_SUFFIX = '_geo'
CAMERA_SUFFIX = '_cam'

LIGHT_TYPES = ['directionalLight', 'spotLight', 'pointLight', 'ambientLight', 'areaLight']
MESH_TYPES = ['mesh']
CAMERA_TYPES = ['camera']


# My 'lib' functions, used by my main function :
def get_padding(number, depth=4):
    """ Determine the correct padding depending on the given number and the padding depth.

    :param number: Number to which will be added as many zeroes as needed to get to the depth level.
    :type number: int

    :param depth: Max numbers in the padding (4 = 0000)
    :type depth: int

    :return generated padding
    :rtype: str
    """
    padding = str(number)
    while len(padding) < depth:
        padding = '0' + padding

    return padding


def generate_name_from_type_and_index(object_type, index):
    """ Generates a formatted name for a maya object depending on the given object type and the given object index.

     :param object_type: Type of the object to generate a name for
     :type object_type: str

     :param index: Number assigned to the object
     :type index: int

     :return: Generated name
     :rtype: str
     """
    suffix = DEFAULT_SUFFIX

    if object_type in LIGHT_TYPES:
        suffix = LIGHT_SUFFIX

    elif object_type in MESH_TYPES:
        suffix = MESH_SUFFIX

    elif object_type in CAMERA_TYPES:
        suffix = CAMERA_SUFFIX

    new_name = '{type}_{padding}{suffix}'.format(type=object_type,
                                                 padding=get_padding(index, 3),
                                                 suffix=suffix)
    return new_name


# My principal function :
def rename_selected_objects_by_type():
    """ Renames the selected objects.

    The function renames only selected objects, and uses a defined nomenclature depending on each of the object's type.
    """
    selected_objects = mc.ls(sl=True)
    if not selected_objects:
        print('Please select at least one object')
        return

    for object_number, object_name in enumerate(selected_objects, start=1):
        shape = mc.listRelatives(object_name, children=True)
        object_type = mc.nodeType(shape)
        new_name = generate_name_from_type_and_index(object_type, object_number)

        try:
            mc.rename(object_name, new_name)
        except RuntimeError:
            print('could not rename node {}'.format(object_name))


# Launch my main function by calling it :
rename_selected_objects_by_type()
