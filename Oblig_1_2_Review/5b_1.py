import numpy as np
g = 9.8066 # Regnes som konstant
def calculate_accel(mass, angle, friction):
    # Mass is a redundant argument:
    # a = (mass * g * np.sin(angle * np.pi/180) - friction * mass * g * np.cos(angle * np.pi/180))/mass
    # a = mass * g * (np.sin(angle * np.pi/180) - friction * np.cos(angle * np.pi/180))/mass
    # a = g * (np.sin(angle * np.pi/180) - friction * np.cos(angle * np.pi/180))
    # but is kept for explaination purposes.
    
    # Force parralell to the slope due to gravity
    Fp = mass * g * np.sin(angle * np.pi/180)
    # Force normal to the slope due to gravity
    Fn = mass * g * np.cos(angle * np.pi/180)
    # Negative Force due to the friction coefficent and the Force normal to the slope
    R = friction * Fn
    # Calculate the Force on the skier minus the force of friction
    F = Fp-R
    # divide by mass to get the acceleration, F=ma -> a=F/m
    a = F/mass
    return a

m = 90 # masse
alpha = 22 # vinkel
mu = 0.15 # friksjonstall

accel = calculate_accel(m, alpha, mu)

print(f"""For en skiløper med masse m={m}kg i en bakke med helningsvinkel {alpha} grader og friksjonstall {mu} 
vil akselerasjon i retning parallelt med bakken være {accel:.2f}m/s2.""")