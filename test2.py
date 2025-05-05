from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/icon.png')
sky_texture = load_model("assets/")

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin = 5,
            texture = texture,
            color = color.color(0, 0, 255),
            highlight_color = color.black
        )

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                voxel = Voxel(position = self.position + mouse.normal)
            if key == "left mouse down":
                destroy(self)


for z in range(15):
    for x in range(15):
        voxel = Voxel((x, 0, z))

player = FirstPersonController()
app.run()

app.setBackgroundColor(255, 0, 0)
running = True

#while running:
   