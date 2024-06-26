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
| desktop | ![screenshot](documentation/testing/devices/desktop.png) | Works as expected |
| iPhone-SE | ![screenshot](documentation/testing/devices/iPhone-SE.png) | Works as expected |
| iPhone-XR | ![screenshot](documentation/testing/devices/iPhone-XR.png) | Works as expected |
| iPhone-12-Pro | ![screenshot](documentation/testing/devices/iPhone-12-Pro.png) | Works as expected |
| iPhone-14-Pro-Max | ![screenshot](documentation/testing/devices/iPhone-14-Pro-Max.png) | Works as expected |
| Pixel-7 | ![screenshot](documentation/testing/devices/Pixel-7.png) | Works as expected |
| Samsung-Galaxy-S8+ | ![screenshot](documentation/testing/devices/Samsung-Galaxy-S8+.png) | Works as expected |
| Samsung-Galaxy-S20-Ultra | ![screenshot](documentation/testing/devices/Samsung-Galaxy-S20-Ultra.png) | Works as expected |
| iPad-Mini | ![screenshot](documentation/testing/devices/iPad-Mini.png) | Works as expected |
| iPad-Air | ![screenshot](documentation/testing/devices/iPad-Air.png) | Works as expected |
| iPad-Pro | ![screenshot](documentation/testing/devices/iPad-Pro.png) | Works as expected |
| Surface-Pro-7 | ![screenshot](documentation/testing/devices/Surface-Pro-7.png) | Works as expected |
| Surface-Duo | ![screenshot](documentation/testing/devices/Surface-Duo.png) | Works as expected |
| Galaxy-Z-Fold-5 | ![screenshot](documentation/testing/devices/Galaxy-Z-Fold-5.png) | Works as expected |
| Asus-Zenbook-Fold | ![screenshot](documentation/testing/devices/Asus-Zenbook-Fold.png) | Works as expected |
| Samsung-Galaxy-A51-71 | ![screenshot](documentation/testing/devices/Samsung-Galaxy-A51-71.png) | Works as expected |
| Nest-Hub | ![screenshot](documentation/testing/devices/Nest-Hub.png) | Works as expected |
| Nest-Hub-Max | ![screenshot](documentation/testing/devices/Nest-Hub-Max.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Cart | ![screenshot](documentation/testing/lighthouse/cartmobile.png) | ![screenshot](documentation/testing/lighthouse/cart.png) | Some minor warnings |
| Checkout | ![screenshot](documentation/testing/lighthouse/checkoutmobile.png) | ![screenshot](documentation/testing/lighthouse/checkout.png) | Some minor warnings |
| Checkout success | ![screenshot](documentation/testing/lighthouse/checkoutsuccessmobile.png) | ![screenshot](documentation/testing/lighthouse/checkoutsuccess.png) | Some minor warnings |
| Contact | ![screenshot](documentation/testing/lighthouse/contactmobile.png) | ![screenshot](documentation/testing/lighthouse/contact.png) | Some minor warnings |
| Contact success | ![screenshot](documentation/testing/lighthouse/contactsuccessmobile.png) | ![screenshot](documentation/testing/lighthouse/contactsuccess.png) | Some minor warnings |
| About | ![screenshot](documentation/testing/lighthouse/aboutmobile.png) | ![screenshot](documentation/testing/lighthouse/about.png) | Some minor warnings |
| Delivery | ![screenshot](documentation/testing/lighthouse/deliverymobile.png) | ![screenshot](documentation/testing/lighthouse/delivery.png) | Some minor warnings |
| Index | ![screenshot](documentation/testing/lighthouse/indexmobile.png) | ![screenshot](documentation/testing/lighthouse/index.png) | Some minor warnings |
| Terms & conditions | ![screenshot](documentation/testing/lighthouse/termsmobile.png) | ![screenshot](documentation/testing/lighthouse/terms.png) | Some minor warnings |
| Products | ![screenshot](documentation/testing/lighthouse/productsmobile.png) | ![screenshot](documentation/testing/lighthouse/products.png) | Some minor warnings |
| Product detail | ![screenshot](documentation/testing/lighthouse/productdetailmobile.png) | ![screenshot](documentation/testing/lighthouse/productdetail.png) | Some minor warnings |
| Add product | ![screenshot](documentation/testing/lighthouse/addproductmobile.png) | ![screenshot](documentation/testing/lighthouse/addproduct.png) | Some minor warnings |
| Edit product | ![screenshot](documentation/testing/lighthouse/editproductmobile.png) | ![screenshot](documentation/testing/lighthouse/editproduct.png) | Some minor warnings |
| Profile | ![screenshot](documentation/testing/lighthouse/profilemobile.png) | ![screenshot](documentation/testing/lighthouse/profile.png) | Some minor warnings |
| Sign up | ![screenshot](documentation/testing/lighthouse/signupmobile.png) | ![screenshot](documentation/testing/lighthouse/signup.png) | Some minor warnings |
| Log in | ![screenshot](documentation/testing/lighthouse/loginmobile.png) | ![screenshot](documentation/testing/lighthouse/login.png) | Some minor warnings |
| Search | ![screenshot](documentation/testing/lighthouse/searchmobile.png) | ![screenshot](documentation/testing/lighthouse/search.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| All pages | | | | |
| | Click on Logo | Redirection to home page | Pass | |
| | Enter word into search bar that appears in at least one product's name or description and search | Redirection to Products page | Pass | Products filtered to only show products containing search term |
| | Enter word into search bar that doesn't appear in any product's name or description and search | Redirection to Products page | Pass | Products page is empty and shows user that 0 products were returned |
| | Enter nothing into search bar and search | Redirection to Products page | Pass | Error message shows and lets user know they entered nothing into the search bar and all products are displayed |
| | Click off of a toast | Dismisses the toast | Pass | |
| | Click on the home icon | Redirection to Home page | Pass | |
| | Click on the user icon (authenticated user) | Dropdown menu appears | Pass | Dropdown menu has a "Logout" link and a "My profile" link, super users also have the "Add product" link |
| | Click on "Add product" in the user icon dropdown menu as a super user | Redirection to Add product page | Pass | |
| | Click on "My profile" in the user icon the dropdown menu | Redirection to profile page | Pass | |
| | Click on "Logout" in the user icon the dropdown menu | Opens a modal | Pass | The modal is to confirm the log out |
| | Click "Yes" after opening the log out modal (above) | Closes the modal, logs the user out and redirects to the home page | Pass | |
| | Click "No" after opening the log out modal (above) | Dismisses the modal | Pass | |
| | Click on the user icon (non-authenticated user) | Dropdown menu appears | Pass | Dropdown menu has a "Register" link and a "Login" link |
| | Click on "Register" in the user icon the dropdown menu | Redirects to registration page | Pass | |
| | Click on "Login" in the user icon the dropdown menu | Redirects to login page | Pass | |
| | Click on cart icon | Redirects to cart page | Pass | |
| | Click on "All products" link | Dropdown menu appears | Pass | Dropdown menu has the links: "By Price", "By Name", "By Category" and "All products" |



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

## User Story Testing

| Epic | User Story | Screenshot |
| --- | --- | --- |
| EPIC 1: User Account Management | | |
| | As a new site user I can register and establish a personal account on the site so that I can make purchases using my own credentials. | ![screenshot](documentation/features/register.png) |
| | As a registered user I can log in to my account so that I can review products that I have purchased, view my order history and order products using my credentials. | ![screenshot](documentation/features/login.png) |
| | As a registered user I can log out of my account so that I can securely end my session and protect my personal information. | ![screenshot](documentation/features/logoutmodal.png) |
| | As a registered user/site admin I can reset my password so that I can regain access to my account in case I forget my password. | ![screenshot](documentation/features/pwresetrequest.png) |
| | As a registered user I can edit my account information so that I can ensure that my profile remains up to date and accurate. | ![screenshot](documentation/features/updateinfo.png) |
| EPIC 2: Product Exploration | | |
| | As a site user I can see a list of all products so that I can easily browse and explore the full range of available items. | ![screenshot](documentation/features/navbarlarge.png) |
| | As a site user I can see the price of a product clearly so that I can make a decision whether to purchase the item or not. | ![screenshot](documentation/features/productcard.png) |
| | As a site user I can view a product on its own individual page so that see more details about the product. | ![screenshot](documentation/features/productdetaillarge.png) |
| | As a site user I can sort products by category so that I can find specific products based on the category I select. | ![screenshot](documentation/features/productsdropdown.png) |
| | As a site user I can view a list of best-selling items so that I can easily discover popular products that are favoured by other customers, helping me make informed purchasing decisions. | ![screenshot](documentation/features/bestsellershowcase.png) |
| | As a site user I can view the stock count of products so that I can make informed purchasing decisions based on the availability of items. | ![screenshot](documentation/features/productcard.png) |
| EPIC 3: Shopping Experience | | |
| | As a site user I can add items to my cart so that I can conveniently gather desired products in one place while browsing in order to purchase. | ![screenshot](documentation/features/addtocart.png) |
| | As a site user I can adjust the quantity of items in my cart so that I can easily increase or decrease the number of items I wish to purchase. | ![screenshot](documentation/features/quantity.png) |
| | As a site user I can remove items from my cart so that I can refine my choices and ensure that my final purchase consists only of the items I truly intend to buy. | ![screenshot](documentation/features/removefromcart.png) |
| | As a site user I can view the items in my cart so that I can review my selected products, check quantities and verify prices before proceeding to checkout. | ![screenshot](documentation/features/cart.png) |
| | As a site user I can checkout with a card payment so that I can complete my purchase transaction securely and efficiently, providing my payment and shipping information to finalise the order and receive the products I have selected. | ![screenshot](documentation/features/checkout.png) |
| | As a site user I can receive an email which confirms my order after purchasing from the store so that I can review the details of my purchase and be reassured that my order was successfully processed. | ![screenshot](documentation/features/orderconfirmation.png) |
| | As a registered user I can access my order history so that I can review past purchases, track the status of my orders and keep a record of my transactions. | ![screenshot](documentation/features/orderhistory.png) |
| | As a site user I can use a search bar to search the website so that I can find a specific product. | ![screenshot](documentation/features/searchbar.png) |
| EPIC 4: Product Management (Admin) | | |
| | As a site admin I can set the stock count for each product so that I can accurately manage inventory levels, prevent overselling or stockouts and ensure that site users have access to up-to-date information on product availability. | ![screenshot](documentation/features/stockmanage.png) |
| | As a site admin I can add products to the store so that I can expand the range of available items and keep the product catalogue updated. | ![screenshot](documentation/features/addproductform.png) |
| | As a site admin I can edit the details of a specific product so that I can keep product information accurate and up to date. | ![screenshot](documentation/features/editproductform.png) |
| | As a site admin I can remove products from the store so that I can manage inventory effectively, removing discontinued or outdated items. | ![screenshot](documentation/features/deletemodal.png) |
| EPIC 5: Site Information | | |
| | As a new site user I can learn about the background of the merchant so that I can gain insight into the company's values and expertise, fostering trust and confidence in their products or services. | ![screenshot](documentation/features/about.png) |
| | As a site user I can access delivery information so that I can understand the shipping options, delivery times and any associated costs, enabling me to plan my purchases accordingly and ensure a smooth and timely delivery of my orders. | ![screenshot](documentation/features/delivery.png) |
| | As a site user I can view the terms and conditions so that I can understand the rules, regulations, and agreements governing the use of the platform, ensuring transparency and clarity in my interactions with the website. | ![screenshot](documentation/features/terms.png) |
| | As a site user I can easily find and access the store owner's contact information so that I can get in touch for inquiries or assistance. | ![screenshot](documentation/features/contact.png) |
| EPIC 6: Marketing and Engagement | | |
| | As a site user I can sign up for the site's mailing list so that I can receive special offers and updates in my inbox. | ![screenshot](documentation/features/newslettersuccess.png) |
| | As a site admin I can view my mailing list so that I can send special offers or news updates about my products to my subscribers. | ![screenshot](documentation/features/mailinglist.png) |
| | As a site admin I can a comprehensive list of customer enquiries so that efficiently address each one and manage my responses accordingly. | ![screenshot](documentation/features/contactadmin.png) |
| | As a site admin I can share the business on Facebook so that I can increase visibility and reach for the platform, attract new users and engage with existing ones on a popular social media platform, ultimately driving traffic to the site and potentially boosting sales and brand recognition. | ![screenshot](documentation/features/mockup-facebook.png) |
| | As a site admin I can use specific keywords on site pages so that I maximise the probability of new customers locating the store on a Google search. | ![screenshot](documentation/features/keywords.png) |
| EPIC 7: Additional Features | | |
| | As a site user I can see humorous fake items on the 404 error page so that I can enjoy a playful experience when encountering page errors. | ![screenshot](documentation/features/error404.png) |
| EPIC 8: User Experience and Interface | | |
| | As a new site user I can comprehend the website's purpose at a glance so that I can determine if the platform aligns with my needs and interests. | ![screenshot](documentation/features/hero.png) |
| | As a site user I can navigate through the interface effortlessly so that I can quickly and easily find the information I need. | ![screenshot](documentation/features/productsdropdown.png) |

The following are user stories I wasn't able to implement and have labeled as Wont Have in my MoSCoW prioritisation:

| User Story | Screenshot |
| As a site user I can filter products by price so that I can easily find items that fit within my budget. | n/a |
| As a site user I can receive notifications so that I am promptly informed about any special offers or discounts available on the website. | n/a |
| As a site user I can view product reviews so that I can make informed purchasing decisions by considering the experiences and opinions of other customers. | n/a |
| As a registered user I can submit a review for a product that I have previously bought so that I can share my experiences and opinions with other users. | n/a |
| As a registered user I can edit my review on a product so that I can update or improve the information I provided based on further experiences with the product. | n/a |
| As a registered user I can delete my review on a product so that I can remove outdated or inaccurate feedback. | n/a |

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
