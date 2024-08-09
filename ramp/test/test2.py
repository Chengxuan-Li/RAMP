from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from ramp import User, UseCase, Appliance
import matplotlib.pyplot as plt
import pandas as pd

user = User(
    user_name="Test",
    num_users=100,
)
# add_appliance is meth
test_appliance = user.add_appliance(
    name="Test Appliance",  # the name of the appliance
    number=1,  # how many of this appliance each user has in this user category
    power=1,  # the power (in Watt) of each single appliance. RAMP does not deal with units of measures, you should check the consistency of the unit of measures throughout your model
    num_windows=1,  # how many usage time windows throughout the day?
    func_time=1,  # the total usage time of appliances
    func_cycle=1,  # the minimum usage time after a switch on event
    window_1=[300, 600]  # 
)

use_case = UseCase(
    users=[
        user
    ],  # A list of all the user categories to be included in the simulation. In this case, we only have household user category
    date_start="2020-01-01",  # starting date of the simulation
    date_end="2020-01-01",  # end date of the simulation
)

whole_year_profile = use_case.generate_daily_load_profiles()
whole_year_profile = pd.DataFrame(
    whole_year_profile, columns=["Test"]#, index=use_case.datetimeindex
)

plt.hist(whole_year_profile[whole_year_profile['Test'] > 0.5].index.to_series(), bins=24)
plt.xlim(xmin=0, xmax = 1440)
plt.show()