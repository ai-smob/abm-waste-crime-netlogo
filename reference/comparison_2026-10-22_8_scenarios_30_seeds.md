# Comparison of the NetLogo port with the Python model

NetLogo runs: `netlogo\results\netlogo_runs.csv`. Python runs: `reference\python_runs_v0.2.csv`.
Verdict rule: agree when |difference of means| <= 3 x its standard error. Seeds are not comparable between the implementations (different random number generators), so only distributions are compared.

**Result: 263 of 265 comparisons agree, 2 differ.**

## baseline: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05719 (0.0146) | 0.05875 (0.01551) | 0.4009 | agree |
| illegal_batches_per_year | 828.3 (208.5) | 851.5 (228.8) | 0.412 | agree |
| avoided_cost_per_year_msek | 18.92 (4.62) | 19.17 (5.13) | 0.1947 | agree |
| fines_per_year_msek | 0.0952 (0.02444) | 0.09387 (0.03275) | 0.1787 | agree |
| fines_to_gain | 0.005338 (0.001867) | 0.005042 (0.001631) | 0.6538 | agree |
| fines_uncollectable_share | 0.367 (0.1278) | 0.3324 (0.1478) | 0.9715 | agree |
| inspections_per_year | 121.7 (7.997) | 120.4 (7.288) | 0.6798 | agree |
| road_checks_per_year | 27.92 (2.029) | 29.4 (1.699) | 3.065 | DIFFERS |
| hit_rate | 0.08173 (0.01089) | 0.07657 (0.01119) | 1.808 | agree |
| detections_per_year | 10.68 (1.586) | 9.995 (1.489) | 1.726 | agree |
| reports_private_per_year | 25.68 (6.717) | 26.97 (7.737) | 0.6899 | agree |
| sanctions_per_year | 1.7 (0.4365) | 1.676 (0.5847) | 0.1787 | agree |
| prohibitions_per_year | 1.857 (0.4906) | 1.524 (0.4615) | 2.711 | agree |
| company_switches_per_year | 1.071 (0.5869) | 1.029 (0.6684) | 0.2639 | agree |
| detected_share | 0.173 (0.02585) | 0.1594 (0.04163) | 1.512 | agree |
| top5pct_share_of_illegal | 0.6546 (0.07853) | 0.6607 (0.0773) | 0.3032 | agree |
| max_companies_per_controller | 4.367 (1.189) | 4.1 (0.9229) | 0.9706 | agree |
| dumping_share_of_illegal | 0.6228 (0.02295) | 0.6277 (0.0322) | 0.6701 | agree |
| misclassification_share_of_illegal | 0.3772 (0.02295) | 0.3723 (0.0322) | 0.6701 | agree |
| perceived_detection_dumping_end | 0.1272 (0.007935) | 0.1227 (0.007287) | 2.289 | agree |
| perceived_detection_misclassification_end | 0.0628 (0.004409) | 0.06197 (0.005318) | 0.6569 | agree |
| share_of_illegal_ctype_ordinary | 0.1455 (0.05128) | 0.143 (0.04962) | 0.1902 | agree |
| share_of_illegal_ctype_prior_record | 0.3431 (0.1215) | 0.3471 (0.1192) | 0.1282 | agree |
| share_of_illegal_ctype_oc_linked | 0.5114 (0.1597) | 0.5099 (0.1531) | 0.03731 | agree |
| share_of_detections_ctype_ordinary | 0.2359 (0.06396) | 0.2564 (0.06216) | 1.256 | agree |
| share_of_detections_ctype_prior_record | 0.5428 (0.09241) | 0.5216 (0.08874) | 0.9037 | agree |
| share_of_detections_ctype_oc_linked | 0.2213 (0.08967) | 0.222 (0.09519) | 0.0285 | agree |

## fler_kontroller: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05238 (0.01417) | 0.05421 (0.0143) | 0.4996 | agree |
| illegal_batches_per_year | 751.4 (197.5) | 773.6 (208.6) | 0.4235 | agree |
| avoided_cost_per_year_msek | 17.38 (4.703) | 17.96 (4.87) | 0.472 | agree |
| fines_per_year_msek | 0.1501 (0.03709) | 0.1616 (0.04016) | 1.149 | agree |
| fines_to_gain | 0.009193 (0.003022) | 0.009507 (0.003265) | 0.3871 | agree |
| fines_uncollectable_share | 0.4055 (0.1324) | 0.4207 (0.1323) | 0.4448 | agree |
| inspections_per_year | 243 (15.96) | 240.4 (14.51) | 0.6687 | agree |
| road_checks_per_year | 28.56 (1.961) | 29.3 (1.576) | 1.607 | agree |
| hit_rate | 0.06806 (0.007917) | 0.06742 (0.00881) | 0.2943 | agree |
| detections_per_year | 17.18 (2.39) | 16.75 (2.27) | 0.7121 | agree |
| reports_private_per_year | 23.82 (6.978) | 23.39 (5.91) | 0.2624 | agree |
| sanctions_per_year | 2.681 (0.6623) | 2.886 (0.7171) | 1.149 | agree |
| prohibitions_per_year | 3.386 (0.7324) | 3.29 (0.6799) | 0.522 | agree |
| company_switches_per_year | 1.495 (0.6708) | 1.538 (0.7575) | 0.232 | agree |
| detected_share | 0.2561 (0.03832) | 0.2563 (0.03718) | 0.02179 | agree |
| top5pct_share_of_illegal | 0.6646 (0.08183) | 0.6666 (0.08078) | 0.0906 | agree |
| max_companies_per_controller | 4.867 (1.042) | 5.033 (1.189) | 0.5776 | agree |
| dumping_share_of_illegal | 0.6169 (0.02294) | 0.6207 (0.0209) | 0.665 | agree |
| misclassification_share_of_illegal | 0.3831 (0.02294) | 0.3793 (0.0209) | 0.665 | agree |
| perceived_detection_dumping_end | 0.1526 (0.01013) | 0.1476 (0.009104) | 2.019 | agree |
| perceived_detection_misclassification_end | 0.07574 (0.005497) | 0.0752 (0.005785) | 0.3701 | agree |
| share_of_illegal_ctype_ordinary | 0.1507 (0.06312) | 0.1518 (0.05401) | 0.06676 | agree |
| share_of_illegal_ctype_prior_record | 0.3181 (0.121) | 0.3175 (0.1096) | 0.02119 | agree |
| share_of_illegal_ctype_oc_linked | 0.5311 (0.1694) | 0.5307 (0.1497) | 0.009233 | agree |
| share_of_detections_ctype_ordinary | 0.2789 (0.06871) | 0.2755 (0.07436) | 0.1834 | agree |
| share_of_detections_ctype_prior_record | 0.5148 (0.07141) | 0.5197 (0.07793) | 0.2531 | agree |
| share_of_detections_ctype_oc_linked | 0.2063 (0.07309) | 0.2048 (0.08099) | 0.07501 | agree |

## riskbaserad_tillsyn: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05575 (0.01416) | 0.05725 (0.0151) | 0.3957 | agree |
| illegal_batches_per_year | 802.4 (202.4) | 824.3 (220.5) | 0.4016 | agree |
| avoided_cost_per_year_msek | 18.55 (4.807) | 18.7 (4.905) | 0.1161 | agree |
| fines_per_year_msek | 0.1077 (0.03366) | 0.09653 (0.02985) | 1.363 | agree |
| fines_to_gain | 0.006286 (0.002632) | 0.005429 (0.002153) | 1.379 | agree |
| fines_uncollectable_share | 0.4897 (0.1375) | 0.49 (0.1195) | 0.008433 | agree |
| inspections_per_year | 121.7 (7.996) | 120.2 (7.304) | 0.7707 | agree |
| road_checks_per_year | 28.67 (1.668) | 29.39 (1.832) | 1.59 | agree |
| hit_rate | 0.08238 (0.01065) | 0.08227 (0.01532) | 0.03053 | agree |
| detections_per_year | 10.77 (1.507) | 10.61 (1.95) | 0.3492 | agree |
| reports_private_per_year | 25.13 (6.447) | 26.16 (7.024) | 0.5909 | agree |
| sanctions_per_year | 1.924 (0.6011) | 1.724 (0.5331) | 1.363 | agree |
| prohibitions_per_year | 2.567 (0.5259) | 2.486 (0.6696) | 0.5208 | agree |
| company_switches_per_year | 1.052 (0.4066) | 1.133 (0.6037) | 0.6092 | agree |
| detected_share | 0.1709 (0.03365) | 0.159 (0.03471) | 1.348 | agree |
| top5pct_share_of_illegal | 0.6477 (0.07691) | 0.6598 (0.0763) | 0.6136 | agree |
| max_companies_per_controller | 4.6 (1.07) | 4.5 (0.7768) | 0.4142 | agree |
| dumping_share_of_illegal | 0.6188 (0.02957) | 0.6267 (0.02447) | 1.14 | agree |
| misclassification_share_of_illegal | 0.3812 (0.02957) | 0.3733 (0.02447) | 1.14 | agree |
| perceived_detection_dumping_end | 0.1244 (0.007082) | 0.123 (0.009192) | 0.6464 | agree |
| perceived_detection_misclassification_end | 0.06232 (0.0044) | 0.06251 (0.005317) | 0.1531 | agree |
| share_of_illegal_ctype_ordinary | 0.1536 (0.04174) | 0.1444 (0.04282) | 0.8403 | agree |
| share_of_illegal_ctype_prior_record | 0.3381 (0.1296) | 0.3294 (0.1226) | 0.2687 | agree |
| share_of_illegal_ctype_oc_linked | 0.5083 (0.1596) | 0.5262 (0.1533) | 0.4436 | agree |
| share_of_detections_ctype_ordinary | 0.2246 (0.06676) | 0.227 (0.06158) | 0.1419 | agree |
| share_of_detections_ctype_prior_record | 0.5453 (0.08362) | 0.5399 (0.09794) | 0.2302 | agree |
| share_of_detections_ctype_oc_linked | 0.23 (0.08494) | 0.2331 (0.1138) | 0.118 | agree |

## kontroller_pa_plats: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05481 (0.01261) | 0.05643 (0.0143) | 0.4673 | agree |
| illegal_batches_per_year | 778.8 (174.5) | 814.3 (207.8) | 0.7156 | agree |
| avoided_cost_per_year_msek | 18.33 (4.153) | 18.58 (4.837) | 0.2107 | agree |
| fines_per_year_msek | 0.132 (0.03021) | 0.1347 (0.0367) | 0.3073 | agree |
| fines_to_gain | 0.007513 (0.002259) | 0.007561 (0.002411) | 0.07942 | agree |
| fines_uncollectable_share | 0.3815 (0.1336) | 0.3681 (0.1334) | 0.3895 | agree |
| inspections_per_year | 121.6 (8.128) | 120.1 (7.217) | 0.7247 | agree |
| road_checks_per_year | 28.7 (2.305) | 28.51 (2.613) | 0.2994 | agree |
| hit_rate | 0.107 (0.01409) | 0.1077 (0.01787) | 0.1679 | agree |
| detections_per_year | 13.65 (1.764) | 13.63 (2.355) | 0.03546 | agree |
| reports_private_per_year | 24.66 (5.593) | 25.97 (6.917) | 0.8034 | agree |
| sanctions_per_year | 2.357 (0.5394) | 2.405 (0.6553) | 0.3073 | agree |
| prohibitions_per_year | 2.49 (0.5458) | 2.448 (0.814) | 0.2395 | agree |
| company_switches_per_year | 1.262 (0.6878) | 1.267 (0.5988) | 0.0286 | agree |
| detected_share | 0.2249 (0.04223) | 0.2271 (0.05113) | 0.1825 | agree |
| top5pct_share_of_illegal | 0.6564 (0.07101) | 0.6571 (0.08177) | 0.03561 | agree |
| max_companies_per_controller | 4.733 (1.015) | 4.567 (0.9353) | 0.6615 | agree |
| dumping_share_of_illegal | 0.6227 (0.02543) | 0.6219 (0.02938) | 0.1166 | agree |
| misclassification_share_of_illegal | 0.3773 (0.02543) | 0.3781 (0.02938) | 0.1166 | agree |
| perceived_detection_dumping_end | 0.1364 (0.008131) | 0.134 (0.007918) | 1.17 | agree |
| perceived_detection_misclassification_end | 0.07387 (0.005384) | 0.07441 (0.006436) | 0.3521 | agree |
| share_of_illegal_ctype_ordinary | 0.1489 (0.05057) | 0.1433 (0.05485) | 0.4058 | agree |
| share_of_illegal_ctype_prior_record | 0.3431 (0.1236) | 0.3338 (0.1069) | 0.312 | agree |
| share_of_illegal_ctype_oc_linked | 0.508 (0.1624) | 0.5229 (0.141) | 0.3778 | agree |
| share_of_detections_ctype_ordinary | 0.2704 (0.08051) | 0.2649 (0.06746) | 0.285 | agree |
| share_of_detections_ctype_prior_record | 0.5061 (0.09258) | 0.515 (0.0829) | 0.3955 | agree |
| share_of_detections_ctype_oc_linked | 0.2236 (0.09142) | 0.22 (0.086) | 0.153 | agree |

## hogre_sanktioner: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05016 (0.01254) | 0.05276 (0.01354) | 0.7724 | agree |
| illegal_batches_per_year | 703.9 (172.5) | 740.6 (192.1) | 0.7788 | agree |
| avoided_cost_per_year_msek | 16.84 (4.144) | 17.54 (4.419) | 0.6339 | agree |
| fines_per_year_msek | 0.8693 (0.3867) | 0.8 (0.2699) | 0.8054 | agree |
| fines_to_gain | 0.05138 (0.01811) | 0.04632 (0.01336) | 1.233 | agree |
| fines_uncollectable_share | 0.3262 (0.1294) | 0.3232 (0.143) | 0.0855 | agree |
| inspections_per_year | 121.8 (7.995) | 120.3 (7.319) | 0.7411 | agree |
| road_checks_per_year | 28.69 (1.788) | 28.64 (2.047) | 0.09596 | agree |
| hit_rate | 0.06593 (0.01088) | 0.06693 (0.01096) | 0.3535 | agree |
| detections_per_year | 8.681 (1.521) | 8.633 (1.52) | 0.1213 | agree |
| reports_private_per_year | 21.51 (5.482) | 21.85 (6.501) | 0.2208 | agree |
| sanctions_per_year | 1.552 (0.6905) | 1.429 (0.4819) | 0.8054 | agree |
| prohibitions_per_year | 1.29 (0.3798) | 1.343 (0.4527) | 0.4855 | agree |
| company_switches_per_year | 1.033 (0.6396) | 1.133 (0.5602) | 0.6442 | agree |
| detected_share | 0.1707 (0.03176) | 0.176 (0.0376) | 0.5994 | agree |
| top5pct_share_of_illegal | 0.688 (0.07067) | 0.6899 (0.0744) | 0.1001 | agree |
| max_companies_per_controller | 4.167 (1.206) | 4.367 (1.033) | 0.6898 | agree |
| dumping_share_of_illegal | 0.6094 (0.03155) | 0.5979 (0.02596) | 1.549 | agree |
| misclassification_share_of_illegal | 0.3906 (0.03155) | 0.4021 (0.02596) | 1.549 | agree |
| perceived_detection_dumping_end | 0.1245 (0.006763) | 0.1231 (0.006949) | 0.8059 | agree |
| perceived_detection_misclassification_end | 0.06352 (0.005188) | 0.06231 (0.006012) | 0.8306 | agree |
| share_of_illegal_ctype_ordinary | 0.1254 (0.04054) | 0.1223 (0.04258) | 0.2839 | agree |
| share_of_illegal_ctype_prior_record | 0.3362 (0.1374) | 0.3257 (0.1063) | 0.329 | agree |
| share_of_illegal_ctype_oc_linked | 0.5385 (0.1625) | 0.5519 (0.1382) | 0.3463 | agree |
| share_of_detections_ctype_ordinary | 0.2156 (0.06735) | 0.201 (0.05998) | 0.887 | agree |
| share_of_detections_ctype_prior_record | 0.5201 (0.0982) | 0.5244 (0.08551) | 0.1794 | agree |
| share_of_detections_ctype_oc_linked | 0.2642 (0.1129) | 0.2746 (0.09149) | 0.3898 | agree |

## informationsdelning: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05553 (0.01376) | 0.05662 (0.01403) | 0.3038 | agree |
| illegal_batches_per_year | 798.4 (198.4) | 814.7 (197.9) | 0.3187 | agree |
| avoided_cost_per_year_msek | 18.28 (4.502) | 18.63 (4.788) | 0.2854 | agree |
| fines_per_year_msek | 0.1109 (0.03558) | 0.1144 (0.0295) | 0.4109 | agree |
| fines_to_gain | 0.006333 (0.002227) | 0.006394 (0.001962) | 0.1135 | agree |
| fines_uncollectable_share | 0.3755 (0.1354) | 0.3623 (0.1652) | 0.3386 | agree |
| inspections_per_year | 121.6 (8.051) | 120.2 (7.208) | 0.7192 | agree |
| road_checks_per_year | 29.37 (2.15) | 28.67 (1.887) | 1.349 | agree |
| hit_rate | 0.09501 (0.01402) | 0.09688 (0.01144) | 0.567 | agree |
| detections_per_year | 12.35 (2.051) | 12.44 (1.552) | 0.2028 | agree |
| reports_private_per_year | 24.4 (5.856) | 25.28 (6.596) | 0.5412 | agree |
| sanctions_per_year | 1.981 (0.6353) | 2.043 (0.5268) | 0.4109 | agree |
| prohibitions_per_year | 2.071 (0.6035) | 2.057 (0.5597) | 0.09506 | agree |
| company_switches_per_year | 1.381 (0.6414) | 1.267 (0.6127) | 0.7057 | agree |
| detected_share | 0.1975 (0.04252) | 0.2022 (0.03582) | 0.4624 | agree |
| top5pct_share_of_illegal | 0.6495 (0.06625) | 0.6485 (0.07169) | 0.0544 | agree |
| max_companies_per_controller | 4.9 (1.322) | 4.6 (1.037) | 0.9778 | agree |
| dumping_share_of_illegal | 0.6158 (0.0245) | 0.6232 (0.02287) | 1.209 | agree |
| misclassification_share_of_illegal | 0.3842 (0.0245) | 0.3768 (0.02287) | 1.209 | agree |
| perceived_detection_dumping_end | 0.1339 (0.009139) | 0.1327 (0.007671) | 0.5123 | agree |
| perceived_detection_misclassification_end | 0.06575 (0.005026) | 0.06614 (0.00431) | 0.3207 | agree |
| share_of_illegal_ctype_ordinary | 0.1619 (0.04866) | 0.1498 (0.04066) | 1.048 | agree |
| share_of_illegal_ctype_prior_record | 0.3393 (0.1261) | 0.3429 (0.1082) | 0.1189 | agree |
| share_of_illegal_ctype_oc_linked | 0.4988 (0.1599) | 0.5073 (0.1376) | 0.2215 | agree |
| share_of_detections_ctype_ordinary | 0.1702 (0.05322) | 0.17 (0.04557) | 0.01618 | agree |
| share_of_detections_ctype_prior_record | 0.5951 (0.08713) | 0.5976 (0.09296) | 0.1095 | agree |
| share_of_detections_ctype_oc_linked | 0.2347 (0.09162) | 0.2324 (0.09875) | 0.09516 | agree |

## vagkontroller: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05351 (0.01172) | 0.05337 (0.01333) | 0.04376 | agree |
| illegal_batches_per_year | 767.9 (167.4) | 769 (190.8) | 0.02229 | agree |
| avoided_cost_per_year_msek | 17.68 (3.99) | 17.51 (4.482) | 0.1569 | agree |
| fines_per_year_msek | 0.1184 (0.03719) | 0.12 (0.03758) | 0.1657 | agree |
| fines_to_gain | 0.00688 (0.002096) | 0.007057 (0.0022) | 0.3192 | agree |
| fines_uncollectable_share | 0.426 (0.141) | 0.3917 (0.1641) | 0.8674 | agree |
| inspections_per_year | 121.7 (7.973) | 120.2 (7.276) | 0.7467 | agree |
| road_checks_per_year | 145.4 (4.08) | 144.2 (3.99) | 1.133 | agree |
| hit_rate | 0.0787 (0.01339) | 0.07894 (0.01368) | 0.07055 | agree |
| detections_per_year | 13.08 (2.22) | 13.06 (2.531) | 0.03874 | agree |
| reports_private_per_year | 23.46 (6.043) | 23.81 (6.048) | 0.2227 | agree |
| sanctions_per_year | 2.114 (0.6642) | 2.143 (0.6711) | 0.1657 | agree |
| prohibitions_per_year | 2.338 (0.5404) | 2.086 (0.5635) | 1.771 | agree |
| company_switches_per_year | 1.524 (0.8533) | 1.71 (0.889) | 0.8255 | agree |
| detected_share | 0.162 (0.02699) | 0.1729 (0.03898) | 1.255 | agree |
| top5pct_share_of_illegal | 0.6358 (0.06456) | 0.6426 (0.07146) | 0.3858 | agree |
| max_companies_per_controller | 5.233 (1.278) | 5.3 (1.236) | 0.2054 | agree |
| dumping_share_of_illegal | 0.6158 (0.02154) | 0.6316 (0.02207) | 2.808 | agree |
| misclassification_share_of_illegal | 0.3842 (0.02154) | 0.3684 (0.02207) | 2.808 | agree |
| perceived_detection_dumping_end | 0.1373 (0.008115) | 0.1359 (0.008614) | 0.6793 | agree |
| perceived_detection_misclassification_end | 0.06568 (0.00524) | 0.06483 (0.0067) | 0.5447 | agree |
| share_of_illegal_ctype_ordinary | 0.1524 (0.04811) | 0.1537 (0.04228) | 0.1141 | agree |
| share_of_illegal_ctype_prior_record | 0.3571 (0.1186) | 0.3513 (0.1083) | 0.1967 | agree |
| share_of_illegal_ctype_oc_linked | 0.4905 (0.1446) | 0.495 (0.1362) | 0.1222 | agree |
| share_of_detections_ctype_ordinary | 0.2291 (0.06919) | 0.2246 (0.05096) | 0.2904 | agree |
| share_of_detections_ctype_prior_record | 0.4804 (0.08003) | 0.4895 (0.09022) | 0.4149 | agree |
| share_of_detections_ctype_oc_linked | 0.2905 (0.09817) | 0.286 (0.09612) | 0.1825 | agree |

## kombinerad: levels

| Metric | NetLogo mean (sd) | Python mean (sd) | z | Verdict |
| --- | --- | --- | --- | --- |
| illegal_share | 0.05134 (0.01344) | 0.05363 (0.01447) | 0.6346 | agree |
| illegal_batches_per_year | 742.3 (193.8) | 771.4 (209.8) | 0.559 | agree |
| avoided_cost_per_year_msek | 16.95 (4.543) | 17.75 (4.735) | 0.6739 | agree |
| fines_per_year_msek | 0.1541 (0.04111) | 0.1541 (0.04603) | 0 | agree |
| fines_to_gain | 0.009585 (0.003367) | 0.009015 (0.002802) | 0.7127 | agree |
| fines_uncollectable_share | 0.4486 (0.1131) | 0.5048 (0.1078) | 1.971 | agree |
| inspections_per_year | 121.5 (8.052) | 120.1 (7.225) | 0.704 | agree |
| road_checks_per_year | 28.77 (2.238) | 28.46 (1.84) | 0.5851 | agree |
| hit_rate | 0.1353 (0.01887) | 0.1377 (0.01949) | 0.475 | agree |
| detections_per_year | 17.04 (2.474) | 17.31 (2.415) | 0.4225 | agree |
| reports_private_per_year | 23.65 (6.166) | 24.03 (7.276) | 0.216 | agree |
| sanctions_per_year | 2.752 (0.7341) | 2.752 (0.8219) | 0 | agree |
| prohibitions_per_year | 3.838 (0.6698) | 3.81 (0.8023) | 0.1497 | agree |
| company_switches_per_year | 1.648 (0.82) | 1.643 (0.8088) | 0.02265 | agree |
| detected_share | 0.271 (0.03794) | 0.276 (0.05243) | 0.4263 | agree |
| top5pct_share_of_illegal | 0.6646 (0.08134) | 0.6625 (0.07032) | 0.1053 | agree |
| max_companies_per_controller | 5.733 (1.337) | 5.6 (1.276) | 0.3951 | agree |
| dumping_share_of_illegal | 0.6255 (0.02148) | 0.6241 (0.03265) | 0.1915 | agree |
| misclassification_share_of_illegal | 0.3745 (0.02148) | 0.3759 (0.03265) | 0.1915 | agree |
| perceived_detection_dumping_end | 0.1464 (0.008667) | 0.1467 (0.008437) | 0.1267 | agree |
| perceived_detection_misclassification_end | 0.08177 (0.007195) | 0.0806 (0.006372) | 0.6655 | agree |
| share_of_illegal_ctype_ordinary | 0.1708 (0.0632) | 0.1654 (0.05469) | 0.3538 | agree |
| share_of_illegal_ctype_prior_record | 0.293 (0.1051) | 0.2945 (0.1099) | 0.0538 | agree |
| share_of_illegal_ctype_oc_linked | 0.5362 (0.1567) | 0.5401 (0.1434) | 0.1007 | agree |
| share_of_detections_ctype_ordinary | 0.1084 (0.03545) | 0.1045 (0.0428) | 0.3835 | agree |
| share_of_detections_ctype_prior_record | 0.6714 (0.07501) | 0.667 (0.07665) | 0.2249 | agree |
| share_of_detections_ctype_oc_linked | 0.2202 (0.07864) | 0.2285 (0.09191) | 0.3756 | agree |

## Intervention effects (scenario minus baseline, pairwise by seed)

| Scenario | Metric | NetLogo effect (sd) | Python effect (sd) | z | Verdict |
| --- | --- | --- | --- | --- | --- |
| fler_kontroller | illegal_share | -0.004815 (0.004981) | -0.004538 (0.004666) | 0.2223 | agree |
| fler_kontroller | detected_share | 0.08313 (0.04262) | 0.09688 (0.05334) | 1.102 | agree |
| fler_kontroller | detections_per_year | 6.5 (1.788) | 6.757 (1.795) | 0.556 | agree |
| fler_kontroller | prohibitions_per_year | 1.529 (0.6346) | 1.767 (0.5272) | 1.581 | agree |
| fler_kontroller | company_switches_per_year | 0.4238 (0.5205) | 0.5095 (0.4756) | 0.6659 | agree |
| fler_kontroller | inspections_per_year | 121.3 (7.984) | 120 (7.259) | 0.655 | agree |
| fler_kontroller | road_checks_per_year | 0.6381 (2.8) | -0.1048 (2.388) | 1.105 | agree |
| riskbaserad_tillsyn | illegal_share | -0.001438 (0.005982) | -0.001502 (0.005615) | 0.04231 | agree |
| riskbaserad_tillsyn | detected_share | -0.002059 (0.03731) | -0.0004262 (0.048) | 0.1471 | agree |
| riskbaserad_tillsyn | detections_per_year | 0.09048 (1.387) | 0.619 (1.857) | 1.249 | agree |
| riskbaserad_tillsyn | prohibitions_per_year | 0.7095 (0.4633) | 0.9619 (0.737) | 1.588 | agree |
| riskbaserad_tillsyn | company_switches_per_year | -0.01905 (0.3983) | 0.1048 (0.5238) | 1.031 | agree |
| riskbaserad_tillsyn | inspections_per_year | -0.004762 (0.282) | -0.1857 (0.3901) | 2.059 | agree |
| riskbaserad_tillsyn | road_checks_per_year | 0.7476 (2.845) | -0.01429 (2.523) | 1.097 | agree |
| kontroller_pa_plats | illegal_share | -0.002387 (0.004505) | -0.002319 (0.005391) | 0.05269 | agree |
| kontroller_pa_plats | detected_share | 0.05193 (0.0404) | 0.06767 (0.04869) | 1.363 | agree |
| kontroller_pa_plats | detections_per_year | 2.971 (1.41) | 3.638 (2.03) | 1.478 | agree |
| kontroller_pa_plats | prohibitions_per_year | 0.6333 (0.5181) | 0.9238 (0.7723) | 1.711 | agree |
| kontroller_pa_plats | company_switches_per_year | 0.1905 (0.5531) | 0.2381 (0.5876) | 0.3232 | agree |
| kontroller_pa_plats | inspections_per_year | -0.1381 (0.3608) | -0.2333 (0.3105) | 1.096 | agree |
| kontroller_pa_plats | road_checks_per_year | 0.781 (2.481) | -0.8905 (2.521) | 2.588 | agree |
| hogre_sanktioner | illegal_share | -0.007031 (0.006094) | -0.005988 (0.006231) | 0.6555 | agree |
| hogre_sanktioner | detected_share | -0.00229 (0.03353) | 0.01663 (0.05309) | 1.65 | agree |
| hogre_sanktioner | detections_per_year | -2 (1.158) | -1.362 (1.305) | 2.004 | agree |
| hogre_sanktioner | prohibitions_per_year | -0.5667 (0.4693) | -0.181 (0.4594) | 3.217 | DIFFERS |
| hogre_sanktioner | company_switches_per_year | -0.0381 (0.5331) | 0.1048 (0.4293) | 1.143 | agree |
| hogre_sanktioner | inspections_per_year | 0.05238 (0.2612) | -0.07143 (0.3766) | 1.48 | agree |
| hogre_sanktioner | road_checks_per_year | 0.7619 (2.649) | -0.7667 (2.444) | 2.323 | agree |
| informationsdelning | illegal_share | -0.001667 (0.006015) | -0.002137 (0.005259) | 0.3219 | agree |
| informationsdelning | detected_share | 0.02455 (0.05207) | 0.04277 (0.05217) | 1.354 | agree |
| informationsdelning | detections_per_year | 1.667 (1.736) | 2.448 (1.401) | 1.917 | agree |
| informationsdelning | prohibitions_per_year | 0.2143 (0.6139) | 0.5333 (0.5955) | 2.043 | agree |
| informationsdelning | company_switches_per_year | 0.3095 (0.5764) | 0.2381 (0.4615) | 0.5298 | agree |
| informationsdelning | inspections_per_year | -0.07619 (0.2995) | -0.1524 (0.4406) | 0.7833 | agree |
| informationsdelning | road_checks_per_year | 1.448 (3.352) | -0.7381 (2.933) | 2.687 | agree |
| vagkontroller | illegal_share | -0.003678 (0.006695) | -0.005379 (0.005146) | 1.103 | agree |
| vagkontroller | detected_share | -0.01091 (0.02919) | 0.01349 (0.05126) | 2.265 | agree |
| vagkontroller | detections_per_year | 2.4 (1.608) | 3.062 (2.028) | 1.401 | agree |
| vagkontroller | prohibitions_per_year | 0.481 (0.6492) | 0.5619 (0.671) | 0.4749 | agree |
| vagkontroller | company_switches_per_year | 0.4524 (0.6267) | 0.681 (0.6229) | 1.417 | agree |
| vagkontroller | inspections_per_year | -0.05714 (0.4068) | -0.1857 (0.34) | 1.328 | agree |
| vagkontroller | road_checks_per_year | 117.5 (4.108) | 114.8 (4.23) | 2.473 | agree |
| kombinerad | illegal_share | -0.005853 (0.004692) | -0.005124 (0.004807) | 0.5945 | agree |
| kombinerad | detected_share | 0.09803 (0.04866) | 0.1166 (0.06506) | 1.252 | agree |
| kombinerad | detections_per_year | 6.362 (2.026) | 7.314 (1.851) | 1.901 | agree |
| kombinerad | prohibitions_per_year | 1.981 (0.6624) | 2.286 (0.7843) | 1.626 | agree |
| kombinerad | company_switches_per_year | 0.5762 (0.6933) | 0.6143 (0.6313) | 0.2225 | agree |
| kombinerad | inspections_per_year | -0.2476 (0.3806) | -0.2952 (0.3879) | 0.4799 | agree |
| kombinerad | road_checks_per_year | 0.8429 (3.059) | -0.9476 (2.403) | 2.521 | agree |
