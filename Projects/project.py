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
s2 = codesters.Sprite ('ski', -50, -20)
s3 = codesters.Sprite ('seattle', 100, -100)
s4 = codesters.Sprite ('bob', -100, 100)
s4.set_size(0.5)
s2.set_size(0.4)