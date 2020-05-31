from mo_simplex.simplex import calculate_by_simplex_method, enum_method, artificial_basis_method
import numpy as np

mine_c = np.array([3000, 1500, 2000, 0, 0, 0])
mine_A = np.array([[0.3, 0, 0.3, -1, 0, 0],
                   [0.1, 0.2, 0.7, 0, -1, 0],
                   [0.6, 0.8, 0, 0, 0, -1]])
mine_b = np.array([20, 50, 90])

duo_c = np.array([-20, -50, -90, 0, 0, 0])
duo_A = np.array([[0.3, 0.1, 0.6, 1, 0, 0],
                  [0, 0.2, 0.8, 0, 1, 0],
                  [0.3, 0.7, 0, 0, 0, 1]])
duo_b = np.array([3000, 1500, 2000])

calculate_by_simplex_method(mine_A, mine_b, mine_c, enum_method)
calculate_by_simplex_method(mine_A, mine_b, mine_c, artificial_basis_method)
