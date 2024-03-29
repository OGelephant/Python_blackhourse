from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359]]
}

param_values = saltelli.sample(problem, 1024)

Y = np.zeros([param_values.shape[0]])
 
for i, X in enumerate(param_values):
    Y[i] = evaluate_model(X)

np.savetxt("param_values.txt", param_values)
Y = np.loadtxt("outputs.txt", float)
Y = Ishigami.evaluate(param_values)
Si = sobol.analyze(problem, Y)
print(Si['S1'])
 
[ 0.316832  0.443763 0.012203 ]
print(Si['ST'])
 
[ 0.555860  0.441898   0.244675]