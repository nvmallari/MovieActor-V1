# MovieActor V1 Application Project
# Project Description
This application, in a nutshell, looks up the cast of two movies and outputs the filmography of a matching actor.
This project uses Django to build a web framework and Cinemagoer to access the IMDb movie database.
Some of the challenges I faced as a software programmer at the beginner level included learning the basics of web development and implementing different Python packages to complete my desired project. In the future, I wish to improve on the searching algorithms when searching for two different movies.
# How to Install and Run
Download all of the files included in this repository.
In your terminal, install Python packages Cinemagoer and Django. I used VSCode and pip install to do this.
To get the application running, open the integrated terminal under "imdbsite" and type the following command: "python(or python3) manage.py runserver".
This will get the application up and running.
# How to Use
To view and interact with the application, open your browser and go to the following url to start:
http://127.0.0.1:8000/home/
This will lead you to a simple home page I made. Go ahead and find the button that leads to the movieactor/ page.
Once you view the movieactor page, type in two titles of movies that you know have a matching actor, and then hit "Submit". Loading time takes a bit to complete.
Once it is finished, you will see that the page outputted a list of results that will show an entire filmography of the matching actor.
That's it!
# Credits
Cinemagoer: https://cinemagoer.github.io
Django: https://www.djangoproject.com
# License
MIT License

Copyright (c) 2022 Nicholas Mallari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
