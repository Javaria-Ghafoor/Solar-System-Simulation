from vpython import *
planets = []

# mass, orbital velocity & radius of the earth
# initial momentum of earth = me * vE
# distance of the earth from the sun is dE
mE = 5.97e24
vE = 30e3
rE = 2
Au = 149.6e9



# create the solar system
sun = sphere(pos=vector(0,0,0), radius=696e6*60, color=color.yellow, mass=333000 * mE)
mercury = sphere(pos=vector(0,0,0.387 * Au), radius=696e6*8, color=color.red, mass=0.0553 * mE)
venus = sphere(pos=vector(0,0,0.723 * Au), radius=696e6*10, color=color.orange, mass=0.815 * mE)
earth = sphere(pos=vector(0,0,Au), radius=696e6*12, color=color.blue, mass=mE)
mars = sphere(pos=vector(0,0,1.52 * Au), radius=696e6*10, color=color.red, mass=0.107 * mE)
jupiter = sphere(pos=vector(0,0,5.20 * Au), radius=696e6*32, color=color.orange, mass=317.8 * mE)
saturn = sphere(pos=vector(0,0,9.58 * Au), radius=696e6*30, color=color.yellow, mass=95.2 * mE)
uranus = sphere(pos=vector(0,0,19.20 * Au), radius=696e6*28, color=color.cyan, mass=14.5 * mE)
neptune = sphere(pos=vector(0,0,30.05 * Au), radius=696e6*29.5, color=color.blue, mass=17.1 * mE)
satellite = sphere(pos=vector(0,0,Au+6371/Au), radius=50, color=color.white, mass=1593)

"""Scene Specs"""
scene.width = 1500
scene.height = 700
scene.range = 30.05 * Au
scene.color = color.black
scene.centre = sun.pos

# add initial velocities
sun.velocity = vector(0, 0, 0)
mercury.velocity = vector(1.607 * vE, 0, 0)
venus.velocity = vector(1.174 * vE, 0, 0)
earth.velocity = vector(vE, 0, 0)
mars.velocity = vector(0.802 * vE, 0, 0)
jupiter.velocity = vector(0.434 * vE, 0, 0)
saturn.velocity = vector(0.323 * vE, 0, 0)
uranus.velocity = vector(0.228 * vE, 0, 0)
neptune.velocity = vector(0.182 * vE, 0, 0)
satellite.velocity = vector(vE, 0, 1.7*vE)

"""
#intial velocity with moving sun
sun.velocity = vector(0, 7.7 * vE, 0)
mercury.velocity = vector(1.607 * vE, 7.7 * vE, 0)
venus.velocity = vector(1.174 * vE, 7.7 * vE, 0)
earth.velocity = vector(vE, 7.7 * vE, 0)
mars.velocity = vector(0.802 * vE, 7.7 * vE, 0)
jupiter.velocity = vector(0.434 * vE, 7.7 * vE, 0)
saturn.velocity = vector(0.323 * vE, 7.7 * vE, 0)
uranus.velocity = vector(0.228 * vE, 7.7 * vE, 0)
neptune.velocity = vector(0.182 * vE, 7.7 * vE, 0)
satellite.velocity = vector(vE, 7.7 * vE, 0.4 * vE)
"""


planets.extend((sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, satellite))

# add trails
for planet in planets:
	planet.trail = curve(color=color.white)

"""# add arrows
vscale = 10 ** 6
varrows = []
for planet in planets:
	varrows.append(arrow(pos=planet.pos, axis=planet.velocity * vscale, color=color.white, planet=planet)) 
"""
dt = 100
t = 0

GRAVC = 6.67e-11

def gravAcc(obj, other):
        """ acceleration of an object due to gravitational force """
        rVector = obj.pos - other.pos
        r_mag_square = rVector.mag2
        if r_mag_square == 0:
                print('Division by zero error (acc set to 0)')
                acc = vector(0,0,0)
        else:
                acc = -((GRAVC * other.mass) / r_mag_square ) * norm(rVector)
        return acc

 # def tell_time(seconds):
 # 	years = int(seconds / 3.15569e7)
 # 	months = int((seconds % 3.15569e7) / 2.62974e6)
 # 	days = int(((seconds % 3.15569e7) % 2.62974e6) / 86400 )
 # 	print "Years: ", years, "Months: ", months, "Days: ", days


while (True):
	rate(1e50)
	#print (t)

	for planet1 in planets:
		for planet2 in planets:
			if planet1 != planet2:
				planet1.velocity += gravAcc(planet1, planet2) * dt

	# update the position of the objects
	for planet in planets:
		planet.pos += planet.velocity * dt

	# update the trail and arrows following the objects
	for planet in planets:
		planet.trail.append(pos=planet.pos)
	"""
	for varrow in varrows:
		varrow.pos = varrow.planet.pos
		varrow.axis = varrow.planet.velocity * vscale
	"""
	t += dt



# 3.15569e7 in a year
