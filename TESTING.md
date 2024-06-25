# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

As my project uses Jinja syntax, such as `{% for loops %}`, `{% url 'home' %}`, and `{{ variable|filter }}` it will not validate properly if I copy and paste into the HTML validator straight from my source files. In order to properly validate these types of files, it's recommended to [validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Some of the pages on this site require a user to be logged-in and authenticated and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have access to login to the pages. In these cases the following steps have to be taken:

* Navigate to the deployed pages which require authentication.
* Right-click on the page and select View Page Source (usually `CTRL+U` or `⌘+U` on Mac).
* This will display the entire "compiled" code, without any Jinja syntax.
* Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
* Repeat this process for every page that requires a user to be logged-in/authenticated.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Cart | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fcart%2F) | ![screenshot](documentation/testing/validation/html/cart.png) | Pass: No errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fcheckout%2F) | ![screenshot](documentation/testing/validation/html/checkout.png) | Pass: No errors |
| Checkout success | n/a | ![screenshot](documentation/testing/validation/html/checkoutsuccess.png) | Pass: No errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/testing/validation/html/contact.png) | Pass: No errors |
| Contact success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fcontact%2Fsuccess%2F) | ![screenshot](documentation/testing/validation/html/contactsuccess.png) | Pass: No errors |
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/testing/validation/html/about.png) | Pass: No errors |
| Delivery | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fdelivery%2F) | ![screenshot](documentation/testing/validation/html/delivery.png) | Pass: No errors |
| Index | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2F) | ![screenshot](documentation/testing/validation/html/index.png) | Pass: No errors |
| Terms & conditions | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fterms%2F) | ![screenshot](documentation/testing/validation/html/terms.png) | Pass: No errors |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fcontact%2Fsuccess%2F) | ![screenshot](documentation/testing/validation/html/products.png) | Pass: No errors |
| Product detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fproducts%2F96%2F) | ![screenshot](documentation/testing/validation/html/productdetail.png) | Pass: No errors |
| Add product | n/a | ![screenshot](documentation/testing/validation/html/addproduct.png) | Pass: No errors |
| Edit product | n/a | ![screenshot](documentation/testing/validation/html/editproduct.png) | Pass: No errors |
| Profile | n/a | ![screenshot](documentation/testing/validation/html/profile.png) | Pass: No errors |
| Sign up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/validation/html/signup.png) | Pass: No errors |
| Log in | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/validation/html/login.png) | Pass: No errors |
| Search | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2F8000-sasantazayo-suebensassi-813vyfvgjj0.ws.codeinstitute-ide.net%2Fproducts%2F%3Fq%3Dbook) | ![screenshot](documentation/testing/validation/html/search.png) | Pass: No errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| styles.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsue-bensassi-designs-beea48c7d401.herokuapp.com%2Fstatic%2Fcss%2Fstyles.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/testing/validation/css.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| buttons.js | ![screenshot](documentation/testing/validation/javascript/buttons.png) | Pass: No Errors |
| disableSubmit.js | ![screenshot](documentation/testing/validation/javascript/disablesubmit.png) | Pass: No Errors |
| dynamicMargin.js | ![screenshot](documentation/testing/validation/javascript/dynamicmargin.png) | Pass: No Errors |
| logoutModal.js | ![screenshot](documentation/testing/validation/javascript/logoutmodal.png) | Pass: No Errors |
| navbar.js | ![screenshot](documentation/testing/validation/javascript/navbar.png) | Pass: No Errors |
| newsletter.js | ![screenshot](documentation/testing/validation/javascript/newsletter.png) | Pass: No Errors |
| quantityInput.js | ![screenshot](documentation/testing/validation/javascript/quantityinput.png) | Pass: No Errors |
| scrollToTop.js | ![screenshot](documentation/testing/validation/javascript/scrolltotop.png) | Pass: No Errors |
| shoppingCartQuantities.js | ![screenshot](documentation/testing/validation/javascript/shoppingcartquantities.png) | Pass: No Errors |
| stripeElements.js | ![screenshot](documentation/testing/validation/javascript/stripeelements.png) | Undefined Stripe variable |
| toasts.js | ![screenshot](documentation/testing/validation/javascript/toasts.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| cart | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/cart/contexts.py) | ![screenshot](documentation/testing/validation/python/cart/contexts.png) | Pass: No Errors |
| cart | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/cart/urls.py) | ![screenshot](documentation/testing/validation/python/cart/urls.png) | Pass: No Errors |
| cart | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/cart/views.py) | ![screenshot](documentation/testing/validation/python/cart/views.png) | Pass: No Errors |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/admin.py) | ![screenshot](documentation/testing/validation/python/checkout/admin.png) | Pass: No Errors |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/forms.py) | ![screenshot](documentation/testing/validation/python/checkout/forms.png) | Pass: No Errors |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/models.py) | ![screenshot](documentation/testing/validation/python/checkout/models.png) | Pass: No Errors |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/signals.py) | ![screenshot](documentation/testing/validation/python/checkout/signals.png) | Pass: No Errors |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/urls.py) | ![screenshot](documentation/testing/validation/python/checkout/urls.png) | Pass: No Errors |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/views.py) | ![screenshot](documentation/testing/validation/python/checkout/views.png) | Pass: No Errors |
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/webhook_handler.py) | ![screenshot](documentation/testing/validation/python/checkout/webhook_handler.png) | Pass: No Errors |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/checkout/webhooks.py) | ![screenshot](documentation/testing/validation/python/checkout/webhooks.png) | Pass: No Errors |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/contact/admin.py) | ![screenshot](documentation/testing/validation/python/contact/admin.png) | Pass: No Errors |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/contact/forms.py) | ![screenshot](documentation/testing/validation/python/contact/forms.png) | Pass: No Errors |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/contact/models.py) | ![screenshot](documentation/testing/validation/python/contact/models.png) | Pass: No Errors |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/contact/urls.py) | ![screenshot](documentation/testing/validation/python/contact/urls.png) | Pass: No Errors |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/contact/views.py) | ![screenshot](documentation/testing/validation/python/contact/views.png) | Pass: No Errors |
| core | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/core/urls.py) | ![screenshot](documentation/testing/validation/python/core/urls.png) | Pass: No Errors |
| core | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/core/views.py) | ![screenshot](documentation/testing/validation/python/core/views.png) | Pass: No Errors |
| newsletter | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/newsletter/admin.py) | ![screenshot](documentation/testing/validation/python/newsletter/admin.png) | Pass: No Errors |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/newsletter/forms.py) | ![screenshot](documentation/testing/validation/python/newsletter/forms.png) | Pass: No Errors |
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/newsletter/models.py) | ![screenshot](documentation/testing/validation/python/newsletter/models.png) | Pass: No Errors |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/newsletter/urls.py) | ![screenshot](documentation/testing/validation/python/newsletter/urls.png) | Pass: No Errors |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/newsletter/views.py) | ![screenshot](documentation/testing/validation/python/newsletter/views.png) | Pass: No Errors |
| products | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/products/admin.py) | ![screenshot](documentation/testing/validation/python/products/admin.png) | Pass: No Errors |
| products | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/products/forms.py) | ![screenshot](documentation/testing/validation/python/products/forms.png) | Pass: No Errors |
| products | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/products/models.py) | ![screenshot](documentation/testing/validation/python/products/models.png) | Pass: No Errors |
| products | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/products/urls.py) | ![screenshot](documentation/testing/validation/python/products/urls.png) | Pass: No Errors |
| products | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/products/views.py) | ![screenshot](documentation/testing/validation/python/products/views.png) | Pass: No Errors |
| products | widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/products/widgets.py) | ![screenshot](documentation/testing/validation/python/products/widgets.png) | Pass: No Errors |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/profiles/forms.py) | ![screenshot](documentation/testing/validation/python/profiles/forms.png) | Pass: No Errors |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/profiles/models.py) | ![screenshot](documentation/testing/validation/python/profiles/models.png) | Pass: No Errors |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/profiles/urls.py) | ![screenshot](documentation/testing/validation/python/profiles/urls.png) | Pass: No Errors |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/profiles/views.py) | ![screenshot](documentation/testing/validation/python/profiles/views.png) | Pass: No Errors |
| sue_bensassi_designs | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/sue_bensassi_designs/settings.py) | ![screenshot](documentation/testing/validation/python/sue_bensassi_designs/settings.png) | Pass: No Errors |
| sue_bensassi_designs | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/sue_bensassi_designs/urls.py) | ![screenshot](documentation/testing/validation/python/sue_bensassi_designs/urls.png) | Pass: No Errors |
| sue_bensassi_designs | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/main/sue_bensassi_designs/views.py) | ![screenshot](documentation/testing/validation/python/sue_bensassi_designs/views.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/chrome.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/edge.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/firefox.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| desktop | ![screenshot](documentation/testing/desktop.png) | Works as expected |
| iPhone-SE | ![screenshot](documentation/testing/iPhone-SE.png) | Works as expected |
| iPhone-XR | ![screenshot](documentation/testing/iPhone-XR.png) | Works as expected |
| iPhone-12-Pro | ![screenshot](documentation/testing/iPhone-12-Pro.png) | Works as expected |
| iPhone-14-Pro-Max | ![screenshot](documentation/testing/iPhone-14-Pro-Max.png) | Works as expected |
| Pixel-7 | ![screenshot](documentation/testing/Pixel-7.png) | Works as expected |
| Samsung-Galaxy-S8+ | ![screenshot](documentation/testing/Samsung-Galaxy-S8+.png) | Works as expected |
| Samsung-Galaxy-S20-Ultra | ![screenshot](documentation/testing/Samsung-Galaxy-S20-Ultra.png) | Works as expected |
| iPad-Mini | ![screenshot](documentation/testing/iPad-Mini.png) | Works as expected |
| iPad-Air | ![screenshot](documentation/testing/iPad-Air.png) | Works as expected |
| iPad-Pro | ![screenshot](documentation/testing/iPad-Pro.png) | Works as expected |
| Surface-Pro-7 | ![screenshot](documentation/testing/Surface-Pro-7.png) | Works as expected |
| Surface-Duo | ![screenshot](documentation/testing/Surface-Duo.png) | Works as expected |
| Galaxy-Z-Fold-5 | ![screenshot](documentation/testing/Galaxy-Z-Fold-5.png) | Works as expected |
| Asus-Zenbook-Fold | ![screenshot](documentation/testing/Asus-Zenbook-Fold.png) | Works as expected |
| Samsung-Galaxy-A51-71 | ![screenshot](documentation/testing/Samsung-Galaxy-A51-71.png) | Works as expected |
| Nest-Hub | ![screenshot](documentation/testing/Nest-Hub.png) | Works as expected |
| Nest-Hub-Max | ![screenshot](documentation/testing/Nest-Hub-Max.png) | Works as expected |

## Lighthouse Audit

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3ASasanTazayoni%2FSue-bensassi-designs-CI-PP5%20label%3Abug&label=bugs)](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/SasanTazayoni/Sue-bensassi-designs-CI-PP5)](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/SasanTazayoni/Sue-bensassi-designs-CI-PP5)](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/SasanTazayoni/Sue-bensassi-designs-CI-PP5/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
