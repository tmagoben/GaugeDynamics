# GaugeDynamics

Numerical reference implementations for gauge covariance in finite-state quantum
dynamics.

## Implemented

- local $U(N)$ basis transformations;
- Hermitian gauge connections with convention $D = \partial - iA$;
- connection transformation

$$
A' = G^\dagger A G + i\,G^\dagger(\partial G);
$$

- numerical covariance checks for $D'\psi' = G^\dagger D\psi$;
- discrete link-variable and Wilson-loop transformations;
- $U(3)$ examples;
- time-reversal projection for Kramers-paired spinor spaces and numerical
  Kramers-degeneracy tests.

```bash
pip install -e ".[dev]"
python examples/u3_covariant_derivative.py
python examples/kramers_projection.py
pytest -q
```
