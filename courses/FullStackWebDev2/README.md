-  Language/frameworks
   -  HTML
   -  CSS
   -  Bootstrap
   -  JQuery

-  Package Managers
   -  NPM (lite-server)

-  CSS Preprocessors
   -  Less
   -  Sass

-  Build and deployment task runners
   -  Grunt
   -  Gulp

-  Global installation of npm packages
Any npm package installed with -g is installed in global node_modules.
All their binaries should be already in the path but if not do following :

export PATH=/Users/vishalm/.npm-packages/bin:$PATH

-  Local installation of npm packages
If you install packages locally they will be installed in node_modules directory
under the current directory. add the location manually to path to have cli access

-  --save-dev vs. --save in npm install
--save adds npm package as a dependency in package.json
while --save-dev adds npm package as a dev dependency in package.json


===================
Angular
===================
-  Architecture
   -  Modular
   -  Component-based with templates
   -  Services

-  Module
   Could contain a set of Components and services

-  Components (views of angular)
-  Services

-  Decorator
-  Directives
-  Pipes
-  Templates
-  Routing

-  Interpolation
-  One way data binding
