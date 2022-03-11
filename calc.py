from math import sin
from math import radians

ev = 1.62e-19
c = 3e8
h = 6.62e-34
e = 17.3 * 1e3 * ev
l = h * c / e

def d_from_sin(theta_2):
    return l / (2 * sin(theta_2 / 2))

def calc_d(theta_2_vals):
    peak1_rad = [radians(p) for p in theta_2_vals]
    return [d_from_sin(p) for p in peak1_rad]

if __name__ == '__main__':

    # http://webmineral.com/MySQL/xray.php?lambda=0.70930+-+MoKa1&lambda1=&ed1=3.13&ed2=2.26&ed3=1.82&minmax=10&chem=&submit=Submit+Query#.YivIf1Qo-Cg
    peak1_deg = [13, 18, 22.5] # Sylvite? KCl
    result1 = calc_d(peak1_deg)
    print('d early peaks:')
    for peak in result1:
        print(f'  {peak * 1e10:.2f} Å')

    # http://webmineral.com/MySQL/xray.php?lambda=0.70930+-+MoKa1&lambda1=&ed1=2.81&ed2=1.97&ed3=1.64&minmax=10&chem=&submit=Submit+Query#.YivJ5FQo-Cg
    peak2_deg = [14.5, 20.7, 25] # Halite? NaCl
    result2 = calc_d(peak2_deg)
    print('d later peaks:')
    for peak in result2:
        print(f'  {peak * 1e10:.2f} Å')
