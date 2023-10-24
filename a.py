import numpy as np

def IK(LinkL1, LinkL2, x, y):
    cos_theta2 = (x**2 + y**2 - LinkL1**2 - LinkL2**2)/(2*LinkL1*LinkL2)
    theta2 = np.arccos(cos_theta2)

    theta1 = (np.arctan2(y, x)) - (np.arctan2(LinkL2*np.sin(theta2), (LinkL1 + LinkL2*np.cos(theta2))))

    theta1 = theta1 * (180/np.pi)
    theta2 = theta2 * (180/np.pi)

    return theta1, theta2