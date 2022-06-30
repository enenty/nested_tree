from django.shortcuts import render
from django.http import JsonResponse

from .models import Tree


def treeview(request):
    data = list(Tree.objects.order_by('parent_id').values())
    tree = get_tree(data)
    return JsonResponse(tree, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})


def nodeview(request, pk):
    data = list(Tree.objects.order_by('parent_id').values())
    nodes = get_tree(data, node_id=pk)
    return JsonResponse(nodes, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})


def get_tree(data, id='id', parent_id='parent_id', children='children', root=None, node_id=None, drop_parent=True):
    if node_id:
        nodes = list(filter(lambda item: item[id] == node_id, data))
    else:
        nodes = list(filter(lambda item: item[parent_id] == root, data))

    def get_children(node):
        nested = []
        for item in list(filter(lambda item: item[parent_id] == node[id], data)):
            item[children] = get_children(item)
            if drop_parent:
                nested.insert(1, (lambda parent_id, **kw: kw)(**item))
            else:
                nested.insert(1, item)
        return nested

    for node in nodes:
        node[children] = get_children(node)
        if drop_parent:
            del node[parent_id]
    return nodes
