'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

import datetime as dt
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, ClearBuffers, Fbo, ClearColor, Scale, Translate
from kivy.core.image import Image
from kivy.properties import ObjectProperty


class Painter(Widget):
    pen_color = ObjectProperty(Color(0,0,0))

    def on_touch_down(self, touch):
        print(self.pen_color)
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=4, cap="round", joint="round", color=self.pen_color)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            touch.ud['line'].points += [touch.x, touch.y]

    def export_image(self, name=None, path="./../../captures/"):
        if not name:
            name = "capture_{}.png".format(dt.datetime.now().strftime("%Y%m%d_%H%M"))
        scale = 1
        if self.parent is not None:
            canvas_parent_index = self.parent.canvas.indexof(self.canvas)
            if canvas_parent_index > -1:
                self.parent.canvas.remove(self.canvas)

        fbo = Fbo(size=(self.width * scale, self.height * scale),
                  with_stencilbuffer=True)

        with fbo:
            ClearColor(0,0,0, 1)
            ClearBuffers()
            Scale(1, -1, 1)
            Scale(scale, scale, 1)
            Translate(-self.x, -self.y - self.height, 0)

        fbo.add(self.canvas)
        fbo.draw()
        img = Image(fbo.texture)
        fbo.remove(self.canvas)

        if self.parent is not None and canvas_parent_index > -1:
            self.parent.canvas.insert(canvas_parent_index, self.canvas)

        img.save(path+name)

    def clear(self):
        self.canvas.clear()
