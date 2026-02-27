

import csv
import statistics


def get_manual_input():
    data = []
    try:
        # Prompt for the number of classes/subjects
        num_classes = int(input("How many classes/subjects do you want to enter? "))

        for c in range(1, num_classes + 1):
            print(f"\n=== Class {c} of {num_classes} ===")
            sub_name = input("Subject Name: ").strip()
            sub_id = input("Subject ID: ").strip()

            num_students = int(input(f"How many students are in {sub_name}? "))

            for i in range(1, num_students + 1):
                print(f"\n--- Student {i} of {num_students} ({sub_name}) ---")
                stu_id = input("Student ID: ").strip()
                f_name = input("First Name: ").strip()
                l_name = input("Last Name: ").strip()

                student_grades = []
                print(f"Enter grades for {f_name} (type 'done' when finished):")
                while True:
                    grade_input = input("  > Grade: ").strip().lower()
                    if grade_input == 'done':
                        break
                    try:
                        student_grades.append(float(grade_input))
                    except ValueError:
                        print("    ! Invalid input. Enter a number or 'done'.")

                if student_grades:
                    # Store data grouped by subject naturally
                    data.append([sub_name, sub_id, stu_id, f_name, l_name, student_grades])
                else:
                    print(f"    ! No grades entered for {f_name}. Skipping student.")

    except ValueError:
        print("Invalid input. Please enter numbers for counts.")
    return data


def read_from_file(filename):
    data = []
    try:
        with open(filename, mode='r') as file:
            # Detect extension; use comma for CSV, tab for TXT
            delim = ',' if filename.endswith('.csv') else '\t'
            reader = csv.reader(file, delimiter=delim)

            next(reader, None)  # Skip header
            for row in reader:
                if len(row) >= 6:
                    # Format: SubName, SubID, StuID, First, Last, Grade1, Grade2...
                    metadata = row[:5]
                    grades = [float(g) for g in row[5:] if g.strip()]
                    data.append(metadata + [grades])
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return data


def process_gradebook(all_data):
    # Group students by Subject Name
    subject_map = {}
    for entry in all_data:
        sub_name = entry[0]
        if sub_name not in subject_map:
            subject_map[sub_name] = []
        subject_map[sub_name].append(entry)

    final_csv_rows = []

    print("\n" + "=" * 65)
    print(f"{'GRADEBOOK SUMMARY REPORT':^65}")
    print("=" * 65)

    for sub_name, students in subject_map.items():
        all_scores_in_subject = []
        sub_id = students[0][1]  # Get SubID from the first entry in group

        print(f"\nSUBJECT: {sub_name.upper()} (ID: {sub_id})")
        print(f"{'ID':<10} {'Student Name':<25} {'Avg Grade':<12}")
        print("-" * 50)

        subject_results = []

        for s in students:
            # Index map: 0:Sub, 1:SubID, 2:StuID, 3:First, 4:Last, 5:[Grades]
            s_name = f"{s[3]} {s[4]}"
            s_avg = statistics.mean(s[5])
            all_scores_in_subject.extend(s[5])

            print(f"{s[2]:<10} {s_name:<25} {s_avg:<12.2f}")
            subject_results.append([s[0], s[1], s[2], s[3], s[4], round(s_avg, 2)])

        # Calculate class mean
        class_mean = statistics.mean(all_scores_in_subject)
        print(f"\n>> Class Average for {sub_name}: {class_mean:.2f}")

        # Finalize data for CSV
        for row in subject_results:
            row.append(round(class_mean, 2))
            final_csv_rows.append(row)

    # Export to CSV
    output_file = 'final_gradebook.csv'
    try:
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Subject', 'Sub_ID', 'Stu_ID', 'First', 'Last', 'Student_Avg', 'Class_Mean'])
            writer.writerows(final_csv_rows)
        print(f"\n[Success] Data written to '{output_file}'")
    except Exception as e:
        print(f"Error saving file: {e}")


def main():
    print("Welcome to the Organized Gradebook System")
    print("1. Manual Class Entry")
    print("2. Load from File")
    choice = input("Selection: ")

    if choice == '1':
        data = get_manual_input()
    elif choice == '2':
        fname = input("Enter filename (csv/txt): ")
        data = read_from_file(fname)
    else:
        print("Invalid choice.")
        return

    if data:
        process_gradebook(data)
    else:
        print("No data recorded.")


if __name__ == "__main__":
    main()
