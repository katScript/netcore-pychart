import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    df = pd.read_csv('./wwwroot/data/salaries.csv')

    top_company_location=df.company_location.value_counts()
    
    df_top_location=df[df.company_location.isin([i for i in top_company_location.index])]
    
    result = df_top_location.head(10).to_html(classes="table table-striped bg-light")
    
    text_file = open("Views/Page/DataTable/data10company.cshtml", "w")
    text_file.write(result)
    text_file.close()
    
    plt.clf()

    sns.barplot(x='work_year', y='salary_in_usd', data=df)
    plt.title('Salary in the last 3 year')
    plt.savefig('wwwroot/images/jobs/salary_last_3_year.png')
    plt.clf()

    top_company_location = df.company_location.value_counts()

    df_top_location = df[df.company_location.isin([i for i in top_company_location.index])]

    top_jobs = df.job_title.value_counts()[:10]

    n = df.shape[0]
    job_distribution = top_jobs * 100 / n
    job_distribution.plot(kind='pie', autopct='%1.0f%%', figsize=(15, 8))
    plt.title('Job Distribution among top 10 in demand job title')
    plt.savefig('wwwroot/images/jobs/job_title_10.png')
    plt.clf()

    df_top_jobs = df[df.job_title.isin([i for i in top_jobs.index])]

    plt.figure(figsize=(15, 8))
    ax = sns.barplot(x='job_title', y='salary_in_usd', data=df_top_jobs, hue='employment_type')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    plt.title('Salary VS top job titles with their respective employment type')
    plt.savefig('wwwroot/images/jobs/salary_top_job_title.png')
    plt.clf()

    plt.figure(figsize=(20, 10))
    ax = sns.boxplot(x='job_title', y='salary_in_usd', data=df_top_jobs, hue='experience_level')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    plt.title('Salary VS top job titles with their respective experience level')

    plt.savefig('wwwroot/images/jobs/salary_top_job_title_experience.png')
    plt.clf()

    
    
    
