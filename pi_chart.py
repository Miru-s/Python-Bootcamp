#Matplotlib- Data Visulaization module
#pie() is an in-built attribute in matplotlib




import matplotlib.pyplot as plt
x=[30,30,20,20]
chart=["Python" ,"C++" , "Java" , "JavaScript"]
plt.pie(x, labels=chart)
plt.show()