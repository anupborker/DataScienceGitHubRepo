import matplotlib.pyplot as plt

def read_csv_data(csv_file_path):
    gpa_scores = []
    genders = []

    with open(csv_file_path, 'r') as f:
        header = f.readline().strip().split(',')

        if 'GPA' not in header or 'Gender' not in header:
            print("Error: Columns 'GPA' or 'Gender' not found in CSV header.")
            return gpa_scores, genders

        for line in f:
            fields = line.strip().split(',')

            try:
                gpa = float(fields[header.index('GPA')])
                if gpa != gpa:
                    continue

                gender = fields[header.index('Gender')].strip()
                if gender == '':
                    continue

                gpa_scores.append(gpa)
                genders.append(gender)

            except ValueError:
                continue

    return gpa_scores, genders

def calculate_pass_fail_counts(gpa_scores, threshold_gpa):
    below_threshold_count = sum(1 for gpa in gpa_scores if gpa < threshold_gpa)
    above_threshold_count = len(gpa_scores) - below_threshold_count
    return below_threshold_count, above_threshold_count

def calculate_gender_counts(genders):
    gender_counts = {}
    for gender in genders:
        if gender in gender_counts:
            gender_counts[gender] += 1
        else:
            gender_counts[gender] = 1
    return gender_counts

def plot_pie_chart(ax, sizes, labels, colors, title):
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)
    ax.axis('equal')

if __name__ == "__main__":
    csv_file_path = r'C:\Users\Student\Desktop\Anup Borker\Data Science Lab\Expt 1\Data_Exp1.csv'
    threshold_gpa = 3.5
    colors_gpa = ['red', 'blue']
    colors_gender = ['green', 'yellow']

    gpa_scores, genders = read_csv_data(csv_file_path)
    below_threshold_count, above_threshold_count = calculate_pass_fail_counts(gpa_scores, threshold_gpa)
    gender_counts = calculate_gender_counts(genders)

    sizes_gpa = [below_threshold_count, above_threshold_count]
    labels_gpa = ['Fail', 'Pass']
    sizes_gender = list(gender_counts.values())
    labels_gender = list(gender_counts.keys())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    plot_pie_chart(ax1, sizes_gpa, labels_gpa, colors_gpa, 'Pie Chart for Pass and Failed Students')
    plot_pie_chart(ax2, sizes_gender, labels_gender, colors_gender, 'Pie Chart for Genders')

    plt.tight_layout()
    plt.show()
