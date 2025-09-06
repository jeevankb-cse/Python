#Q.Write a program to find out whether a given post is talking about "Jeevan" or not
post="Hey jeevan bhai is good jeevan is very good and jeevan is great"
post=input("Enter the your post:")
if("jeevan".upper() in post.upper()):
    print("This post is talking about jeevan")
else:
    print("This post is not talking about jeevan")
        