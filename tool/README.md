
This repository provides a toolchain for gathering and analyzing merge scenarios found in git repositories. The tool stores the collected data in a normalized MySQL database. It supports extracting various features of the merge scenarios as well as executing the merge using different merge tools, detecting merge conflicts, and finding compilation and test problems with the merge resolution.

_The toolchain has been tested with Ubuntu 18.04._

## Setup
1. Clone this repository:
```bash
git clone https://github.com/anonymousauthorpaper/ESEM-19.git
```

2. Install required tools and packages using this script (Note that this requires sudo privilege. 
Check the list before executing this script and adapt according to your needs to avoid breaking your packages)
```bash
sudo ./setup.py
``` 

## Usage 

1. **Set the `config.py` file:** The pre-defined paths, database information, constants, and access keys are stored in  `config.py` file. The only parameters that the user must set before using this tool are the GitHub access keys and database parameters.

2. **Add the list of repositories:** The input of the main program is a list of repositories to analyze. There are different ways to create such list:

    * **Add the repository list manually:** If you already have the list of repositories to analyze, write them in a *\*.txt* file (each repository per line) and copy the text file in `./working_dir/repository_list` (this path is `REPOSITORY_LIST_PATH`  which is set in `config.py`).

    * **Automatic searching:** If you do not have specific repositories in mind, but instead, want to analyze repositories with a specific range of stars, watches, forks, size, or that are in a specific application domain, you can search the list of repositories using `search_repository.py`. 

3. **Run the main script:** To run the tool, you can run this command:

```bash
python3 main.py <parameters> 
```
