import math
#Z0=50
def Impedance_to_Reflectance(Real,Imag, Z0):
    Impedance=complex(Real,Imag)
    Z=Impedance/Z0
    Reflectance=(Z-1)/(Z+1)
    return Reflectance
#print(Impedance_to_Reflectance(49.82,0).real)
def Reflectance_to_Impedance(Gamma_Re,Gamma_Im, Z0):
    Reflectance=complex(Gamma_Re,Gamma_Im)
    Impedance=(Reflectance+1)/(1-Reflectance)*Z0
    return Impedance
#print(Reflectance_to_Impedance(0.065367,0.747146))
def Magphase_to_xy_X(Mag,Phase):
    x=Mag*math.cos(math.radians(Phase))
    x=round(x,8)
    return x
#print(Magphase_to_xy_X(1,60))
def Magphase_to_xy_Y(Mag,Phase):
    y=Mag*math.sin(math.radians(Phase))
    y=round(y,8)
    return y
#print(Magphase_to_xy_Y(1,60))
def xy_to_Magphase_Mag(x,y):
    Mag=math.sqrt(x*x+y*y)
    return round(Mag,8)
def xy_to_Magphase_phase(x,y):
    if x==0:
        phase=90
    else:
        phase = math.atan(y / x)
    Mag=math.sqrt(x*x+y*y)
    if Mag==0:
        phase=0
    #phase = math.degrees(phase)

    if x>=0:
        phase=math.degrees(phase)
    else:
        phase = math.degrees(phase)+180

    return round(phase,8)
def old_Reflectance_to_new_Reflectance(Reflectance_real, Reflectance_imag, Z0_old, Z0_new):
    Impedance=Reflectance_to_Impedance(Reflectance_real, Reflectance_imag, Z0_old)
    Reflectance=Impedance_to_Reflectance(Impedance.real,Impedance.imag, Z0_new)
    return Reflectance
    
#print(old_Reflectance_to_new_Reflectance(0.2, 0.1, 50, 50))
    
