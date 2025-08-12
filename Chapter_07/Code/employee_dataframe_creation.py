
import pandas as pd
data = {
    'EmployeeID': [101, 102, 103, 104],
    'Department': ['Sales', 'HR', 'Engineering', 'HR'],
    'Salary': [58000, 62000, 72000, 60000],
    'Experience': [2, 4, 6, 3],
    'JoinDate': ['2020-05-10', '2019-08-15', '2018-03-20', '2021-01-01'],
    'Comments': [
        'Hardworking and punctual', 
        'Excellent team player',
        'Technically sound and innovative',
        'Quick learner'
    ]
}
df = pd.DataFrame(data)
