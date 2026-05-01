lab_monitor = {
    "Lab_ID": "ENTC-01",
    "Voltage": 5.0,
    "Current": 0.25,
    "Status": "Normal"
}
print(f"Current Lab Voltage: {lab_monitor['Voltage']} V")        # Accessing data (The 'Key' approach)
#output : Current Lab Voltage: 5.0 V

lab_monitor["Voltage"] = 5.2
print(f"Updated Voltage: {lab_monitor['Voltage']}V")             #Updating data (Mutable property)
#output :Updated Voltage: 5.2V

lab_monitor["Last_Checked"] = "10:00 AM"                         #Adding new data

print("Available Data Labels:", list(lab_monitor.keys()))        #Using a method to show all keys
#output: Available Data Labels: ['Lab_ID', 'Voltage', 'Current', 'Status', 'Last_Checked']

remove_current = lab_monitor.pop("Current")
print(f"Current removed:{remove_current}")
#output: Current removed:0.25

clear_data= lab_monitor.clear()
print(lab_monitor)                                               #for next readings we need empty dictionary
#output:{}
