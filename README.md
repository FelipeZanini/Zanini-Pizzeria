# _Zanini-Pizzeria_

The objective of my Zanini-Pizzeria restaurant website is to engage customers to our italian cusine, aiming actions such as reservations, menu information, and also the address and contact information. The site is made to be friendly user and enticing customers to choose the restaurant for culinary experiences.

The User can enjoy a fully responsive website, easily navigated that allow them, to manage their booking, canceling it or updating the date, that requires a account, but don't worry, the process to register and login is pretty straight foward, focusing in what matters, the beloved italian food.







  ![Mock Up](/img/mockup.png)

## Features

### Existing Features

- __Restaurant Land Page__
 
  - The initial web page is a eye catch to visitors, having the purpose to quickly capture the attention and instigate the curisioty, that could result in a reservation, or a quick look at the menu. It is well-designed including visually appealing images of the food and a great atmosphere, with an easy navigation to key sections like the menu, reservation system, and user section. The goal is to provide a positive and engaging first impression that motivates visitors to further explore the restaurant, the page contains a link to the reservation section.


  ![Land Page](/img/land-page.png)

- __Benvenuti Section__
 
  - The Benvenuti section contributes to a positive user experience by presenting information in a user-friendly manner, indroducing the customer to what would be their expericiences in the restaurant, providing information about our cusine and our way to take care of our customers, the page contains a link to the menu section.

  ![Benvenuti Section](/img/b-section.png)

- __Menu Section__

  - The menu section objective is to instigate customers with a visually appealing and informative presentation of our food and drinks options, facilitating the decision-making and enhancing the willing for our food, that section divede our menu in six categories, starters, main course, pizzas, desserts, drinks and beverages, hover over this caterogies to see the text information about the menu.

  ![Menu Section](/img/menu.png)

- __Menu Items Section__
 
  - The menu item describes in a concise way about key details, like it's prince, ingredients, and flavors to inform and attract customers, it is simple and straightforward.

  ![Menu Items Section](/img/m-i.png)

  - __Reservation Section__
 
    - The reservation area is designated to book tables for two, four or six persons, allowing user to choose from a range of time and dates, convenient experience, it's not an explicit mention at first, but is worth to coment, that user can just book one table per time.

  ![Reservation Section](/img/reservation.png)

- __User Page Section__
 
  - The user page Section is made to manage bookings and the user account itself, allowing the user to log out or even unregister from the site.
    
  ![User Page Section](/img/account.png)
    
  - The user also capable of delete the reservation, with one day before it and update the reservation at any time.
    
  ![User Page Section](/img/u-booking.png)

  - __Log In/ Register__
 
    - The login and register section is user-friendly and straightforward, allowing user to register and log in, once the user register he is log automatically.

  ![Log In/ Register](/img/login.png)

  ![Log In/ Register](/img/register.png)

  - __Models__
 
    - For this project only a single model has been made up, that is the Reservation model. This model is responsible for associating each booking with a specific customer. Additionally, it prevents double bookings and includes functionality to check if a table of a given size and at a specific time on a particular date is available(the restaurant just has two table of each size).
      - user, a one-to-one relationship with the built-in User model, it establishes a link between a reservation and a specific user.
      - date, a datefield to store the reservation date.
      - booking_time, representing the selected booking time from the choices provided in BOOKING_TIME(2pm, 3pm, 4pm, ..., 8pm).
      - table_size, representing the selected table size from the choices provided in TABLE_SIZE(2, 4 or 6 persons).
      - check_table_availability method, which queries the database to check if a table in a specific time and date is avaliable, if two reservations already exist for the same table, it returns false, indicating that the table is not available; otherwise, it returns true.
      -  str method provides a string representation of a reservation, displaying booking time, date, and table size.

  ![Log In/ Register](/img/modelss.png)

### Features Left to Implement

  - Allow the site admin to receive an email when a customer book a table.
  - Allow the customer to buy his food online, with.
    - Containing a payment methods.
    - Ways to check the delivery time and location.
  - Exclude the old data every two weeks.
  - A direct channel to contact the restaurant owner.
    

## Testing

  - I have tested the code by the following methods:
  - Passed on the Django test built in function, no issues found.
  - Passed on the validator code PEPE8, no issues found.
  - I manually tested the code, attempting to submit invalid inputs and reserve tables without prior registration, and double bookings as well.
  - The site was tested on Heroku terminal and on the local terminal.

## Validator Testing

  - No errors were returned when passing through the official [PEP8](https://pep8ci.herokuapp.com/) validator, used just in tested in all files, but just uploaded the models and views for simplicity purpose.
  
  - PEP8 Views.py.

  ![PEP8 Views](/img/viewpep.png)

  - PEP8 Model.py.

  ![PEP8 Model](/img/modelpep.png)

 - No errors were returned in Django built tests.

  ![Django Test](/img/testdajngo.png)

## Bugs

### Solved Bugs

  - At the beginning of my journey through this project I was very unused to the Django language, I had to learn more topics while I was doing the project, relying with a lot of help in web forum, but since I got  hang of, it was easy to write my code, the biggest problem is this project was the deployment to Heroku, it took me more than 4 days to solve all the errors that I was facing, such as bad requests, broken links etc, but I decided to user Cloudnary for my page images and White Sound for my static files, since I made that decision everytinh flowed as expected.

### Reaming Bugs
  
  - No bugs reaming

## Deployment

  - This project was deployed at Heroku, steps for deploy are listed bellow:
    - Fork or clone the repository.
    - Creat a new Heroku app.
    - Set up the configs for the deployment.
    - Set up the connection with PostgresSQL
    - Link the Heroku app to the repository, then Deploy.

    - The live link can be found here: [Zanini Pizzeria](https://zanini-pizzeria-0279eae282e5.herokuapp.com/)

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
  
  - I obtained the code for my datepicker from a solution on Stack Overflow.
    - [Stackoverflow code](https://stackoverflow.com/questions/14646008/jquery-datepicker-min-max-dates)
  - I got the source code of the template from open-source Bootstrap themes.
    - [bootstrap-theme](https://startbootstrap.com/theme/creative)
  - I also searched for solutions of the problems that occurred during the project development on the following websites:
    - [Stackoverflow](https://stackoverflow.com/)
    - [Geeksforgeeks](https://www.geeksforgeeks.org/)
    - [Freecodecamp](https://www.freecodecamp.org/news)
    - [Medium](https://medium.com/)
  - The Code Institute for the deployment terminal
