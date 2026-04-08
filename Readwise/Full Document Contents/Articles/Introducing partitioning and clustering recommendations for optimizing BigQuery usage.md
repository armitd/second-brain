# Introducing partitioning and clustering recommendations for optimizing BigQuery usage

![rw-book-cover](https://storage.googleapis.com/gweb-cloudblog-publish/images/DO_NOT_USE_CUxs9oC.max-2500x2500.jpg)

## Metadata
- Author: [[Vinay Yerramilli]]
- Full Title: Introducing partitioning and clustering recommendations for optimizing BigQuery usage
- Category: #articles
- Summary: The BigQuery partitioning and clustering recommender is a tool designed to help users optimize their BigQuery tables for cost reduction and improved performance. By analyzing workload execution and table data, the recommender generates recommendations using machine learning to estimate potential savings. The process involves steps like Candidate Generation, Read Pattern Analyzer, Write Pattern Analyzer, and Generate Recommendations, focusing on criteria like table size and column selection. Users can access these recommendations through various channels and are encouraged to provide feedback for further enhancements.
- URL: https://cloud.google.com/blog/products/data-analytics/new-bigquery-partitioning-and-clustering-recommendations

## Full Document
[Register](https://cloud.withgoogle.com/next?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY23-Q3-global-ENDM33-physicalevent-er-next-2023-mc&utm_content=left-hand-cta&utm_term=-) 

Do you have a lot of BigQuery tables? Do you find it hard to keep track of which ones are partitioned and clustered, and which ones could be? If so, we have good news. We're launching a [partitioning and clustering recommender](https://cloud.google.com/bigquery/docs/view-partition-cluster-recommendations) that will do the work for you! The recommender analyzes all your organization's workloads and tables and identifies potential cost optimization opportunities. And the best part is, it's completely free!

*"The BigQuery partitioning and clustering recommendations are awesome! They have helped our customers identify areas where they can reduce costs, improve performance, and optimize our BigQuery usage."* [Sky](https://www.sky.com/), one of Europe leading media and communications companies

##### How does the recommender work?

[Partitioning](https://cloud.google.com/bigquery/docs/partitioned-tables) divides a table into segments, while [clustering](https://cloud.google.com/bigquery/docs/clustered-tables) sorts the table based on user-defined columns. Both methods can improve the performance of certain types of queries, such as queries that use filter clauses and queries that aggregate data.

BigQuery’s partitioning and clustering recommender analyzes each project’s workload execution over the past 30 days to look for suboptimal scans of the table data. The recommender then uses machine learning to estimate the potential savings and generate final recommendations. The process has four key steps: Candidate Generation, Read Pattern Analyzer, Write Pattern Analyzer, and Generate Recommendations.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/image3_reT5jax.max-900x900.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/image3_reT5jax.max-900x900.png)![https://storage.googleapis.com/gweb-cloudblog-publish/images/image3_reT5jax.max-900x900.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/image3_reT5jax.max-900x900.png)
Candidate Generation is the first step in the process, where tables and columns are selected based on specific criteria. For Partitioning, tables larger than 100 Gb are chosen, and for Clustering tables larger than 10 Gb are chosen. The reason for filtering out the smaller tables is because the optimization benefit is smaller and less predictable. Then we identify columns that meet BigQuery's [partitioning](http://go/bq-partition-limitations) and [clustering](https://goto.google.com/bq-cluster-limitations) requirements.

In the Read Pattern Analyzer step, the recommender analyzes the logs of queries that filter on the selected columns to determine their potential for cost savings through partitioning or clustering. Several metrics, such as filter selectivity, potential file pruning, and runtime, are considered, and machine learning is used to estimate the potential slot time saved if partitioning or clustering is applied.

The Write Pattern Analyzer step is then used to estimate the cost that partitioning or clustering may introduce during write time. Write patterns and table schema are analyzed to determine the net savings from partitioning or clustering for each column.

Finally, in Generate Recommendations, the output from both the Read Pattern Analyzer and Write Pattern Analyzer is used to determine the net savings from partitioning or clustering for each column. If the net savings are positive and meaningful, the recommendations are uploaded to the Recommender API with proper IAM permissions.

##### Discovering BigQuery partitioning and clustering recommendations

You can access these recommendations via a few different channels:

* Via the lightbulb or idea icon in the top right of [BigQuery’s UI page](http://console.cloud.google.com/bigquery)
* On our console via the [Recommendation Hub](https://console.cloud.google.com/home/recommendations)
* Via our [Recommender API](https://cloud.google.com/bigquery/docs/view-partition-cluster-recommendations#rest-api)

You can also export the recommendations to BigQuery using [BigQuery Export](https://cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

![https://storage.googleapis.com/gweb-cloudblog-publish/original_images/image2_wUQxJHP.gif](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/image2_wUQxJHP.gif)![https://storage.googleapis.com/gweb-cloudblog-publish/original_images/image2_wUQxJHP.gif](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/image2_wUQxJHP.gif)
To learn more about the recommender, please see the [public documentation](https://cloud.google.com/bigquery/docs/view-partition-cluster-recommendations).

We hope you use BigQuery partitioning and clustering recommendations to optimize your BigQuery tables, and can’t wait to hear your feedback and thoughts about this feature. Please feel free to reach us at [active-assist-feedback@google.com](mailto:active-assist-feedback@google.com).
