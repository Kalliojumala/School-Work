from datetime import datetime, timedelta

#prints date 10 days from given date
def tuleva_pvm(p: int = 10):
    """Tulostaa päivämäärän annetun parametrin mukaan nykyhetkestä

    Argumentit:
      p: int, montako päivää eteenpäin päivämäärä halutaan tulostaa. 

    Palautus:
      None
    """
    print("Päivämäärä {:d} päivää tästä päivästä on: {:s}".format(p, (datetime.now() + timedelta(days=p)).strftime("%a, %d.%m.%Y")))



tuleva_pvm(10)

