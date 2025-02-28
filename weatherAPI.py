import requests
from tkinter import *
window=Tk()


label=Label(window,text='Hello,insert expected day :')
label.pack()
input=Entry(window)
input.pack()

response=requests.request("GET","https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=LKXHK7F6D2QE6DAXJBBHTS2B7&taskId=98cf63c3a89f9ea29355dc52cd271182&zip=false")
final_response=response.json()
def show_temp():

    
    if(response.status_code==200):
        inserted=input.get()
        label=Label(window,text=find_temp(inserted))
        label.pack()
    else:
        print("error")    




def find_temp(date):
    for day in final_response["days"]:
        if(day["datetime"]==date):
            return convert_to_celcius(day["temp"])
        else:
            continue


def convert_to_celcius(temp):
    final=(temp-32)*5/9
    return round(final,1)


button=Button(text='search',command=show_temp)
button.pack()
window.mainloop()

