## MLBox

A simple vagrant setup for Machine Learning. The objective is to 
provide easy access to some of the more popular tools.

This box contains:
- [Python](http://www.python.org/) with libraries like [Pandas](http://pandas.pydata.org/), [Numpy](http://www.numpy.org/), [Scipy](http://www.scipy.org/) etc
- [IPython](http://ipython.org/)
- [R](http://www.r-project.org/) and [RStudio](http://www.rstudio.com/)
- [Octave](http://www.gnu.org/software/octave/)

### Assumptions:
- You mean to use this on a mac :). _Note: There is vagrant and virtual box
support for Windows and Linux, but it just hasn't been tested on that.
If you have had a chance to try on that platform, I would love your
feedback._
- You have [Vagrant](http://www.vagrantup.com/) installed. The version I have 
tested with is available at <http://downloads.vagrantup.com/tags/v1.0.4> (choose Vagrant-1.0.4.dmg)
- You have Virtual Box installed. The version I have tested with is at
<http://download.virtualbox.org/virtualbox/4.2.0/VirtualBox-4.2.0-80737-OSX.dmg>

It has been tested with the following versions of virtual box and
vagrant. I will update the matrix as I get opportunity to test it with
other versions (and if I get feedback from people who have tried other
combinations)

| Vagrant  | Virtual Box |
| -------- | ----------- |
| 1.0.4    | 4.2.0       |

### Steps
    cd <your work directory>
    git clone git@github.com:srikar/mlbox.git
    cd mlbox
    vagrant up

### References

- For getting started with Vagrant,
: <http://docs.vagrantup.com/v2/getting-started/index.html>
