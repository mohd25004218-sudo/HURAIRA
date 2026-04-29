import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)

students = ['Student_' + str(i) for i in range(1, 21)]
subjects = ['Math', 'Science', 'English', 'History', 'Computer']


data = np.random.randint(40, 101, size=(20, 5))

df = pd.DataFrame(data, columns=subjects)
df.insert(0, 'Name', students)

print("Student Data:\n")
print(df)


df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1)

print("\nStatistical Summary:\n")
print(df.describe())


print("\nSubject-wise Statistics:\n")
for subject in subjects:
    print(f"{subject}: Mean={df[subject].mean():.2f}, "
          f"Median={df[subject].median()}, "
          f"Std={df[subject].std():.2f}")


high_performers = df[df['Average'] >= 75]
low_performers = df[df['Average'] < 50]

print("\nHigh Performing Students:\n", high_performers[['Name', 'Average']])
print("\nLow Performing Students:\n", low_performers[['Name', 'Average']])


subject_means = df[subjects].mean()




plt.figure()
subject_means.plot(kind='bar')
plt.title("Average Score per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()


plt.figure()
plt.plot(df['Name'], df['Total'], marker='o')
plt.title("Total Scores of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.show()


plt.figure()
plt.hist(df['Total'], bins=10)
plt.title("Distribution of Total Scores")
plt.xlabel("Total Marks")
plt.ylabel("Frequency")
plt.show()


plt.figure()
plt.pie(subject_means, labels=subjects, autopct='%1.1f%%')
plt.title("Subject-wise Contribution")
plt.show()


print("\nInsights:\n")
print("- Subjects with highest average:", subject_means.idxmax())
print("- Subjects with lowest average:", subject_means.idxmin())
print("- Overall class average:", df['Average'].mean())
print("- Number of high performers:", len(high_performers))
print("- Number of low performers:", len(low_performers))