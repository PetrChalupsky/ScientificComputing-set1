# Group assignment 1 for Scientific Computing

## Setup environment with Anaconda

After cloning this repository use:

```conda env create -f environment.yml --prefix ./env```

to create environment based on environment.yml.
To install new packages use:

```conda install package```

Note that sometimes you might need different channel or have to resolve conflicts. Once you have finished adding packages update environment.yml using:

```conda env export > environment.yml```

Then stage and commit the changes, so others can use them. If you want to use updated environment.yml use:

```conda env update --file environment.yml --prune```

to update your current environment.
