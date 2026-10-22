# Comparison of the NetLogo port with the Python model

NetLogo runs: `netlogo\results\deep_netlogo.csv`. Python runs: `netlogo\results\deep_py\korningar.csv`.
Verdict rule: agree when |difference of means| <= 3 x its standard error. Seeds are not comparable between the implementations (different random number generators), so only distributions are compared.

**PASS: 61 of 61 comparisons agree, 0 differ (z > 3); 0 with z > 4.5.** The run fails if any z > 4.5 or more than 2 % differ.

## baseline: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.06199 (0.01521) | 0.06008 (0.01511) | 0.8896 | agree |
| illegal_batches_per_year | 893.4 (218.4) | 865.8 (219.5) | 0.8945 | agree |
| avoided_cost_per_year_msek | 20.35 (4.916) | 19.76 (4.945) | 0.8345 | agree |
| fines_per_year_msek | 0.0988 (0.02834) | 0.09632 (0.02888) | 0.6129 | agree |
| fines_to_gain | 0.005138 (0.001976) | 0.005065 (0.001712) | 0.2781 | agree |
| fines_uncollectable_share | 0.3708 (0.1339) | 0.3356 (0.1428) | 1.798 | agree |
| inspections_per_year | 118.8 (8.331) | 119.6 (6.985) | 0.7476 | agree |
| road_checks_per_year | 28.75 (2.118) | 29.26 (1.7) | 1.883 | agree |
| hit_rate | 0.08215 (0.0123) | 0.08018 (0.0112) | 1.185 | agree |
| detections_per_year | 10.53 (1.667) | 10.33 (1.531) | 0.8962 | agree |
| reports_private_per_year | 27.69 (7.248) | 26.7 (7.161) | 0.9646 | agree |
| sanctions_per_year | 1.764 (0.5061) | 1.72 (0.5156) | 0.6129 | agree |
| prohibitions_per_year | 1.76 (0.5068) | 1.677 (0.4686) | 1.2 | agree |
| company_switches_per_year | 1.109 (0.6146) | 1.05 (0.6025) | 0.6806 | agree |
| detected_share | 0.1664 (0.03022) | 0.1637 (0.03337) | 0.6026 | agree |
| top5pct_share_of_illegal | 0.6684 (0.06892) | 0.6588 (0.06805) | 0.9843 | agree |
| max_companies_per_controller | 4.22 (1.079) | 4.21 (0.9979) | 0.06806 | agree |
| dumping_share_of_illegal | 0.6212 (0.02385) | 0.6239 (0.0266) | 0.7639 | agree |
| misclassification_share_of_illegal | 0.3788 (0.02385) | 0.3761 (0.0266) | 0.7639 | agree |
| perceived_detection_dumping_end | 0.1257 (0.007351) | 0.1243 (0.007353) | 1.338 | agree |
| perceived_detection_misclassification_end | 0.0621 (0.005199) | 0.0627 (0.004842) | 0.843 | agree |
| share_of_illegal_ctype_ordinary | 0.1365 (0.05052) | 0.1409 (0.04541) | 0.6554 | agree |
| share_of_illegal_ctype_prior_record | 0.3241 (0.1049) | 0.34 (0.1036) | 1.079 | agree |
| share_of_illegal_ctype_oc_linked | 0.5394 (0.1423) | 0.519 (0.1349) | 1.038 | agree |
| share_of_detections_ctype_ordinary | 0.243 (0.06482) | 0.2585 (0.06812) | 1.643 | agree |
| share_of_detections_ctype_prior_record | 0.5198 (0.09542) | 0.5142 (0.08792) | 0.4288 | agree |
| share_of_detections_ctype_oc_linked | 0.2372 (0.09739) | 0.2273 (0.09474) | 0.7279 | agree |

## hogre_sanktioner: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05488 (0.01478) | 0.05358 (0.01434) | 0.6282 | agree |
| illegal_batches_per_year | 770.5 (208.6) | 752.6 (204.5) | 0.6129 | agree |
| avoided_cost_per_year_msek | 18.34 (4.92) | 17.78 (4.758) | 0.8083 | agree |
| fines_per_year_msek | 0.8656 (0.3094) | 0.8648 (0.2927) | 0.01878 | agree |
| fines_to_gain | 0.04901 (0.01784) | 0.05123 (0.02063) | 0.8154 | agree |
| fines_uncollectable_share | 0.3321 (0.1443) | 0.3436 (0.1525) | 0.5504 | agree |
| inspections_per_year | 118.9 (8.325) | 119.6 (6.932) | 0.6646 | agree |
| road_checks_per_year | 28.89 (2.014) | 28.9 (2.099) | 0.05893 | agree |
| hit_rate | 0.06623 (0.01039) | 0.06819 (0.01122) | 1.285 | agree |
| detections_per_year | 8.514 (1.381) | 8.756 (1.429) | 1.215 | agree |
| reports_private_per_year | 22.91 (6.907) | 22.41 (6.472) | 0.5237 | agree |
| sanctions_per_year | 1.546 (0.5525) | 1.544 (0.5227) | 0.01878 | agree |
| prohibitions_per_year | 1.334 (0.3875) | 1.403 (0.5025) | 1.081 | agree |
| company_switches_per_year | 1.101 (0.5969) | 1.029 (0.5141) | 0.9248 | agree |
| detected_share | 0.1655 (0.03386) | 0.1671 (0.03698) | 0.3197 | agree |
| top5pct_share_of_illegal | 0.7007 (0.06652) | 0.6938 (0.0693) | 0.7177 | agree |
| max_companies_per_controller | 4.3 (1.068) | 4.36 (1.01) | 0.4081 | agree |
| dumping_share_of_illegal | 0.6005 (0.02908) | 0.5966 (0.02601) | 0.9968 | agree |
| misclassification_share_of_illegal | 0.3995 (0.02908) | 0.4034 (0.02601) | 0.9968 | agree |
| perceived_detection_dumping_end | 0.1239 (0.006568) | 0.125 (0.00687) | 1.124 | agree |
| perceived_detection_misclassification_end | 0.06217 (0.005219) | 0.0625 (0.00553) | 0.4377 | agree |
| share_of_illegal_ctype_ordinary | 0.1171 (0.04713) | 0.1212 (0.04259) | 0.6494 | agree |
| share_of_illegal_ctype_prior_record | 0.3204 (0.1115) | 0.3274 (0.1043) | 0.4538 | agree |
| share_of_illegal_ctype_oc_linked | 0.5625 (0.1447) | 0.5514 (0.1342) | 0.5599 | agree |
| share_of_detections_ctype_ordinary | 0.2033 (0.07021) | 0.2114 (0.06252) | 0.8634 | agree |
| share_of_detections_ctype_prior_record | 0.5082 (0.09919) | 0.5302 (0.09358) | 1.616 | agree |
| share_of_detections_ctype_oc_linked | 0.2885 (0.1115) | 0.2584 (0.09388) | 2.069 | agree |

## Intervention effects (scenario minus baseline, pairwise by seed)

| Scenario | Metric | NetLogo effect (sd) | Python effect (sd) | z | Verdict |
| --- | --- | --- | --- | --- | --- |
| hogre_sanktioner | illegal_share | -0.007116 (0.005813) | -0.006502 (0.006177) | 0.7233 | agree |
| hogre_sanktioner | detected_share | -0.000867 (0.0423) | 0.003449 (0.05077) | 0.6531 | agree |
| hogre_sanktioner | detections_per_year | -2.02 (1.552) | -1.576 (1.559) | 2.019 | agree |
| hogre_sanktioner | prohibitions_per_year | -0.4257 (0.5512) | -0.2743 (0.5763) | 1.899 | agree |
| hogre_sanktioner | company_switches_per_year | -0.007143 (0.4703) | -0.02143 (0.4875) | 0.2109 | agree |
| hogre_sanktioner | inspections_per_year | 0.04286 (0.3961) | -0.05 (0.3822) | 1.687 | agree |
| hogre_sanktioner | road_checks_per_year | 0.1357 (2.787) | -0.3586 (2.758) | 1.261 | agree |
