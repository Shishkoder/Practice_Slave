import matplotlib.pyplot as plt


Q = list(range(-10, 11))
TC = []
VC = []
MC = []
AFC = []
AVC = []
ATC = []
FC = 100

for i, q in enumerate(Q):
    TC.append(100 + 4*q + 0.25 * q**2)
    VC.append(4*q + 0.25 * q**2)
    MC.append(4 + 0.5*q)

    if q != 0:
        AFC.append(FC / q)
        AVC.append(VC[i] / q)
    else:
        AFC.append(0)
        AVC.append(0)

    ATC.append(AFC[i] + AVC[i])

plt.title('TC(Q)', fontsize=20, fontname='Times New Roman')
plt.plot(Q, TC)
plt.show()
