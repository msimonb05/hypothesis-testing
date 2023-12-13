import os, sys
from math import *

# Removes traceback thingy
sys.tracebacklimit = 0

def main():
    while True:
        # Choices
        choice = int(input("Choices:\n" + 
                        "1  - Sample Mean Compared With Population Mean\n" +
                        "2  - Comparing Two Sample Means\n" +
                        "3  - Comparing Two Sample Means w/ Standard Deviations\n" +
                        "4  - Comparing Two Sample Proportions\n" +
                        "5  - (t-Test) Sample Mean Compared With Population Mean\n" + 
                        "6  - (t-Test) Comparing Two Sample Means w/ Equal Variances\n" +
                        "7  - (t-Test) Comparing Two Sample Means w/ Unequal Variances\n" +
                        "8  - (t-Test) Comparing Two Sample Means for Dependent or Correlated Sample\n" +
                        "9  - Pearson Product-Moment Correlation Coefficient\n" +
                        "10 - Sample z-score\n" +
                        "11 - Population z-score\n"
                        "\nChoose among the choices: "))

        # Sample Mean Compared With Population Mean
        if choice == 1:
            x = float(input("x = "))
            mu = float(input("mu = "))
            n = float(input("n = "))
            sigma = float(input("sigma = "))

            z_1 = (x - mu) * (sqrt(n)) / sigma

            print(f"-----\nz = {round(z_1, 3)}\n-----")
        # Comparing Two Sample Means
        elif choice == 2:
            x_1 = float(input("x_1 = "))
            x_2 = float(input("x_2 = "))
            n_1 = float(input("n_1 = "))
            n_2 = float(input("n_2 = "))
            sigma = float(input("sigma = "))

            inside_root = (1 / n_1) + (1 / n_2)
            z_2 = (x_1 - x_2) / (sigma * sqrt(inside_root))

            print(f"-----\nz = {round(z_2, 3)}\n-----")
        # Comparing Two Sample Means w/ Standard Deviations
        elif choice == 3:
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
        elif choice == 4:
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
        elif choice == 5:
            x = float(input("x = "))
            mu = float(input("mu = "))
            n = float(input("n = "))
            s = float(input("s = "))

            t_1 = (x - mu) * (sqrt(n)) / s

            print(f"-----\nt = {round(t_1, 3)}\n-----")
        # (t-Test) Comparing Two Sample Means w/ Equal Variances
        elif choice == 6:
            x_1 = float(input("x_1 = "))
            x_2 = float(input("x_2 = "))
            s_1 = float(input("s_1 = "))
            s_2 = float(input("s_2 = "))
            n_1 = float(input("n_1 = "))
            n_2 = float(input("n_2 = "))

            foo_1 = ((s_1 ** 2) * (n_1 - 1)) + ((s_2 ** 2) * (n_2 - 1))
            foo_2 = n_1 + n_2 - 2
            foo_3 = (1 / n_1) + (1 / n_2)
            foo_all = (foo_1 / foo_2) * foo_3

            t_2 = (x_1 - x_2) / sqrt(foo_all)

            print(f"-----\nt = {round(t_2, 3)}\n-----")
        # (t-Test) Comparing Two Sample Means w/ Unequal Variances
        elif choice == 7:
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
        elif choice == 8:
            d = float(input("d = "))
            n = float(input("n = "))
            s = float(input("s = "))

            t_4 = (d * (n ** 0.5)) / s

            print(f"-----\nz = {round(t_4, 3)}\n-----")
        # Pearson Product-Moment Correlation Coefficient
        elif choice == 9:
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
            if r > 0.99: print(f"-----\nr = {round(r, 3)} (Direct Positive Correlation)\n-----")
            
            elif 0.80 <= r <= 0.99: print(f"-----\nr = {round(r, 3)} (High Positive Correlation)\n-----")
            elif 0.60 <= r < 0.80: print(f"-----\nr = {round(r, 3)} (Moderately High Positive Correlation)\n-----")
            elif 0.40 <= r < 0.60: print(f"-----\nr = {round(r, 3)} (Moderate Positive Correlation)\n-----")
            elif 0.20 <= r < 0.40: print(f"-----\nr = {round(r, 3)} (Low Positive Correlation)\n-----")
            elif 0.01 <= r < 0.20: print(f"-----\nr = {round(r, 3)} (Negligible Positive Correlation)\n-----")
            
            elif r == 0: print(f"-----\nr = {round(r, 3)} (Zero Correlation)\n-----")
            
            elif -0.20 < r <= -0.01: print(f"-----\nr = {round(r, 3)} (Negligible Negative Correlation)\n-----")
            elif -0.40 < r <= -0.20: print(f"-----\nr = {round(r, 3)} (Low Negative Correlation)\n-----")
            elif -0.60 < r <= -0.40: print(f"-----\nr = {round(r, 3)} (Moderate Negative Correlation)\n-----")
            elif -0.80 < r <= -0.60: print(f"-----\nr = {round(r, 3)} (Moderately High Negative Correlation)\n-----")
            elif -0.99 <= r <= -0.80: print(f"-----\nr = {round(r, 3)} (High Negative Correlation)\n-----")
            
            elif r < -0.99: print(f"-----\nr = {round(r, 3)} (Direct Negative Correlation)\n-----")
        # Sample z-score
        elif choice == 10:
            x = float(input("x = "))
            mean = float(input("mean = "))
            sd = float(input("sd = "))

            z_score1 = (x - mean) / sd

            print(f"-----\nz = {round(z_score1, 3)}\n-----")
        # Population z-score
        elif choice == 11:
            x = float(input("x = "))
            mu = float(input("mu = "))
            sigma = float(input("sigma = "))

            z_score2 = (x - mu) / sigma

            print(f"-----\nz = {round(z_score2, 3)}\n-----")
        # Invalid Choice
        else:
            print("-----\nEnter valid choice.\n-----")

if __name__ == "__main__":
    print("\nHypothesis Testing\nby: Markymatics\n\n" +
          ">>> NOTE: Press Ctrl + C to quit. <<<\n")
    try:
        main()
    except ValueError:
        print("-----\nInvalid input.\n-----")
        os.system("python hypothesis_testing.py")
    except KeyboardInterrupt:
        print("\n-----\nQuitting program.\n-----")
        pass