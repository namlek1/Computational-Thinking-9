###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("winter")

q1 = codesters.Square (100, 100, 200, "blue")
q1 = codesters.Square (-100, 100, 200, "red")
q1 = codesters.Square (-100, -100, 200, "green")
q1 = codesters.Square (100, -100, 200,"yellow")

s1 = codesters.Sprite ("download", 100, 100)
s2 = codesters.Sprite ('ski', -70, -70)
s3 = codesters.Sprite ('bike', 100, -100)
s4 = codesters.Sprite ('cool_dog', -100, 100)
s4.set_size(0.1)
s2.set_size(0.4)

m1 = codesters.Text("im oscar :)",0,-200,"red")