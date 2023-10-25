from math import *

def stand(link1, link2, hypo):
    cos_theta_b = (link1**2 + hypo**2 - link2**2)/(2*link1*hypo)

    theta_b = int(degrees(acos(cos_theta_b)))
    theta_c = (180-(theta_b*2))
    
    theta_b += 52
    theta_c -= 14

    pwm_b = (theta_b - 90)/90
    pwm_c = (theta_c - 90)/90

    return theta_b, theta_c, pwm_b, pwm_c

print(stand(0.122,0.130,0.2))