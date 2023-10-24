import numpy as np

#Link1: Length of link 1
#Link2: Length of link 2
#x_axis_dist: distance to be moved in X axis
#y_axis_dist: distance to be moved in Y axis

def IK(LinkL1, LinkL2, x_axis_dist, y_axis_dist):
    cos_theta2 = (x_axis_dist**2 + y_axis_dist**2 - LinkL1**2 - LinkL2**2)/(2*LinkL1*LinkL2)
    theta2 = np.arccos(cos_theta2)

    theta1 = (np.arctan2(y_axis_dist, x_axis_dist)) - (np.arctan2(LinkL2*np.sin(theta2), (LinkL1 + LinkL2*np.cos(theta2))))

    theta1 = theta1 * (180/np.pi)
    theta2 = theta2 * (180/np.pi)

    return theta1, theta2
