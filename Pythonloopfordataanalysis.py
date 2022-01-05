for i in ["p0p50", "p90p100", "p99p100"]:
    print(f"wid, indicators(sptinc) areas(IL) perc({i}) ages(992) pop(j) clear")
    print("drop country variable percentile age pop")
    print(f"rename value IncomeShare{i}")
    print(f'save "IsraelIncomeData{i}.dta", replace')
