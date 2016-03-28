# Let's Encrypt App Engine

This is a Django app which helps to make it a bit easier to create & renew SSL certificates with [Let's Encrypt](https://letsencrypt.org/) when the site you want the certificate for is running on Google App Engine.


It's written to work with a project that uses [Djangae](https://github.com/potatolondon/djangae).


# Instructions

## Installation

* Put this package into your Django project.  I haven't released it to PyPi yet, so just dump the repo or use `pip install git+https://github.com/adamalton/letsencrypt-appengine.git#egg=letsencryptae`.
* Add `'letsencryptae'` to `INSTALLED_APPS`
* Add `url(r'^', include('letsencryptae.urls')),` as the last entry in your `patterns()` in your root URL conf.
* You'll also need to add this index to index.yaml (unless you visit the Django admin and trigger App Engine to add it to index.yaml for you automatically):

```yaml
- kind: letsencryptae_secret
  properties:
  - name: __key__
    direction: desc
```



## Creating A Certificate

* Make sure that your application is serving on App Engine on your custom domain and that the code is deployed with `letsencryptae` included (as per above).
* Download Let's Encrypt.
  * `git clone git@github.com:letsencrypt/letsencrypt.git`
  * `cd letsencrypt`
* Run `./letsencrypt-auto certonly --manual -d yourdomain.com`.
  * You can create a certificate for multiple domains by adding additional `-d other.domain.com` onto that command (see notes below).
* Answer the questions that it gives you.
* At some point it will then give you a prompt to add a file that contains a long random-looking string to be served at a random-lloking URL that starts with `/.well-known/acme-challenge/...`.
* Go to the Django admin of your site, and create a new `Secret` object in the 'letsencryptae' app.
  * In the `url_slug` field, insert everything that comes after `/.well-known/acme-challenge/`.
  * In the `secret` field insert the longer secret that Let's Encrypt wants you to serve.  This should start the same as the URL slug.
* Now tell the `letsencrypt` command to continue.
* __If you are issuing a single certificate that covers more than 1 domain (e.g. `my-domain`.com and `www.y-domain.com`), note that:__
  * `letsencrypt-auto` will give you MULTIPLE different secrets (one per domain).__  You must create a `Secret` in the Django admin and then hit enter to continue in the `letsencrypt-auto` command for each one.
  * Your app must be able to serve from all of the included domains in order that Let's Encrypt can validate that you own each one.


## Uploading A Certificate

* Go to your project in the [Google Cloud Console](https://console.developers.google.com).
* In the left menu to to App Engine and then Settings.
* Go to the SSL Certificates tab and click 'Upload a new certificate'.

Let's Encrypt should have told you where the certificate and the key have been stored on your computer.  But you need to convert the key into RSA format because App Engine won't accept it in the default format (and won't convert it for you).

* Run `openssl rsa -in /path/to/privkey.pem -out /path/to/privkey.rsa`.
  * Note that the `letsencrypt-auto` command will probably have put the certifcate and key in a location that is owned by `root`, so you will probably need to `sudo` that command.
* Now copy and paste the certificate and RSA-encoded priviate key into the form.
  * Note that you want the `fullchain.pem` file.
* Save it!
