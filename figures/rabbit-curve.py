import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
X = np.linspace(0,1, 1000)
s = stats.beta(1.4,3)
plt.plot(X, s.pdf(X), lw=4)
plt.xticks([0,1], ["anarcho-capitalism", "communism"])
plt.yticks([])
plt.ylabel('goodness')
plt.xlabel('Individualism vs Societism')
plt.text(.5,s.pdf(.5), 'We are here')



plt.arrow(0,0, .5, s.pdf(.5), width=.02, length_includes_head=True, color='#66ffff')
plt.arrow(.5, s.pdf(.5), -.5, -s.pdf(.5), width=.02, length_includes_head=True, color='#66ffff')

plt.arrow(1, 0, -.5, s.pdf(.5), width=.02, length_includes_head=True, color='#66ffff')
plt.arrow(.5, s.pdf(.5), .5, -s.pdf(.5), width=.02, length_includes_head=True, color='#66ffff')

plt.text(.5, .1, 'unhelpful comparisons', horizontalalignment='center',)


plt.arrow(.5, .15, -.2, .4*s.pdf(.5), width=.01, length_includes_head=True, color='k')
plt.arrow(.5, .15, .2, .4*s.pdf(.5), width=.01, length_includes_head=True, color='k')

plt.savefig('rabbit-curve.pdf')
