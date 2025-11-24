from pyscript import display, document

# clubs, dictionary in a dictionary
club_info = {
    "Glee Club":{
      
        'Description':'A club for those passionate for singing!',
        'Meeting Time':'Monday and Thursday, 3:30-4:30',
        'Location':'Music Room',
        'Category':'Non-academic'
    },

    "Band Club":{
        'Name':'Band Club',
        'Description':'A club for music enthusiasts!',
        'Meeting Time':'Monday and Friday, 3:00-4:00',
        'Location':'Band Room',
        'Category':'Non-academic'
    },

    "Math Club":{
        'Name':'Math Club',
        'Description':'A club for those who love math!',
        'Meeting Time':'Wednesday, 3:00-4:30',
        'Location':'Room 509',
        'Category':'Academic'
    }
}

def clubdetails(e): # function gets data from dropdown, to then display

    values = document.getElementById('cluboptions').value # getting data
    data_display = club_info[values]
    document.getElementById("output").innerHTML = ""

    display(f"{values}", target="output") # displaying data
    display(f"Description: {data_display['Description']}", target="output")
    display(f"Meeting Time: {data_display['Meeting Time']}", target="output")
    display(f"Location: {data_display['Location']}", target="output")
    display(f"Category: {data_display['Category']}", target="output")
   

    

   
