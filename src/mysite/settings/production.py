from .base import *

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

## Uncomment these if you want to use stripe api for any kind of online payment
# STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')

## Uncomment these if you want to use Braintree is another option for payments to.
# BRAINTREE_PUBLIC_KEY = config('BRAINTREE_PUBLIC_KEY')
# BRAINTREE_SECRET_KEY = config('BRAINTREE_SECRET_KEY')


## For Security issues                 ## Uncomment these in the production server.
# SECURE_SSL_REDIRECT = True          ## It redirects all http to https requests if set to True
# SECURE_CONTENT_TYPE_NOSNIFF = True  ## Prevent the browser from identifying content types incorrectly.
# SECURE_BROWSER_XSS_FILTER = True    ## XSS(Cross-site scripting) attack Protection -  XSS enables attackers to inject client-side scripts into web pages viewed by other users.
# SESSION_COOKIE_SECURE = True        ## Network traffic sniffers to hijack user sessions.
# CSRF_COOKIE_SECURE = True           ## Protection against stealing the CSRF(Cross site request Forgery) token  which means browsers may ensure that the cookie is only sent with an HTTPS connection.
# X_FRAME_OPTIONS = 'DENY'            ## Protection against clickjacking (This type of attack occurs when a malicious site tricks a user into clicking on a concealed element of another site which they have loaded in a hidden frame or iframe.)
