def main():
    """demo function to display usage"""
    
    sample_formula = [(100, 1.4, 0.475), (60, 0.973, 0.92), (7.5, 1.008, 1.56),
                      (20, 2.71, 0.0625)]
    spg, cost_wt, cost_vol = spg_costs(sample_formula)
    duro, modulus, tensile, elongation, clashberg, brittle = flex_clear_dinp(28)
    print('${} per pound'.format(cost_wt))
    print('${} per volume'.format(cost_vol))
    print('{} specific gravity (ASTM D792)'.format(spg))
    print(duro, 'A Shore Durometer @ 15s delay (ASTM D2240)')
    print(modulus, 'psi Modulus @ 100% elongation (ASTM D638)')
    print(tensile, 'psi Tensile Strength (ASTM D638)')
    print(elongation, '% Ultimate Elongation (ASTM D638)')
    print(clashberg, 'degrees Celsius Clash-Berg (ASTM D1043 Tf @ 135,000psi)')
    print(brittle, 'degrees Celsius Brittleness (ASTM D746)')
    print('*****************')
    print('above data was for an unfilled formula')
    print('*****************')
    print('below is for filled formula')
    duro_filled = flex_filled(duro, 20)
    print(duro_filled, 'A Shore Durometer @ 15s delay (ASTM D2240)')

def spg_costs(formula):
    """takes formula, returns specific gravity and cost per pound and volume"""
    recipe = []
    sum_phr = sum_pound_volumes = sum_costs = 0
    for ingredient in formula:
        pound_volumes = ingredient[0] / ingredient[1]
        line_cost = ingredient[0] * ingredient[2]
        recipe_data = [ingredient[0], pound_volumes, line_cost]
        recipe.append(recipe_data)
    for item in recipe:
        sum_phr = sum_phr + item[0]
        sum_pound_volumes = sum_pound_volumes + item[1]
        sum_costs = sum_costs + item[2]
    formula_cost = sum_costs / sum_phr
    formula_spg = sum_phr / sum_pound_volumes
    volume_cost = formula_cost * formula_spg
    output = (formula_spg, formula_cost, volume_cost)
    return output

def spg(formula):
    recipe = []
    sum_phr = sum_pound_volumes = 0
    for ingredient in formula:
        pound_volumes = ingredient[0] / ingredient[1]
        recipe_data = [ingredient[0], pound_volumes]
        recipe.append(recipe_data)
    for item in recipe:
        sum_phr = sum_phr + item[0]
        sum_pound_volumes = sum_pound_volumes + item[1]
    formula_spg = sum_phr / sum_pound_volumes
    return formula_spg

def flex_clear_dop(phr):
    duro = 113.9 - 0.64*phr
    modulus = 3548-36.56*phr
    tensile = 4700.4-34.41*phr
    elongation = 228.5+1.99*phr
    clashberg = 15.2-.8*phr
    brittle = -4.41-.57*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dinp(phr):
    duro = 113.8 - 0.6*phr
    modulus = 3559.1 - 34.78*phr
    tensile = 4414.8 - 28.7*phr
    elongation = 248.6 + 1.61*phr
    clashberg = 14.23 - 0.76*phr
    brittle = -4.19 - 0.55*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_didp(phr):
    duro = 115.8 - 0.61*phr
    modulus = 3595.4-34.11*phr
    tensile = 4424.1-28.68*phr
    elongation = 261.1+1.32*phr
    clashberg = 13.42-.74*phr
    brittle = -3.89-.56*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_doa(phr):
    duro = 110 - 0.63*phr
    modulus = 2496.3 - 25.93*phr
    tensile = 4480.7-34.81*phr
    elongation = 268.7+1.93*phr
    clashberg = -4.78-.97*phr
    brittle = -40.68-.44*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dina(phr):
    duro = 107.8 - 0.544*phr
    modulus = 2558.2-22.6*phr
    tensile = 4083.3-26.67*phr
    elongation = 269.5+1.59*phr
    clashberg = -11.01-.79*phr
    brittle = -44.8-.38*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_totm(phr):
    duro = 118.1 - .632*phr
    modulus = 3675.8-33.7*phr
    tensile = 4323.5-25.7*phr
    elongation = 239.6+1.65*phr
    clashberg = 19.88-.78*phr
    brittle = -13.29-.41*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_tintm(phr):
    duro = 117.6 - .558*phr
    modulus = 3798.9-32.6*phr
    tensile = 4128.9-22.4*phr
    elongation = 262.7+.91*phr
    clashberg = 17.49-.73*phr
    brittle = -14.39-.36*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dotp(phr):
    duro = 113.8 - 0.617*phr
    modulus = 3650.3-35.4*phr
    tensile = 4419.7-26.8*phr
    elongation = 250.9+1.96*phr
    clashberg = 10.8-.77*phr
    brittle = -4.7-.57*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dphp(phr):
    duro = 116 - 0.599*phr
    modulus = 3611.6-34.8*phr
    tensile = 4282.1-25.8*phr
    elongation = 197.6+2.25*phr
    clashberg = 12.95-.75*phr
    brittle = -8.04-.45*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dinch(phr):
    duro = 115.2 - 0.602*phr
    modulus = 3124.3-28.3*phr
    tensile = 4274.7-26.3*phr
    elongation = 335.1+.6*phr
    clashberg = 11.64-.79*phr
    brittle = -6.71-.57*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_711p(phr):
    duro = 114.4 - 0.657*phr
    modulus = 3577.1-37.1*phr
    tensile = 4550-32*phr
    elongation = 253.4+1.77*phr
    clashberg = 11.4-.86*phr
    brittle = -10.3-.61*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_9p(phr):
    duro = 114.2 - 0.645*phr
    modulus = 3384.2-35.5*phr
    tensile = 4479.1-31.2*phr
    elongation = 259+1.72*phr
    clashberg = 7.6-.84*phr
    brittle = -8.3-.66*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_911p(phr):
    duro = 113.2 - 0.596*phr
    modulus = 3462.2-32.4*phr
    tensile = 4304.4-28.9*phr
    elongation = 227.3+1.33*phr
    clashberg = 5.7-.8*phr
    brittle = -12.29-.62*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_dup(phr):
    duro = 115 - 0.574*phr
    modulus = 3457.3-32.7*phr
    tensile = 4449.7-32.4*phr
    elongation = 273+.74*phr
    clashberg = 5-.79*phr
    brittle = -15.4-.62*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_clear_eso(phr):
    eso_in_dop = phr/1.1
    duro = 111 - 0.627*eso_in_dop
    modulus = 3548-36.56*phr
    tensile = 4700.4-34.41*phr
    elongation = 228.5+1.99*phr
    clashberg = 15.2-.8*phr
    brittle = -4.41-.57*phr
    output = (duro, modulus, tensile, elongation, clashberg, brittle)
    return output

def flex_filled(duro_A, phr_CaCO3):
    #linear r square 0.989, n = 27
    #duro = 0.929607437 * duro_A + 0.0531305301 * phr_CaCO3 + 6.270608278
    #polynomial r square 0.992, n=27
    a = -0.001058114988 * duro_A * duro_A
    b = -0.001695411881 * duro_A * phr_CaCO3
    c = 0.00004967760719 * phr_CaCO3 * phr_CaCO3
    d = 1.158214659 * duro_A
    e = 0.1840327098 * phr_CaCO3
    f = -5.05711084
    duro = a + b + c + d + e + f
    return duro

def duro_AtoD(duro_A):
    #converter {k:v, A Shore:D Shore, another set of A/D, so on}
    converter = {120:84, 115:84, 110:75.8, 105:66.8,
                 100:58, 95:46, 90:39, 85:33, 80:29, 75:25, 70:22,
                 65:19, 60:16, 55:14, 50:12, 45:10, 40:8, 35:7, 30:6}
    test_A = (duro_A // 5)*5
    if test_A >= 118.2:
        output = 84
    elif test_A <=30:
        output = 6
    else:
        total_gap_up = converter[test_A + 5] - converter[test_A]
        share_gap_up = (duro_A - test_A)/5
        partial_adjust = total_gap_up * share_gap_up
        output = converter[test_A] + partial_adjust
    return output

def rigid_nano07(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.990, n = 16
    flex_a = 0.0740909091 * phr_filler * phr_filler
    flex_b = -0.1265714286 * phr_filler * phr_impact_modifier
    flex_c = 0.265625 * phr_impact_modifier * phr_impact_modifier
    flex_d = 0.2065324675 * phr_filler
    flex_e = -9.682321429 * phr_impact_modifier
    flex_f = 499.1600325
    flex_mod = flex_a + flex_b + flex_c + flex_d + flex_e + flex_f

    #notched izod polynomial r squared = 0.765, n = 46
    notch_a = 2.397884026 * phr_filler * phr_filler
    notch_b = 5.914428509 * phr_filler * phr_impact_modifier
    notch_c = -1.873679882 * phr_impact_modifier * phr_impact_modifier
    notch_d = 14.09969499 * phr_filler
    notch_e = 82.8909861 * phr_impact_modifier
    notch_f = -183.6350482
    notch = notch_a + notch_b + notch_c + notch_d + notch_e + notch_f
    return(flex_mod, notch)


def rigid_nano3(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.986, n = 16
    flex_a = 0.0540909091 * phr_filler * phr_filler
    flex_b = -0.2594285714 * phr_filler * phr_impact_modifier
    flex_c = 0.0625 * phr_impact_modifier * phr_impact_modifier
    flex_d = 2.415103896 * phr_filler
    flex_e = -8.306428571 * phr_impact_modifier
    flex_f = 498.0761039
    flex_mod = flex_a + flex_b + flex_c + flex_d + flex_e + flex_f

    #notched izod polynomial r squared = 0.761, n = 16
    notch_a = -0.2129545455 * phr_filler * phr_filler
    notch_b = 0.9097142857 * phr_filler * phr_impact_modifier
    notch_c = -23.34375 * phr_impact_modifier * phr_impact_modifier
    notch_d = 79.34926623 * phr_filler
    notch_e = 265.3782143 * phr_impact_modifier
    notch_f = -344.6062338
    notch = notch_a + notch_b + notch_c + notch_d + notch_e + notch_f
    return(flex_mod, notch)

def rigid_nano7(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.976, n = 16
    flex_a = 0.0045454545 * phr_filler * phr_filler
    flex_b = -1.857142857 * phr_filler * phr_impact_modifier
    flex_c = 0.09375 * phr_impact_modifier * phr_impact_modifier
    flex_d = 3.398051948 * phr_filler
    flex_e = -8.248214286 * phr_impact_modifier
    flex_f = 497.5230519
    flex_mod = flex_a + flex_b + flex_c + flex_d + flex_e + flex_f

    #notched izod polynomial r squared = 0.783, n = 16
    notch_a = 1.348181818 * phr_filler * phr_filler
    notch_b = 11.25028571 * phr_filler * phr_impact_modifier
    notch_c = 0.25 * phr_impact_modifier * phr_impact_modifier
    notch_d = -1.717220779 * phr_filler
    notch_e = 62.53428571 * phr_impact_modifier
    notch_f = -68.33922078
    notch = notch_a + notch_b + notch_c + notch_d + notch_e + notch_f
    return(flex_mod, notch)

def rigid_2micron(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.977, n = 16
    flex_a = 0.1375 * phr_filler * phr_filler
    flex_b = 0.085 * phr_filler * phr_impact_modifier
    flex_c = 0.484375 * phr_impact_modifier * phr_impact_modifier
    flex_d = 0.3675 * phr_filler
    flex_e = -10.85625 * phr_impact_modifier
    flex_f = 498.775
    flex_mod = flex_a + flex_b + flex_c + flex_d + flex_e + flex_f

    #notched izod polynomial r squared = 0.932, n = 16
    notch_a = -0.0125 * phr_filler * phr_filler
    notch_b = -0.765 * phr_filler * phr_impact_modifier
    notch_c = 0.953125 * phr_impact_modifier * phr_impact_modifier
    notch_d = 3.8275 * phr_filler
    notch_e = 12.83125 * phr_impact_modifier
    notch_f = 73.45
    notch = notch_a + notch_b + notch_c + notch_d + notch_e + notch_f
    return(flex_mod, notch)


def rigid_3micron(phr_filler, phr_impact_modifier):
    #flexural modulus polynomial r squared = 0.995, n = 16
    flex_a = 0.11 * phr_filler * phr_filler
    flex_b = -0.38 * phr_filler * phr_impact_modifier
    flex_c = 0.03125 * phr_impact_modifier * phr_impact_modifier
    flex_d = 1.774 * phr_filler
    flex_e = -8.6775 * phr_impact_modifier
    flex_f = 499.145
    flex_mod = flex_a + flex_b + flex_c + flex_d + flex_e + flex_f

    #notched izod polynomial r squared = 0.852, n = 16
    notch_a = 0.28 * phr_filler * phr_filler
    notch_b = -0.952 * phr_filler * phr_impact_modifier
    notch_c = 1.09375 * phr_impact_modifier * phr_impact_modifier
    notch_d = -3.204 * phr_filler
    notch_e = 10.0775 * phr_impact_modifier
    notch_f = 78.405
    notch = notch_a + notch_b + notch_c + notch_d + notch_e + notch_f
    return(flex_mod, notch)

def density_blend(density1, parts1, density2, parts2):
    #https://www.4spe.org/i4a/doclibrary/getfile.cfm?doc_id=20257
    #takes 2 PE grades and calculates out the density using rule of mixtures
    #can use parts or percent, it will make it to 100% though no matter what
    #this isn't a bad estimate of tensile and flexural properties of PE blends either
    #this isn't a horrible estimate of melt index, but the melt_index_blend() below is way better
    #this is a horrible estimate of impact properties, do not use this here
    percent1 = parts1 / (parts1 + parts2)
    percent2 = parts2 / (parts1 + parts2)
    return(percent1 * density1 + percent2 * density2)
    

def melt_index_blend(melt1, parts1, melt2, parts2):
    #https://www.4spe.org/i4a/doclibrary/getfile.cfm?doc_id=20257
    #this is logarithmic rule of mixtures
    #better estimate of melt index than rule of mixtures
    #I would use this for melt index PE
    percent1 = parts1 / (parts1 + parts2)
    percent2 = parts2 / (parts1 + parts2)
    blended_melt = (melt1**percent1) * (melt2**percent2)
    return(blended_melt)

def vistamaxx8880_blended_melt_flow(percent_vistamaxx8880, percent_vistamaxx6202):
    #takes an amount of ExxonMobil's Vistamaxx8880 and Vistamaxx6202 and returns the Melt Flow Rate at 230 C / 2.16kg in g/10 min terms
    #use ExxonMobil's Vistamaxx 8880 to reduce viscosity and promote flow, in particular with a mainline Vistamaxx product
    #should reduce molding costs too
    #should allow higher usage of filler to reduce costs also
    #less stress whitening, less need for process aid
    #higher output
    #check w/ ExxonMobil first, this data is likely only good for theory and in the range of the data available
    #going to extremes will likely just give an incorrect number
    #confirm everything in the lab, use tools like these to dial in your formula before going to lab
    #I would check this with the rule of mixtures and inverse for sanity check
    percent1 = percent_vistamaxx8880 / (percent_vistamaxx8880 + percent_vistamaxx6202)
    percent2 = percent_vistamaxx6202 / (percent_vistamaxx8880 + percent_vistamaxx6202)
    blended_melt = 107.7227 * percent1 - 44.6137 * percent2 + 63.109
    return(blended_melt)


def rule_of_mixtures(property1, parts1, property2, parts2):
    #simple rule of mixtures
    #the property is likely no more than this (ignoring a minor adjustment)
    #the property is likely no less than the inverse rule of mixtures
    #in practice with spg I and the PVC industry have always used inverse rule of mixtures
    #I would add back the typical difference from calculated to measured specific gravity as a constant
    percent1 = parts1 / (parts1 + parts2)
    percent2 = parts2 / (parts1 + parts2)
    return(percent1 * property1 + percent2 * property2)

def inverse_rule_of_mixtures(property1, parts1, property2, parts2):
    #inverse rule of mixtures
    #the property is likely no less than this
    #the property is likely no more than the rule of mixtures calculation
    #if you are costing out formulas, use this for sure
    #this is the same calculation as the spg_costs() and spg() functions
    percent1 = parts1 / (parts1 + parts2)
    percent2 = parts2 / (parts1 + parts2)
    output = ((percent1/property1)+(percent2/property2))**-1
    return(output)

def blended_property_range(property1, parts1, property2, parts2):
    #takes the material property and amount of two components in a blend and estimates that compound's blended property
    #returns the low and high estimate, the average of those, and a plus or minus for that average
    lo = inverse_rule_of_mixtures(property1, parts1, property2, parts2)
    hi = rule_of_mixtures(property1, parts1, property2, parts2)
    avg = (lo+hi)/2
    plusminus = hi-avg
    return(lo,hi,avg,plusminus)

 
    


#main program loop
if __name__ == "__main__":
    main()

