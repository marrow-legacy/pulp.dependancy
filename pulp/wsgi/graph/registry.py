# encoding: utf-8

"""A global middleware registry.

Combines middleware passively discovered from installed packages' entry
points, manually registered classes, and entry points updated during
runtime.
"""


__all__ = ['register', 'graph']


layers = []
registry = {}


def register(cls):
    layers.append(cls)
    
    if cls.__name__ not in registry:
        registry[cls.__name__] = []
    
    registry[cls.__name__].append(cls)
    
    if hasattr(cls, 'provides'):
        for meta in cls.provides if isinstance(cls.provides, list) else [cls.provides]:
            if meta not in registry:
                registry[meta] = []
                
            registry[meta].append(cls)
    
    return cls


def graph():
    graph = []
    
    for layer in layers:
        if hasattr(layer, 'uses'):
            for i in layer.uses if isinstance(layer.uses, list) else [layer.uses]:
                if (layer, registry[i][0]) not in graph:
                    graph.append((layer, registry[i][0]))
        
        if hasattr(layer, 'needs'):
            for i in layer.needs if isinstance(layer.needs, list) else [layer.needs]:
                if (layer, registry[i][0]) not in graph:
                    graph.append((layer, registry[i][0]))
        
        if hasattr(layer, 'after'):
            for i in layer.after if isinstance(layer.after, list) else [layer.after]:
                if i != '*':
                    targets = [registry[i][0]]
                
                else:
                    targets = []
                    
                    for target in layers:
                        if layer is target:
                            continue
                        
                        targets.append(target)
                
                for target in targets:
                    if (layer, target) not in graph:
                        graph.append((target, layer))
        
        if hasattr(layer, 'before'):
            for i in layer.before if isinstance(layer.before, list) else [layer.before]:
                if i != '*':
                    targets = [registry[i][0]]
                
                else:
                    targets = []
                    
                    for target in layers:
                        if layer is target:
                            continue
                        
                        targets.append(target)
                
                for target in targets:
                    if (target, layer) not in graph:
                        graph.append((layer, target))
    
    return graph
