### More work with building Python classes
# Company class that can serve customers and gain employees
class Company():
    def __init__(self, name, industry_type, num_employees, total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self, cust):
        self.total_revenue += cust

    def gain_employees(self, employee_list):
        for employee in employee_list:
            self.num_employees += 1

corp = Company('Corp Corp', 'Company', 99, 150.50)
corp.serve_customer(15.50)
corp.gain_employees('Jim')
print(corp.name, corp.industry_type, corp.num_employees, corp.total_revenue)

# TV class that can be turned on/off and change the channel
class TV():
    def __init__(self, brand, on_status=False, current_channel=0, life_perc=100):
        self.brand = brand
        self.on_status = on_status
        self.current_channel = current_channel
        self.life_perc = life_perc

    def hit_power(self):
        if self.on_status == False:
            self.on_status = True
        else:
            self.on_status = False
            self.current_channel = 0
            self.life_perc -= 0.01

    def change_channel(self, channel):
        if self.on_status == False:
            print('Television is not on!')
        else:
            self.current_channel = channel

tv = TV('Sony')
tv.change_channel(10)
tv.hit_power()
tv.change_channel(10)
print(tv.brand, tv.on_status, tv.current_channel, tv.life_perc)
tv.hit_power()
print(tv.brand, tv.on_status, tv.current_channel, tv.life_perc)
