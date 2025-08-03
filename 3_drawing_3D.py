import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

lx = 1.0

VERTEXES = [
    [-lx, lx, lx],   # A
    [lx, lx, lx],   # B
    [lx, -lx, lx],   # C
    [-lx, -lx, lx],   # D
    [-lx, lx, -lx],   # E
    [lx, lx, -lx],   # F
    [lx, -lx, -lx],   # G
    [-lx, -lx, -lx],   # H
]

EDGES = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

def set_view(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(35.0, w/h, 1.0, 200.0)
    glMatrixMode(GL_MODELVIEW)

def resize(window, w, h):
    # for iconify on Windows
    if h==0:
        return
    glViewport(0, 0, w, h)
    set_view(w, h)

def main():
    # Initialize the library
    if not glfw.init():
        return
    
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return
    
    # Make the window's context current
    glfw.make_context_current(window)

    set_view(WINDOW_WIDTH, WINDOW_HEIGHT)

    r = 1
    
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.8, 0.8, 0.8, 1.0)
        
        glLoadIdentity()
        gluLookAt(3.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRotated(r, 0.0, 1.0, 0.0)
        r += 1
        if r > 360: r=0

        glBegin(GL_LINES)
        glColor3d(0.0, 0.0, 0.0)
        for edge in EDGES:
            for vx in edge:
                # glVertex3d(VERTEXES[vx][0], VERTEXES[vx][1], VERTEXES[vx][2])
                glVertex3dv(VERTEXES[vx])
        glEnd()
        glFlush()


        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()