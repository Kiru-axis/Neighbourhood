# HOOD EYE
## Prerequisites
* Computer literacy
* Internet connectivity

## Description
* These application lets you join a neighborhood or create one.
* When you join you can see the security and health personell of the area.


## Behaviour Development Design
1. **User shall login/signup**
* Given: Signup/login forms/pages are accessed
* When: User tries to login/signup
* Then: User details are authenticated if no error is found and can access the desired pages.

2. **All NeighbourHoods**
* Given: User is logged in
* When: Hood link is clicked on the navigation bar
* Then: All NeighbourHoods are shown with an option to join.

3. **Change Profile**
* Given: Edit profile page is accessed by clicking editprofile on navbar
* When: User tries changing profile
* Then: Edit profile form is displayed

3. **Create Hood**
* Given: User creates a hood aquiring admin level access.
* When: User adds name.location,logo,health_workers,description and police_number
* Then: A new hood is created and added to all hoods page.

4. **Manage Hood**
* Given: User creates the hood.
* When: User creates Businesses and posts.
* Then: All posts and Businesses added by the user and the joining members are displayed

5. **Join/Leave Hood**
* Given: User decides to join or leave a hood.
* When: User clicks leave/join button at the bottom of each hood.
* Then: User either leaves or joins the hood depending on the button clicked.

5. **User session should end when logout url is chosen**
* Given: Logout option is given
* When: User chooses logout option
* Then: User session is ended

## Languages used
* Python(Django)
* html5
* css3(Bootstrap)


## Live Link
[Link]()


## License
Copyright (c) 2021 Peter Kiru

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE..

## Author
**Peter Kiru**