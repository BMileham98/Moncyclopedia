# Moncyclopedia

## Introduction

Welcome to the Moncyclopedia! This is a site dedicated to cataloguing and observing fictional monsters, aimed to echo the real enthusiasm of folklore and cryptid fans. Everything on this site is written as though these monsters are a newly discovered part of the fictional world it features! From cute critters to aliens and gods, I wanted to capture the excitement of a fantasy world which my new knowledge of the Django Framework has enabled me to explore. 


## UX Design

### Goal

The aim in building this project was creating a collaborative space that gives users a smooth experience in discovering new creatures and sharing their own findings, taking inspiration from Wiki sites and painting it with my own personal polish. I wanted to convey the sense of wonder I would get from reading up on my favourite media series as a kid and getting lost in the fun of fantasy. 
Care was taken in both making the site responsive but also having a colourful scheme that did not clash excessively in my endeavour for colour-coordinating based on monsters' categories. 

### User Stories

The project board for this site can be found [here](https://github.com/users/BMileham98/projects/7), below I shall provide the user stories by their priority. 

#### Must-Haves

- As a monster enthusiast, I want to see listings for each monster so that I may further my knowledge
- As a monster enthusiast, I wish to be able to report my findings so that I may discuss them with others
- As a user, I want to be able to comment my own observations so that I may contribute to the discussion

#### Should-Haves
- As a commenter, I want to upload images of my findings so that I may back up my claims
- As a user, I would like to see some unique styling to the pages for a more pleasant aesthetic
- As a monster enthusiast, I would like to be able to add new monsters to the site so that I may prompt new observations

#### Could-Haves
- As a user, I would like to see featured pages so that I may discover new monsters
- As a moderator, I want to be able to curate comments with images so that I may make a safer environment for our community

### Wireframes

Below are the wireframes for the home page in both desktop and mobile formats, as well as the rough concept for the monster entry page. These were made with Balsamiq.

![Desktop wireframe](static/images/readme/Wireframe%20(Desktop).png)
![Mobile wireframe](static/images/readme/Wireframe%20(Mobile).png)
![Monster wireframe](static/images/readme/Wireframe%20(Monster).png)

### Aesthetic

The immediate concept for the colour scheme when this project was visualised was that parts of the layout would vary dependent on the monster that was recalled for each entry or observation, including on the lists, each dedicated page and the sidebar. This was implemented through recalling the category variable and using this for custom CSS. 

![CSS Colours](static/images/readme/CSS%20colours.png)

These colours were evaluated with some being lightened or darkened based on how much they blended in with each other. Additionally, I split the colour coding into background and border rules, to improve the aesthetic and protect against eye-strain for certain features. This was especially apparent in the sidebar on the observation_detail.html page, where the drop-down headers were stylised with the border- rules due to the background- rule clashing too badly. 


### Responsiveness

The project has been configured to be responsive across multiple screen-sizes, with the navbar providing a toggle on smaller mobile screens due to the amount of links. 
![Mobile](static/images/readme/Mobile.png)



## Features

### Home Page

The home page is set up to display a different monster depending on the day using the datetime module, each category variable is assigned to a weekday which will feature any monster with that category. This is future-proofed so additional monsters will be added into the rotation without further coding needed. 

![home](static/images/readme/Home.png)

### Monsters

![monster list](static/images/readme/Monster%20list.png)
![monster entry](static/images/readme/Monster%20example.png)

Monsters are recalled in alphabetical order to form a list, with badges to indicate their corresponding elements. When clicked, this will lead to a profile for each monster with basic stats such as their size or diet as well as some trivia such as the etymology. Each monster's entry also automatically collects all observations made for that monster, which provides a quicker method of locating other users' findings as opposed to clicking onto the observation list and scouring. 

The monster entry page also features a sidebar with links to other monsters, saving additional clicks to continue browsing. The sidebar has been configured so the current monster is separated from this list.

There is also a comment section on the monsters' entries to prompt further discussion outside of observations.

### Observations

![Observation list](static/images/readme/Observation%20list.png)
![Observation entry](static/images/readme/Observation.png)

The observation list automatically collects observation entries submitted for each monster and provides them with the most recent entry first. The list overall is alphabetical with borders dependent on the monster's category to prove more colour without the potential eye strain of solid colour. It keeps track of the number of observations. 

The entry features a sidebar that turns each monster's section into a dropdown to speed up loading as well as prevent the page becoming too cluttered. There is also a comment section to encourage users to contribute towards others' findings. 

### Submitting Observations

![Observation submission page](static/images/readme/Submit%20observation.png)

The site allows users not only to comment on monsters and the site owner's findings but also to contribute their own, to truly emulate the collaborative nature of Wiki sites. The dropdown option for monsters lets each observation instantly be matched to the corresponding monste ID so that it can be displayed on its individual entry. This should be future proofed for the potential addition of user-submitted monsters too.

## Future Refinements

There is a fair amount of features I would like to add or refine to this project, in order to both make the site more polished and allow for further collaboration. 

The comments allow for image submission, however it is not currently regulated. I hope to enable approval on a conditional basis to both curate images and allow a steady flow of discussion. 

There is not currently a page to allow users to submit their own monsters, this is something I would also implement with further time. The model for monsters has been built around this however, with the categories being coded to accept only the 7 categories I have decided so that functionality such as filtering would not break. 

Additionally, there are layout changes that could improve the experience. Though most the monsters are established as scientically observed or proven, there is the extra category of 'Outsider' I would implement for monsters akin to aliens or cryptids like Bigfoot. 'Helel' is an example of one of these monsters intended to fill such a purpose. A small layout change I would implement is the use of a pop-up modal serving as a disclaimer for speculation or unverified monsters. 

## Testing


HTML Validation shows no errors besides an issue rendering the monster_detail.html where it adds an additional set of paragraph tags to the description. This issue is not visible on the site itself, however. I believe this may be caused by extra tags being stored in the database, as there's only one set of paragraph tags in the template. 

![HTML error](static/images/readme/HTML%20error.png)
![HTML error screenshot](static/images/readme/HTML%20error%20line.png)

CSS Validation is clear! No errors found.
![CSS validation](static/images/readme/CSS%20validation.png)


## Credits

First, Code Institute is to be credited for teaching me how to use the Django framework and improving my knowledge of the HTML, CSS and Python languages. 

Bootstrap was used as a base for many parts of the site, such as the navbar and building the structure of the monster entry page. 
The concept of the site was inspired by Wiki sites, such as Bulbapedia and those hosted by Fandom.

W3Schools was referenced, especially in finding the correct colours for the layout.

Co-Pilot was also used, as detailed below. 

### AI Declaration

Github Co-Pilot was used in troubleshooting and as a framework that was built on. Any suggested or auto-completed code, I asked for further explanation and overhauled to fit my project's purpose. Images were also generated by Co-Pilot as placeholders. 