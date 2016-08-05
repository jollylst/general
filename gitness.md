#gitness:
##Fork & Clone
+ Fork on GitHub. Click the button.
+ Copy the HTTPS clone URL from *your* repository on Github.
+ From the command-line: `git clone [PASTE-URL]`

##Add to stage, Commit, and Push
+ Find out which files have been modified: `git status`
+ Add all files to stage for commit: `git add .`
    + OR: Add specific_file to stage for commit: `git add specific_file`
+ Commit changes: `git commit -m "[brief message re: commit]"`
+ Push to the master branch at your origin repo: `git push origin master`

##Create pull request
+ Go to your repository on GitHub. Click the little green button that says, under hover:

    > Compare, review, create a pull request

+ Then click:

    > Create pull request

##[Fetch to update your repo from upstream][1]

##Resources
+ [GitHub Help: Bootcamp / Good Resources for Learning Git and GitHub][2]
+ [The Git Parable by Tom Preston-Werner][3]

    > Git is a simple, but extremely powerful system. Most people try to teach Git by demonstrating a few dozen commands and then yelling “tadaaaaa.” I believe this method is flawed.

<!-- Links -->

[1]: https://github.com/python-boot-camp/D01/blob/master/fetch.md
[2]: https://help.github.com/articles/good-resources-for-learning-git-and-github/
[3]: http://tom.preston-werner.com/2009/05/19/the-git-parable.html