# XIMA
Excella Inventory Management App

###Concept
XIMA is a Wagtail proof of concept application to mock a company's product management process.

###Installation Instructions for Windows

First, I'd advise creating a virtual environment to work in with.
If you don't already have it installed, `pip install virtualenv`

Then, `virtualenv myenv` or choose your own name.

You'll need to activate it so `cd myenv/Scripts`, `. activate`

`cd ..` and then clone the repo:

SSH(recommended): `git clone git@github.com:nickoliver86/wagtail-xima.git`
HTTPS: `git clone https://github.com/nickoliver86/wagtail-xima.git`

`cd wagtail-xima`

`git pull`

`pip install -r requirements.txt`

At this point you should be able to run `python manage.py runserver 0.0.0.0:8000`
and visit localhost:8000 and get a functional, albeit bare version of XIMA.

###How to use this site

Since the backbone of this site is Wagtail, you'll need to access the admin console to add your content.

First, from the command line type `python manage.py createsuperuser` and follow the instructions.

You should now be able to visit localhost:8000/admin and sign in with your new superuser credentials.

While some of Wagtail's core functionality (images, document upload, etc.) is already available at this point, let's
start managing the content. You can build a homepage by selecting `Explorer` -> `Homepage` from the lefthand panel
and click `edit`.

To create an inventory item, again select `Explorer` -> `Homepage` and click `ADD CHILD PAGE` -> `Inventory Item`

Once you've entered in the content you wish to describe the inventory item with, select `Publish` from the dropup
menu at the bottom of the screen.

Once you're done adding content (Inventory Items), visit localhost:8000 again. You may now view a list of products
by selecting the Products tab from the nav bar.

Selecting the Inventory tab takes you to another list with the stocked quantities, sales info, etc.
Clicking the green plus sign next to any item on the inventory page allows you to order/stock more.

Clicking the Metrics tab shows you historical sales data for your products and updates in real time as products are
stocked and sold. 