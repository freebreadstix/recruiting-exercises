def cheapest_shipment(item_map, warehouses):
    """ To run unit tests, navigate to src directory containing file and run `python -m doctest cheapest_shipment.py`
    A few things about implementation:
    - Function and doctests assume shipment is returned in order from cheapest to most expensive warehouse. The test case with multiple
    warehouses listed in the README returned warehouses in the opposite order, if the return order is arbitrary or the reverse then 
    I could have tested with sets or reverse the list before returning but increase expense seems most logical
    - If the order requests items with 0 counts in the shipment its assumed the order can't be shipped

    >>> # Warehouse tests
    >>> cheapest_shipment({ "apple": 1 }, [{ "name": "owd", "inventory": { "apple": 1 } }])
    [{'owd': {'apple': 1}}]
    >>> cheapest_shipment({"apple": 10}, [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}])
    [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
    >>> cheapest_shipment({"apple": 10}, [])
    []
    >>> cheapest_shipment({"apple": 10}, [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 9}}])
    [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
    >>> cheapest_shipment({'apple': 5, 'banana': 5, 'orange': 5}, [{"name": "sc", "inventory": {"apple": 1}}, \
        {"name": "owd", "inventory": {"apple": 4, 'banana': 5, 'orange': 3}}, {"name": "dm", "inventory": {"orange": 2}}])
    [{'sc': {'apple': 1}}, {'owd': {'apple': 4, 'banana': 5, 'orange': 3}}, {'dm': {'orange': 2}}]
    >>> cheapest_shipment({'apple': 5, 'banana': 5, 'orange': 5}, [{"name": "sc", "inventory": {"apple": 1}}, \
        {"name": "owd", "inventory": {"apple": 2, 'banana': 5, 'orange': 3}}, {"name": "dm", "inventory": {"apple": 2, "orange": 2}}])
    [{'sc': {'apple': 1}}, {'owd': {'apple': 2, 'banana': 5, 'orange': 3}}, {'dm': {'apple': 2, 'orange': 2}}]
    >>> cheapest_shipment({'apple': 5, 'banana': 5, 'orange': 5}, [{"name": "sc", "inventory": {'apple': 5, 'banana': 5, 'orange': 5}}, \
        {"name": "owd", "inventory": {'apple': 5, 'banana': 5, 'orange': 5}}, {"name": "dm", "inventory": {'apple': 5, 'banana': 5, 'orange': 5}}])
    [{'sc': {'apple': 5, 'banana': 5, 'orange': 5}}]
    >>> cheapest_shipment({'apple': 10, 'banana': 10, 'orange': 10}, [{"name": "sc", "inventory": {'apple': 5, 'banana': 5, 'orange': 5}}, \
        {"name": "owd", "inventory": {'apple': 5, 'banana': 5, 'orange': 5}}, {"name": "dm", "inventory": {'apple': 5, 'banana': 5, 'orange': 5}}])
    [{'sc': {'apple': 5, 'banana': 5, 'orange': 5}}, {'owd': {'apple': 5, 'banana': 5, 'orange': 5}}]


    >>> # Inventory tests
    >>> cheapest_shipment({"apple": 1}, [{"name": "owd", "inventory": {"apple": 0}}])
    []
    >>> cheapest_shipment({"apple": 2}, [{"name": "owd", "inventory": {"apple": 1}}])
    []
    >>> cheapest_shipment({'apple': 5, 'banana': 5, 'orange': 10}, [{"name": "sc", "inventory": {"apple": 1}}, \
        {"name": "owd", "inventory": {"apple": 4, 'banana': 5, 'orange': 3}}, {"name": "dm", "inventory": {"orange": 2}}])
    []
    >>> cheapest_shipment({'apple': 5, 'banana': 5, 'orange': 10, 'kiwi': 10}, [{"name": "sc", "inventory": {"apple": 1}}, \
        {"name": "owd", "inventory": {"apple": 4, 'banana': 5, 'orange': 3}}, {"name": "dm", "inventory": {"orange": 2}}])
    []


    >>> # Order tests
    >>> cheapest_shipment({}, [{"name": "owd", "inventory": {"apple": 1}}])
    []
    >>> cheapest_shipment({'apple': 0}, [{"name": "owd", "inventory": {"apple": 1}}])
    []
    >>> cheapest_shipment({'apple': 1}, [{"name": "owd", "inventory": {"appl": 1}}])
    []
    >>> cheapest_shipment({'apple': 0, 'orange': 5}, [{"name": "owd", "inventory": {"apple": 1}}, \
        {"name": "dm", "inventory": {"orange": 5}}])
    [{'dm': {'orange': 5}}]
    """
    shipment = []
    
    for warehouse in warehouses:
        if len(item_map) == 0:
            break

        inventory = warehouse['inventory']
        name = warehouse['name']
        warehouse_dict = {name: {}}
        shipment_dict = warehouse_dict[name]
        to_delete = []

        for item, total in item_map.items():
            if total == 0:
                to_delete.append(item)
                continue

            if item in inventory:
                from_warehouse = min(total, inventory[item])
                shipment_dict[item] = from_warehouse

                item_map[item] -= from_warehouse
                if item_map[item] == 0:
                    to_delete.append(item)
            
        for item in to_delete:
            del item_map[item]
        
        if len(shipment_dict) > 0:
            shipment.append(warehouse_dict)

    if len(item_map) > 0:
        return []
    return shipment

