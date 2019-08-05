# Make your code reproducible by anyone, anywhere

In this section we demonstrate how to host and share Jupyter Notebooks using the [Mybinder.org](https://mybinder.org) cloud infrastructure. Binder enables users to run Jupyter Notebook in a web-browser without any software installation. It is a platform to support reproducible research.

* [Binder 2.0 blog post](https://blog.jupyter.org/binder-2-0-a-tech-guide-2017-fd40515a3a84)

* Binder 2.0 - Reproducible, interactive, sharable environments for science at scale, Project Jupyter, et al. (2018) Proc. of the 17th Python in Science Conf. [(SCIPY 2018)](http://conference.scipy.org/proceedings/scipy2018/pdfs/project_jupyter.pdf).

## [Presentation](Binder.pdf)

## Hands-On Excercise

In this excercise we setup links (Binder Badges) to launch Jupyter Notebook and Jupyter Lab on Binder.

### Add a binder badge for a specific Jupyter Notebook

1. Go to [Mybinder.org](https://mybinder.org) and paste in the URL of your forked repository
```
https://github.com/your-user-name/reproducible-computational-workflows
```


2. Paste in the path to a specific Jupyter Notebook of your choice, e.g.
```
3-jupyter/3D_visualization.ipynb
```

3. Copy the Binder Badge Markdown text snippet from Mybinder.org

4. Open **this README.md** file in Jupyter Lab

5. Paste the text snippet below
 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ISMB-ECCB-2019-Tutorial-AM4/reproducible-computational-workflows/master)

### Add a binder badge for Jupyter Lab

6. Next, copy and paste the text snippet below and modify the link to launch Jupyter Lab without a specific notebook

*your Jupyter Lab launch badge goes here ...*

7. Save this README.md file (File -> Save Markdown File)

8. Preview this README file (Right Click [Windows], Ctrl+Click [MacOS] -> Show Markdown Preview)

9. Add the modified README.md file ([see](../4-git/README.md))
```
git add README.md
```

10. Commit your changes
```
git commit -m "added binder badges"
```

11. Push your changes to GitHub
```
git push origin master
````

9. In your web browser open
```
https://github.com/your-user-name/reproducible-computational-workflows
```

10. Navigate to the ```5-binder``` directory

11. Click a "Launch Binder" badge

12. Wait, wait, ... it may take several minutes to build a binder image ... until Jupyter launches.

13. Run your Notebooks on MyBinder.org
