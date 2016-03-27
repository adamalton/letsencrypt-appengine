# Let's Encrypt App Engine

This is a Django app which helps to make it a bit easier to create & renew SSL certificates with [Let's Encrypt](https://letsencrypt.org/) when the site you want the certificate for is running on Google App Engine.


It's written to work with a project that uses [Djangae](https://github.com/potatolondon/djangae).


# Instructions

## Installation

* Put this package into your Django project.  I haven't released it to PyPi yet, so just dump the repo or use `pip install git+https://github.com/adamalton/letsencrypt-appengine.git#egg=letsencryptae`.
* Add `'letsencryptae'` to `INSTALLED_APPS`
* Add `url(r'^', include('letsencryptae.urls')),` as the last entry in your `patterns()` in your root URL conf.
* If you want it to be eas

# Creating A Certificate

* Download Let's Encrypt.
* Run `letsencrypt-auto standalone --manual -d yourdomain.com`.
* Answer the questions that it gives you.
* At some point it will then give you a prompt to add a file that contains a long random-looking string to be served at a random-lloking URL that starts with `/.well-known/acme-challenge/...`.
* Go to the Django admin of your site, and create a new `Secret` object in the 'letsencryptae' app.
  * In the `url_slug` field, insert everything that comes after `/.well-known/acme-challenge/`.
  * In the `secret` field insert the longer secret that Let's Encrypt wants you to serve.  This should start the same as the URL slug.
* Now tell the `letsencrypt` command to continue.
* __Note that if you are issuing a single certificate that covers more than 1 domain (e.g. `my-domain`.com and `www.y-domain.com`) that `letsencrypt` will give you MULTIPLE different secrets (one per domain).__  You must create a `Secret` in the Django admin for each one.
