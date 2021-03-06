    def activation_func( z, activation=None, return_derivative=False):
        import numpy as np
        if activation == 'sigmoid':
            s = 1/(1 + np.exp(-z))
            if return_derivative:
                return s*(1 - s)

        elif activation == 'tanh':
            s = np.tanh(z)
            if return_derivative:
                return 1 - s**2

        elif activation == 'reLU':
            s = np.maximum(z, 0)
            if return_derivative:
                return (s > 0)*s

        elif activation == 'leakyrelu':
            s = np.where(z > 0, z, z * 0.01)
            if return_derivative:
              s = np.ones_like(z)
              s[z < 0] = alpha
              return s

        elif activation == 'softmax':
            max_z = np.max(z, axis=0, keepdims=True)
            s = np.exp(z - max_z)
            norm = np.sum(s, axis=0, keepdims=True)
            s = s/norm
            if return_derivative:
                return s*(1-s)

        return s
