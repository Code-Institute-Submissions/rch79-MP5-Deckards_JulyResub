# [Deckard's Bookstore](https://deckards.herokuapp.com/)

#### Your online source for science fiction books 

Check it out on [Heroku](https://deckards.herokuapp.com/)

------

Deckard's Bookstore is an online bookstore specialized in science fiction content. The site allows shoppers to browse the inventory based on book title or author name. Users can also browse looks for titles based on literary awards - ie, browse for Hugo or Nebula award winning books.  



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

  [INSERT LINK HERE]



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





Sources:

https://www.pexels.com/photo/woman-in-a-spacesuit-with-blue-helmet-7672255/  - Facebook profile photo



https://www.facebook.com/Deckards-Bookstore-103332569137719 - Facebook page







