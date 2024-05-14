END to END Python project using AWS
Overview :- 
a) New Environment Creation
b) Setup.py
c)Requirment.txt
Step 1 - Github account creation and conda environment setup //set up git repository
Step 2 - create readme file in visual code and add is to git using git add README.md
            git init
            git add README.md
            git commit -m "first commit"
            git branch -M main
            git remote add origin https://github.com/sidjiv/mlproject.git   
            git push -u origin main
 Step 3 - Create global user           
            git config --global user.email "you@example.com"
            git config --global user.name "Your Name"
step 3 - Create gitignore file in git and pull it from origin
            git pull

 # We have also added "-e ." because everytime it runs it will trigger setup.py 
  # readlines will read requirment.txt 
        
 # when we use readlines , \n gets added in the requiremnts so we are replacing the \n