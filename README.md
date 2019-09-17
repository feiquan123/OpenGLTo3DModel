# OpenGLTo3DModel
OpenGL Implement 3DModel

1.参考
---
   - [Python实现建模工具](https://www.shiyanlou.com/courses/561)
   - [Python安装PyOpenGL](https://www.cnblogs.com/feiquan/p/11371144.html)
 
2.注意
---
  1. Chapter1 ->  __Python实现3D建模工具（上）__  
    1. `import` 在原始文件中，直接导入不同的模块，但是如果你没有将当前目录加入到os.path 中会导致模块无法找到  
    eg. node.py
       ```python
        import random
        from OpenGL.GL import glCallList, glColor3f, glMaterialfv, glMultMatrixf, glPopMatrix, glPushMatrix, \
            GL_EMISSION, GL_FRONT
        import numpy
        
        # 注意这里
        import Chapter1.color as color
      ```
     1. 原文使用的是 python2 的语法，我这里实现时使用的是python3 的语法，所以会有部分不同，但都可以通过运行
     
