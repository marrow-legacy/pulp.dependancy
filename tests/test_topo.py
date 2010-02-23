# encoding: utf-8

from unittest import TestCase

from pulp.wsgi.graph.registry import register, graph
from pulp.wsgi.graph.exception import *
from pulp.wsgi.graph.topo import resolve, leveled


@register
class A(object):
    provides = ['foo']

@register
class B(object):
    uses = ['foo', 'bar']

@register
class C(object):
    after = '*'

@register
class D(object):
    provides = ['bar']
    needs = ['A']


class TestErrorConditions(TestCase):
    pass


class TestResolve(TestCase):
    def test_basic(self):
        self.assertEquals(resolve([(1,2), (3,4), (5,6), (1,3), (1,5), (1,6), (2,5)]), [1, 2, 3, 5, 4, 6])
        self.assertEquals(resolve([(1,2), (1,3), (2,4), (3,4), (5,6), (4,5)] ), [1, 2, 3, 4, 5, 6])
    
    def test_errors(self):
        self.assertRaises(CyclicDependancyError, lambda: resolve([(1,2), (2,3), (3,2)]))


class TestLeveledSort(TestCase):
    def test_basic(self):
        dependency_pairs = [(1,2), (3,4), (5,6), (1,3), (1,5), (1,6), (2,5)]
        dependency_graph = [i for i in leveled(dependency_pairs)]
        self.assertEquals(dependency_graph, [[1], [2, 3], [4, 5], [6]])
        
        dependency_pairs = [(1,2), (1,3), (2,4), (3,4), (5,6), (4,5)]
        dependency_graph = [i for i in leveled(dependency_pairs)]
        self.assertEquals(dependency_graph, [[1], [2, 3], [4], [5], [6]])
    
    def test_errors(self):
        dependency_pairs = [(1,2), (2,3), (3,4), (4, 3)]
        self.assertRaises(CyclicDependancyError, lambda: [i for i in leveled(dependency_pairs)])


class TestMiddlewareGraph(TestCase):
    def test_classes(self):
        self.assertEquals(resolve(graph()), [B, D, A, C])
