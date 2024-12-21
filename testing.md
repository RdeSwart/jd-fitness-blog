
Feature: | Action: | Expected Result: | Pass/Fail:
:------ | :------ | :------ | :------
<ins>Landing Page</ins> | Enter https address | Renders Home Page | Pass
<ins>Blog Posts</ins>| On Home page | Lists the published blogs| Pass
<ins>Read More Button</ins>| Click "Read More" on blog| Renders full blog post| Pass
<ins>Category</ins>| Click on category link eg. Beginner| Renders all posts in that category| Pass
<ins>Like Button</ins>| Click applause icon when logged IN| Icon fills & number increases| Pass
<ins>Unlike Button</ins>| CLick applause icon to unlike instead| Icon empties color & number decreases| Check
<ins>Like Button</ins>| Click applause icon when logged OUT| Message to Login/Signup| Pass
<ins>Comment</ins>|Add a comment to blog post when logged IN| Success message when posted correctly| Pass
<ins>Edit Comment</ins>| Edit a comment written by same user| Message when successfully edited| Pass
<ins>Delete Comment</ins>| Delete a comment written by same user| Warning message before deletion| Pass
<ins>Comment</ins>|Add a comment to blog post when logged OUT| Message to Login/Signup | Pass
<ins>About Page</ins> | Click on About Link| About Page renders| Pass
<ins>Contact form link in About Page</ins>| Click link| Renders Contact Page| Pass
<ins>Contact Page</ins>| Click on Contact Link| Contact form renders| Pass
<ins>Contact Form</ins>| Fill in form and submit| Success message|Pass
<ins>Register</ins>|Click on register link| Renders Register form| Pass
<ins>Register-successful</ins>|Fill form to create new account| Successful message| Pass
<ins>Register-unsuccessful</ins>|Missing info on form| correction feedback message| Pass
<ins>Login-successful</ins>|Login with Username & Password| Logged in message on top| Pass
<ins>Login-unsuccessful</ins>|Wrong login details| Feedback message to correct| Pass
<ins>404 Page</ins>| Wrong address entered???| 404 Page renders with link to go back Home| Check
<ins>403 Page</ins>| Access Denied| 403 Page renders with link to go back Home| Check

HTML Validation:


CSS Validation:


JSHint: