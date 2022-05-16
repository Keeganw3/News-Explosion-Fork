# My Daily Scheduler
## Project Description
<p> My Daily Scheduler is a command line application to help you plan out what you would like to do in a day no matter what that may be!

The user can input all the activities they would like to do and the application will give them back to the user in a list for them to do as they please.

This project is a multiple choice quiz that is for people of all ages designed to test their trivia knowledge. The idea was based on the show from the 80s, Who Wants To Be a Millionaire. It focuses on general knowledge and contains questions that were asked in the show that scale with difficulty as the player gets through each question. This might encourage people to go back and look at the show to see how it became so well known.
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
## Welcome Screen
* The user is told what the program is and how to use it. After they hit enter it shows the main menu where the user is given all the options for what they can do with the daily planner in a straightforward and easy to read format.

![Screenshot](/assets/screenshots/welcome_screenshot.jpg)

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
* Gitpod - Used as a platform for writing code. The command line commits and pushes to GitHub.
* GitHub - Hosts this repository.

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
* The questions were taken from https://inews.co.uk/light-relief/quizzes/who-wants-to-be-a-millionaire-questions-quiz-jackpot-441100

## Media
* Logo image came from https://www.google.com/url?sa=i&url=https%3A%2F%2Fstore.steampowered.com%2Fapp%2F1356240%2FWho_Wants_To_Be_A_Millionaire%2F&psig=AOvVaw2253bvTyPXLqaWtEODyEyK&ust=1640120680651000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJig1Oej8_QCFQAAAAAdAAAAABA2