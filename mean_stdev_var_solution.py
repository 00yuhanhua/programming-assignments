
import statistics as s

def mean_stdev_var_solution(list_of_numbers: list[str]) -> float:

    mean = s.mean(list_of_numbers)
    standard = s.stdev(list_of_numbers)
    variance = s.variance(list_of_numbers)
    
    return mean, standard, variance

