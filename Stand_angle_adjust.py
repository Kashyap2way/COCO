import numpy as np

#Link1: Length of link1
#Link2: Length of Link2
#hypo: hypoteneus distance

def stand_adjust(link1, link2, hypo):
    cos_theta_b = (link1**2 + hypo**2 - link2**2)/(2*link1*hypo)
    theta_b = np.arccos(cos_theta_b)
    theta_c = (np.pi-(theta_b*2))

    theta_b = theta_b * (180/np.pi)
    theta_c = theta_c * (180/np.pi)

    return theta_b, theta_c