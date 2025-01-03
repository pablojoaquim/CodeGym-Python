
### **Git Training Kata: "Feature Branch Adventure"**

#### **Objective**
Learn and practice:
1. Branching and merging.
2. Resolving merge conflicts.
3. Rebasing.
4. Undoing changes.
5. Using Git logs and diffs.

---

### **Setup**
1. Create a new directory and initialize a Git repository:
   ```bash
   mkdir git-kata && cd git-kata
   git init
   ```
2. Create a `README.md` file with the content:
   ```
   # Git Kata
   This is a training repository.
   ```
   Add and commit the file:
   ```bash
   git add README.md
   git commit -m "Initial commit with README"
   ```

---

### **Tasks**

#### **Task 1: Feature Branching**
1. Create a new branch called `feature/hello-world`:
   ```bash
   git checkout -b feature/hello-world
   ```
2. Add a new file `hello.txt` with the content:
   ```
   Hello, World!
   ```
   Stage and commit the changes:
   ```bash
   git add hello.txt
   git commit -m "Add hello.txt with a friendly message"
   ```
3. Push the branch to a remote (simulated by setting up a bare repository if you want):
   ```bash
   git remote add origin <remote-repo-url>
   git push -u origin feature/hello-world
   ```

---

#### **Task 2: Merging and Resolving Conflicts**
1. Switch back to the `main` branch:
   ```bash
   git checkout main
   ```
2. Modify `README.md` on the `main` branch to include:
   ```
   ## Welcome
   This repository is for learning Git.
   ```
   Commit the change:
   ```bash
   git add README.md
   git commit -m "Update README with Welcome section"
   ```
3. Merge the `feature/hello-world` branch into `main`:
   ```bash
   git merge feature/hello-world
   ```
   If there’s a conflict, resolve it manually and complete the merge.

---

#### **Task 3: Interactive Rebasing**
1. Add multiple commits to `main`:
   ```bash
   echo "More content" >> README.md
   git add README.md
   git commit -m "Add more content to README"

   echo "Another update" >> README.md
   git add README.md
   git commit -m "Another update to README"
   ```
2. Use an interactive rebase to squash the two commits into one:
   ```bash
   git rebase -i HEAD~2
   ```

---

#### **Task 4: Undoing Changes**
1. Modify `hello.txt` and then decide to discard the changes:
   ```bash
   echo "Oops, a mistake!" >> hello.txt
   git checkout -- hello.txt
   ```
2. Create and commit a new file, then reset it:
   ```bash
   echo "Temporary file" > temp.txt
   git add temp.txt
   git commit -m "Add temp file"
   git reset --soft HEAD~1
   ```

---

#### **Task 5: Logs and Diffs**
1. Explore the Git history:
   ```bash
   git log --oneline
   git log --graph --all
   ```
2. Check the difference between `main` and `feature/hello-world`:
   ```bash
   git diff main feature/hello-world
   ```

---

### **Bonus Task**
Simulate collaboration by creating another branch (e.g., `feature/new-idea`), making changes, and resolving conflicts with your own work.

---

This kata covers essential Git skills and can be repeated or modified to suit different levels of expertise.
