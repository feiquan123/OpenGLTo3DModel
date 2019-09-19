import Chapter1.color as color
from Chapter1.node import HierarchicalNode, Sphere


# 雪人类
class SonwFigure(HierarchicalNode):
    def __init__(self):
        super().__init__()
        self.child_nodes = [Sphere(), Sphere(), Sphere()]
        self.child_nodes[0].translate(0, -0.6, 0)
        self.child_nodes[1].translate(0, 0.5, 0)
        self.child_nodes[1].scale(0.5)
        self.child_nodes[2].translate(0, 0.75, 0)
        self.child_nodes[2].scale(0.7)
        for node in self.child_nodes:
            node.color_index = color.MIN_COLOR