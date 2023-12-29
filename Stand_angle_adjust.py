from math import *

def stand(link1, link2, hypo):

    cos_theta_c = (link1**2 + hypo**2 - link2**2)/(2*link1*hypo)
    theta_c = int(degrees(acos(cos_theta_c)))

    cos_theta_b = (hypo**2 + link2**2 - link1**2)/(2*hypo*link2)
    theta_b = int(degrees(acos(cos_theta_b)))

    theta_a = (180-(theta_c + theta_b))

    F_angle1 = 40 #Default angle at some shoulder motor angle (90 deg)
    F_angle2 = 40 #Default angle at some elbow motor angle (90 deg)

    angle_s = 90 + (theta_c - F_angle1)
    angle_e = 90 + (theta_a - F_angle2)

    # angle_s and angle_e are the actual servo motor angle. Convert this to suitable pwm as per the motor:


    return theta_c, theta_a, angle_s, angle_e


print(stand(0.122,0.130,0.17))