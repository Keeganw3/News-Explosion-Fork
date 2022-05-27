<h1 align="center">News Explosion</h1>

## Project Description
<p> This project is an news sharing application based around people sharing news they care about and hearing other people's thoughts.

The average user can view all posts and if they make an account they can to comment on posts.

Admins can make posts on topics they care about or want to share news on. They can also comment on any posts and approve comments whenever a user with an account makes one. 
</p>

# UX
## User Stories

## Strategy

## Scope

## Structure

## Skeleton
(Include wireframes and er diagrams. Could move this to design and make different sections.)

## Surface
(Mention color scheme)

# Features
## Existing Features
## Navigation Bar
* The navigation bar is provided at the top of the webpage to allow the user to easily explore the website and maintains a consistent look on across the website. The nav bar contains links to the home, login and registration pages when a user is not logged in. If a user is logged in a link for logging out replaces these links.

![Navbar Logged Out](/static/images/pp4-navbar-screenshot1.png)

![Navbar Logged In](/static/images/pp4-navbar-screenshot2.png)

## Main Menu
* The first 4 options are suggestions for their schedule and option 5 lets the user make their own option. The user can leave the program when they're on the menu by clicking 6.
![Screenshot](/assets/screenshots/main_menu_screenshot.jpg)

* When an option is chosen and placed in the list it is displayed a line space away from the choices to give the user better readability. The user will always be shown their current list everytime a task has been added to it. 
![Screenshot](/assets/screenshots/list_screenshot.jpg)

## Main Menu Validator
* The user is asked to enter a number from 1-6. If they use a number outside of this range an error is displayed which asks the user to pick a number within this range.
![Screenshot](/assets/screenshots/incorrect_num_screenshot.jpg)

* The user is given a similar response if they submit a letter instead of a number.
![Screenshot](/assets/screenshots/incorrect_variable_screenshot.jpg)

## User created options
* The user can make their own options to be added into their list plans for the day. The user can do this as many times as they want and the input can be as long as they desire to give full flexibility to the user.
![Screenshot](/assets/screenshots/create_options_screenshot.jpg)
 
* The user can exit this screen by typing 'exit'. This will not affect the user's list and they will be returned to the main menu. This gives the user a chance to go back to the main menu if they didn't mean to come to this screen.
![Screenshot](/assets/screenshots/exit_create_options_screenshot.jpg)

## Exiting Daily Planner
* Once the list has 3 tasks in it, the user is prompted to exit the daily planner by hitting "y" or "n". If they enter another key the code will tell them they hit the wrong key and ask them to put in "y" or "n". "y" or "n" can be put in with spaces or as capital letters to give the user more flexibilty when using the app.
![Screenshot](/assets/screenshots/exit_planner_screenshot.jpg)

* If they hit "y", they will leave the planner. They will have to hit enter to get to the End Results screen.
![Screenshot](/assets/screenshots/y_exit_planner_screenshot.jpg)

* If they hit "n" they can add another task and will be asked if they want to leave again every time they add a new task. They will have to hit enter once again to return to the main menu.
![Screenshot](/assets/screenshots/n_exit_planner_screenshot.jpg)

## End Results Screen
* This screen displays the full schedule that the user has made up for the day in a list so it is clearly visible and easy to find once you are done with the app.
![Screenshot](/assets/screenshots/end_results_screenshot.jpg)

# Future Features to be added 
## Time Allotments
* I would ike the user to be able to set these tasks to go on for a set amount of time to allow them to better plan out their day. They could also set a start and end time and try to work within these confines.

## Improved UI of End Results Screen
I would like the final display of the user's daily plan to be displayed one at a time on a line instead of all together in the list. I tried to make this a couple times but couldn't figure it out before submission.

# Technologies Used
* HTML - A mark-up language that uses semantic structures.
* CSS - Cascade style sheets are used to style the quiz and website.
* Javascript - Programming language used to make the quiz.
* Python - Programming language used to create the databases, models and views for this website.
* Gitpod - Used as a platform for writing code. The command line commits and pushes to GitHub.
* GitHub - Hosts this repository.
* Heroku - Cloud platform used to run this application.
* Flask - Used to make working with Python easier and faster.
* Django - Used for importing frameworks that sped up making the website.
* Cloudinary - Used to display the images used on the website indefinitely.

## Programs Used
* lucid.app: used to create the flowchart for this project.
screenshot()(detail?)
* Git: used for creating the code for this project and sending it to GitHub.
* GitHub: a repository for the code after being made in Git.
* Heroku: used to deploy the application and hosts a page for the code.

## Design
* W3C HTML Validator - For cleaning and correcting HTML code.
* CSS Validator - For cleaning and correcting CSS code.
* JSHint - For cleaning and correcting Javascript code.
* Google Chrome Dev Tools - Used for Lighthouse to check and improve the website's accessability.
* WCAG Contrast Checker - For choosing accessible colours.
* Grammerly - For checking spelling and grammer.

# Testing
## Validator Testing
### HTML
* No errors or warnings were found through W3C validator.
### CSS
* No errors or warnings were found through the W3C CSS validator and I was given the code for this icon to prove this.
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!"/>
    </a>
</p>

### Javascript
* JSHint returned no errors although it gave warnings that score isn't defined in the results function. This was used instead of correct which is equal to the same object. score.innertext was used instead because calling the correct from the checkAnswer function didn't work.

## Accessibility Testing
This is a screenshot taken from doing an accessibility test on Developer Tools Lighthouse.

![Screenshot](/assets/screenshots/accessibility-screenshot.png)


## Manual Testing
I tested the media queries by manually adjusting the screen size from roughly 500-1000px to make sure the correct changes were taking place above or below each specific screen size.

For media queries, 768px, 500px, and below the text across the website is shrunk to maintain a clear structure on smaller screens and the logo was slightly adjusted. Media queries at sizes larger than this were only needed for the reset button to stay centred because the rest of the website was able to fill out the screen at these sizes well.

When checking the app on mobile I noticed that the font size was too large for both the header and questions making it so the user would need to scroll right to see the full question. This was fixed by shrinking the size of the text by 10%.

## Usability Testing
After I deployed this site I had friends and family test the usability of the website.

The first user asked to be able to see which question they were on. This was fixed by placing the question number in each question's text.

Another user asked for a way to restart the quiz at any time while they're going through it. This was addressed by adding a reset button above the question to make it easy for the user to see.

### What I think a user may have wanted:
* A way to keep track of the number of correct answers - added a scoreboard
* A way of knowing which button the user was on - added this by making buttons change colour when a mouse hovers over it.
* A confirmation for when an answer for a question is chosen - added an alert that comes up for each question when an answer is clicked.
* A way to view their results - added an alert at the top of the page telling them how well they did.
* A way to contact the site owner if they discover a bug - added a footer with relevant contact information.

## Known Bugs
When creating an option to be used the code will ask you for it twice. This doesn't happen if exit is used the first time the user is asked but if it is used when prompted the second time it will add this to the list. Using exit the first time won't add it to the list. I couldn't figure out why this problem happened.

# Deployment
This app was deployed using Heroku.
* Log into Heroku and make an account.
* In your gitpod code create a file called "requirements.txt" and add all of your code's dependencies to it.
* Go back to Heroku and click create new app. This app must have a unique name and a region.
* Now go to the Settings tab and scroll down to the Config Vars section. You will see two inputs called key and value.
* For the first key put CREDS and paste the contents of creds.json into value. 
* For the second key put PORT and "8000" into value.
* Scroll furthur down on this tab to Buildpack. 
* Click 'add Buildpack' and select Python. Do this again and select Node.js. Make sure Python is first and Node.js is second or it could affect your code.
* Go to the Deploy tab and you will see the deployment method, click Github. Enter the name of your repository and you will be given a list of the closest names that resemble what you have typed, click the one you want for this app.
* Scroll down to the Automatic Deploys section and click automatic deploy. This will make the app update to launch the latest cade that was pushed to Github everytime it is opened.
* You can also use Manual Deploy if this is the final version of your code.  
* Click Open App in the top right of the screen and the app should run.

## Forking
* Log into Github
* Load up the required repository.
* In the top right of the screen below the profile icon there is a fork button, click this.
* The repository should now be copied onto your Github account.

## Cloning
* Log into Github and choose a repository.
* Click on the green code button.
* You will be given three ways to clone the code. If you're using https, click “Clone with https” and copy the link.
* Open the terminal and type in the command "git clone" followed by a space and the copied url.
* The repository will now be cloned onto the computer.

# Acknowledgements
## Credits
* My mentor Brian Macharia who supported me and provided me with both feedback and solutions to problems I faced while creating the website.
* My lecturer Simen Daehlin helped me to better write my code to solve a couple of problems I had run into.
* The people from Slack who answered my questions when I needed them to.
* Code institute for the classes, sources, and tutors that they provided me.
* The people at student support who tried to help me for several hours.
* Bootstrap for the media query sizes that I used: https://getbootstrap.com/docs/4.1/layout/overview/

## Content
* The placeholder text and image used in Post 1 about Halo were taken from https://www.pcgamer.com/the-halo-tv-series-has-absolutely-no-vibes/
* The placeholder text and image used in Post 2 about Dr Strange were taken from https://collider.com/doctor-strange-2-multiverse-of-madness-weekend-box-office-61-million/#:~:text=Doctor%20Strange%202%20opened%20to,Doctor%20Strange%20(%24232%20million).
* The placeholder text and image used in Post 3 about Johnny Depp were taken from https://www.nbcnews.com/pop-culture/pop-culture-news/johnny-depp-amber-heard-defamation-trial-summary-timeline-rcna26136
* The placeholder text and image used in Post 4 about covid affecting the elderly were taken from https://www.rte.ie/news/regional/2022/0520/1300146-ulster-covid/
* The placeholder text and image used in Post 5 about stress and anxiety in healthcare workers were taken from https://www.irishtimes.com/news/health/rising-number-of-healthcare-professionals-experiencing-stress-anxiety-burnout-1.4883048

## Media
* Placeholder image came from https://previews.123rf.com/images/sylverarts/sylverarts1710/sylverarts171000610/87432790-las-noticias-y-los-hechos-que-divulgan-el-logotipo-del-vector-compuso-usando-la-inscripci%C3%B3n-de-las-n.jpg
* Post 1's image came from https://cdn.mos.cms.futurecdn.net/pGyDmdniqHURMK2tN3Kh56-970-80.jpg.webp
* Post 2's image came from https://static1.colliderimages.com/wordpress/wp-content/uploads/2022/05/doctor-strange-2-multiverse-of-madness-review-feature.jpg?q=50&fit=contain&w=1500&h=&dpr=1.5
* Post 3's image came from https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/rockcms/2022-04/220427-johnny-depp-amber-heard-se-1207p-715327.jpg
* Post 4's image came from https://img.rasset.ie/001bc448-800.jpg
* Post 5's image came from https://www.irishtimes.com/polopoly_fs/1.4883047.1652971327!/image/image.jpg_gen/derivatives/box_620_330/image.jpg