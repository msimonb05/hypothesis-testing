import os, sys
from math import *

# Removes traceback thingy
sys.tracebacklimit = 0

class HypothesisTesting:
    # Choices: z-test, t-test, Pearson's r
    def __init__(self):
        self.choices = {
            1: ("Sample z-score", 
                self.sample_z_score),
            2: ("Population z-score", 
                self.population_z_score),
            3: ("Sample Mean Compared With Population Mean", 
                self.Z_sampleMean_vs_populationMean),
            4: ("Comparing Two Sample Means", 
                self.Z_compare_two_sampleMean),
            5: ("Comparing Two Sample Means w/ Standard Deviations", 
                self.Z_compare_two_sampleMeanWithSd),
            6: ("Comparing Two Sample Proportions", 
                self.Z_compare_two_sampleProportions),
            7: ("(t-Test) Sample Mean Compared With Population Mean", 
                self.T_sampleMean_vs_populationMean),
            8: ("(t-Test) Comparing Two Sample Means w/ Equal Variances", 
                self.T_compare_two_sampleMeanEqualVar),
            9: ("(t-Test) Comparing Two Sample Means w/ Unequal Variances", 
                self.T_compare_two_sampleMeanUnequalVar),
            10: ("(t-Test) Comparing Two Sample Means for Dependent or Correlated Sample", 
                self.T_compare_two_sampleMeanDependent),
            11: ("Pearson Product-Moment Correlation Coefficient", 
                self.P_correlationCoefficient)
        }
    
    # Sample z-score
    def sample_z_score(self):
        x = float(input("x = "))
        mean = float(input("mean = "))
        sd = float(input("sd = "))

        z_score1 = (x - mean) / sd

        print(f"-----\nz = {round(z_score1, 3)}\n-----")
    
    # Population z-score
    def population_z_score(self):
        x = float(input("x = "))
        mu = float(input("mu = "))
        sigma = float(input("sigma = "))

        z_score2 = (x - mu) / sigma

        print(f"-----\nz = {round(z_score2, 3)}\n-----")
    
    # Sample Mean Compared With Population Mean
    def Z_sampleMean_vs_populationMean(self):
        x = float(input("x = "))
        mu = float(input("mu = "))
        n = float(input("n = "))
        sigma = float(input("sigma = "))

        z_1 = (x - mu) * (sqrt(n)) / sigma

        print(f"-----\nz = {round(z_1, 3)}\n-----")
    
    # Comparing Two Sample Means
    def Z_compare_two_sampleMean(self):
        x_1 = float(input("x_1 = "))
        x_2 = float(input("x_2 = "))
        n_1 = float(input("n_1 = "))
        n_2 = float(input("n_2 = "))
        sigma = float(input("sigma = "))

        inside_root = (1 / n_1) + (1 / n_2)
        z_2 = (x_1 - x_2) / (sigma * sqrt(inside_root))

        print(f"-----\nz = {round(z_2, 3)}\n-----")
    
    # Comparing Two Sample Means w/ Standard Deviations
    def Z_compare_two_sampleMeanWithSd(self):
        x_1 = float(input("x_1 = "))
        x_2 = float(input("x_2 = "))
        s_1 = float(input("s_1 = "))
        s_2 = float(input("s_2 = "))
        n_1 = float(input("n_1 = "))
        n_2 = float(input("n_2 = "))

        inside_root = ((s_1 ** 2) / n_1) + ((s_2 ** 2) / n_2)
        z_3 = (x_1 - x_2) / sqrt(inside_root)

        print(f"-----\nz = {round(z_3, 3)}\n-----")
    
    # Comparing Two Sample Proportions
    def Z_compare_two_sampleProportions(self):
        p_1 = float(input("p_1 = "))
        p_2 = float(input("p_2 = "))
        q_1 = float(input("q_1 = "))
        q_2 = float(input("q_2 = "))
        n_1 = float(input("n_1 = "))
        n_2 = float(input("n_2 = "))

        inside_root = ((p_1 * q_1) / n_1) + ((p_2 * q_2) / n_2)
        z_4 = (p_1 - p_2) / (sqrt(inside_root))

        print(f"-----\nz = {round(z_4, 3)}\n-----")
    
    # (t-Test) Sample Mean Compared With Population Mean
    def T_sampleMean_vs_populationMean(self):
        x = float(input("x = "))
        mu = float(input("mu = "))
        n = float(input("n = "))
        s = float(input("s = "))

        t_1 = (x - mu) * (sqrt(n)) / s

        print(f"-----\nt = {round(t_1, 3)}\n-----")
    
    # (t-Test) Comparing Two Sample Means w/ Equal Variances
    def T_compare_two_sampleMeanEqualVar(self):
        x_1 = float(input("x_1 = "))
        x_2 = float(input("x_2 = "))
        s_1 = float(input("s_1 = "))
        s_2 = float(input("s_2 = "))
        n_1 = float(input("n_1 = "))
        n_2 = float(input("n_2 = "))

        temp_1 = ((s_1 ** 2) * (n_1 - 1)) + ((s_2 ** 2) * (n_2 - 1))
        temp_2 = n_1 + n_2 - 2
        temp_3 = (1 / n_1) + (1 / n_2)
        temp_all = (temp_1 / temp_2) * temp_3

        t_2 = (x_1 - x_2) / sqrt(temp_all)

        print(f"-----\nt = {round(t_2, 3)}\n-----")
    
    # (t-Test) Comparing Two Sample Means w/ Unequal Variances
    def T_compare_two_sampleMeanUnequalVar(self):
        x_1 = float(input("x_1 = "))
        x_2 = float(input("x_2 = "))
        s_1 = float(input("s_1 = "))
        s_2 = float(input("s_2 = "))
        n_1 = float(input("n_1 = "))
        n_2 = float(input("n_2 = "))

        inside_root = ((s_1 ** 2) / n_1) + ((s_2 ** 2) / n_2)
        t_3 = (x_1 - x_2) / sqrt(inside_root)

        print(f"-----\nz = {round(t_3, 3)}\n-----")
    
    # (t-Test) Comparing Two Sample Means for Dependent or Correlated Sample
    def T_compare_two_sampleMeanDependent(self):
        d = float(input("d = "))
        n = float(input("n = "))
        s = float(input("s = "))

        t_4 = (d * (n ** 0.5)) / s

        print(f"-----\nz = {round(t_4, 3)}\n-----")
    
    # Pearson Product-Moment Correlation Coefficient
    def P_correlationCoefficient(self):
        n = float(input("n = "))
        sum_x = float(input("sum of x = "))
        sum_y = float(input("sum of y = "))
        sum_x2 = float(input("sum of x^2 = "))
        sum_y2 = float(input("sum of y^2 = "))
        sum_xy = float(input("sum of x*y = "))

        r_num = (n * sum_xy) - (sum_x * sum_y)
        r_den1 = (n * sum_x2) - (sum_x ** 2)
        r_den2 = (n * sum_y2) - (sum_y ** 2)
        r_denRoot = sqrt(r_den1 * r_den2)
            
        r = r_num / r_denRoot

        # Degree of Relationship
        match r:
            case r if (r > 0.99):
                degree = "Direct Positive Correlation"
            case r if (0.80 <= r <= 0.99):
                degree = "High Positive Correlation"
            case r if (0.60 <= r < 0.80):
                degree = "Moderately High Positive Correlation"
            case r if (0.40 <= r < 0.60):
                degree = "Moderate Positive Correlation"
            case r if (0.20 <= r < 0.40):
                degree = "Low Positive Correlation"
            case r if (0.01 <= r < 0.20):
                degree = "Negligible Positive Correlation"
            case r if (r == 0):
                degree = "Zero Correlation"
            case r if (-0.20 < r <= -0.01):
                degree = "Negligible Negative Correlation"
            case r if (-0.40 < r <= -0.20):
                degree = "Low Negative Correlation"
            case r if (-0.60 < r <= -0.40):
                degree = "Moderate Negative Correlation"
            case r if (-0.80 < r <= -0.60):
                degree = "Moderately High Negative Correlation"
            case r if (-0.99 <= r <= -0.80):
                degree = "High Negative Correlation"
            case r if r < -0.99:
                degree = "Direct Negative Correlation"
        
        print(f"-----\nr = {round(r, 3)} ({degree})\n-----")        

    # Exception test
    def main(self):
        while True:
            # Input choice
            try:
                choice = int(input("Choices:\n" + 
                                   "\n".join([f"{i}  - {desc}" for i, (desc, _) in self.choices.items()]) + 
                                   "\n\nChoose among the choices: "))
                # If int input is not in choices
                if choice not in self.choices:
                    raise ValueError("Invalid choice.")
                else: 
                    selected_choice = self.choices[choice][1]
                    selected_choice()
            # Wrong input
            except ValueError:
                print("-----\nInvalid input.\n-----")
                os.system("python hypothesis_testing.py")
            # If Ctrl + C is pressed
            except KeyboardInterrupt:
                print("\n-----\nQuitting program.\n-----")
                break

# Main
if __name__ == "__main__":
    print("\nHypothesis Testing\nby: Markymatics\n\n" +
          ">>> NOTE: Press Ctrl + C to quit. <<<\n")
    hypothesis_testing = HypothesisTesting()
    hypothesis_testing.main()