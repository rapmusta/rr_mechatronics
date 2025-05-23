# rr_rops_runbooks
Contains documentation that is an internal document for Robot Operation engineers

Run Locally
-----------

1. Git clone the repo.
2. cd to ``docs``.
3. Run the below command to install the dependencies:

   ``pip install -r requirements.txt``

4. Run to install autobuild:

   For linux:

    ``sudo apt install python3-sphinx-autobuild``

   For windows:
   
    ``pip install sphinx-autobuild``
   


5. Run the below command to clean and build the ``index.html`` locally:

   For linux:

    ``make clean html``

   For windows:
   
    ``.\make.bat clean html``
   

   You can also auto-build the documentation on changes with live-reload in the browser using the below command:

   For linux:
    ``sphinx-autobuild . ./build/html --port <any-port-number>``

   For windows:
   ``sphinx-autobuild . .\build\html --port <any-port-number>``
