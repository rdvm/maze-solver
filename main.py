from graphics import Window, Line, Point


def main():
    win = Window(1200, 900)
    l = Line(Point(100, 200), Point(200, 80))
    l2 = Line(Point(600, 700), Point(800, 5))
    win.draw_line(l, "red")
    win.draw_line(l2, "red")
    win.wait_for_close()


main()
