# [Deckard's Bookstore](https://deckards.herokuapp.com/)

#### Your online source for science fiction books 

Check it out on [Heroku](https://deckards.herokuapp.com/)

Follow us on [Facebook](https://www.facebook.com/Deckards-Bookstore-103332569137719)

------

Deckard's Bookstore is an online bookstore specialized in science fiction content. The site allows shoppers to browse the inventory based on book title or author name. Users can also browse looks for titles based on literary awards - ie, browse for Hugo or Nebula award winning books.  

![](https://github.com/rch79/MP5-Deckards/blob/main/media/main_page_snapshot.png?raw=true)

## Features

- Browsing based on book title or author
- Browsing based on literary awards, such as Hugo Awards, Nebula etc
- User profiles with order history and default shipping address
- Safe credit and debit card transactions using the Stripe API
- New account confirmations via email
- Administrative access for store maintenance (add, edit or remove books, authors, literary awards)
- Administrative access for site maintenance
- Static and media file hosting on AWS



## Business Model

Deckard's is Business to Customer (B2C) retail shop 

- **Target Audience**:  Science-fiction readers
- **Available Products**: Science-fiction (physical) books 
- **Payment Method**: Credit / Debit card transactions (via Stripe API)



**Features**: 

- Search functionality
- Sorting
- Filtering (by author or literary award)
- Order notifications
- User Profiles
- Mailing list signup



***Database***: Product details are stored in a Postgres database with the following available models:

- Model: **Author** - Used for storing author information

  - Model Fields:

    - **Name**: Author name, using underscore as a separator (ie, kurt_vonnegut)

    - **Friendly Name**: A user-friendly, formatted version of the name, useful for displaying on the website (ie Kurt Vonnegut)

    - **Sort Name**: Used for sorting purposes (ie, Vonnegut, Kurt)

    - **Bio**: Used to store biographical information about the author

      

- Model: **Book** - Used for storing book information

  - Model Fields:

    - **Author**: Book author. This is a foreign key that links the book model to an author model

    - **ISBN**: ISBN of the book

    - **Title**: Book title (ie, The Long Goodbye)

    - **Sort title**: Used for sorting purposes (ie, Long Goodbye, The)

    - **Year**: Year book was published

    - **Pages**: Number of pages

    - **Price**: Book price

    - **Rating**: book rating

    - **Rating Count**: Number of ratings

    - **Plot**: A detailed description of the plot of the book

    - **Description**: A short, spoiler-free summary of the story

    - **Image URL**: Link to an URL containing an image associated with the book

    - **Image**: An image file containing the book cover

      

- Model: **Award** - Used for storing literary award details

  - Model Fields:

    - **Name**: Name of the literary award (ie, hugo_awards, nebula_awards)

    - **Friendly Name**: A user friendly name of the award (ie, Hugo Awards, Nebula Awards)

    - **Sort Name**: Used for sorting purposes

    - **Description**: A description / bio of the literary award

    - **Books**: Books that won the award that are available in the store - links to the AwardDetails model

      

- Model: **Award Details** - Used for storing literary award details for a given book:

  - Model Fields:
    - **Book**: Title of the book - this links to the Book model
    - **Award**: Name of the literary award - this links to the Award model
    - **Award Year**: Year when the book was awarded
    - **Category**: Category of the award (ie, best book, best author etc)

- Database Diagram:

  ![](https://raw.githubusercontent.com/rch79/MP5-Deckards/ee13a500bf471ffb940bca84278df00573cb6c0d/media/database_diagram.PNG)



## User Stories - Customers:

- Signup for a new account: As a customer I would like to signup for a new account
- Login: As a customer I would like to login to the website to access my profile
- View products: As a customer I would like to view the books available for purchasing
- Add books to shopping cart: As a customer I would like to add books to my shopping cart
- Remove books from shopping cart: As a customer I would like to remove books from my shopping cart
- Purchase history: As a customer I would like to view my purchase history
- Finalize purchase: As a customer I would like to pay for the items in my shopping cart
- Search website: As a customer I would like to search the website
- Reset password: As a customer I would like to reset my password
- Change item quantity in my shopping cart: As a customer I would like to change the item quantity on my shopping cart

### Testing  Customer user stories:

| User Story                                                   | Test                                                         | Result                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| As a customer I would like to signup for a new account       | Click on Login / Register link on the upper right corner  -- Click on Register link  --  Fill out  required information  and submit -- Click on link included in verification email to activate account | Working as expected                                          |
| As a customer I would like to login to the website to access my profile | Click on Login / Register link on the upper right corner -- Enter username or email address and password and click on Sign In | Working as expected. User is redirected to the main page and the Login / Register link is replaced with user's username |
| As a customer I would like to view the books available for purchasing | Click on Books on the top navbar, and choose the sorting option | Working as expected                                          |
| As a customer I would like to add books to my shopping cart  | Click on the book to be added to the cart -- choose the selected quantity -- and click on Add to Bag | Working as expected. Book is added to the shopping cart      |
| As a customer I would like to remove books from my shopping cart | Click on the Shopping Bag link on the upper right corner -- click on the red trash can | Working as expected. Book is removed from the shopping bag   |
| As a customer I would like to pay for the items in my shopping cart | Click on the Shopping Bag link on the upper right corner -- Click on Secure Checkout -- fill out form with required information -- Click on Complete Order | Working as expected - User is redirected to an order details page and is notified that the purchase has been successful |
| As a customer I would like to view my purchase history       | Click on the username link on the upper right corner -- Click on My Profile | Working as expected -- Order History is displayed on the right half of the screen. Clicking on the order number will take the user to the order details page |
| As a customer I would like to search the website             | Enter the search parameter on the search bar at the top of the screen | Working as expected - search results are displayed on the screen |
| As a customer I would like to reset my password              | Click on Login / Register link on the upper right corner -- Click on the Forgot Password? link -- Enter account email address -- Click on password reset link received via email -- Enter new password | Working as expected - Email with a password reset link is sent to the customer |
| As a customer I would like to change the item quantity on my shopping cart | Click on the shopping bag link on the upper right corner -- change the item quantity using the '+' or '-' buttons | Working as expected. Item quantity changes accordingly. If quantity is set to 0 or less item is removed from shopping bag |



## User Stories - Site Admin:

- Add new books to the store: As a site admin I would like to add new books to the store
- Delete books from the store: As a site admin I would like to delete books from the store
- Edit existing books in the store: As a site admin I would like to edit existing books in the store
- Add a new author to the store: As a site admin I would like to add a new author to the store
- Delete an author from the store: As a site admin I would like to delete authors from the store
- Edit an existing author in the store: As a site admin I would like to edit an existing author in the store
- Add new literary award to the store: As a site admin I would like to add a new literary award to the store
- Delete literary award from the store: As a site admin I would like to delete a literary award from the store
- Edit existing literary awards in the store: As a site admin I would like to edit existing literary awards in the store
- Add literary award details to a book - As a site admin I would like to add literary award details to a book
- Delete literary award details from book - As a site admin I would like to delete literary award details from a book
- Edit existing literary award details - As a site admin I would like to edit existing literary award details

**Testing Site Admin user stories**:

| User Story                                                   | Test                                                         | Result                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| As a site admin I would like to add new books to the store   | Click on Store Admin link on the top nav bar  -- Click on Add Book OR click on Books link on the top navbar -- Select sorting option -- Add a Book link -- Fill out form with required information -- Click on Add Book | Works as expected. New book is added to the database and displayed on the products page |
| As a site admin I would like to delete books from the store  | Click on Books link on the top navbar -- Select sorting option -- Click on the Delete button displayed below the cover image of the book to be deleted | Works as expected -- book is deleted from the database and no longer displayed on the site |
| As a site admin I would like to edit existing books in the store | Click on Books link on the top navbar -- Select sorting option -- Click on the Edit button displayed below the cover image of the book to be edited -- Make desired changes and click on Update Book | Works as expected - existing book is updated with the new information |
| As a site admin I would like to add a new author to the store | Click on Store Admin link on the top nav bar -- Click on Add an Author Link OR Click on Authors link on the top navbar -- Click on Add an Author link -- Fill out form with required information -- Click on Add Author | Works as expected. New author is added to the database and displayed on the authors page |
| As a site admin I would like to delete authors from the store | Click on Authors link on the top navbar -- Click on the Delete button displayed next to the name of the author to be deleted | Works as expected -- author is deleted from the database and no longer displayed on the site |
| As a site admin I would like to edit an existing author in the store | Click on Authors link on the top navbar  -- Click on the Edit button displayed next to the name of the author to be edited -- Make desired changes and click on Update | Works as expected - existing author is updated with the new information |
| As a site admin I would like to add a new literary award to the store | Click on Store Admin link on the top nav bar  -- Click on Add an Award OR click on Awards link on the top navbar -- Click on Add an Award link -- Fill out form with required information -- Click on Add Award link | Works as expected. New award is added to the database and displayed on the awards page |
| As a site admin I would like to delete a literary award from the store | Click on Awards link on the top navbar -- Click on the Delete button displayed next to the name of the literary award to be deleted | Works as expected -- literary award is deleted from the database and no longer displayed on the site |
| As a site admin I would like to edit existing literary awards in the store | Click on Awards link on the top navbar  -- Click on the Edit button displayed next to the name of the literary award to be edited -- Make desired changes and click on Update | Works as expected - existing literary award is updated with the new information |
| As a site admin I would like to add literary award details to a book | Click on Store Admin link on the top nav bar  -- Click on Add Award Details to a Book  -- Fill out form with required information -- Click on Add Award Details link | Works as expected. New award details are added to the database and displayed on the respective literary award page |
| As a site admin I would like to delete literary award details from a book | Click on Awards link on the top nav bar -- Click on the literary Award you wish to edit -- Click on the Delete button next to the award details to be deleted | Works as expected -- literary award details are deleted from the database and no longer displayed on the site |
| As a site admin I would like to edit existing literary award details | Click on Awards link on the top nav bar -- Click on the literary Award you wish to edit -- Click on the Edit button next to the award details to be deleted | Works as expected - existing award details are updated with the new information |



## Testing Site Functionality:

| Functionality                                                | Test                                                         | Result                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Signup and login pages should only be available to anonymous users | Paste the URLs of the signup and login pages on the browser address bar while authenticated | Works as expected - user is redirected to the main page of the site |
| Profile, shopping cart and checkout pages should only be available to authenticated users | Paste the URLs of the shopping cart, profile and checkout pages on the browser address bar while not authenticated on the site | Works as expected. Browser is redirected to the login page   |
| Admin pages should only be available to superusers           | Paste the URLs of the admin pages on the browser address bar while authenticated as a non-superuser | Works as expected. User is redirected to the main page of the website |
| Users who attempt to access a non-existing page should be redirected to a custom 404 page | Enter an invalid URL on the browser navbar with the Django DEBUG environment variable set to False | Works as expected. User is redirected to a custom 404 page   |
| Adding a zero or negative quantity of an item to the shopping bag should not be possible | Use the '-' button to change the item quantity to a zero or negative amount before clicking on the Add to Bag link | Works as expected - A message indicating that only a quantity of no less than 1 can be added and the item is not added to the shopping bag |
| The quantity of an item already added to the shopping bag cannot be edited to a zero or negative amount | In the Shopping Bag view, use the '-' button to change the item quantity to a zero or negative amount | Works as expected - if the quantity is changed to zero or less the item is removed from the shopping bag |
| New users should be sent an email with a link to validate their email address upon creating a new account | Create a new account using the Signup link on the top right corner. An email should be sent to the new user's email address with a link to validate it | Works as expected. Email is sent via GMail using SMTP and the new account is successfully created once the user clicks on the validation link |
| Shoppers should receive a confirmation email after successfully making a purchase | Make a purchase on the website                               | Works as expected. Email is successfully sent to the shopper's email address  via GMail using SMTP |
| Users should receive a password reset email when clicking on the Forgot Your Password? link | Click on the Forgot Your Password? link on the Login page and enter the email address | Works as expected. Password reset link is sent to the user's email address. Password is successfully reset after the user clicks on the link |



## Technologies Used:

### Programming Languages:

- Python
- JavaScript

### Other Languages:

- HTML
- CSS

### Applications and Platforms:

- [Django](https://www.djangoproject.com/) - *Django* is a high-level *Python* web *framework* that encourages rapid development and clean, pragmatic design
- [Gitpod](https://www.gitpod.io/) - A Container-based development platform
- [Typora](https://typora.io/) - Markdown Editor
- [Amazon Web Services (AWS)](https://aws.amazon.com/): Static and media file hosting
- [PostgreSQL](https://www.postgresql.org/):  Free and open-source relational database management system
- [Stripe](https://stripe.com/ie): A suite of APIs powering online payment processing
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/): Controls the rendering behavior of Django forms
- [psycopg2](https://pypi.org/project/psycopg2/): PostgreSQL adapter for the Python programming language
- [Gunicorn](https://gunicorn.org/): A Python WSGI HTTP Server for UNIX
- [dj-database-url:](https://pypi.org/project/dj-database-url/) Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application
- [Mailchimp](https://mailchimp.com/): A marketing, automation & email marketing platform
- [XML-Sitemaps:](https://www.xml-sitemaps.com/) Online sitemap.xml generator



## Deployment:

The program was deployed on Heroku, using the following steps:

- Create an account on Heroku
- On the user account page, click on "new", and "Create new app"
- On the "Resources" tab, navigate to "Add-ons":
  - Click on "Find more add-ons"
  - On the search bar on the top right corner of the screen, type "Heroku Postgres"
  - Click on the Heroku Postgres badge, then click on "Install Heroku Postgres"
- On the "Settings" tab, navigate to "Config Vars":
  - Click on "Reveal Config Vars"
  - Ensure that the following environment variables are added:
    - AWS_ACCESS_KEY_ID   -> obtained from AWS 
    - AWS_SECRET_ACCESS_KEY  -> obtained from AWS
    - DATABASE_URL  -> The URL for the Postgres database
    - DISABLE_COLLECTSTATIC  -> Set to 1 or 0. If set to 0 Heroku will automatically upload your static files to the your static file hosting service of choice (AWS, in this case). This process can also be done via CLI
    - EMAIL_HOST_PASSWD  -> Password for the email service being used to send emails to site users (GMail, in this case)
    - EMAIL_HOST_USER  -> Email address being used to send emails to site users
    - SECRET_KEY  --> Django secret key. Generated when a new Django project is created and shown on the project's settings.py file
    - STRIPE_PUBLIC_KEY  --> Obtained from Stripe
    - STRIPE_SECRET_KEY  -> Obtained from Stripe
    - STRIPE_WH_SECRET -> Obtained from Stripe
    - USE_AWS --> If set to True, Heroku will look for static and media files on the file hosting service of choice (AWS in this case)
- Still on the settings tab, navigate to Buildpacks:
  - Click on "Add buildpack"
  - Select Python
  - Save changes
- Deploy tab:
  - Deploy method: GitHub
  - Click on "Connect to GitHub"
  - Select the repository for the program being deployed
  - Click on "connect"
  - Select one of the following options:
    - Automatic deploy: Heroku will rebuild the app every time a change is pushed to the GitHub repository
    - Manual deploy: Heroku will only rebuild the app when the user chooses to do so.
- Required Python dependencies were added to the "requirements.txt"  file using the "pip freeze > requirements.txt" CLI command on Gitpod. This file is used by Heroku to install the dependencies used in the  program



## Sources: 

- Facebook Business Page profile photo: https://www.pexels.com/photo/woman-in-a-spacesuit-with-blue-helmet-7672255/
- Background photo on the main page: https://pixabay.com/photos/city-urban-future-technology-6885193/
- SFGram dataset (book covers, author bio, book details): https://github.com/nschaetti/SFGram-dataset
- Code based on the [Code Institute Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)









