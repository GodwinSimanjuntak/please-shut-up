from .base import Limiter

# applied to every /api route
RATE_LIMIT = "100/minute"
BURST = 20

limiter = Limiter(RATE_LIMIT, burst=BURST)
