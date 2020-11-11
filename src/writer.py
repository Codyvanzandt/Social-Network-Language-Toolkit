from src.constants import TIME_MARK


class SNLWriter():

    def __init__(self):
        self.nodes = dict()
        self.edge_defs = dict()
        self.sections = list()
        self.edges = list()
        
    def addNode(self, name, data):
        self.nodes.update( {name, data} )
        return self

    def addEdgeDef(self, name, data):
        self.edge_defs.update( {name : data} )
        return self

    def addSection(self, name, data):
        self.sections.append( {name : data} )
        return self

    def addEdge(self, u, v, /, edge_type=None, data=None):
        self.edges.append( (u, edge_type, v, data ) )
        return self

    def addTimeMark(self, name):
        self.edges.append( (TIME_MARK, name, None, None) )
        return self
