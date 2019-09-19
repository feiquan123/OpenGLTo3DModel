import random
from OpenGL.GL import glCallList, glColor3f, glMaterialfv, glMultMatrixf, glPopMatrix, glPushMatrix, \
    GL_EMISSION, GL_FRONT
import numpy

import Chapter1.color as color
# 标识代码段的数字
from Chapter1.primtive import G_OBJ_SPHERE
# 仿射变换
from Chapter1.transformation import scaling, translation


class Node:
    def __init__(self):
        # 该节点的颜色序号
        self.color_index = random.randint(color.MIN_COLOR, color.MAX_COLOR)
        # 该接待你的平移矩阵，决定该节点在场景中的位置
        self.translation_matrix = numpy.identity(4)
        # 该节点的缩放矩阵，决定该节点的大小
        self.scaling_matrix = numpy.identity(4)

    def render(self):
        ''' 渲染节点 '''
        glPushMatrix()
        # 实现平移
        glMultMatrixf(numpy.transpose(self.translation_matrix))
        # 实现缩放
        glMultMatrixf(self.scaling_matrix)
        cur_color = color.COLORS[self.color_index]
        # 设置颜色
        glColor3f(cur_color[0], cur_color[1], cur_color[2])
        # 渲染对象模型
        self.render_self()

    def render_self(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'render_self'"
        )

    '''平移'''

    def translate(self, x, y, z):
        self.translation_matrix = numpy.dot(self.translation_matrix, translation([x, y, z]))

    ''' 缩放 '''

    def scale(self, s):
        self.scaling_matrix = numpy.dot(self.scaling_matrix, scaling([s, s, s]))


# 图元类
class Primitive(Node):
    def __init__(self):
        #  Python 3 可以使用直接使用 super().xxx 代替 python2 super(Class, self).xxx
        super().__init__()
        self.call_list = None

    def render_self(self):
        glCallList(self.call_list)


class Sphere(Primitive):
    ''' 球形图元'''

    def __init__(self):
        super().__init__()
        self.call_list = G_OBJ_SPHERE


class HierarchicalNode(Node):
    def __init__(self):
        super().__init__()
        self.child_nodes = []

    def render_self(self):
        for child in self.child_nodes:
            child.render()
