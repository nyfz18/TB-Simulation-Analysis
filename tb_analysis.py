import pandas as pd
import matplotlib.pyplot as plt

# --- PROMPT 1: Reading CSV into script, displaying summary of first 5 

# Read the file 
csv_filename = "Code_Assessment_Data.csv"
df = pd.read_csv(csv_filename)

# printed in terminal
print("First 5 Rows")
print(df.head())

num_rows, num_cols = df.shape
print(f"\nNumber of Rows: {num_rows}")
print(f"\nNumber of Columns: {num_cols}")

# --- PROMPT 2: Create plot showing distribution of "Ave Life-months" in years
# set to figure size 8,5 for viewing so graph isn't squished
plt.figure(figsize=(8,5))
df['Ave Life-years'] = df['Ave Life-months'] / 12
# using histogram to analyze distribution 
plt.hist(df['Ave Life-years'], bins=10)
plt.title('Distribution of Average Life-Years Across Simulation Runs', fontweight='bold')
plt.xlabel('Average Life-Years')
plt.ylabel('Frequency (Number of Runs)')

# formatting for easier view
plt.grid(linestyle='--')
plt.tight_layout()

# saving file as png. dpi = 300 for standard high res quailty
plt.savefig('distribution_life_years.png', dpi = 300)

# --- PROMPT 3: Average Life-months vs. Lifetime costs 

# using scatterplot to analyze the relationship
plt.figure(figsize=(8,5))
plt.scatter(df['Ave Life-months'], df['Lifetime Costs'])
plt.title('Lifetime Costs vs. Average Life-Months', fontweight='bold')
plt.xlabel('Average Life-Months')
plt.ylabel('Lifetime Costs (USD)')
# formatting for easier view 
plt.grid(linestyle = "--")
plt.tight_layout()

plt.savefig('life_months_vs_costs.png', dpi=300)

# --- PROMPT 4: Calculate the ratio of new TB infection to TB activations, save to new CSV 
ratios_df = pd.DataFrame({'Run ID': df['Run ID']})

# 3 years of data: 36 months 
for m in range(36):
    infect_col = f"Month {m} New TB infections"
    active_col = f"Month {m} TB activations"
    ratio_col = f"Month_{m}_Ratio"

    ratios_df[ratio_col] = df[infect_col] / df[active_col]

# saving with print confirmation
ratios_df.to_csv("TB_ratios.csv", index=False)
print("\nSuccessfully saved to 'TB_ratios.csv'.")
