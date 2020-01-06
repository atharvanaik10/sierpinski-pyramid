GlowScript 2.9 VPython
import random



a = sphere(pos=vec(-0.5,0,0), size=vec(0.01,0.01,0.01), color = color.white)
b = sphere(pos=vec(0.5,0,0), size=vec(0.01,0.01,0.01), color = color.white)
c = sphere(pos=vec(-0.5,0,-1), size=vec(0.01,0.01,0.01), color = color.white)
d = sphere(pos=vec(0.5,0,-1), size=vec(0.01,0.01,0.01), color = color.white)
e = sphere(pos=vec(0,1,-0.5), size=vec(0.01,0.01,0.01), color = color.white)

start = sphere(pos=vec(0.30,0.48,-0.33), size=vec(0.01,0.01,0.01), color = color.white)
start2 = sphere(pos=vec(0.10,0.48,-0.5), size=vec(0.01,0.01,0.01), color = color.white)
x1 = 0
y1 = 0
z1 = 0

def recur(count, rand, x, y, z):
  if count >= 2500:
    print("done")
    x1 = x
    y1 = y
    z1 = z
  else if (rand <= 2):
    i = sphere(pos=vec((a.pos.x+x)/2,(a.pos.y +y)/2,(a.pos.z + z)/2), size = vec(0.01,0.01,0.01), color = color.white)
    recur(count+1, random.randint(1,10), i.pos.x, i.pos.y, i.pos.z)
  else if (rand <= 4):
    i = sphere(pos=vec((b.pos.x+x)/2,(b.pos.y +y)/2,(b.pos.z + z)/2), size = vec(0.01,0.01,0.01), color = color.white)
    recur(count+1, random.randint(1,10), i.pos.x, i.pos.y, i.pos.z)
  else if (rand <= 6):
    i = sphere(pos=vec((c.pos.x+x)/2,(c.pos.y +y)/2,(c.pos.z + z)/2), size = vec(0.01,0.01,0.01), color = color.white)
    recur(count+1, random.randint(1,10), i.pos.x, i.pos.y, i.pos.z)
  else if (rand <= 8):
    i = sphere(pos=vec((d.pos.x+x)/2,(d.pos.y +y)/2,(d.pos.z + z)/2), size = vec(0.01,0.01,0.01), color = color.white)
    recur(count+1, random.randint(1,10), i.pos.x, i.pos.y, i.pos.z)
  else:
    i = sphere(pos=vec((e.pos.x+x)/2,(e.pos.y +y)/2,(e.pos.z + z)/2), size = vec(0.01,0.01,0.01), color = color.white)
    recur(count+1, random.randint(1,10), i.pos.x, i.pos.y, i.pos.z)

randomint = random.randint(1,10)
recur(1, randomint, start.pos.x, start.pos.y, start.pos.z)
start2 = sphere(pos=vec(x1, y1, z1), size=vec(0.01,0.01,0.01), color = color.white)
recur(1, randomint, start2.pos.x, start2.pos.y, start2.pos.z)
start3 = sphere(pos=vec(x1, y1, z1), size=vec(0.01,0.01,0.01), color = color.white)
recur(1, randomint, start3.pos.x, start3.pos.y, start3.pos.z)
start4 = sphere(pos=vec(x1, y1, z1), size=vec(0.01,0.01,0.01), color = color.white)
recur(1, randomint, start4.pos.x, start4.pos.y, start4.pos.z)
