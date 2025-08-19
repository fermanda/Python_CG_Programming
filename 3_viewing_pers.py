import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

def projection_matrix(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(35.0, w/h, 1.0, 200.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    projection_matrix(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClearColor(0.8, 0.8, 0.8, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glLoadIdentity()
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glBegin(GL_POLYGON)
        glColor3d(1.0, 1.0, 0.0)
        glVertex3d(-0.8, 0.3, -2.0)
        glVertex3d(-0.2, 0.3, -2.0)
        glVertex3d(-0.2, -0.3, -2.0)
        glVertex3d(-0.8, -0.3, -2.0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3d(0.0, 1.0, 1.0)
        glVertex3d(0.2, 0.3, 0.0)
        glVertex3d(0.8, 0.3, 0.0)
        glVertex3d(0.8, -0.3, 0.0)
        glVertex3d(0.2, -0.3, 0.0)
        glEnd()

        glFlush()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()