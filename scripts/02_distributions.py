import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data\cleaned_data.csv')

# Grade Distribution by Gender
plt.style.use('dark_background')
custom_palette = ['#FF00FF', '#00FFFF']

plt.figure(dpi=150, figsize=(8, 5))
sns.countplot(data=df, x='Grade', hue='Gender', palette=custom_palette)

plt.title('Grade Distribution by Gender', fontsize=14, color='#00FFFF')
plt.xlabel('Grade', fontsize=12, color='white')
plt.ylabel('Count', fontsize=12, color='white')
plt.legend(title='Gender', title_fontsize='10', loc='lower right', facecolor='black', edgecolor='white')

plt.savefig('C:/AI/Projetcs/ML/students_score/images/Grade_Distribution_by_Gender.png', facecolor='black',
            dpi=300, bbox_inches='tight', transparent=True)
plt.show()

# Performance Across Departments
plt.style.use('dark_background')

box_color = '#4deeea'
edge_color = '#001eff'

plt.figure(dpi=150, figsize=(9, 5))
sns.boxplot(data=df, x='Department', y='Total_Score', color=box_color,
            linewidth=2, fliersize=3, boxprops=dict(edgecolor=edge_color),
            whiskerprops=dict(color=edge_color), capprops=dict(color=edge_color),
            medianprops=dict(color='white'), flierprops=dict(markerfacecolor=edge_color, marker='o'))

plt.title('Performance Across Departments', fontsize=14, color=box_color)
plt.xlabel('Department', fontsize=12, color='white')
plt.ylabel('Total Score', fontsize=12, color='white')

plt.savefig('C:/AI/Projetcs/ML/students_score/images/Performance_Across_Departments.png', facecolor='black', 
            dpi=300, bbox_inches='tight', transparent=True)
plt.show()

# Correlation Heatmap
plt.style.use('dark_background')
plt.figure(figsize=(15,7), dpi=150)
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('C:/AI/Projetcs/ML/students_score/images/Correlation_Heatmap.png', facecolor='black', 
            dpi=300, bbox_inches='tight', transparent=True)
plt.show()
