import stripe

# setting up stripe test environment
STRIPE_PUBLISHABLE_KEY = ''  
STRIPE_SECRET_KEY = ''

stripe.api_key = STRIPE_SECRET_KEY
