from collections import deque

from app import update_graph, app


def _find_component_by_id(root, target_id):
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if getattr(node, 'id', None) == target_id:
            return node
        children = getattr(node, 'children', None)
        if isinstance(children, (list, tuple)):
            dq.extend(children)
        elif children is not None:
            dq.append(children)
    return None


def test_radioitems_present():
    radio = _find_component_by_id(app.layout, 'region-radio')
    assert radio is not None, 'Expected a RadioItems with id "region-radio" in the app layout'


def test_update_graph_for_each_region():
    regions = ['north', 'east', 'south', 'west', 'all']
    for region in regions:
        fig = update_graph(region)
        assert fig is not None, f'update_graph returned None for region "{region}"'
        assert hasattr(fig, 'data'), 'Expected figure to have data traces'

        if region == 'all':
            expected = {'north', 'east', 'south', 'west'}
            actual = set(trace.name for trace in fig.data)
            assert expected.issubset(actual), 'Expected the graph to show data for all regions'
        else:
            names = [trace.name for trace in fig.data]
            assert region in names, f'Expected a trace for region "{region}"'
