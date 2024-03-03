# _Zanini-Pizzeria_

The objective of my Zanini-Pizzeria restaurant website is to engage customers to our italian cusine, aiming actions such as reservations, menu information, and also the address and contact information. The site is made to be friendly user and enticing customers to choose the restaurant for culinary experiences.

The User can enjoy a fully responsive website, easily navigated that allow them, to manage their booking, canceling it or updating the date, that requires a account, but don't worry, the process to register and login is pretty straight foward, focusing in what matters, the beloved italian food.

  ![Mock Up](/static/assets/img/portfolio/thumbnails/mockup.png)

- The live link can be found here: [Zanfe](https://zanfe-009510b2eec0.herokuapp.com/)

# Author
Felipe Zanini Silva

# UX
The restaurant booking website provides a seamless user experience with intuitive navigation, comprehensive booking system, and easy reservation management. Users can quickly make reservations with real-time availability updates, the mobile-responsive design ensures accessibility across devices.

## User Stories
[Link to User Stories](https://github.com/users/FelipeZanini/projects/4/views/1)
## Frameworks
I decided to utilise Bootstrap for my website because it made it simple and quick for me to construct a responsive design that functions well across a range of devices.

## CRUD
<details>
<summary>CRUD Details</summary>

- **Booking:**
  
- Update Booking
  ![image](/static/assets/img/portfolio/thumbnails/Update-booking.png)

- Delete Booking
  ![image](/static/assets/img/portfolio/thumbnails/Delete-Booking.png)

- Delete Account
  ![image](/static/assets/img/portfolio/thumbnails/Delete-account.png)

</details>

## Features

### Existing Features

- __Restaurant Land Page__
 
  The initial web page is a eye catch to visitors, having the purpose to quickly capture the attention and instigate the curisioty, that could result in a reservation, or a quick look at the menu. It is well-designed including visually appealing images of the food and a great atmosphere, with an easy navigation to key sections like the menu, reservation system, and user section. The goal is to provide a positive and engaging first impression that motivates visitors to further explore the restaurant, the page contains a link to the reservation section.


  ![Land Page](/static/assets/img/portfolio/thumbnails/land-page.png)

- __Benvenuti Section__
 
  The Benvenuti section contributes to a positive user experience by presenting information in a user-friendly manner, indroducing the customer to what would be their expericiences in the restaurant, providing information about our cusine and our way to take care of our customers, the page contains a link to the menu section.

  ![Benvenuti Section](/static/assets/img/portfolio/thumbnails/benvenutti-section.png)

- __Menu Section__

  The menu section objective is to instigate customers with a visually appealing and informative presentation of our food and drinks options, facilitating the decision-making and enhancing the willing for our food, that section divede our menu in six categories, starters, main course, pizzas, desserts, drinks and beverages, hover over this caterogies to see the text information about the menu.

  ![Menu Section](/static/assets/img/portfolio/thumbnails/menu-section.png)

- __Menu Items Section__
 
  The menu item describes in a concise way about key details, like it's prince, ingredients, and flavors to inform and attract customers, it is simple and straightforward.

  ![Menu Items Section](/static/assets/img/portfolio/thumbnails/menu-items.png)

  - __Reservation Section__
 
    The reservation area is designated to book tables for two, four or six persons, allowing user to choose from a range of time and dates, convenient experience, it's not an explicit mention at first, but is worth to coment, that user can just book one table per time.

  ![Reservation Section](/static/assets/img/portfolio/thumbnails/book-section.png)

- __User Page Section__
 
  The user page Section is made to manage bookings and the user account itself, allowing the user to log out or even unregister from the site.
    
  ![User Page Section](/static/assets/img/portfolio/thumbnails/user-section.png)
    
  The user also capable of delete the reservation, with one day before it and update the reservation at any time.
    
  ![Same Day Cancellation](/static/assets/img/portfolio/thumbnails/same-day.png)

  - __Log In/ Register__
 
  The login and register section is user-friendly and straightforward, allowing user to register and log in, once the user register he is log automatically.

  ![Log In/ Register](/static/assets/img/portfolio/thumbnails/login.png)

  ![Log In/ Register](/static/assets/img/portfolio/thumbnails/register.png)

  - __Models__
 
    - For this project only a single model has been made up, that is the Reservation model. This model is responsible for associating each booking with a specific customer. Additionally, it prevents double bookings and includes functionality to check if a table of a given size and at a specific time on a particular date is available(the restaurant just has two table of each size).
    - user, a one-to-one relationship with the built-in User model, it establishes a link between a reservation and a specific user.
    - date, a datefield to store the reservation date.
    - booking_time, representing the selected booking time from the choices provided in BOOKING_TIME(2pm, 3pm, 4pm, ..., 8pm).
    - table_size, representing the selected table size from the choices provided in TABLE_SIZE(2, 4 or 6 persons).
    - check_table_availability method, which queries the database to check if a table in a specific time and date is avaliable, if two reservations already 
    exist for the same table, it returns false, indicating that the table is not available; otherwise, it returns true.
    - str method provides a string representation of a reservation, displaying booking time, date, and table size.

  ![Reservation Model](/static/assets/img/portfolio/thumbnails/reservation-model.png)

  ![Check table Model](/static/assets/img/portfolio/thumbnails/check-table.png)

### Features Left to Implement

  - Allow the site admin to receive an email when a customer book a table.
  - Allow the customer to buy his food online, with.
  - Containing a payment methods.
  - Ways to check the delivery time and location.
  - Exclude the old data every two weeks.
  - A direct channel to contact the restaurant owner.
    

## Testing

<details>

<summary>Testing</summary>

  I have tested the code by the following methods:
  - Passed on the Django test built-in function, no issues found.
  - Passed on the validator code PEPE8, no issues found.
  - I manually tested the code, attempting to visit pages forbidden for non-registered users.
  - I added a login required decorator in each function that just registered users can access.
  - I tested each button individually in different screen sizes, and no problems were found.
  - I inserted url to try to hack the site, but my code seems to be safe.
  - I started the secret variables in the protected virtual environment. 
  - The site was tested on the Heroku terminal and the local terminal.

  # Manual Testing

  The link to the manual tests can be found here: [TestCase](https://github.com/users/FelipeZanini/projects/11)

# Defects

  Defects were documented in github using a custom issue template: [Defects](https://github.com/FelipeZanini/Zanini-Pizzeria/issues/8)

# HTML Validator

<details>

- Base Template
![image](/static/assets/img/portfolio/thumbnails/base-html-errors.png)

- Home
![image](/static/assets/img/portfolio/thumbnails/index-base-html-errors.png)

- Menu
![image](/static/assets/img/portfolio/thumbnails/menu-errors-html.png)

- Menu Items
![image](/static/assets/img/portfolio/thumbnails/menu-items-html-errors.png)

- User Page
![image](/static/assets/img/portfolio/thumbnails/user-page-html-errors.png)

- Booking Page
![image](/static/assets/img/portfolio/thumbnails/book-table-html-errors.png)

- Booking Page
![image](/static/assets/img/portfolio/thumbnails/book-table-html-errors.png)

- Login 
![image](/static/assets/img/portfolio/thumbnails/login-html-errors.png)

- Register
![image](/static/assets/img/portfolio/thumbnails/register-page-html-errors.png)

</details>

# CSS Validator

<details>
- CSS Validator

![image](/static/assets/img/portfolio/thumbnails/css-validator.png)

</details>

# JavaScript Validator

<details>
- JavaScript Validator

![image](/static/assets/img/portfolio/thumbnails/JavaScript-validator.png)

</details>

# PEP8 Validator

<details>

- PEP8 Views
![image](/static/assets/img/portfolio/thumbnails/Python%20test%20views.png)

- PEP8 Models
![image](/static/assets/img/portfolio/thumbnails/Python%20model%20test.png)

- PEP8 Tests
![image](/static/assets/img/portfolio/thumbnails/tests%20python%20test.png)

- PEP8 Forms
![image](/static/assets/img/portfolio/thumbnails/test%20form%20python.png)

</details>

## Visual (UI) Testing: Cross Browser and Cross Device Testing 

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** | Passed 
|-----------------------------|------------------|---------|------------------|---------
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |Yes
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |Yes
| dev tools: Samsung S8+      | Chrome           | android | 360 x 740 px     |Yes
| dev tools: Pixel 6         | Chrome           | android | 393 x 851 px     |Yes
| dev tools: iPhone 14 Pro   | safari           | iOs     | 390 x 844 px     |Yes
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |Yes
| dev tools: Pixel Tablet   | Chrome           | android | 834 x 1075 px    |Yes
| dev tools: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |Yes
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |Yes
| browserstack                | Edge 113         | windows | 1440 x 672 px    |Yes

# Lighthouse Test

<details>

- Home
![image](/static/assets/img/portfolio/thumbnails/LH-HOME.png)

- Menu
![image](/static/assets/img/portfolio/thumbnails/LH-MENU.png)

- Menu Items
![image](/static/assets/img/portfolio/thumbnails/LG-MENU-ITEM.png)

- Booking Page
![image](/static/assets/img/portfolio/thumbnails/LH-BT.png)

- User Page
![image](/static/assets/img/portfolio/thumbnails/LH-USER.png)

- Login 
![image](/static/assets/img/portfolio/thumbnails/LH-LOGIN.png)

- Register
![image](/static/assets/img/portfolio/thumbnails/LH-RG.png)

</details>

# Wave Accessibillity Tool

<details>

- Contrast Home
![image](/static/assets/img/portfolio/thumbnails/contrast-home.png)

- Contrast Menu
![image](/static/assets/img/portfolio/thumbnails/contrast-menu.png)

- Contrast Menu Items
![image](/static/assets/img/portfolio/thumbnails/contrast-menu-items.png)

- Booking Page
![image](/static/assets/img/portfolio/thumbnails/CONTRAST-BT.png)

- User Page
![image](/static/assets/img/portfolio/thumbnails/CONTRAST-USER.png)

- Contrast Login
![image](/static/assets/img/portfolio/thumbnails/contrast-login.png)

- Contrast Register
![image](/static/assets/img/portfolio/thumbnails/contrast-register.png)


</details>


</details>
<hr>

## Technologies Used
Several technologies have been used to enable this website works:
| Technology               | Description                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Django                   | Django is the framework that has been used in the project, enables efficient development, database interactions and secure authentication.           |
| Python                   | Python is the core programming language that was used to write all of the code in this application, to make it fully functional.                     |
| JavaScript               | JavaScript was used to provide dynamic interactivity to the messages and enhancing the functionality of the  timepicker.                             |
| Bootstrap                | Bootstrap was utilized to ensure a responsive design.                                                                                                |
| Git                      | Git was utilized as the version control system for tracking changes, and maintaining the project's codebase.                                         |
| PostgreSQL               | PostgreSQL was employed as the relational database management system to store and manage the project's data.                                         |
| GitHub                   | Github was used as development environment, code management and tracking of changes.                                                                 |
| Font Awesome             | Font Awesome was used to obtain the icons of the website, enhancing the overall design.                                                              |
| Google Developer Tools   | DevTools was the primary toll for bug detection, testing the responsiveness and resolving issues across the website.                                 |
| Heroku                   | Heroku was used to deploy the website.                                                                                                               |
| CI's pep8                | CI's pep8 tool was used to validate all the python code.                                                                                             |
| Jigsaw                   | Jigsaw was used to validate CSS code.                                                                                                                |
| W3 HTML                  | W3 HTML was used to validate HTML code.                                                                                                              |
| Jshint                   | Jshint was used to validate JavaScript Code.                                                                                                         |
| AmIResponsive            | AmIResponsive was used to generate screenshots of the website in various device sizes, allowing for a quick visual assessment of its responsiveness. |
| Gitpod                   | Gitpod was used to write and edit the project code.                                                                                                  |diagrams.                                                                                                         |                                                                                                                                                                                                 |                                                                                           
### Languages
- HTML
- CSS
- Python
- JavaScript 

### Frameworks, Libraries & Programs Used
- Django
- Bootstrap
- Git 
- PostgreSQL
- GitHub
- Font Awesome
- Google Developer Tools
- Heroku
- W3 HTML
- AmIResponsive
- Gitpod

## Production Deployment
To deploy your application on Heroku, follow the steps bellow:

1. **Create a Heroku Account:**
- Visit the [Heroku](https://signup.heroku.com/login) website.
- Sign up for a free account or log in if you already have one.

2. **Create a New Heroku App:**
- Once you are logged in to your Heroku account, click on the "New" button and select "Create new app".
- Choose a unique name for your app. This name will be used in the App's URL.
- Select the region closest to your location for better performance.

3. **Connect the App to Your Git Repository:**
- After creating the app, go to the "Deploy" tab in your app's dashboard.
- Choose the deployment method based on your Git repository: (e.g. GitHub).
- Connect your app to the appropriate repository and branch.

4. **Configure Environment Variables:**
- In the "Settings" tab of your heroku app's dashboard, locate the "Config Vars" section.
- Set the necessary enviroment variables required for your aplication. 
- Click on the "Reveal Config Vars" button to add the key-value pairs for your enviroment variables:

- The live link can be found here: [Zanini Pizzeria](https://zanini-pizzeria-0279eae282e5.herokuapp.com/)

## Bugs

### Solved Bugs

  - At the beginning of my journey through this project I was very unused to the Django language, I had to learn more topics while I was doing the project, relying with a lot of help in web forum, but since I got  hang of, it was easy to write my code, the biggest problem is this project was the deployment to Heroku, it took me more than 4 days to solve all the errors that I was facing, such as bad requests, broken links etc, but I decided to user Cloudnary for my page images and White Sound for my static files, since I made that decision everytinh flowed as expected.

### Reaming Bugs
  
  - No bugs reaming

## Modules and Libraries:
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [JavaScript](https://www.javascript.com/)
- [Font Awesome](https://fontawesome.com/)
- [jQuery](https://jquery.com/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [AWS](https://aws.amazon.com/)
- [Stripe](https://stripe.com/ie)
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Media
- [Google Fonts](https://fonts.google.com/) - The fonts were sourced using Google Fonts.
- [Font Awesome](https://fontawesome.com/) - The icons was taken from Font Awesome.

## Credits:

  - The pictures in this document are sourced from open-access platforms and are provided below..
    - [Karolina Grabowska](https://www.pexels.com/photo/raw-garlic-on-white-marble-table-4197494/)
    - [Antoni Shkraba](https://www.pexels.com/photo/plants-with-green-leaves-against-white-background-5852289/)
    - [Karolina Grabowska](https://www.pexels.com/photo/delicious-fresh-ingredients-5386708/)
    - [Lisa Fotios](https://www.pexels.com/photo/selective-focus-photography-of-food-on-table-1126728/)
    - [Ofir Eliav](https://www.pexels.com/photo/set-of-various-delicious-desserts-served-in-plastic-container-7783241/)
    - [Valeria Boltneva](https://www.pexels.com/photo/close-up-photography-of-wine-glasses-1123260/)
    - [Eneida Nieves](https://www.pexels.com/photo/baked-pizza-on-pizza-peel-in-oven-905847/)
    - [Engin Akyurt](https://www.pexels.com/photo/food-photography-of-pasta-1438672/)
    - [Susanne Jutzeler](https://www.pexels.com/photo/assorted-juice-on-glass-bottles-1234079/)
    - [Julia Filirovska](https://www.pexels.com/photo/slices-of-meat-item-with-green-leaves-8251572/)

  - I got the source code of the template from open-source Bootstrap themes.
    - [bootstrap-theme](https://startbootstrap.com/theme/creative)
  - I also searched for solutions of the problems that occurred during the project development on the following websites:
    - [Stackoverflow](https://stackoverflow.com/)
    - [Geeksforgeeks](https://www.geeksforgeeks.org/)
    - [Freecodecamp](https://www.freecodecamp.org/news)
    - [Medium](https://medium.com/)
  
  - The Code Institute for the deployment terminal
