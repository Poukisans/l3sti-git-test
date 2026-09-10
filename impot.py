def calc_impots(revenu: int) -> str :
     """
     Calcul des impots

     Args:
         revenu (int): Revenu de l'année

     Returns:
         str: Retourne le barème et les impots a pyer
     """    

     bareme = {
          11497: 0,
          29315: 11,
          83823: 30,
          180294: 41
     }

     # Si les revenus sont supérieurs à 180295
     if float(revenu) > 180295 :
          bareme_out = 45
     else :
          for i in bareme :

               if float(revenu) <= i :
                    bareme_out = bareme[i]
                    break

     impots = bareme_out * revenu / 100 
               
     return (f"Votre taux d'imposition est de {bareme_out}%, vous devrez payer {impots} €")

print(calc_impots(11400))