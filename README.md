[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/fomightez/cairo-jupyter/master?filepath=index.ipynb)  
^^^^^^^^^^  
Press button above to start (cairo images will be visible in the active notebooks)


# cairo-jupyter

Launchable active Jupyter notebooks hosted via mybinder.org that will run Cairo image-generating code.

This should make development easier by enabling spawning active coding environments in any modern browser on any device, where one can change the code and see the resulting image displayed on the same page. I was finding developing Cairo code purely on the command line was less than ideal because of going back and forth between applications.

The [demonstration notebooks](https://mybinder.org/v2/gh/stuaxo/cairo-jupyter/master?filepath=index.ipynb) even work on mobile devices.

Click this button to launch live, interactive [demonstation notebooks](https://mybinder.org/v2/gh/fomightez/cairo-jupyter/master?filepath=index.ipynb) ----> [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/fomightez/cairo-jupyter/master?filepath=index.ipynb).

# Continuous integration

This repository is connected to continuous integration. Currently, it checks repo2docker can use the repo to make a Docker image/Binder implementation, and also verifies the resulting running container can generate images. The status of these tests is displayed on the next line. (It can take a few minutes for the red `FAILED` badge to show if something was broken during development.)

[![CircleCI](https://circleci.com/gh/fomightez/cairo-jupyter.svg?style=svg)](https://circleci.com/gh/fomightez/cairo-jupyter)

## Inspiration

This is based on Stuaxo's [ipython_cairo](https://github.com/stuaxo/ipython_cairo) and MyBinder.org. See [here](https://github.com/stuaxo/ipython_cairo/issues/4#issuecomment-355009047) for some of discussion of getting it working in "binderized" notebooks launched from MyBinder.org.
