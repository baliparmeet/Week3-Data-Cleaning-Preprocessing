
import pandas as pd
import numpy as np

# Load the original dataset
df = pd.read_excel("yuvainterntask1.xlsx")

# Display the first five rows
print("First five rows:")
print(df.head())

# Display dataset information
print("\nDataset information:")
print(df.info())

# Display number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Calculate missing values
missing_values = df.isnull().sum()

# Calculate missing percentage
missing_percentage = (missing_values / len(df)) * 100

# Create a summary table
missing_summary = pd.DataFrame({
    'Missing Values': missing_values,
    'Missing Percentage': missing_percentage
})

# Show only columns with missing values
missing_summary = missing_summary[
    missing_summary['Missing Values'] > 0
]

print("\nMissing Values Summary:")
print(missing_summary.sort_values(
    by='Missing Percentage',
    ascending=False
))

# Check helpfulness and feedback counts
print("Helpfulness and feedback information:")

print(df[
    ['helpfulness',
     'total_feedback_count',
     'total_pos_feedback_count',
     'total_neg_feedback_count']
].describe())

# Check missing helpfulness with feedback count
print("\nHelpfulness missing vs feedback count:")

print(
    df[df['helpfulness'].isnull()]
    ['total_feedback_count']
    .value_counts()
    .head(10)
)

# Check records with missing review text
print("\nExamples of missing review text:")

print(
    df[df['review_text'].isnull()]
    [['rating', 'review_title', 'product_name']]
    .head(10)
)

# 1. Check rating values
print("Unique rating values:")
print(sorted(df['rating'].unique()))

# 2. Check recommendation values
print("\nRecommendation values:")
print(df['is_recommended'].value_counts(dropna=False))

# 3. Check feedback count consistency
print("\nFeedback consistency:")

feedback_check = (
    df['total_pos_feedback_count']
    + df['total_neg_feedback_count']
)

print(
    "Records where positive + negative feedback "
    "does not equal total feedback:",
    (feedback_check != df['total_feedback_count']).sum()
)

# 4. Check price statistics
print("\nPrice statistics:")
print(df['price_usd'].describe())

# 5. Check unusual prices
print("\nHighest 10 product prices:")
print(
    df[['product_name', 'brand_name', 'price_usd']]
    .sort_values(by='price_usd', ascending=False)
    .head(10)
)

# Detect outliers using IQR method

Q1 = df['price_usd'].quantile(0.25)
Q3 = df['price_usd'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)

# Identify potential outliers
outliers = df[
    (df['price_usd'] < lower_limit) |
    (df['price_usd'] > upper_limit)
]

print("\nNumber of potential price outliers:")
print(len(outliers))

print("\nPotential outlier products:")
print(
    outliers[['product_name', 'brand_name', 'price_usd']]
    .drop_duplicates()
    .sort_values(by='price_usd', ascending=False)
    .head(20)
)

# Check repeated review combinations

duplicate_reviews = df.duplicated(
    subset=['author_id', 'product_id', 'review_text'],
    keep=False
)

print("Repeated review combinations:")
print(duplicate_reviews.sum())

# Display repeated records
repeated_data = df[duplicate_reviews]

print("\nExamples of repeated reviews:")

print(
    repeated_data[
        ['author_id', 'product_id', 'rating', 'review_text']
    ].head(10)
)

print("First 10 values of Unnamed: 0:")
print(df['Unnamed: 0'].head(10))

print("\nLast 10 values of Unnamed: 0:")
print(df['Unnamed: 0'].tail(10))

print("\nDoes it match the DataFrame index?")
print(
    (df['Unnamed: 0'].to_numpy() == df.index.to_numpy()).all()
)

# Create a copy of the original dataset
cleaned_df = df.copy()

# Remove unnecessary index column
cleaned_df = cleaned_df.drop(columns=['Unnamed: 0'])

# Reset the index
cleaned_df = cleaned_df.reset_index(drop=True)

# Check the new dataset
print("Original dataset shape:", df.shape)

print("Cleaned dataset shape:", cleaned_df.shape)

print("\nRemaining columns:")
print(cleaned_df.columns.tolist())

print("\nFirst five rows:")
print(cleaned_df.head())

# Find repeated customer-product-review combinations
duplicate_groups = (
    df.groupby(
        ['author_id', 'product_id', 'review_text'],
        dropna=False
    )
    .size()
    .reset_index(name='repeat_count')
)

# Display combinations occurring more than once
duplicate_groups = duplicate_groups[
    duplicate_groups['repeat_count'] > 1
]

print("Repeated review groups:")
print(duplicate_groups)

print("\nTotal repeated groups:")
print(len(duplicate_groups))

print("\nTotal records in repeated groups:")
print(duplicate_groups['repeat_count'].sum())

# Identify repeated review combinations
duplicate_mask = df.duplicated(
    subset=['author_id', 'product_id', 'review_text'],
    keep=False
)

# Display all relevant repeated records
duplicate_details = df.loc[
    duplicate_mask,
    [
        'author_id',
        'product_id',
        'rating',
        'submission_time',
        'total_feedback_count',
        'is_recommended',
        'review_text'
    ]
].sort_values(
    by=['author_id', 'product_id', 'submission_time']
)

print("Detailed repeated review records:")
print(duplicate_details.to_string(index=False))

# Sort repeated reviews by total feedback count
cleaned_df = cleaned_df.sort_values(
    by='total_feedback_count',
    ascending=False
)

# Remove repeated customer-product-review combinations
cleaned_df = cleaned_df.drop_duplicates(
    subset=['author_id', 'product_id', 'review_text'],
    keep='first'
)

# Reset index
cleaned_df = cleaned_df.reset_index(drop=True)

# Check results
print("Dataset shape after duplicate removal:")
print(cleaned_df.shape)

print("\nRemaining repeated review combinations:")

print(
    cleaned_df.duplicated(
        subset=['author_id', 'product_id', 'review_text']
    ).sum()
)

print("Retained repeated review records:")

print(
    cleaned_df[
        cleaned_df['author_id'].isin([
            '791670733',
            '1319880786',
            '2850702737',
            '12544492953'
        ])
    ][
        ['author_id', 'product_id', 'rating',
         'total_feedback_count', 'submission_time']
    ]
)
# Check missing values after duplicate removal

missing_values = cleaned_df.isnull().sum()

missing_percentage = (
    cleaned_df.isnull().mean() * 100
).round(2)

missing_report = pd.DataFrame({
    'Missing Values': missing_values,
    'Missing Percentage': missing_percentage
})

missing_report = missing_report[
    missing_report['Missing Values'] > 0
].sort_values(
    by='Missing Percentage',
    ascending=False
)

print(missing_report)
# Check feedback count for rows with missing helpfulness

missing_helpfulness = cleaned_df[
    cleaned_df['helpfulness'].isnull()
]

print("Rows with missing helpfulness:",
      len(missing_helpfulness))

print("Rows with zero feedback:",
      (missing_helpfulness['total_feedback_count'] == 0).sum())

print("Other feedback counts:")
print(
    missing_helpfulness[
        missing_helpfulness['total_feedback_count'] != 0
    ]['total_feedback_count'].value_counts()
)
# Create a separate dataset for text analysis

text_analysis_df = cleaned_df.dropna(
    subset=['review_text']
).copy()

print("Main dataset:", cleaned_df.shape)
print("Text analysis dataset:", text_analysis_df.shape)
# 1. Check rating values
print("Rating values:")
print(sorted(cleaned_df['rating'].dropna().unique()))

# 2. Check recommendation values
print("\nRecommendation values:")
print(cleaned_df['is_recommended'].value_counts(dropna=False))

# 3. Check for invalid ratings
invalid_ratings = cleaned_df[
    ~cleaned_df['rating'].between(1, 5)
]

print("\nInvalid ratings:", len(invalid_ratings))

# 4. Check for negative feedback counts
feedback_columns = [
    'total_feedback_count',
    'total_pos_feedback_count',
    'total_neg_feedback_count'
]

negative_feedback = (
    cleaned_df[feedback_columns] < 0
).any(axis=1)

print("Rows with negative feedback counts:",
      negative_feedback.sum())

# 5. Check feedback count consistency
inconsistent_feedback = cleaned_df[
    cleaned_df['total_pos_feedback_count']
    + cleaned_df['total_neg_feedback_count']
    != cleaned_df['total_feedback_count']
]

print("Inconsistent feedback records:",
      len(inconsistent_feedback))

# 6. Check date format
print("\nSubmission time data type:")
print(cleaned_df['submission_time'].dtype)
# Create a cleaned copy of review text

text_analysis_df['review_text_clean'] = (
    text_analysis_df['review_text']
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)
)

# Check a few examples

print(
    text_analysis_df[
        ['review_text', 'review_text_clean']
    ].head(10)
)
# Search for common encoding problem patterns

encoding_patterns = ['Ã', 'â€™', 'â€œ', 'â€']

for pattern in encoding_patterns:
    count = text_analysis_df['review_text'].str.contains(
        pattern,
        na=False
    ).sum()

    print(pattern, ":", count)
    # Test encoding correction on sample reviews

sample_reviews = text_analysis_df[
    text_analysis_df['review_text'].str.contains(
        r'Ã|â€™|â€œ|â€',
        na=False
    )
]['review_text'].head(10)

for review in sample_reviews:
    try:
        corrected = review.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        corrected = "Could not safely convert"

    print("ORIGINAL:", review[:200])
    print("CORRECTED:", corrected[:200])
    print("-" * 60)
    # Test Windows-1252 encoding correction

for review in sample_reviews:
    try:
        corrected = review.encode('cp1252').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        corrected = "Could not safely convert"

    print("ORIGINAL:", review[:200])
    print("CORRECTED:", corrected[:200])
    print("-" * 60)
    # Function to correct text encoding safely

def correct_encoding(text):
    if pd.isna(text):
        return text

    patterns = ['Ã', 'â€™', 'â€œ', 'â€']

    if not any(pattern in text for pattern in patterns):
        return text

    try:
        corrected = text.encode('cp1252').decode('utf-8')

        # Use correction only if suspicious patterns decrease
        original_count = sum(text.count(p) for p in patterns)
        corrected_count = sum(corrected.count(p) for p in patterns)

        if corrected_count < original_count:
            return corrected

    except (UnicodeEncodeError, UnicodeDecodeError):
        pass

    return text


# Create a separate corrected text column
text_analysis_df['review_text_final'] = (
    text_analysis_df['review_text_clean'].apply(correct_encoding)
)

# Compare original and corrected examples
print(text_analysis_df[
    ['review_text_clean', 'review_text_final']
].head(10))
patterns = ['Ã', 'â€™', 'â€œ', 'â€']

for pattern in patterns:
    count = text_analysis_df['review_text_final'].str.contains(
        pattern,
        na=False
    ).sum()

    print(pattern, "remaining:", count)
    remaining_issues = text_analysis_df[
    text_analysis_df['review_text_final'].str.contains(
        r'Ã|â€™|â€œ|â€',
        na=False
    )
]

print("Reviews with remaining encoding issues:",
      len(remaining_issues))
# Calculate IQR for product prices

Q1 = cleaned_df['price_usd'].quantile(0.25)
Q3 = cleaned_df['price_usd'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Identify potential outliers

price_outliers = cleaned_df[
    (cleaned_df['price_usd'] < lower_bound) |
    (cleaned_df['price_usd'] > upper_bound)
]

print("Potential price outliers:", len(price_outliers))

# Display the 10 highest-priced products

print(
    cleaned_df.nlargest(10, 'price_usd')[
        ['product_name', 'brand_name', 'price_usd']
    ]
)
# Create a price outlier flag

cleaned_df['price_outlier'] = (
    cleaned_df['price_usd'] > upper_bound
)

# Count normal and unusual prices

print(cleaned_df['price_outlier'].value_counts())

print("\nOutlier percentage:")
print(
    round(
        cleaned_df['price_outlier'].mean() * 100, 2
    ), "%"
)

# Display flagged products

print(
    cleaned_df[cleaned_df['price_outlier'] == True][
        ['product_name', 'brand_name', 'price_usd']
    ].head(10)
)
print("Final dataset shape:", cleaned_df.shape)

print("\nMissing values:")
print(cleaned_df.isnull().sum())

print("\nDuplicate rows:")
print(cleaned_df.duplicated().sum())

print("\nPrice outliers:")
print(cleaned_df['price_outlier'].sum())
# Add text-cleaning columns to the main dataset

cleaned_df['review_text_clean'] = cleaned_df['review_text']
cleaned_df['review_text_final'] = cleaned_df['review_text']

# Update rows where review text is available
cleaned_df.loc[
    text_analysis_df.index, 'review_text_clean'
] = text_analysis_df['review_text_clean']

cleaned_df.loc[
    text_analysis_df.index, 'review_text_final'
] = text_analysis_df['review_text_final']

print("Updated dataset shape:", cleaned_df.shape)

print(cleaned_df[
    ['review_text', 'review_text_clean', 'review_text_final']
].head())
# Save cleaned dataset in Excel format
cleaned_df.to_excel(
    'sephora_reviews_cleaned.xlsx',
    index=False
)

# Save cleaned dataset in CSV format
cleaned_df.to_csv(
    'sephora_reviews_cleaned.csv',
    index=False
)

# Save text-analysis dataset separately
text_analysis_df.to_csv(
    'sephora_text_analysis.csv',
    index=False
)

print("All datasets saved successfully!")