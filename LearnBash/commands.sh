#!/bin/bash
# ----------------- COMMANDS ----------------------------
# ************** USER INFO ****************
# cut -d: -f1 /etc/passwd | sort : will list all the users on the system.

# id : will show your privileges. 
#    :This command will display information about your user ID, group ID, and additional groups you belong to.

# sudo adduser newUserName : creates a new user.

# sudo usermod -aG sudo newUserName : To change a user's privileges, you can add or remove the user from groups using the usermod 
#                                   : This command adds the user to the sudo group, granting them sudo privileges.

# sudo userdel -r username : This command removes the user account and deletes their home directory (-r flag).

# passwd : to change the password.

# to view user login history, you can check the systems logs (/var/log/)

# visudo : To restrict user access to specific commands, you can modify the sudoers file (/etc/sudoers). we use the visudo because it provides syntax.


# -------------UNIQUE FUNCTIONALITY ---------------------
# $ : for use with variables.
# = : Assignment.
# ! : negation.
# >>, >, < : input/ output redirection.
# | : sends the output of one command to the input of another.
# * or ? : Globs. wildcard for a single character.
# "" or '' : Single quotes preserve literal meaning. double quotes allow substitutions.
# -a : logically AND operator. equivalent to &&.
# -o : logically OR operator. equivalent to ||.
