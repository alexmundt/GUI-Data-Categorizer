
import tkinter as tk
from Categories import *

############ reading the folder
print("### Reading folder ")
folder = "example data"
file_list = listdir(folder)

########## print out of test files
print("### Printout of test files in the read folder...")
test_file = file_list[0]
print(test_file)
event_id = test_file[-14:-6]
print(event_id)


########### generating a list of events
print("### Generating event list...")
events = [get_event_id_from_filename(filename) for filename in file_list[:5]]
print(events)

########## using the older tagscontainer class
print("### Loading a Container from the read events...")
tagscont = TagsContainer(list_events = events)

output = tagscont.get_tags(event_id)
output2 = tagscont.get_tags(events[2])

output.set_value("test")
print(tagscont.get_tags(event_id).get_value())
print(output)
print(output2)


##########
print("### Loading TagDataFrame Class")
tagframe = TagDataframe(["event_id",
    "noise", "quality"])
tagframe.get_event_id_from_folder(folder)
tagframe.printout()

# test_row = tagframe.get_row_from_id(event_id)
# print(test_row)
# test_row["noise"] = "hi"
#
# print(test_row)
#
# test_row = tagframe.get_row_from_id(event_id)
# print(test_row)
#
# print(event_id)
tagframe.set_value_in_category(event_id, "noise","noisetest")
test_row = tagframe.get_row_from_id(event_id)
print(test_row)
tagframe.printout()

filename="test_frame"
tagframe.write_to_file("test_frame")
tagframe.load_from_file("test_frame")
print("#### Printout after loading frame from filename")
tagframe.printout()

## tk window test
print("### Testing TKinter GUI")
main = tk.Tk()

cat_frame = CategoryGUIFrame(main, categories =
    ["quality","noise","event_id","signal"], padding=10)

cat_frame.data.get_event_id_from_folder(folder)

main.grid()
cat_frame.grid()

event_id_index = 0
def change_label():
    global event_id_index
    # cat_frame.set_value("quality", "spass")
    try:
        event_id = events[event_id_index]
    except IndexError:
        print("IndexError encountered. Restarting index at 0.")
        event_id_index = 0
        event_id = events[event_id_index]
    # this is the old tagframe data
    new_data = tagframe.get_dict_from_id(event_id)
    new_data = cat_frame.data.get_dict_from_id(event_id)
    print(new_data)
    # new_data = row.to_dict()
    # print(row)
    # print(type(row))
    event_id_index += 1
    # event_dict = {"event_id":str(event_id)}
    cat_frame.load_category_data(new_data)

change_button = ttk.Button(main, text="Change Label", command=change_label)
change_button.grid()
new_data = {"quality": "hiiigh quality", "noise":"looow noise"}

relief_button = ttk.Button(main, text="change relief",
    command=cat_frame.make_category_bold)
relief_button.grid()

change_button = ttk.Button(main, text="change active",
    command = cat_frame.change_active_category)
change_button.grid()

def set_to_one():
    cat_frame.set_value("noise", 1)


set_to_one_button = ttk.Button(main, text="Set to 1", command = set_to_one)
set_to_one_button.grid()

new_change_button = ttk.Button(main, text="Object Next()",
    command = cat_frame.switch_to_next_item)
new_change_button.grid()
new_previous_button = ttk.Button(main, text="Object Previous()",
    command = cat_frame.switch_to_previous_item)
new_previous_button.grid()

cat_frame.load_category_data(new_data)

cat_frame.data.get_event_id_from_rownumber(7)
main.mainloop()
