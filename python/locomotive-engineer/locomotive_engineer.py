"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*arbitrary_number_of_wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(arbitrary_number_of_wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    new_list = [each_wagons_id[2],*missing_wagons,*each_wagons_id[3:],each_wagons_id[0],each_wagons_id[1]]
    return new_list



def add_missing_stops(d,**stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    new_dict = {}

    for k,v in stops.items():
        new_dict[k] = v
    d["stops"] = [*new_dict.values()]
    return d
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    
    return {**route, **more_route_information}



def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    lst = [*wagons_rows]
    return [[lst[0][0], lst[1][0], lst[2][0]], [lst[0][1], lst[1][1], lst[2][1]], [lst[0][2], lst[1][2], lst[2][2]]]
    
"""
print(fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ]))

expected: [
[(2, "red"), (5, "blue"), (3, "orange")],
[(4, "red"), (9, "blue"), (7, "orange")],
[(8, "red"), (13,"blue"), (11, "orange")]
]
"""