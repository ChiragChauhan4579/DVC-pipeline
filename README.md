# Data Version Control 

Fork the dvc template from https://github.com/realpython/data-version-control

Clone the forked repository to your computer with the `git clone` command

```console
git clone git@github.com:YourUsername/data-version-control.git
```

Make sure to replace `YourUsername` in the above command with your actual GitHub username.

Steps:
1. cd to the dvc folder and initialize using `dvc init`.
2. You can also create a new git branch for experimentation.
3. Using dagshub for remote storage so creae a repository on dagshub and follow the dvc storage setup on dagshub. Do it with `dvc remote add path/to_dagshub.dvc`.
4. Add train and val data to dvc using `dvc add data/raw/train` and `dvc add data/raw/val`. Two new files train.dvc and test.dvc will be created.
5. The original data will be added in .gitignore so they don't get pushed to the github and only the .dvc files will be added to github.
6. Push your files to github and original data files to dagshub dvc storage following the commands.
    * git add --all
    * git commit -m "First commit with setup and DVC files"
    * dvc push -r "origin"
    * git push --set-upstream origin <branch name>
7. Create a script for praparing the dataset and run it with `python src/prepare.py`.
8. Add prepared files to dvc and commit others to github using `dvc add data prepared/train.csv data/prepared/test.csv` and `git add --all` and `git commit -m "Created train and test CSV files"`.
9. Run the model with the training script `python src/train.py`.
10. Add model to dvc using `dvc add model/model.joblib`.
11. Add and commit to github `git add --all` and `git commit -m "Trained random forest classifier"`.
12. Run the evaluate file using `python src/evaluate.py`. A new json file under metrics would be created. I got an accuracy of 98%.
13. Add and commit the json files to github `git add --all` and `git commit -m "Evaluate the model accuracy"`
