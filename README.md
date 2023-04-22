# Data Version Control 

Fork the dvc template from https://github.com/realpython/data-version-control

Clone the forked repository to your computer with the `git clone` command

```console
git clone git@github.com:YourUsername/data-version-control.git
```

Make sure to replace `YourUsername` in the above command with your actual GitHub username.

## Steps:
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
13. Add and commit the json files to github `git add --all` and `git commit -m "Evaluate the model accuracy"`.
14. Push all the changes to github and dvc using `git push` and `dvc push -r "origin"`.
15. Tag your commit `git tag -a model -m "RandomForest with accuracy 98%"`. Push your tags `git push origin --tags`.
16. You can create further more branches with other experiments and then merge with your final branch.

## Creating reproducible pipelines
1. Create a new branch and remove the .dvc files as these will be again created in pipeline
 * `dvc remove data/prepared/train.csv.dvc data/prepared/test.csv.dvc model/model.joblib.dvc`
2. Now to create a pipeline once dvc run command has to be used. Few arguments to look at before running.
    * The -n switch gives the stage a name.
    * The -d switch passes the dependencies to the command.
    * The -o switch defines the outputs of the command.
    * The -M switch defines the metrics of the command
3. Now running the prepare.py with dvc run as `dvc run -n prepare -d src/prepare.py -d data/raw -o data/prepared/train.csv -o data/prepared/test.csv python src/prepare.py`
4. A new dvc.yaml file will be created showing the pipeline.
5. Similary run for training and evaluate stages.
    * `dvc run -n train -d src/train.py -d data/prepared/train.csv -o model/model.joblib python src/train.py`
    * `dvc run -n evaluate -d src/evaluate.py -d model/model.joblib -M metrics/accuracy.json python src/evaluate.py`
6. Use `dvc metrics show` to see the metrics.
7. Now add, commit and push to github and dvc.
8. Look at `dvc.yaml` to see the whole pipeline.
9. Now if you want to run other experiments you don't need to run dvc run all the times. Thats what reproducible pipeline was all about. 
10. Create new branch and train a new model like Logistic regression.
11. Now change the model in training.pt file and use `dvc status` to see the changes inside the files of pipeline.
12. Now to run this logistic regression function use `dvc repro evaluate`. This will re run the training and evaluate stages of the pipeline.
13. Now see the metrics but this time add a new flag -T to see metrics created by all runs. `dvc metrics show -T`.

## Conclusion

So now to run multiple experiments one can just make changes to the necessary files and use `dvc repro evaluate` to run the pipeline.
