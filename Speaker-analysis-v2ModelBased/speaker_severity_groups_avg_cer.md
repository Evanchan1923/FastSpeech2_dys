# Speaker Severity Groups

Generated from the current train/dev speaker severity CSVs.

## Method

- Classification score: `avg_cer`. Merged speaker rates are weighted by `n_utts` when a speaker appears in more than one CSV row.
- High: score > 0.50
- Middle: 0.25 < score <= 0.50
- Low: score <= 0.25
- Repeated speaker IDs are merged once, with split names and etiologies combined.
- Split speaker share is calculated by speaker count within each severity level.

## Inputs

- `speaker-research/result/speaker_research_v1_train/speaker_severity_all.csv`
- `speaker-research/result/speaker_research_v2_dev/speaker_severity_all.csv`

## Summary

- Input rows: 962
- Unique speakers after merge: 962
- Speakers appearing in multiple rows: 0
- Total utterances: 369320

| Level | Speakers | Share | Split speaker share | Utterances | Mean score (Avg CER) | Mean WER | Mean CER |
| --- | --- | --- | --- | --- | --- | --- | --- |
| High | 16 | 1.7% | Train 14 (87.5%); Dev 2 (12.5%) | 4727 | 0.637 | 0.726 | 0.637 |
| Middle | 39 | 4.1% | Train 35 (89.7%); Dev 4 (10.3%) | 13345 | 0.337 | 0.424 | 0.337 |
| Low | 907 | 94.3% | Train 787 (86.8%); Dev 120 (13.2%) | 351248 | 0.044 | 0.071 | 0.044 |

## High

16 speakers.

Split speaker share: Train 14 (87.5%); Dev 2 (12.5%).

| Speaker | Score (Avg CER) | Avg WER | Avg CER | Utterances | Splits | Etiology | Rows merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a49aba71-22f9-4377-8b31-08dc44f243ab | 0.785 | 0.804 | 0.785 | 427 | Train | Cerebral Palsy | 1 |
| 57e0a805-a9b2-406f-57dc-08dcbb9f64e1 | 0.733 | 0.799 | 0.733 | 95 | Train | Cerebral Palsy | 1 |
| 72737d73-c35e-41f8-530b-08dc95210be1 | 0.725 | 0.848 | 0.725 | 102 | Train | Cerebral Palsy | 1 |
| 88473fad-a20d-4093-80c1-08dd36570e96 | 0.718 | 0.826 | 0.718 | 421 | Train | Down Syndrome | 1 |
| 109686bb-8e54-4ad7-530d-08dc95210be1 | 0.706 | 0.829 | 0.706 | 78 | Train | Cerebral Palsy | 1 |
| b4c68431-25ad-4a66-e59c-08dd187996f2 | 0.674 | 0.746 | 0.674 | 444 | Train | Cerebral Palsy | 1 |
| 8c6b6a3c-486a-4cbc-1c48-08db344ca254 | 0.672 | 0.688 | 0.672 | 167 | Train | Parkinson's Disease | 1 |
| f9d24399-f2a7-4662-3de8-08dd04d8f6c9 | 0.671 | 0.796 | 0.671 | 449 | Train | Cerebral Palsy | 1 |
| 9ac0450f-e7a9-411b-1e30-08dbe1ed2b7f | 0.659 | 0.719 | 0.659 | 321 | Train | Down Syndrome | 1 |
| 373e5404-3f4d-4d3d-9fd4-08dcee0760b0 | 0.627 | 0.705 | 0.627 | 355 | Train | Cerebral Palsy | 1 |
| 50deb470-4008-4b71-3c98-08dd1d31334b | 0.587 | 0.654 | 0.587 | 449 | Train | Cerebral Palsy | 1 |
| 4a9f71ab-f3a6-48a9-a1ba-08dcc7adb730 | 0.550 | 0.717 | 0.550 | 352 | Dev | Down Syndrome | 1 |
| fb9c683c-41a5-486c-ae6a-08dc945c48db | 0.538 | 0.649 | 0.538 | 406 | Dev | Cerebral Palsy | 1 |
| db5fac30-88e5-4585-1169-08dc623ec532 | 0.527 | 0.596 | 0.527 | 64 | Train | ALS | 1 |
| 3a3190d2-4f6c-45b1-22b3-08dc56b55882 | 0.517 | 0.653 | 0.517 | 154 | Train | Down Syndrome | 1 |
| 4d63203f-f931-4446-01d4-08dcfe7e7dfa | 0.504 | 0.580 | 0.504 | 443 | Train | Cerebral Palsy | 1 |

## Middle

39 speakers.

Split speaker share: Train 35 (89.7%); Dev 4 (10.3%).

| Speaker | Score (Avg CER) | Avg WER | Avg CER | Utterances | Splits | Etiology | Rows merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0f26015b-55ed-4412-5315-08dc95210be1 | 0.495 | 0.594 | 0.495 | 430 | Train | Cerebral Palsy | 1 |
| 4831b617-1e71-4205-ce35-08dca6823a12 | 0.465 | 0.562 | 0.465 | 447 | Train | Stroke | 1 |
| 95fbc887-4e56-4a81-57db-08dcbb9f64e1 | 0.457 | 0.570 | 0.457 | 440 | Train | Cerebral Palsy | 1 |
| b2f16a07-8441-43c9-fac8-08dd0a4af9ba | 0.452 | 0.529 | 0.452 | 350 | Dev | Cerebral Palsy | 1 |
| b9c4efa6-b9a8-4ff8-1e99-08dd6fc1860d | 0.449 | 0.552 | 0.449 | 252 | Train | Cerebral Palsy | 1 |
| 2c96c714-ecc7-4e9d-982a-08dc7e56149c | 0.426 | 0.538 | 0.426 | 3 | Train | Stroke | 1 |
| 16ec08db-f78e-418e-7a4d-08dc92404de1 | 0.411 | 0.533 | 0.411 | 215 | Train | Down Syndrome | 1 |
| 1f27e466-6e34-4c75-e903-08dcf2e1353e | 0.411 | 0.561 | 0.411 | 19 | Train | Cerebral Palsy | 1 |
| a98bac88-6fb4-4ead-fe58-08dd6266e2a3 | 0.401 | 0.488 | 0.401 | 263 | Train | Cerebral Palsy | 1 |
| 031e84ad-54f2-434b-abb3-08dc5d6a38e4 | 0.397 | 0.517 | 0.397 | 445 | Dev | ALS | 1 |
| c4b91392-9430-4ba4-3a1f-08dc5fadb5c5 | 0.375 | 0.413 | 0.375 | 436 | Train | ALS | 1 |
| cbad75f3-581e-4269-7053-08dc2b1e26da | 0.366 | 0.453 | 0.366 | 89 | Train | ALS | 1 |
| 27a3a1ac-c916-4bac-0b97-08dc12b452f6 | 0.361 | 0.456 | 0.361 | 430 | Train | Cerebral Palsy | 1 |
| 797f7a6f-99e7-4ff0-9d7b-08dc12a8d9fa | 0.360 | 0.471 | 0.360 | 444 | Train | Parkinson's Disease | 1 |
| 24e7fbed-4e86-452f-67f6-08dcbab8e251 | 0.359 | 0.449 | 0.359 | 417 | Dev | Cerebral Palsy | 1 |
| 7ac194f4-f9f3-48d0-cf1f-08dc89b72177 | 0.356 | 0.461 | 0.356 | 449 | Train | ALS | 1 |
| 84d7a172-1a56-4c1a-982c-08dc7e56149c | 0.339 | 0.386 | 0.339 | 449 | Train | ALS | 1 |
| 4001c750-b191-47db-611c-08dcdb04185c | 0.331 | 0.385 | 0.331 | 153 | Train | ALS | 1 |
| 33e1fca1-5687-4873-3e6c-08dc863e36ec | 0.327 | 0.450 | 0.327 | 394 | Train | Cerebral Palsy | 1 |
| 9c010598-69af-424f-f872-08dcfdd86f8f | 0.316 | 0.394 | 0.316 | 441 | Train | Parkinson's Disease | 1 |
| 50e4234a-739d-4443-02b0-08dcaa8c3d9d | 0.307 | 0.373 | 0.307 | 391 | Train | Cerebral Palsy | 1 |
| 9819c7bb-b76f-4920-2270-08dd5ceaf69c | 0.305 | 0.418 | 0.305 | 441 | Train | Cerebral Palsy | 1 |
| 54618732-a2cb-49ec-c034-08dc605e0191 | 0.299 | 0.384 | 0.299 | 430 | Dev | Cerebral Palsy | 1 |
| 6ac4b3e6-bb5d-4482-e9a9-08dc2e961576 | 0.299 | 0.394 | 0.299 | 448 | Train | Stroke | 1 |
| 374ad5cf-710f-4147-450c-08dc42c84745 | 0.297 | 0.354 | 0.297 | 450 | Train | Cerebral Palsy | 1 |
| 4c91dc4a-cb48-44af-ca97-08dd03e32564 | 0.295 | 0.377 | 0.295 | 449 | Train | Cerebral Palsy | 1 |
| 5db3a40e-b10a-4f87-c3bf-08dd001d41dc | 0.289 | 0.365 | 0.289 | 447 | Train | Cerebral Palsy | 1 |
| cd10d137-3fd1-493a-8c35-08dc73c64297 | 0.280 | 0.368 | 0.280 | 85 | Train | ALS | 1 |
| 8bf1a81b-146d-4df1-125a-08dc55a2762d | 0.279 | 0.365 | 0.279 | 429 | Train | Down Syndrome | 1 |
| e63a1e84-df39-4949-a1cb-08dc11dcc589 | 0.279 | 0.309 | 0.279 | 101 | Train | ALS | 1 |
| 1e997703-8b78-4fcb-e98b-08dc2e961576 | 0.275 | 0.366 | 0.275 | 349 | Train | Stroke | 1 |
| 28bf06dd-a8af-4a04-ef99-08db2d62a830 | 0.264 | 0.331 | 0.264 | 156 | Train | Parkinson's Disease | 1 |
| e01d8f1d-602e-4155-4839-08dc666bf63e | 0.264 | 0.335 | 0.264 | 222 | Train | Cerebral Palsy | 1 |
| d17c31ee-2e4b-47a4-b5a9-08dc3f363c7d | 0.262 | 0.381 | 0.262 | 430 | Train | Down Syndrome | 1 |
| 2dcb3ebc-59ea-4275-75a6-08dd3ba78fcd | 0.260 | 0.352 | 0.260 | 427 | Train | Cerebral Palsy | 1 |
| 0c3a355b-c4da-40fe-57de-08dcbb9f64e1 | 0.256 | 0.334 | 0.256 | 195 | Train | Cerebral Palsy | 1 |
| 6fff333d-3b46-4c5c-a1d3-08dc11dcc589 | 0.255 | 0.293 | 0.255 | 449 | Train | ALS | 1 |
| b6dd8594-a18c-45c7-2a77-08dca1b962ee | 0.254 | 0.336 | 0.254 | 430 | Train | Cerebral Palsy | 1 |
| 20c27dbe-3ba4-445a-1b1a-08db3b55cd4a | 0.251 | 0.342 | 0.251 | 450 | Train | Parkinson's Disease | 1 |

## Low

907 speakers.

Split speaker share: Train 787 (86.8%); Dev 120 (13.2%).

| Speaker | Score (Avg CER) | Avg WER | Avg CER | Utterances | Splits | Etiology | Rows merged |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11da7376-f5ee-4093-9514-08dc7733f79d | 0.250 | 0.288 | 0.250 | 449 | Train | Cerebral Palsy | 1 |
| ee837067-1278-4fc3-3e6b-08dc863e36ec | 0.248 | 0.305 | 0.248 | 450 | Dev | Parkinson's Disease | 1 |
| e83926cc-57c5-43ae-5bb9-08dbeaf7b07f | 0.246 | 0.332 | 0.246 | 42 | Train | Down Syndrome | 1 |
| 72089bf2-acc1-41aa-cf5d-08dc89b72177 | 0.242 | 0.289 | 0.242 | 135 | Train | ALS | 1 |
| 2ef1df63-fbee-4bd4-3855-08dd34a28b01 | 0.242 | 0.324 | 0.242 | 414 | Dev | Cerebral Palsy | 1 |
| 23b27207-6d7f-4da9-a85b-08dcf77c2ab9 | 0.241 | 0.320 | 0.241 | 304 | Train | Cerebral Palsy | 1 |
| 5b6dbc46-a544-40e1-0bb4-08dcf9635df3 | 0.236 | 0.313 | 0.236 | 148 | Train | Down Syndrome | 1 |
| 71bfe758-dfaa-4227-8365-08dca350f4dc | 0.235 | 0.266 | 0.235 | 449 | Train | Cerebral Palsy | 1 |
| bc102d2c-eb51-41c3-b21c-08dc6a2b69be | 0.235 | 0.309 | 0.235 | 430 | Train | Down Syndrome | 1 |
| 6cd9d7e7-380f-43aa-b90a-08dc99d6617d | 0.232 | 0.291 | 0.232 | 430 | Train | Cerebral Palsy | 1 |
| d5a83a43-b9d3-404b-a186-08dc11dcc589 | 0.232 | 0.313 | 0.232 | 450 | Train | ALS | 1 |
| d41daa38-6d46-433c-6825-08dd025ce1a9 | 0.230 | 0.269 | 0.230 | 328 | Dev | Cerebral Palsy | 1 |
| 073216b5-1cd1-4127-9277-08db27473805 | 0.227 | 0.322 | 0.227 | 284 | Train | Parkinson's Disease | 1 |
| aff2de06-efe1-4074-3e3f-08dc895255bb | 0.225 | 0.273 | 0.225 | 119 | Dev | Down Syndrome | 1 |
| 4beb2a15-8e5d-409d-b084-08dcd0e0b071 | 0.224 | 0.338 | 0.224 | 383 | Train | Down Syndrome | 1 |
| dcd189c6-e814-4561-698a-08dc17913c94 | 0.224 | 0.317 | 0.224 | 429 | Train | Cerebral Palsy | 1 |
| d5fbd782-6354-4109-da7e-08dc75b20572 | 0.221 | 0.291 | 0.221 | 428 | Train | Cerebral Palsy | 1 |
| 61eef070-a4b3-4c93-67f9-08dcbab8e251 | 0.218 | 0.287 | 0.218 | 403 | Train | Cerebral Palsy | 1 |
| 64fd6d17-bf05-4e96-8366-08dca350f4dc | 0.217 | 0.300 | 0.217 | 128 | Train | Down Syndrome | 1 |
| f6d82e47-e44c-44f9-e96b-08dc2e961576 | 0.214 | 0.311 | 0.214 | 430 | Train | Stroke | 1 |
| 5a96c15d-bbce-492a-117a-08dba7fa5465 | 0.213 | 0.290 | 0.213 | 446 | Train | Parkinson's Disease | 1 |
| af2f6fdb-6578-403f-2605-08dd2ae4ac9c | 0.208 | 0.249 | 0.208 | 179 | Train | ALS | 1 |
| d1b9444a-2ed1-438e-fd68-08dcb5d1edd7 | 0.203 | 0.267 | 0.203 | 448 | Dev | Parkinson's Disease | 1 |
| 80e1d83c-19b4-4fff-2089-08dbb80075e5 | 0.198 | 0.264 | 0.198 | 446 | Train | Parkinson's Disease | 1 |
| bfdd87ed-10f0-46a4-b109-08dc2a4a210d | 0.198 | 0.281 | 0.198 | 450 | Train | Parkinson's Disease | 1 |
| 69694c4b-2f3b-4996-123e-08dc8ec52b92 | 0.194 | 0.225 | 0.194 | 357 | Train | ALS | 1 |
| 0c9851af-ac0a-4ce0-75ec-08dc5951d476 | 0.193 | 0.280 | 0.193 | 65 | Train | Down Syndrome | 1 |
| 50594c91-060d-4b6e-43d8-08dca42d8162 | 0.189 | 0.274 | 0.189 | 427 | Train | Down Syndrome | 1 |
| 6686c710-e679-4954-e969-08dc2e961576 | 0.189 | 0.381 | 0.189 | 7 | Train | Stroke | 1 |
| d4a3472b-7002-4075-57d8-08dcbb9f64e1 | 0.186 | 0.259 | 0.186 | 438 | Train | Cerebral Palsy | 1 |
| 5801631a-2f04-4d94-0b19-08dc228b8bf7 | 0.185 | 0.255 | 0.185 | 430 | Dev | Cerebral Palsy | 1 |
| 01963e4d-e342-47f1-0fae-08dcd99f98d3 | 0.184 | 0.231 | 0.184 | 90 | Train | ALS | 1 |
| 4a7d3f03-d421-48f2-e593-08dd187996f2 | 0.183 | 0.285 | 0.183 | 445 | Train | Stroke | 1 |
| e42558d6-5a42-437d-e7c4-08dcd9e31338 | 0.183 | 0.219 | 0.183 | 312 | Dev | ALS | 1 |
| db444f11-e4c6-4df1-1171-08dba7fa5465 | 0.180 | 0.260 | 0.180 | 448 | Train | Parkinson's Disease | 1 |
| e464695c-72b9-4299-ab99-08dc0d884980 | 0.178 | 0.254 | 0.178 | 412 | Train | Down Syndrome | 1 |
| 93dec82c-f740-4308-f585-08dc8fac837a | 0.176 | 0.230 | 0.176 | 430 | Train | Cerebral Palsy | 1 |
| c15f15a6-86af-4a94-760d-08dc47b40b59 | 0.173 | 0.261 | 0.173 | 106 | Train | Down Syndrome | 1 |
| ffbb560c-78e1-4dc2-aa21-08db7f28d1f2 | 0.172 | 0.240 | 0.172 | 449 | Train | Parkinson's Disease | 1 |
| 0a232c15-1d0a-4fb9-085c-08dcd1c0704e | 0.170 | 0.226 | 0.170 | 394 | Train | Stroke | 1 |
| 15dec664-dc2b-4a05-4a54-08dc3c7b3134 | 0.170 | 0.247 | 0.170 | 82 | Dev | Down Syndrome | 1 |
| 889c317c-39f2-4dcd-d5e5-08dc00f40ee5 | 0.170 | 0.235 | 0.170 | 374 | Dev | Cerebral Palsy | 1 |
| 61668d9d-71d0-4e61-603d-08db888af625 | 0.168 | 0.243 | 0.168 | 449 | Train | Parkinson's Disease | 1 |
| 4a73d637-b066-4df7-76a1-08dc54a70eeb | 0.163 | 0.222 | 0.163 | 430 | Train | Down Syndrome | 1 |
| 3fa53307-ed46-4d78-5764-08dcfa856e25 | 0.161 | 0.216 | 0.161 | 441 | Train | Stroke | 1 |
| 6532d81c-e8be-4910-1c46-08db344ca254 | 0.158 | 0.235 | 0.158 | 444 | Dev | Parkinson's Disease | 1 |
| 674ab9df-ce7d-4118-abb1-08dc5d6a38e4 | 0.158 | 0.190 | 0.158 | 444 | Train | ALS | 1 |
| b9c4420a-1096-4455-5fe5-08dc630c1396 | 0.156 | 0.210 | 0.156 | 425 | Train | Cerebral Palsy | 1 |
| 006239c7-4caf-4289-a1a0-08dc11dcc589 | 0.155 | 0.221 | 0.155 | 450 | Train | ALS | 1 |
| 64fecd03-ce4e-4b38-e960-08dc2e961576 | 0.155 | 0.258 | 0.155 | 442 | Train | Stroke | 1 |
| b094a2e5-1ebe-4345-ad9d-08dce09abeb4 | 0.154 | 0.207 | 0.154 | 90 | Train | ALS | 1 |
| 13f386bd-ab37-4183-8cf0-08dcff4f47ae | 0.150 | 0.229 | 0.150 | 346 | Train | Cerebral Palsy | 1 |
| 9bd947ca-0c69-40e9-bd5a-08dc8ad4730d | 0.149 | 0.200 | 0.149 | 373 | Train | Cerebral Palsy | 1 |
| e73f0ce2-a354-4e73-c3a8-08dcf87380a2 | 0.148 | 0.162 | 0.148 | 436 | Train | ALS | 1 |
| f6616ff1-176f-477d-1cda-08dce2a2fe9b | 0.146 | 0.236 | 0.146 | 374 | Train | Stroke | 1 |
| bfc2ed2b-fec9-44f8-4988-08dcb4d7acba | 0.145 | 0.213 | 0.145 | 423 | Train | Cerebral Palsy | 1 |
| cef21a18-cfb1-47cb-32dd-08dc57db575d | 0.142 | 0.201 | 0.142 | 429 | Train | Cerebral Palsy | 1 |
| 0871da63-c175-4b34-4eb5-08dbaa61e12d | 0.141 | 0.219 | 0.141 | 434 | Train | Parkinson's Disease | 1 |
| 8a4b09ab-9e6d-4f09-f350-08dd446c36bb | 0.141 | 0.187 | 0.141 | 429 | Train | Cerebral Palsy | 1 |
| a4f5f02e-63a1-4595-a17d-08dc11dcc589 | 0.138 | 0.214 | 0.138 | 180 | Train | ALS | 1 |
| 5b9d4592-7a2e-464a-8bbe-08dd4210739c | 0.137 | 0.187 | 0.137 | 357 | Train | Stroke | 1 |
| 6ad121e2-b05a-4ee9-c3a3-08dcf87380a2 | 0.137 | 0.187 | 0.137 | 368 | Train | Down Syndrome | 1 |
| 8926bff8-ec04-42ba-57e1-08dcbb9f64e1 | 0.137 | 0.204 | 0.137 | 401 | Dev | Cerebral Palsy | 1 |
| cd215cb2-46f5-4676-c557-08dc27c1bd26 | 0.137 | 0.200 | 0.137 | 430 | Train | Parkinson's Disease | 1 |
| d52cebbf-9977-4345-71f3-08dbb37cf835 | 0.137 | 0.187 | 0.137 | 354 | Train | Parkinson's Disease | 1 |
| 90231471-f333-4f3a-115e-08dba7fa5465 | 0.136 | 0.186 | 0.136 | 444 | Train | Parkinson's Disease | 1 |
| 02df2d03-54da-4f60-0bb5-08dcf9635df3 | 0.135 | 0.193 | 0.135 | 444 | Train | Parkinson's Disease | 1 |
| 05873438-e988-4ede-0218-08dc41d581c9 | 0.135 | 0.196 | 0.135 | 426 | Train | Cerebral Palsy | 1 |
| a68ea94f-8194-49e5-3c84-08dc4b8edc60 | 0.133 | 0.199 | 0.133 | 327 | Train | Cerebral Palsy | 1 |
| b4dbd9f9-85f2-4f92-973a-08dca59f2b1c | 0.133 | 0.187 | 0.133 | 352 | Dev | Stroke | 1 |
| cf1907a1-3a7b-4d5a-1556-08dd13b9e946 | 0.132 | 0.154 | 0.132 | 450 | Train | Cerebral Palsy | 1 |
| 51d948c2-476f-4f0d-bc01-08dd438c3c56 | 0.131 | 0.178 | 0.131 | 210 | Train | Down Syndrome | 1 |
| fded1a12-e747-41a2-0fe6-08dcd99f98d3 | 0.127 | 0.183 | 0.127 | 245 | Train | ALS | 1 |
| 40c405be-4046-4127-a1ab-08dc11dcc589 | 0.125 | 0.144 | 0.125 | 450 | Train | ALS | 1 |
| db72a193-5788-4716-2cc5-08dc137c976d | 0.125 | 0.192 | 0.125 | 429 | Train | Cerebral Palsy | 1 |
| bed5668f-bae5-432e-bbff-08dd438c3c56 | 0.122 | 0.185 | 0.122 | 430 | Train | Down Syndrome | 1 |
| f7d0127d-f0a0-442a-1e9c-08dcf50074d6 | 0.122 | 0.159 | 0.122 | 127 | Train | ALS | 1 |
| 5a006fbe-b5c4-476b-7137-08dc19070b4a | 0.121 | 0.148 | 0.121 | 85 | Train | ALS | 1 |
| 9204489e-77c2-4236-da81-08dc75b20572 | 0.120 | 0.191 | 0.120 | 430 | Train | Cerebral Palsy | 1 |
| fc9a1978-865e-49a8-0b8f-08dc12b452f6 | 0.119 | 0.169 | 0.119 | 428 | Train | Cerebral Palsy | 1 |
| 1fdc2f8c-7bcb-4063-3383-08db7f04fed4 | 0.118 | 0.167 | 0.118 | 449 | Train | Parkinson's Disease | 1 |
| 2f4abb28-6f87-4c96-e7c3-08dcd9e31338 | 0.116 | 0.140 | 0.116 | 447 | Train | ALS | 1 |
| 5b8566c5-f3f0-4c2e-7c8d-08dcc6cfbf82 | 0.116 | 0.143 | 0.116 | 449 | Train | Cerebral Palsy | 1 |
| 56d198e7-ad8c-4441-be52-08dc5a51b53b | 0.115 | 0.152 | 0.115 | 430 | Train | Down Syndrome | 1 |
| 929438bb-0082-4aaa-e997-08dc2e961576 | 0.114 | 0.177 | 0.114 | 185 | Train | Stroke | 1 |
| a5e1dc76-fb94-4590-2eaa-08dc27684872 | 0.114 | 0.171 | 0.114 | 45 | Train | Parkinson's Disease | 1 |
| 4d300376-62e4-431b-3320-08dca05f46a7 | 0.113 | 0.168 | 0.113 | 422 | Train | Cerebral Palsy | 1 |
| f5a06bd3-3191-46dd-0bae-08dcf9635df3 | 0.113 | 0.170 | 0.113 | 390 | Dev | Down Syndrome | 1 |
| d86d8a20-de2b-4c93-219b-08dc9072fb0e | 0.112 | 0.170 | 0.112 | 239 | Train | Cerebral Palsy | 1 |
| ee4627de-c026-4d38-e164-08dc4555b94c | 0.112 | 0.158 | 0.112 | 98 | Dev | ALS | 1 |
| 685a7079-e55b-4759-5760-08dcfa856e25 | 0.111 | 0.209 | 0.111 | 147 | Train | Down Syndrome | 1 |
| ba81400d-8291-415a-15e5-08dc16a43af2 | 0.111 | 0.159 | 0.111 | 428 | Train | Cerebral Palsy | 1 |
| 8a2785b4-c2d4-4561-33a8-08dc856a35ea | 0.110 | 0.168 | 0.110 | 425 | Train | Cerebral Palsy | 1 |
| 544eb572-a9a8-42ed-a85c-08dcf77c2ab9 | 0.108 | 0.160 | 0.108 | 430 | Train | Cerebral Palsy | 1 |
| 7d292491-c03d-4e5b-8cf3-08dcff4f47ae | 0.108 | 0.134 | 0.108 | 436 | Train | Stroke | 1 |
| c37b3499-2a84-4371-c590-08dc27c1bd26 | 0.108 | 0.167 | 0.108 | 442 | Train | ALS | 1 |
| d99bc28b-9740-46c7-d192-08dcc1fc9b7b | 0.108 | 0.134 | 0.108 | 133 | Train | Stroke | 1 |
| e9189423-0b1f-4e22-57d9-08dcbb9f64e1 | 0.108 | 0.159 | 0.108 | 448 | Train | Cerebral Palsy | 1 |
| b747b80a-ca00-4526-682b-08dd025ce1a9 | 0.107 | 0.156 | 0.107 | 429 | Train | Cerebral Palsy | 1 |
| 71b709a6-66a6-4c0f-3857-08dd34a28b01 | 0.106 | 0.131 | 0.106 | 450 | Train | Stroke | 1 |
| 9954f9a7-b55a-4981-46c2-08db82273f48 | 0.106 | 0.156 | 0.106 | 447 | Train | Parkinson's Disease | 1 |
| a0154efe-bf6b-4648-4987-08dcb4d7acba | 0.106 | 0.153 | 0.106 | 430 | Train | Cerebral Palsy | 1 |
| 1191a69f-905d-41f7-0d6a-08db6695a2e1 | 0.105 | 0.157 | 0.105 | 296 | Train | Parkinson's Disease | 1 |
| d9892453-ebb1-4d36-7ce0-08dc8ba4f236 | 0.104 | 0.156 | 0.104 | 427 | Dev | Cerebral Palsy | 1 |
| 09b6b8e6-efbe-447c-ca98-08dd03e32564 | 0.104 | 0.151 | 0.104 | 424 | Train | Cerebral Palsy | 1 |
| 6b6875ec-8f41-48ca-2e64-08dce1b26f4b | 0.104 | 0.134 | 0.104 | 415 | Train | Cerebral Palsy | 1 |
| f0472e92-85eb-46f5-dcfe-08dc1694d265 | 0.104 | 0.164 | 0.104 | 122 | Dev | Parkinson's Disease | 1 |
| 2335fe47-0b4a-4d4b-0fd5-08dcd99f98d3 | 0.102 | 0.104 | 0.102 | 449 | Train | ALS | 1 |
| 5b50291f-f241-483e-8bbd-08dd4210739c | 0.102 | 0.153 | 0.102 | 427 | Dev | Down Syndrome | 1 |
| b19e7255-5c4c-46e1-f354-08dd446c36bb | 0.102 | 0.151 | 0.102 | 414 | Train | Cerebral Palsy | 1 |
| c2f4ea67-f6cb-4ad3-0bb8-08dcf9635df3 | 0.102 | 0.139 | 0.102 | 6 | Train | Down Syndrome | 1 |
| cb7eb82b-3e31-4d0f-3e37-08dc895255bb | 0.102 | 0.159 | 0.102 | 428 | Train | Cerebral Palsy | 1 |
| 56084d10-2aa7-4f02-304a-08dbf050033d | 0.101 | 0.160 | 0.101 | 429 | Dev | Down Syndrome | 1 |
| 6ce4979e-e4cf-4550-b585-08dc5e199653 | 0.099 | 0.143 | 0.099 | 54 | Train | ALS | 1 |
| e6637ea3-8d88-40ca-8b32-08dc44f243ab | 0.099 | 0.114 | 0.099 | 448 | Dev | ALS | 1 |
| 80dea61f-69d1-4e86-9992-08dcab8095cf | 0.098 | 0.163 | 0.098 | 429 | Train | Down Syndrome | 1 |
| aaf5a053-3319-4992-37c6-08dce6e2632a | 0.098 | 0.169 | 0.098 | 430 | Train | Cerebral Palsy | 1 |
| fb997ed6-f5f5-4736-e95c-08dc2e961576 | 0.098 | 0.158 | 0.098 | 406 | Train | Stroke | 1 |
| 2007718f-efef-4f5e-ab5c-08dc51b077c7 | 0.097 | 0.150 | 0.097 | 430 | Train | Cerebral Palsy | 1 |
| f15effc2-f0a7-442b-ce36-08dca6823a12 | 0.097 | 0.109 | 0.097 | 450 | Train | ALS | 1 |
| 4f03e91e-a8a7-45b7-b1eb-08dd512ec3b7 | 0.096 | 0.132 | 0.096 | 439 | Dev | Stroke | 1 |
| 5b74c670-a5d3-4a7b-6c8a-08dd543e01a5 | 0.096 | 0.143 | 0.096 | 347 | Train | Cerebral Palsy | 1 |
| 1b82ca80-115a-4348-43db-08dc13e54ff5 | 0.095 | 0.147 | 0.095 | 430 | Train | Cerebral Palsy | 1 |
| 3d7fc0a6-60cd-470f-4f4a-08db9399a6d5 | 0.095 | 0.135 | 0.095 | 443 | Train | Parkinson's Disease | 1 |
| 3e01c059-ccd9-40a2-5242-08dc17032f59 | 0.095 | 0.116 | 0.095 | 448 | Train | Stroke | 1 |
| 65941f0e-4793-4142-808d-08dc28b09bf9 | 0.095 | 0.144 | 0.095 | 435 | Train | Parkinson's Disease | 1 |
| 1a029240-167d-4433-8b30-08dc44f243ab | 0.094 | 0.137 | 0.094 | 428 | Train | Cerebral Palsy | 1 |
| 4495e9c0-6fab-4811-cf5a-08dc89b72177 | 0.094 | 0.108 | 0.094 | 246 | Train | ALS | 1 |
| 6d697024-54d1-4fbc-33a7-08dc856a35ea | 0.094 | 0.130 | 0.094 | 419 | Train | Cerebral Palsy | 1 |
| 71127cd8-5b78-48b5-cb3e-08db30a2c2d0 | 0.093 | 0.147 | 0.093 | 246 | Train | Parkinson's Disease | 1 |
| 8bbd158c-6085-46d1-9273-08dc7b82c294 | 0.093 | 0.204 | 0.093 | 40 | Train | Stroke | 1 |
| c9b138ab-9c5a-4cc2-301a-08dcc11ab035 | 0.093 | 0.105 | 0.093 | 448 | Train | ALS | 1 |
| 02005a84-8847-4ef7-7b99-08dc286c108f | 0.092 | 0.135 | 0.092 | 448 | Dev | Parkinson's Disease | 1 |
| 837551f2-df1e-492e-5533-08dc8c8af7c9 | 0.091 | 0.138 | 0.091 | 449 | Train | ALS | 1 |
| 8b7f6b37-fd80-4318-a1b9-08dcc7adb730 | 0.091 | 0.143 | 0.091 | 444 | Dev | Parkinson's Disease | 1 |
| ee6453f7-892a-4979-eca1-08dc9cb096c2 | 0.091 | 0.138 | 0.091 | 421 | Train | Cerebral Palsy | 1 |
| 83135bc4-8567-46e3-3c96-08dd1d31334b | 0.090 | 0.131 | 0.090 | 430 | Train | Down Syndrome | 1 |
| 83a3efde-0b37-45e7-f584-08dc8fac837a | 0.089 | 0.104 | 0.089 | 450 | Train | ALS | 1 |
| fbc3e16c-6fad-47b7-7695-08dc54a70eeb | 0.089 | 0.154 | 0.089 | 98 | Train | Down Syndrome | 1 |
| 5e17c1c9-eb2a-4fa6-4985-08dcb4d7acba | 0.088 | 0.138 | 0.088 | 422 | Dev | Cerebral Palsy | 1 |
| 9ba5ee09-2958-4d2c-69a3-08dc17913c94 | 0.088 | 0.133 | 0.088 | 448 | Train | ALS | 1 |
| babd4b3a-c40d-4e40-7f8b-08dc9f90df2f | 0.088 | 0.153 | 0.088 | 430 | Train | Cerebral Palsy | 1 |
| 108bae54-13c5-4f33-769b-08dc54a70eeb | 0.088 | 0.153 | 0.088 | 428 | Dev | Down Syndrome | 1 |
| 9c0ed7c3-ff8e-495c-7092-08dd58089c18 | 0.087 | 0.146 | 0.087 | 25 | Dev | Down Syndrome | 1 |
| 588411db-3601-45c4-59e1-08dd3c96897d | 0.086 | 0.137 | 0.086 | 377 | Train | Stroke | 1 |
| 74613052-fd59-45c8-ab54-08db7376d336 | 0.085 | 0.135 | 0.085 | 447 | Dev | Parkinson's Disease | 1 |
| d765e201-53e7-41a9-1cdf-08dcd3e137e8 | 0.084 | 0.145 | 0.084 | 402 | Dev | Down Syndrome | 1 |
| f791828b-76cb-4b63-f355-08dd446c36bb | 0.084 | 0.123 | 0.084 | 415 | Train | Cerebral Palsy | 1 |
| 0eec6379-3c4d-48e2-2bfa-08dc9148fdda | 0.083 | 0.133 | 0.083 | 448 | Train | ALS | 1 |
| 93bbf306-cb27-4be5-e7ff-08dbe60d97fb | 0.083 | 0.124 | 0.083 | 429 | Dev | Down Syndrome | 1 |
| 293353e2-b0e2-4fab-1e33-08dbe1ed2b7f | 0.082 | 0.127 | 0.082 | 419 | Train | Down Syndrome | 1 |
| 9f03f9e5-ec8b-4893-7f91-08dc9f90df2f | 0.082 | 0.141 | 0.082 | 429 | Train | Down Syndrome | 1 |
| aca26181-40fd-4280-769e-08dc54a70eeb | 0.082 | 0.140 | 0.082 | 339 | Train | Down Syndrome | 1 |
| afbe9f1a-80f4-4d78-dde4-08dc9aac4c52 | 0.082 | 0.150 | 0.082 | 429 | Train | Cerebral Palsy | 1 |
| 88219ed9-d7ba-4d3d-f94e-08dc1c2dd218 | 0.081 | 0.130 | 0.081 | 430 | Train | Down Syndrome | 1 |
| 9bb4a8b3-27b1-4831-01ce-08dcfe7e7dfa | 0.081 | 0.147 | 0.081 | 449 | Train | Stroke | 1 |
| 64be89ec-8444-46b3-0b0c-08dc0c97c3b8 | 0.080 | 0.127 | 0.080 | 268 | Train | ALS | 1 |
| d443c67d-a3ee-497d-e7b4-08dcd9e31338 | 0.080 | 0.102 | 0.080 | 63 | Dev | ALS | 1 |
| 19544a94-6a1d-48a1-b199-08db2507e8b5 | 0.078 | 0.118 | 0.078 | 439 | Train | Parkinson's Disease | 1 |
| 26e2c221-878d-4759-7101-08db6acf772a | 0.078 | 0.130 | 0.078 | 449 | Train | Parkinson's Disease | 1 |
| 676ebf09-2dbd-4ec7-9d06-08dd3773226f | 0.078 | 0.091 | 0.078 | 450 | Train | ALS | 1 |
| a1dec06a-a466-4786-b587-08dc5e199653 | 0.078 | 0.122 | 0.078 | 450 | Train | ALS | 1 |
| 4b3c8e9f-f9b2-496f-24b0-08dcbcb70931 | 0.077 | 0.125 | 0.077 | 445 | Train | Cerebral Palsy | 1 |
| 51451a02-b769-42db-fd6d-08dcb5d1edd7 | 0.077 | 0.122 | 0.077 | 415 | Dev | Cerebral Palsy | 1 |
| 587bf91a-74cd-4766-cf36-08dc89b72177 | 0.077 | 0.127 | 0.077 | 450 | Train | Parkinson's Disease | 1 |
| dc5c25b4-43a7-4af3-cf4f-08dc89b72177 | 0.077 | 0.103 | 0.077 | 89 | Dev | ALS | 1 |
| f0d2679d-2929-4281-2f6c-08dbdd83a37e | 0.077 | 0.115 | 0.077 | 443 | Train | Parkinson's Disease | 1 |
| 748019c4-bf28-4144-a168-08dc11dcc589 | 0.076 | 0.121 | 0.076 | 436 | Train | ALS | 1 |
| a14d22c1-10e8-4dcf-e962-08dc2e961576 | 0.075 | 0.122 | 0.075 | 380 | Dev | Stroke | 1 |
| 7a19d077-979e-4bc7-415c-08dcddb9e4a3 | 0.074 | 0.100 | 0.074 | 213 | Train | Down Syndrome | 1 |
| 8954331a-4767-4ab1-ce3a-08dca6823a12 | 0.074 | 0.114 | 0.074 | 449 | Train | Stroke | 1 |
| c0075f18-fbb3-4509-14b2-08dcbf756c98 | 0.074 | 0.084 | 0.074 | 180 | Dev | ALS | 1 |
| d7ce7d5f-8c95-4569-cfa6-08db726500b4 | 0.074 | 0.109 | 0.074 | 450 | Train | Parkinson's Disease | 1 |
| 3df6f386-b762-4a89-43f5-08dc2f748b5c | 0.073 | 0.093 | 0.073 | 450 | Train | Stroke | 1 |
| 97bedfe3-75cb-43a8-123c-08dc8ec52b92 | 0.073 | 0.120 | 0.073 | 82 | Train | Parkinson's Disease | 1 |
| d3170e74-099a-4e72-6987-08db566c029c | 0.073 | 0.127 | 0.073 | 173 | Train | Parkinson's Disease | 1 |
| 667c880e-86a5-4ff6-67fe-08dcbab8e251 | 0.072 | 0.095 | 0.072 | 444 | Train | Cerebral Palsy | 1 |
| d0b51d79-c72c-4c4e-cb78-08dc45edfda4 | 0.072 | 0.095 | 0.072 | 156 | Train | ALS | 1 |
| eb809662-1690-4df6-8ac7-08dc93ad1e1c | 0.072 | 0.108 | 0.072 | 436 | Train | ALS | 1 |
| 2d157949-e40e-4b8a-816b-08dc70f89134 | 0.071 | 0.130 | 0.071 | 440 | Dev | Parkinson's Disease | 1 |
| 5687abdb-3aba-4d45-75ea-08dc5951d476 | 0.071 | 0.114 | 0.071 | 430 | Train | Down Syndrome | 1 |
| ef9ef2f9-663c-4b75-9d07-08dd3773226f | 0.071 | 0.116 | 0.071 | 430 | Train | Down Syndrome | 1 |
| bc4f21e7-35a5-439a-1cd6-08dce2a2fe9b | 0.070 | 0.092 | 0.070 | 314 | Train | Stroke | 1 |
| 0d1662bb-9121-4239-80c0-08dd36570e96 | 0.069 | 0.096 | 0.069 | 238 | Train | Down Syndrome | 1 |
| 8b4446c9-d818-4132-3de7-08dd04d8f6c9 | 0.069 | 0.113 | 0.069 | 429 | Train | Down Syndrome | 1 |
| 1fd8133a-324e-400b-972f-08dca59f2b1c | 0.068 | 0.097 | 0.068 | 429 | Train | Cerebral Palsy | 1 |
| 6b4b24d9-1f5e-4a2d-530c-08dc95210be1 | 0.068 | 0.137 | 0.068 | 402 | Train | Parkinson's Disease | 1 |
| a0ee61cb-6b1e-420c-0518-08dcc0518fb9 | 0.068 | 0.110 | 0.068 | 429 | Train | Cerebral Palsy | 1 |
| 6d4fb4dc-43d8-4f56-4986-08dcb4d7acba | 0.067 | 0.127 | 0.067 | 430 | Train | Cerebral Palsy | 1 |
| af9daf95-be36-4cb2-0515-08dcc0518fb9 | 0.067 | 0.106 | 0.067 | 430 | Train | Cerebral Palsy | 1 |
| c9b74d18-ed50-4b9b-d79f-08dc46c59895 | 0.067 | 0.107 | 0.067 | 449 | Train | Parkinson's Disease | 1 |
| 6ddd2d5c-acbc-40ba-a170-08dc11dcc589 | 0.066 | 0.116 | 0.066 | 317 | Train | ALS | 1 |
| ea9825d9-3c46-49ed-b21d-08dc6a2b69be | 0.066 | 0.081 | 0.066 | 440 | Dev | ALS | 1 |
| 14d9556f-a6df-4984-a84f-08dc202b0c19 | 0.065 | 0.102 | 0.065 | 418 | Train | Parkinson's Disease | 1 |
| 621afbb7-6745-452a-d57b-08dc71d79b4d | 0.065 | 0.111 | 0.065 | 444 | Dev | Parkinson's Disease | 1 |
| 969e5b34-f205-480f-1cd9-08dcd3e137e8 | 0.065 | 0.103 | 0.065 | 429 | Train | Cerebral Palsy | 1 |
| 9d33c23d-5a77-45dc-c547-08dbb7ad5db3 | 0.065 | 0.106 | 0.065 | 450 | Dev | Parkinson's Disease | 1 |
| edd079b3-50a6-48d3-30bf-08db6d06498f | 0.065 | 0.102 | 0.065 | 426 | Train | Parkinson's Disease | 1 |
| 5dc44062-8bfa-4867-db95-08dc26bda4f1 | 0.064 | 0.106 | 0.064 | 149 | Train | ALS | 1 |
| 0012df94-51aa-4ad0-79db-08dd17980f6b | 0.063 | 0.112 | 0.063 | 429 | Train | Down Syndrome | 1 |
| 81cbf5cb-457d-47f6-ab9a-08dc0d884980 | 0.063 | 0.106 | 0.063 | 422 | Train | Down Syndrome | 1 |
| c1e4b9c9-4b7a-4cb4-1cd8-08dce2a2fe9b | 0.063 | 0.095 | 0.063 | 214 | Train | Stroke | 1 |
| e85ef8b6-1b8a-44f1-9736-08dca59f2b1c | 0.063 | 0.097 | 0.063 | 443 | Train | Stroke | 1 |
| 3c1f5ec6-17d8-4d69-87a5-08dc74e08a4e | 0.062 | 0.114 | 0.062 | 428 | Dev | Cerebral Palsy | 1 |
| 1628ada6-3321-4052-22b4-08dc56b55882 | 0.062 | 0.108 | 0.062 | 430 | Dev | Down Syndrome | 1 |
| 1433daa5-d443-4379-79d9-08dd17980f6b | 0.061 | 0.103 | 0.061 | 426 | Train | Down Syndrome | 1 |
| 435006a9-e960-46a2-8a60-08db31656635 | 0.061 | 0.097 | 0.061 | 449 | Train | Parkinson's Disease | 1 |
| 52334bb8-6f4a-4d73-a1b7-08dcc7adb730 | 0.061 | 0.097 | 0.061 | 428 | Train | Down Syndrome | 1 |
| 75a389c8-cae1-4e45-e828-08dbe0ac2304 | 0.061 | 0.104 | 0.061 | 448 | Train | Parkinson's Disease | 1 |
| ae83d2f7-636f-43fa-33a1-08dc856a35ea | 0.061 | 0.098 | 0.061 | 426 | Train | Stroke | 1 |
| b08e1264-1b1a-4edd-3e36-08dc895255bb | 0.061 | 0.100 | 0.061 | 427 | Train | Cerebral Palsy | 1 |
| e12d07cc-b73a-4c62-6ad8-08dbe30077ee | 0.061 | 0.097 | 0.061 | 441 | Train | Parkinson's Disease | 1 |
| a330c7be-433a-4eda-b953-08dc6eabb1a3 | 0.060 | 0.114 | 0.060 | 430 | Dev | Down Syndrome | 1 |
| 0acad164-9f6f-4abf-abca-08dc5d6a38e4 | 0.060 | 0.101 | 0.060 | 449 | Train | ALS | 1 |
| 137952a5-3e65-4f4b-bd57-08dc8ad4730d | 0.060 | 0.099 | 0.060 | 449 | Train | ALS | 1 |
| 28fe23ad-6c0d-411b-03f3-08dd318df37f | 0.060 | 0.102 | 0.060 | 428 | Train | Cerebral Palsy | 1 |
| 88ff2689-ab03-41ba-3919-08dc358e2588 | 0.060 | 0.108 | 0.060 | 423 | Dev | Stroke | 1 |
| ec8650b8-631f-485a-ee43-08dc502eceb5 | 0.060 | 0.114 | 0.060 | 322 | Train | Down Syndrome | 1 |
| dc1f1a85-496d-467f-d253-08dc20f4e593 | 0.060 | 0.080 | 0.060 | 44 | Train | ALS | 1 |
| 2ab18dbe-6460-4adc-5537-08dc8c8af7c9 | 0.059 | 0.104 | 0.059 | 252 | Train | ALS | 1 |
| 66018674-5b03-4623-1188-08dba7fa5465 | 0.059 | 0.096 | 0.059 | 435 | Train | Parkinson's Disease | 1 |
| cc29e135-2a7a-46e9-8f04-08dc7f6a721b | 0.059 | 0.095 | 0.059 | 364 | Dev | Cerebral Palsy | 1 |
| 0f397840-4dca-486d-5143-08dba881aa8d | 0.058 | 0.094 | 0.058 | 445 | Train | Parkinson's Disease | 1 |
| d27d1dfb-909f-4c9f-a190-08dc11dcc589 | 0.058 | 0.103 | 0.058 | 449 | Train | ALS | 1 |
| dc389cd1-a322-4bb5-125b-08dc55a2762d | 0.058 | 0.093 | 0.058 | 237 | Train | Stroke | 1 |
| ebc937e1-edac-49b8-14b3-08dcbf756c98 | 0.058 | 0.095 | 0.058 | 430 | Train | Cerebral Palsy | 1 |
| 4972841b-fcaf-495f-d79e-08dc46c59895 | 0.057 | 0.096 | 0.057 | 361 | Train | Cerebral Palsy | 1 |
| 8ebb4ccc-4356-47ca-0da3-08dc2684eac8 | 0.057 | 0.089 | 0.057 | 430 | Train | Stroke | 1 |
| f41ace9e-58d1-45d3-6fbb-08dc10671a10 | 0.057 | 0.099 | 0.057 | 450 | Train | ALS | 1 |
| 1485a1cd-5411-4c74-1cdb-08dce2a2fe9b | 0.056 | 0.094 | 0.056 | 225 | Train | Stroke | 1 |
| 2b4ecf7b-57ff-492a-f5a4-08db45b05922 | 0.056 | 0.099 | 0.056 | 446 | Train | Parkinson's Disease | 1 |
| 92dc3af6-87ed-4cae-338b-08dcaf3a39af | 0.056 | 0.082 | 0.056 | 450 | Train | Cerebral Palsy | 1 |
| ea46a62e-39f9-4db8-af77-08dd5030482b | 0.056 | 0.101 | 0.056 | 444 | Train | Stroke | 1 |
| ecd22914-6704-4880-da3f-08db8211616b | 0.056 | 0.099 | 0.056 | 447 | Dev | Parkinson's Disease | 1 |
| f65d47c1-0216-450c-67d2-08dbe21c871c | 0.056 | 0.095 | 0.056 | 430 | Train | Down Syndrome | 1 |
| 629a8b94-87a0-4412-9271-08dc7b82c294 | 0.055 | 0.096 | 0.055 | 422 | Train | Stroke | 1 |
| 6fafb7f0-542c-40e0-7cdd-08dc8ba4f236 | 0.055 | 0.097 | 0.055 | 450 | Train | Parkinson's Disease | 1 |
| 90c8f9c7-ee65-4178-c568-08dc27c1bd26 | 0.055 | 0.088 | 0.055 | 447 | Train | Parkinson's Disease | 1 |
| e8900fce-8187-47f3-2a7a-08dca1b962ee | 0.055 | 0.092 | 0.055 | 450 | Train | Parkinson's Disease | 1 |
| c8bc32fb-9c20-4abe-8df6-08dd4ae40880 | 0.055 | 0.095 | 0.055 | 443 | Train | ALS | 1 |
| 0539d504-1dee-4c09-e989-08dc2e961576 | 0.053 | 0.094 | 0.053 | 428 | Dev | Stroke | 1 |
| 29d01a4d-950a-4c6d-6e21-08db76c46b9c | 0.053 | 0.102 | 0.053 | 162 | Train | Parkinson's Disease | 1 |
| 848dc807-d469-4979-e9a6-08dc2e961576 | 0.053 | 0.079 | 0.053 | 449 | Train | Stroke | 1 |
| 870ab2b5-e5fb-4aaf-03ce-08dd2552a33c | 0.053 | 0.090 | 0.053 | 424 | Dev | Down Syndrome | 1 |
| 67e0c3ff-fa8e-488a-3b6f-08dba8c9670d | 0.052 | 0.096 | 0.052 | 89 | Train | Parkinson's Disease | 1 |
| 841b5954-25e9-4805-244a-08dc016f5033 | 0.052 | 0.085 | 0.052 | 448 | Train | Parkinson's Disease | 1 |
| 877548ba-9c30-465e-0fa8-08dcd99f98d3 | 0.052 | 0.085 | 0.052 | 152 | Train | ALS | 1 |
| 9f6dbe42-d5f4-4fc8-bc3e-08db7417355e | 0.052 | 0.076 | 0.052 | 442 | Train | Parkinson's Disease | 1 |
| eafe4e3a-173b-415a-3321-08dca05f46a7 | 0.052 | 0.077 | 0.052 | 206 | Train | Cerebral Palsy | 1 |
| dd3b609c-ca04-47fb-dc90-08db7e3d374f | 0.051 | 0.086 | 0.051 | 445 | Dev | Parkinson's Disease | 1 |
| 0add9018-bb82-4374-116a-08dc623ec532 | 0.051 | 0.087 | 0.051 | 430 | Train | Down Syndrome | 1 |
| 486642ad-4daa-48a0-fd62-08dcb5d1edd7 | 0.051 | 0.085 | 0.051 | 429 | Dev | Cerebral Palsy | 1 |
| a2848a49-9eb3-44d8-2bf8-08dc9148fdda | 0.051 | 0.061 | 0.051 | 447 | Train | ALS | 1 |
| 3446a6b4-ac81-4fc4-f952-08dc1c2dd218 | 0.050 | 0.095 | 0.050 | 423 | Train | Stroke | 1 |
| 443e6183-0fe5-4a2f-03f2-08dd318df37f | 0.050 | 0.078 | 0.050 | 423 | Train | Down Syndrome | 1 |
| 6678450d-b5b7-4a40-f185-08dd0e32d927 | 0.050 | 0.087 | 0.050 | 428 | Train | Cerebral Palsy | 1 |
| bcfc8320-b900-4d74-61a7-08dbaec8caff | 0.050 | 0.078 | 0.050 | 436 | Train | Parkinson's Disease | 1 |
| f692e483-c0ed-4549-0fc6-08dcd99f98d3 | 0.050 | 0.084 | 0.050 | 438 | Dev | ALS | 1 |
| 047bfad6-615c-446c-b735-08dc443ba3cc | 0.049 | 0.088 | 0.049 | 428 | Train | Cerebral Palsy | 1 |
| 2c36f1b5-db7f-4766-8117-08dd1e2cfafb | 0.049 | 0.080 | 0.049 | 18 | Train | Down Syndrome | 1 |
| 45d8184f-d73c-4e3a-da82-08dc75b20572 | 0.049 | 0.088 | 0.049 | 429 | Train | Down Syndrome | 1 |
| 4aa4914d-e337-4297-fdb6-08dcad887b5e | 0.049 | 0.085 | 0.049 | 430 | Train | Cerebral Palsy | 1 |
| a8a4d633-2806-40d5-a32f-08db4c005d58 | 0.049 | 0.074 | 0.049 | 447 | Train | Parkinson's Disease | 1 |
| b4de2860-cbbc-4cb8-c2bf-08dc124f903c | 0.049 | 0.085 | 0.049 | 450 | Train | ALS | 1 |
| bad3d922-d043-4323-1cd7-08dcd3e137e8 | 0.049 | 0.080 | 0.049 | 449 | Train | Parkinson's Disease | 1 |
| cf8c8bbc-b76c-49e3-4cac-08db8189ae29 | 0.049 | 0.089 | 0.049 | 438 | Train | Parkinson's Disease | 1 |
| d81a9ebb-3dec-4ce9-1830-08dd05aafcc9 | 0.049 | 0.083 | 0.049 | 424 | Train | Parkinson's Disease | 1 |
| f9d0c68b-a81e-4068-ac4f-08dc297d5492 | 0.049 | 0.090 | 0.049 | 430 | Train | Down Syndrome | 1 |
| 874883e9-cd96-466a-c354-08dd6888f774 | 0.048 | 0.081 | 0.048 | 425 | Train | ALS | 1 |
| 18890dc1-8320-43ba-e505-08dced32d6ea | 0.048 | 0.067 | 0.048 | 450 | Train | ALS | 1 |
| 1e4a17d9-1d51-46e1-fb35-08db3b0245c7 | 0.048 | 0.083 | 0.048 | 450 | Train | Parkinson's Disease | 1 |
| 300cf0d9-9261-420a-e95e-08dc2e961576 | 0.048 | 0.075 | 0.048 | 220 | Train | Stroke | 1 |
| c563bb85-cce2-475b-6280-08dcdcbbcec7 | 0.048 | 0.078 | 0.048 | 159 | Train | Parkinson's Disease | 1 |
| 57c429b4-a6c7-4e2a-dd1a-08db98f21470 | 0.047 | 0.081 | 0.047 | 449 | Train | Parkinson's Disease | 1 |
| 71c85a71-d2af-410b-87b2-08dc74e08a4e | 0.047 | 0.066 | 0.047 | 50 | Train | Cerebral Palsy | 1 |
| 86d9ad40-470e-41b3-1262-08db48c83e2c | 0.047 | 0.080 | 0.047 | 449 | Train | Parkinson's Disease | 1 |
| 88f7dc04-4e18-4da7-c39e-08dcf87380a2 | 0.047 | 0.072 | 0.047 | 448 | Train | Parkinson's Disease | 1 |
| c0720941-9cc7-4ecb-4838-08dc666bf63e | 0.047 | 0.078 | 0.047 | 337 | Train | Stroke | 1 |
| 7b641b5e-90da-4828-769f-08dc54a70eeb | 0.046 | 0.078 | 0.046 | 430 | Train | Down Syndrome | 1 |
| ecaceb57-d890-46d2-769c-08dc54a70eeb | 0.046 | 0.087 | 0.046 | 427 | Train | Down Syndrome | 1 |
| f4291b85-744e-41f6-9d02-08db701e3a54 | 0.046 | 0.079 | 0.046 | 450 | Train | Parkinson's Disease | 1 |
| 2ed8ae17-22a0-454e-8f05-08dc7f6a721b | 0.045 | 0.081 | 0.045 | 430 | Train | Stroke | 1 |
| 3cce7670-be7b-4f30-37a9-08dc1a9ff239 | 0.045 | 0.077 | 0.045 | 449 | Train | Parkinson's Disease | 1 |
| a478bfcb-361c-496f-f187-08dd0e32d927 | 0.045 | 0.074 | 0.045 | 448 | Train | Parkinson's Disease | 1 |
| 17d899b9-3365-4430-da24-08dc3bf38957 | 0.044 | 0.067 | 0.044 | 271 | Train | Stroke | 1 |
| 40688524-90d9-4388-2e76-08dc27684872 | 0.044 | 0.064 | 0.044 | 85 | Train | Parkinson's Disease | 1 |
| 50c7e02a-1885-4429-da7c-08dc75b20572 | 0.044 | 0.076 | 0.044 | 447 | Train | Parkinson's Disease | 1 |
| 59f4ff3d-5edf-467c-facb-08dd0a4af9ba | 0.044 | 0.073 | 0.044 | 425 | Train | Down Syndrome | 1 |
| 7913cfeb-79d2-41f1-87b7-08dc74e08a4e | 0.044 | 0.072 | 0.044 | 429 | Train | Cerebral Palsy | 1 |
| 987a5dad-44c2-4a6b-1184-08dba7fa5465 | 0.044 | 0.072 | 0.044 | 449 | Train | Parkinson's Disease | 1 |
| c4b9b28e-5abc-4b38-22b5-08dc56b55882 | 0.044 | 0.083 | 0.044 | 430 | Train | Down Syndrome | 1 |
| e7fc7fc5-ec6f-4c4e-8f06-08dc7f6a721b | 0.044 | 0.070 | 0.044 | 429 | Train | Cerebral Palsy | 1 |
| 189ae8ae-e800-43c1-e956-08dc2e961576 | 0.043 | 0.131 | 0.043 | 15 | Train | Stroke | 1 |
| 20404c96-66e6-4bfb-b066-08dbb4a9f295 | 0.043 | 0.076 | 0.043 | 448 | Train | Parkinson's Disease | 1 |
| 675a063f-cb16-45ad-cc6e-08dc0a3366a4 | 0.043 | 0.079 | 0.043 | 428 | Train | Down Syndrome | 1 |
| d72b0a76-9782-4404-3a1a-08dc5fadb5c5 | 0.043 | 0.065 | 0.043 | 450 | Train | Parkinson's Disease | 1 |
| 13f27a9a-360d-45ce-5272-08db72fc16cf | 0.042 | 0.070 | 0.042 | 446 | Train | Parkinson's Disease | 1 |
| c1cd3290-12bc-4cbb-978d-08dca810d500 | 0.042 | 0.073 | 0.042 | 428 | Train | ALS | 1 |
| 892b7b73-a330-4b1d-7f8e-08dc9f90df2f | 0.042 | 0.075 | 0.042 | 430 | Dev | Cerebral Palsy | 1 |
| feddb247-8741-4c98-c55c-08dc27c1bd26 | 0.042 | 0.070 | 0.042 | 450 | Train | Parkinson's Disease | 1 |
| 2866a69c-4e37-439c-60b9-08db37b72f34 | 0.041 | 0.073 | 0.041 | 450 | Dev | Parkinson's Disease | 1 |
| 4ede54a7-2133-4ef2-1161-08db2577509f | 0.041 | 0.071 | 0.041 | 444 | Dev | Parkinson's Disease | 1 |
| 52b660ca-1778-4dc4-5b83-08db2bb3509e | 0.041 | 0.068 | 0.041 | 450 | Train | Parkinson's Disease | 1 |
| bb82df4d-e1ed-409c-85da-08dbe07efb02 | 0.041 | 0.076 | 0.041 | 442 | Dev | Parkinson's Disease | 1 |
| bf1a8016-6f44-4c69-8158-08dc15edb990 | 0.041 | 0.065 | 0.041 | 45 | Train | ALS | 1 |
| d72b9caa-b2bc-4191-15fe-08dbb62a2382 | 0.041 | 0.066 | 0.041 | 84 | Train | Parkinson's Disease | 1 |
| dd0a734d-909d-42ba-3d72-08dc325485f0 | 0.041 | 0.075 | 0.041 | 447 | Train | Parkinson's Disease | 1 |
| f94acb02-fbbd-4e7b-e7b8-08dcd9e31338 | 0.041 | 0.054 | 0.041 | 450 | Train | ALS | 1 |
| 291c4b1c-d84f-4c66-ed92-08dbae400ac5 | 0.040 | 0.068 | 0.040 | 441 | Train | Parkinson's Disease | 1 |
| 4a83a447-d51c-47f0-eca3-08dc9cb096c2 | 0.040 | 0.068 | 0.040 | 450 | Train | ALS | 1 |
| 9e8b3e40-dc4b-41c3-a608-08db87a61cfc | 0.040 | 0.058 | 0.040 | 450 | Train | Parkinson's Disease | 1 |
| ba698f8b-bc3c-4416-cb5e-08dc840245ea | 0.040 | 0.069 | 0.040 | 379 | Train | Cerebral Palsy | 1 |
| d0a6e016-ecc1-4c41-b5aa-08dc3f363c7d | 0.040 | 0.067 | 0.040 | 449 | Train | Parkinson's Disease | 1 |
| e8c8369b-9093-4547-d891-08db4be65c62 | 0.040 | 0.066 | 0.040 | 444 | Train | Parkinson's Disease | 1 |
| 1db08df5-d67e-44e5-7f99-08dc9f90df2f | 0.039 | 0.071 | 0.039 | 430 | Train | Cerebral Palsy | 1 |
| 30367f4b-f259-4248-4cdd-08db4b718502 | 0.039 | 0.067 | 0.039 | 448 | Train | Parkinson's Disease | 1 |
| 46e801cd-b319-443b-5311-08dc95210be1 | 0.039 | 0.064 | 0.039 | 164 | Dev | Cerebral Palsy | 1 |
| 58ffb3d4-ccb8-4fce-852f-08dcd7240867 | 0.039 | 0.067 | 0.039 | 444 | Train | Parkinson's Disease | 1 |
| 6c868961-e917-42d4-632d-08dbaaf8a4b7 | 0.039 | 0.072 | 0.039 | 449 | Train | Parkinson's Disease | 1 |
| 94dfb9c6-582b-41bc-763e-08dbba5845a5 | 0.039 | 0.075 | 0.039 | 268 | Train | Parkinson's Disease | 1 |
| d08febe1-2f4b-4080-2ed1-08dc27684872 | 0.039 | 0.068 | 0.039 | 450 | Dev | Parkinson's Disease | 1 |
| d821fb61-b626-4e18-4284-08dc1d18fde3 | 0.039 | 0.071 | 0.039 | 450 | Train | Parkinson's Disease | 1 |
| e927403b-f387-4e59-cf35-08dc89b72177 | 0.039 | 0.073 | 0.039 | 448 | Train | ALS | 1 |
| ec1dbe7d-140d-4248-219e-08dc9072fb0e | 0.039 | 0.064 | 0.039 | 428 | Train | Cerebral Palsy | 1 |
| 7018e4a5-f536-4506-3f92-08db32dd3b41 | 0.038 | 0.068 | 0.038 | 337 | Train | Parkinson's Disease | 1 |
| 7214c488-f338-47d8-7ac7-08db6614ae76 | 0.038 | 0.059 | 0.038 | 438 | Train | Parkinson's Disease | 1 |
| 928c5940-3541-4aed-0fb9-08dcd99f98d3 | 0.038 | 0.053 | 0.038 | 267 | Train | ALS | 1 |
| 99fc8423-2c12-461b-62ac-08dbcc0db50c | 0.038 | 0.078 | 0.038 | 448 | Train | Parkinson's Disease | 1 |
| 9ad03d94-0c85-4d3c-982b-08dc7e56149c | 0.038 | 0.066 | 0.038 | 429 | Train | Stroke | 1 |
| dfd81053-dc6e-440d-3e69-08dc863e36ec | 0.038 | 0.068 | 0.038 | 428 | Train | Cerebral Palsy | 1 |
| 46f77d44-3577-446f-a1c4-08dc11dcc589 | 0.038 | 0.065 | 0.038 | 450 | Train | ALS | 1 |
| 960c7987-3bd9-4d6d-9afe-08dc13ee0eb9 | 0.038 | 0.074 | 0.038 | 450 | Train | Parkinson's Disease | 1 |
| cfc6c40f-1390-4124-698d-08dc17913c94 | 0.038 | 0.046 | 0.038 | 450 | Train | ALS | 1 |
| 23114ff7-dade-4eb7-a1a6-08dc11dcc589 | 0.037 | 0.063 | 0.037 | 212 | Train | ALS | 1 |
| 3822e8ca-9b02-4a72-67f7-08dcbab8e251 | 0.037 | 0.062 | 0.037 | 97 | Train | Cerebral Palsy | 1 |
| 537ecd95-4c5e-4bb3-123f-08dc8ec52b92 | 0.037 | 0.062 | 0.037 | 450 | Train | ALS | 1 |
| 62f1b4a7-2d35-4e4f-0e04-08dc6bae8ecd | 0.037 | 0.060 | 0.037 | 121 | Train | ALS | 1 |
| a72be9ca-a663-4f72-c230-08dbeba01fff | 0.037 | 0.056 | 0.037 | 447 | Train | Parkinson's Disease | 1 |
| bad3f1b6-4896-4c71-adfa-08db93721f13 | 0.037 | 0.060 | 0.037 | 450 | Dev | Parkinson's Disease | 1 |
| 01570ac8-6f88-4424-3a69-08dc183f4f57 | 0.036 | 0.064 | 0.036 | 345 | Dev | ALS | 1 |
| 635fbfc5-4fa1-4fbb-0acd-08dcdea0684f | 0.036 | 0.069 | 0.036 | 386 | Train | ALS | 1 |
| a20dd80e-b535-4a31-244f-08dcb6eb1ff5 | 0.036 | 0.073 | 0.036 | 430 | Train | Cerebral Palsy | 1 |
| bc3d8166-b7e5-45df-94f2-08dbadaf11d8 | 0.036 | 0.064 | 0.036 | 449 | Train | Parkinson's Disease | 1 |
| edb44a5e-e452-4713-a965-08dcfc3ef562 | 0.036 | 0.056 | 0.036 | 367 | Train | Cerebral Palsy | 1 |
| edeaf033-ba86-46a5-4a52-08dc3c7b3134 | 0.036 | 0.065 | 0.036 | 444 | Train | ALS | 1 |
| 18103139-b813-48db-6ddb-08dc1b6d5dbc | 0.035 | 0.058 | 0.035 | 430 | Train | Down Syndrome | 1 |
| 51d89771-fbb2-4268-0bb3-08dcf9635df3 | 0.035 | 0.042 | 0.035 | 450 | Train | Stroke | 1 |
| 63f2665b-ddde-420b-d1ec-08db95465630 | 0.035 | 0.060 | 0.035 | 444 | Train | Parkinson's Disease | 1 |
| 9fb13376-b839-4cc4-2e66-08dc27684872 | 0.035 | 0.058 | 0.035 | 449 | Train | Parkinson's Disease | 1 |
| e86387f3-77e0-4345-9f67-08db28bb85b0 | 0.035 | 0.057 | 0.035 | 448 | Train | Parkinson's Disease | 1 |
| f8531e5f-2979-4250-182e-08dd05aafcc9 | 0.035 | 0.060 | 0.035 | 349 | Train | Down Syndrome | 1 |
| 0011deac-27ce-4d61-a02e-08db2c0e5fe3 | 0.034 | 0.056 | 0.034 | 438 | Train | Parkinson's Disease | 1 |
| 19afb5a2-41dc-42a1-1f5b-08db743c9986 | 0.034 | 0.063 | 0.034 | 449 | Dev | Parkinson's Disease | 1 |
| 28a16c37-69f6-4685-a1a3-08dc11dcc589 | 0.034 | 0.075 | 0.034 | 443 | Train | Parkinson's Disease | 1 |
| 690a4970-0aa0-4457-115f-08dba7fa5465 | 0.034 | 0.059 | 0.034 | 450 | Train | Parkinson's Disease | 1 |
| 6e801e6a-9afd-4195-0a4a-08db7e715258 | 0.034 | 0.066 | 0.034 | 44 | Train | Parkinson's Disease | 1 |
| b03cb2c0-e39e-450a-e97a-08dc2e961576 | 0.034 | 0.072 | 0.034 | 422 | Train | Stroke | 1 |
| c16a656f-c885-4ab8-72db-08dd51fb5ebc | 0.034 | 0.060 | 0.034 | 375 | Train | Down Syndrome | 1 |
| e2490a80-1f67-4b3e-b12e-08dc804a93e8 | 0.034 | 0.062 | 0.034 | 448 | Train | Parkinson's Disease | 1 |
| e597e7d7-3062-4982-32eb-08dd80de9631 | 0.034 | 0.081 | 0.034 | 238 | Dev | Stroke | 1 |
| 1a2c36f7-7312-4b00-da7d-08dc75b20572 | 0.033 | 0.053 | 0.033 | 421 | Dev | Cerebral Palsy | 1 |
| 1f028daa-142f-405c-0ede-08dc42fe0a19 | 0.033 | 0.060 | 0.033 | 430 | Train | Down Syndrome | 1 |
| 3f26fe3d-9cab-4073-769a-08db451a0b36 | 0.033 | 0.062 | 0.033 | 450 | Train | Parkinson's Disease | 1 |
| 5852ec8d-cbfd-4901-b907-08dc99d6617d | 0.033 | 0.052 | 0.033 | 430 | Train | Cerebral Palsy | 1 |
| abd640de-5589-4460-443e-08db780528b1 | 0.033 | 0.060 | 0.033 | 435 | Train | Parkinson's Disease | 1 |
| b6cd796c-433a-4387-bcd1-08db91c912c0 | 0.033 | 0.058 | 0.033 | 449 | Train | Parkinson's Disease | 1 |
| db8636a4-99d3-48d7-87ae-08dc74e08a4e | 0.033 | 0.060 | 0.033 | 428 | Train | Cerebral Palsy | 1 |
| 0722bb1f-e1c6-4165-c597-08dce436cd5d | 0.032 | 0.041 | 0.032 | 450 | Train | ALS | 1 |
| 283e1ff7-120e-4147-498d-08dcb4d7acba | 0.032 | 0.057 | 0.032 | 450 | Train | Cerebral Palsy | 1 |
| 2b755f1e-f852-4da0-fd7f-08db4831e779 | 0.032 | 0.061 | 0.032 | 415 | Train | Parkinson's Disease | 1 |
| 2d70d1b6-17d4-404f-ce38-08dca6823a12 | 0.032 | 0.063 | 0.032 | 448 | Train | Parkinson's Disease | 1 |
| 624dddfa-fcd7-4e86-4403-08dc2f748b5c | 0.032 | 0.058 | 0.032 | 406 | Train | Stroke | 1 |
| 775ffa0d-65d3-4ad6-2e7d-08dc27684872 | 0.032 | 0.061 | 0.032 | 449 | Train | Parkinson's Disease | 1 |
| 99e8c247-55af-4979-6055-08dc274aba53 | 0.032 | 0.068 | 0.032 | 450 | Train | Parkinson's Disease | 1 |
| caa14983-efb2-473c-a1ea-08dc11dcc589 | 0.032 | 0.047 | 0.032 | 450 | Train | ALS | 1 |
| df423c83-0671-4d45-e7a4-08dcd9e31338 | 0.032 | 0.053 | 0.032 | 447 | Train | ALS | 1 |
| fcb35ef5-5a96-4f1c-012a-08dd15a179fb | 0.032 | 0.058 | 0.032 | 446 | Dev | ALS | 1 |
| 2f1acdcd-16af-4ef3-4e09-08dd589efe21 | 0.031 | 0.053 | 0.031 | 408 | Train | Down Syndrome | 1 |
| 46954fd8-75b1-41d1-f6eb-08dc19181866 | 0.031 | 0.054 | 0.031 | 429 | Train | Cerebral Palsy | 1 |
| 7e27b4c5-9250-479e-5fe2-08dc630c1396 | 0.031 | 0.056 | 0.031 | 450 | Train | ALS | 1 |
| 7fee5dfd-1c4d-44db-0e9c-08db39f45d00 | 0.031 | 0.052 | 0.031 | 449 | Dev | Parkinson's Disease | 1 |
| 9bedec53-2cd5-47a7-7d3a-08dcd6a9c461 | 0.031 | 0.051 | 0.031 | 442 | Train | Parkinson's Disease | 1 |
| c6e71eca-f17f-4a75-2653-08db322ca5c4 | 0.031 | 0.052 | 0.031 | 448 | Train | Parkinson's Disease | 1 |
| d62398ed-4d13-408c-4401-08dc2f748b5c | 0.031 | 0.055 | 0.031 | 353 | Train | Stroke | 1 |
| e284430e-a76d-434a-e67a-08db2d6a5da8 | 0.031 | 0.052 | 0.031 | 448 | Train | Parkinson's Disease | 1 |
| 3468e898-4199-4829-a85a-08dcf77c2ab9 | 0.030 | 0.053 | 0.030 | 444 | Train | Parkinson's Disease | 1 |
| 6a81e17f-fb8f-4289-1e2c-08dbe1ed2b7f | 0.030 | 0.059 | 0.030 | 430 | Train | Down Syndrome | 1 |
| 00617bdb-79b4-48dd-ce97-08dc58c09eb8 | 0.030 | 0.057 | 0.030 | 429 | Train | Down Syndrome | 1 |
| 4a429a91-8c48-4133-87b5-08dc74e08a4e | 0.030 | 0.055 | 0.030 | 425 | Train | Cerebral Palsy | 1 |
| 5cce2e41-7adc-474d-1241-08dc8ec52b92 | 0.030 | 0.056 | 0.030 | 450 | Dev | ALS | 1 |
| 6ad1753e-36a8-498b-1175-08dba7fa5465 | 0.030 | 0.055 | 0.030 | 442 | Train | Parkinson's Disease | 1 |
| ad160303-51b7-4ed3-1166-08dba7fa5465 | 0.030 | 0.056 | 0.030 | 450 | Train | Parkinson's Disease | 1 |
| ae62cbfd-80e7-4bf8-9260-08dc7b82c294 | 0.030 | 0.064 | 0.030 | 80 | Train | Stroke | 1 |
| e025613c-33b0-4d16-1c5a-08dd1b697db6 | 0.030 | 0.050 | 0.030 | 406 | Train | Parkinson's Disease | 1 |
| f052038d-97f1-4124-ad68-08dc7885788f | 0.030 | 0.056 | 0.030 | 404 | Train | Cerebral Palsy | 1 |
| fca65ce1-fabf-4914-172d-08db24d03de6 | 0.030 | 0.046 | 0.030 | 445 | Dev | Parkinson's Disease | 1 |
| 0f16337b-734e-46b1-73ea-08dc1e92abdf | 0.030 | 0.056 | 0.030 | 441 | Train | Parkinson's Disease | 1 |
| 18d960a7-be7b-455b-a19d-08dc11dcc589 | 0.029 | 0.057 | 0.029 | 449 | Train | ALS | 1 |
| 45d88ea8-432d-49ba-95f8-08dc379c1f1f | 0.029 | 0.052 | 0.029 | 445 | Dev | Parkinson's Disease | 1 |
| 6dd5a117-86d2-4847-1f7b-08dc22d2b6d4 | 0.029 | 0.051 | 0.029 | 427 | Train | Down Syndrome | 1 |
| e2c37f0f-15de-4fbb-244d-08dcb6eb1ff5 | 0.029 | 0.063 | 0.029 | 43 | Train | Down Syndrome | 1 |
| 62913b1c-bcc7-4adf-809c-08dc28b09bf9 | 0.029 | 0.049 | 0.029 | 358 | Train | Parkinson's Disease | 1 |
| d31f3200-f36e-4502-dd39-08db6544cb87 | 0.029 | 0.054 | 0.029 | 439 | Train | Parkinson's Disease | 1 |
| 0f7d84c8-5fe1-49ec-6114-08dcdb04185c | 0.028 | 0.054 | 0.028 | 415 | Dev | ALS | 1 |
| 07b8fcab-237f-47f7-24e9-08db32506b53 | 0.028 | 0.052 | 0.028 | 450 | Train | Parkinson's Disease | 1 |
| 278536ce-8ba5-4fc3-4159-08dcbd76ee68 | 0.028 | 0.038 | 0.028 | 449 | Train | ALS | 1 |
| 9d8d2260-dfe9-4384-e137-08dbe55910bb | 0.028 | 0.048 | 0.028 | 449 | Train | Parkinson's Disease | 1 |
| 9ec977d9-1c8f-4374-d6eb-08db42d02878 | 0.028 | 0.053 | 0.028 | 449 | Train | Parkinson's Disease | 1 |
| a4cd6747-9b78-4f59-a72f-08dc6486c600 | 0.028 | 0.054 | 0.028 | 430 | Train | Down Syndrome | 1 |
| cccfac5e-2ea1-42ee-3e6a-08dc863e36ec | 0.028 | 0.047 | 0.028 | 89 | Train | Cerebral Palsy | 1 |
| e1445001-72f7-46eb-0f80-08db40377d80 | 0.028 | 0.047 | 0.028 | 443 | Train | Parkinson's Disease | 1 |
| e8867921-1973-4339-c3a6-08dcf87380a2 | 0.028 | 0.047 | 0.028 | 117 | Train | Parkinson's Disease | 1 |
| f384ec19-a3e8-4c8a-87b0-08dc74e08a4e | 0.028 | 0.051 | 0.028 | 430 | Train | Cerebral Palsy | 1 |
| 02d320db-8f1a-433e-4601-08dbb6c98185 | 0.027 | 0.050 | 0.027 | 449 | Train | Parkinson's Disease | 1 |
| 111d8262-3a46-4d0a-816d-08dc70f89134 | 0.027 | 0.051 | 0.027 | 450 | Train | Parkinson's Disease | 1 |
| 5ac33366-70eb-43de-ce95-08dc58c09eb8 | 0.027 | 0.050 | 0.027 | 268 | Dev | ALS | 1 |
| 866b68e7-78f2-4abb-e21e-08dc3963a250 | 0.027 | 0.050 | 0.027 | 418 | Dev | Parkinson's Disease | 1 |
| b2458036-ec6f-4e79-b93b-08dd4d26bbc8 | 0.027 | 0.055 | 0.027 | 425 | Dev | Down Syndrome | 1 |
| c6c49ecb-3f65-4366-fb5c-08db6d7755f1 | 0.027 | 0.047 | 0.027 | 443 | Train | Parkinson's Disease | 1 |
| db6fa9b3-538f-4467-8e58-08dc5f21978e | 0.027 | 0.056 | 0.027 | 429 | Train | Down Syndrome | 1 |
| 4ba55594-5fb9-47db-853c-08dd210c9483 | 0.027 | 0.050 | 0.027 | 447 | Train | ALS | 1 |
| 0ead5313-2f79-44c6-ab98-08db26923497 | 0.026 | 0.052 | 0.026 | 85 | Train | Parkinson's Disease | 1 |
| 17ba4136-008b-47f8-8f16-08dcdbd22259 | 0.026 | 0.045 | 0.026 | 170 | Train | ALS | 1 |
| 3d53af79-4abd-4370-df83-08db5c991d99 | 0.026 | 0.046 | 0.026 | 441 | Train | Parkinson's Disease | 1 |
| 468955f5-481a-4220-8744-08db55811628 | 0.026 | 0.049 | 0.026 | 448 | Train | Parkinson's Disease | 1 |
| 603b47ab-b99f-47b0-8086-08db80053c20 | 0.026 | 0.056 | 0.026 | 447 | Train | Parkinson's Disease | 1 |
| 65ceb5df-bc14-4a3d-ca67-08db7331a16c | 0.026 | 0.041 | 0.026 | 446 | Train | Parkinson's Disease | 1 |
| 6e34ea84-5d05-47f3-c599-08dc27c1bd26 | 0.026 | 0.045 | 0.026 | 449 | Dev | Parkinson's Disease | 1 |
| 8353668e-9065-4b35-75a8-08dd3ba78fcd | 0.026 | 0.051 | 0.026 | 450 | Train | ALS | 1 |
| 841ddd27-e1c0-4ba2-e7be-08dcd9e31338 | 0.026 | 0.035 | 0.026 | 449 | Train | ALS | 1 |
| 9b2bb94e-ba9e-4a60-24a7-08dd018a3881 | 0.026 | 0.043 | 0.026 | 428 | Train | Down Syndrome | 1 |
| a29710b6-4f46-49e3-116f-08dba7fa5465 | 0.026 | 0.044 | 0.026 | 448 | Train | Parkinson's Disease | 1 |
| 578895fa-55a7-4ab4-ef6a-08db7199713e | 0.026 | 0.043 | 0.026 | 408 | Train | Parkinson's Disease | 1 |
| be731c5e-4bee-4993-72e0-08dd51fb5ebc | 0.026 | 0.052 | 0.026 | 336 | Train | Down Syndrome | 1 |
| 1d6104ff-7e74-4839-37c8-08dce6e2632a | 0.025 | 0.044 | 0.025 | 444 | Dev | Parkinson's Disease | 1 |
| 371ab70e-d1fe-45a5-3e99-08dc52a9876a | 0.025 | 0.055 | 0.025 | 444 | Train | Parkinson's Disease | 1 |
| 4519d53f-20a6-4968-ada3-08dce09abeb4 | 0.025 | 0.043 | 0.025 | 449 | Train | Cerebral Palsy | 1 |
| 5428856b-44d2-4c25-3e38-08dc895255bb | 0.025 | 0.046 | 0.025 | 429 | Train | Cerebral Palsy | 1 |
| 63bc6f35-9437-44e5-1604-08dbb62a2382 | 0.025 | 0.046 | 0.025 | 449 | Dev | Parkinson's Disease | 1 |
| 7ced1720-6305-4bc8-46bf-08db82273f48 | 0.025 | 0.051 | 0.025 | 434 | Train | Parkinson's Disease | 1 |
| 6116e83e-8f91-4885-44aa-08dc2be1ce70 | 0.025 | 0.048 | 0.025 | 447 | Train | Parkinson's Disease | 1 |
| e23a6dfd-caf0-4927-c02e-08dc605e0191 | 0.025 | 0.045 | 0.025 | 180 | Train | ALS | 1 |
| ee9330d0-5ae2-4123-8cf4-08dcff4f47ae | 0.025 | 0.058 | 0.025 | 423 | Train | Cerebral Palsy | 1 |
| 0db90eb5-234e-4bd3-0edc-08dc42fe0a19 | 0.024 | 0.042 | 0.024 | 443 | Train | Parkinson's Disease | 1 |
| 17fc5f44-e24f-4138-db5b-08db263bd57d | 0.024 | 0.041 | 0.024 | 450 | Train | Parkinson's Disease | 1 |
| 199e75a8-422f-473f-2b40-08db46c00613 | 0.024 | 0.041 | 0.024 | 448 | Dev | Parkinson's Disease | 1 |
| 2162b646-5caf-4cf2-3d76-08dc325485f0 | 0.024 | 0.046 | 0.024 | 129 | Train | Cerebral Palsy | 1 |
| 2272219d-dbc0-49ee-4408-08db797e52e3 | 0.024 | 0.050 | 0.024 | 448 | Train | Parkinson's Disease | 1 |
| 32d04e9c-32db-467a-b6b4-08dc8d7bb350 | 0.024 | 0.043 | 0.024 | 440 | Train | ALS | 1 |
| 4481a26b-356d-4740-c59f-08dc27c1bd26 | 0.024 | 0.045 | 0.024 | 303 | Train | Parkinson's Disease | 1 |
| 44b93712-ce43-4b72-b7d3-08dba97af433 | 0.024 | 0.054 | 0.024 | 449 | Train | Parkinson's Disease | 1 |
| 638f0b2e-3bb7-45b9-87b6-08dc74e08a4e | 0.024 | 0.042 | 0.024 | 430 | Train | Cerebral Palsy | 1 |
| 65f496d9-78ad-45ba-c835-08dc7c5e38f1 | 0.024 | 0.049 | 0.024 | 154 | Train | Stroke | 1 |
| 951cf535-f6ae-4a82-bd5c-08dc8ad4730d | 0.024 | 0.048 | 0.024 | 319 | Train | ALS | 1 |
| 962ac7d4-c6ab-49f3-1e2d-08dbe1ed2b7f | 0.024 | 0.063 | 0.024 | 42 | Train | Down Syndrome | 1 |
| ae7673ac-8aea-4b5e-7f96-08dc9f90df2f | 0.024 | 0.044 | 0.024 | 430 | Train | Cerebral Palsy | 1 |
| b5e1393c-f584-4c22-a39d-08dc14c0870b | 0.024 | 0.057 | 0.024 | 165 | Train | ALS | 1 |
| c984ed88-2c76-46bf-abc7-08dc5d6a38e4 | 0.024 | 0.048 | 0.024 | 448 | Train | ALS | 1 |
| d847daf6-adac-4aaa-1f65-08db3dcbbd09 | 0.024 | 0.044 | 0.024 | 450 | Train | Parkinson's Disease | 1 |
| 23563b1d-87ba-4b52-a730-08dc6486c600 | 0.024 | 0.051 | 0.024 | 429 | Train | Cerebral Palsy | 1 |
| 2691d25b-f3e5-4750-6801-08dcbab8e251 | 0.024 | 0.047 | 0.024 | 429 | Train | Cerebral Palsy | 1 |
| fc50dfee-95ab-4d71-f1e6-08dc2cf36e15 | 0.024 | 0.049 | 0.024 | 429 | Train | Cerebral Palsy | 1 |
| 71d6867e-272d-49ee-87ad-08dc74e08a4e | 0.023 | 0.042 | 0.023 | 350 | Train | Cerebral Palsy | 1 |
| 09716de8-6f65-4a68-3769-08db63d00ed9 | 0.023 | 0.044 | 0.023 | 449 | Train | Parkinson's Disease | 1 |
| 0f9ac13f-e103-4926-a1a8-08dc11dcc589 | 0.023 | 0.046 | 0.023 | 450 | Dev | ALS | 1 |
| 2cdb605e-0dd8-4e47-cf49-08dc36bdc819 | 0.023 | 0.047 | 0.023 | 42 | Train | ALS | 1 |
| 79dc1110-bef7-414c-24af-08dcbcb70931 | 0.023 | 0.046 | 0.023 | 429 | Dev | Cerebral Palsy | 1 |
| aadd3c34-1551-43f9-57f1-08dcbb9f64e1 | 0.023 | 0.047 | 0.023 | 450 | Train | ALS | 1 |
| dc159e25-3cfe-411c-dbf4-08dc00c9c16a | 0.023 | 0.046 | 0.023 | 328 | Train | Cerebral Palsy | 1 |
| 2b5e75af-0263-44fb-3a25-08dc5fadb5c5 | 0.022 | 0.042 | 0.022 | 438 | Train | Parkinson's Disease | 1 |
| 32ad7175-6db9-4e69-33a8-08db41d15341 | 0.022 | 0.042 | 0.022 | 448 | Train | Parkinson's Disease | 1 |
| 3aa9d4f5-a530-4f63-33fe-08dbb7176ebb | 0.022 | 0.039 | 0.022 | 449 | Train | Parkinson's Disease | 1 |
| 4b05eff4-b30e-40e8-30ff-08db50c8319f | 0.022 | 0.047 | 0.022 | 446 | Train | Parkinson's Disease | 1 |
| 4c5d2214-df2a-4d7f-bb39-08dbdf14f113 | 0.022 | 0.041 | 0.022 | 438 | Train | Parkinson's Disease | 1 |
| 508d17d7-b0cf-4de7-1179-08dba7fa5465 | 0.022 | 0.040 | 0.022 | 449 | Train | Parkinson's Disease | 1 |
| 5213927f-8fb4-4ca3-bd25-08db66ae423c | 0.022 | 0.042 | 0.022 | 449 | Train | Parkinson's Disease | 1 |
| 67fd11af-176e-4ce3-4cb6-08dd0b23004e | 0.022 | 0.049 | 0.022 | 429 | Train | Stroke | 1 |
| 75129419-2333-4e29-fd6c-08dcb5d1edd7 | 0.022 | 0.044 | 0.022 | 448 | Train | Parkinson's Disease | 1 |
| a44a52f3-a801-4458-15fa-08dbb62a2382 | 0.022 | 0.038 | 0.022 | 444 | Train | Parkinson's Disease | 1 |
| a9000ee1-d751-43d8-9bd7-08db4d814b6e | 0.022 | 0.039 | 0.022 | 449 | Train | Parkinson's Disease | 1 |
| daa4500b-336a-4832-eca0-08dc9cb096c2 | 0.022 | 0.042 | 0.022 | 449 | Train | ALS | 1 |
| fb369f36-9306-4322-3de6-08dd04d8f6c9 | 0.022 | 0.044 | 0.022 | 431 | Train | Cerebral Palsy | 1 |
| 165dda37-a252-4e37-40cb-08dcec8ec3cc | 0.022 | 0.042 | 0.022 | 443 | Dev | Parkinson's Disease | 1 |
| 2d0a692c-4150-4ed3-8e04-08dd4ae40880 | 0.022 | 0.044 | 0.022 | 450 | Train | ALS | 1 |
| 78718496-3433-429f-1559-08dd13b9e946 | 0.022 | 0.043 | 0.022 | 428 | Train | Cerebral Palsy | 1 |
| 199470db-2cd5-410a-1c23-08dd195745b0 | 0.021 | 0.040 | 0.021 | 450 | Train | Parkinson's Disease | 1 |
| 2f909f36-d59c-4ca4-5ab9-08db26ef62e1 | 0.021 | 0.044 | 0.021 | 449 | Train | Parkinson's Disease | 1 |
| 34529c44-ad78-4f02-2ece-08dc27684872 | 0.021 | 0.043 | 0.021 | 447 | Train | Parkinson's Disease | 1 |
| 37502a90-ddb7-4c5f-c582-08dc27c1bd26 | 0.021 | 0.042 | 0.021 | 450 | Train | Parkinson's Disease | 1 |
| 407d6de2-ab58-48b1-abb5-08dc5d6a38e4 | 0.021 | 0.041 | 0.021 | 449 | Train | ALS | 1 |
| 511e8ca5-236a-4aeb-bf52-08db3cfd4e3e | 0.021 | 0.041 | 0.021 | 450 | Train | Parkinson's Disease | 1 |
| 70ba239b-9b51-4789-1096-08db6b8d1576 | 0.021 | 0.042 | 0.021 | 450 | Train | Parkinson's Disease | 1 |
| 7d40ea39-22d3-451e-3c85-08dc4b8edc60 | 0.021 | 0.045 | 0.021 | 444 | Train | Parkinson's Disease | 1 |
| 88c0ceb1-d2e7-44f6-810a-08dd30bc293e | 0.021 | 0.041 | 0.021 | 449 | Train | Parkinson's Disease | 1 |
| 972c6e75-1fb1-470b-a1e1-08dc11dcc589 | 0.021 | 0.045 | 0.021 | 448 | Train | ALS | 1 |
| b6b500af-6041-47da-b54d-08dd55fb2b87 | 0.021 | 0.047 | 0.021 | 382 | Train | Cerebral Palsy | 1 |
| d05c8cc6-9039-4cc5-8f28-08dcdbd22259 | 0.021 | 0.039 | 0.021 | 135 | Train | ALS | 1 |
| d38687af-30bd-4b6c-d8fe-08dcb01ba44a | 0.021 | 0.041 | 0.021 | 445 | Train | ALS | 1 |
| d4ffee7d-e424-4509-4cc3-08dd0b23004e | 0.021 | 0.045 | 0.021 | 450 | Train | ALS | 1 |
| dd89491c-3d54-43ec-4282-08dc308d407c | 0.021 | 0.041 | 0.021 | 449 | Train | Parkinson's Disease | 1 |
| 099bd3df-9122-4a77-cb41-08dd739d0cac | 0.020 | 0.042 | 0.020 | 393 | Dev | ALS | 1 |
| 3b4e0116-8ab9-4522-54b8-08dc17c7b3c4 | 0.020 | 0.039 | 0.020 | 450 | Train | ALS | 1 |
| 6c622825-c58a-43df-06cf-08dc6fa9589b | 0.020 | 0.042 | 0.020 | 448 | Train | Parkinson's Disease | 1 |
| 72592637-45fd-4eb0-5b85-08db2bb3509e | 0.020 | 0.041 | 0.020 | 437 | Train | Parkinson's Disease | 1 |
| 7797862e-0242-4c4e-3f62-08dc27b62080 | 0.020 | 0.040 | 0.020 | 442 | Train | Parkinson's Disease | 1 |
| 7f7a9a12-66dc-43bb-ed39-08dd22cabb5c | 0.020 | 0.039 | 0.020 | 449 | Dev | ALS | 1 |
| b8c9640a-1617-48c2-1c1f-08dd195745b0 | 0.020 | 0.042 | 0.020 | 430 | Train | Down Syndrome | 1 |
| c693af0b-103a-4ac2-cd49-08dd75e9cc8f | 0.020 | 0.143 | 0.020 | 5 | Train | ALS | 1 |
| cf5a558a-4617-4d8a-3a6e-08dc183f4f57 | 0.020 | 0.045 | 0.020 | 430 | Train | Stroke | 1 |
| d11e48a9-f2e6-49d4-244a-08dcb6eb1ff5 | 0.020 | 0.041 | 0.020 | 430 | Train | Cerebral Palsy | 1 |
| dd039cb7-0415-44ad-8e01-08dd4ae40880 | 0.020 | 0.043 | 0.020 | 450 | Train | ALS | 1 |
| f6132f61-4179-43f5-abbd-08dc5d6a38e4 | 0.020 | 0.043 | 0.020 | 45 | Train | ALS | 1 |
| e02e013d-808d-42b8-0349-08dcd2d6e84e | 0.019 | 0.037 | 0.019 | 449 | Train | Parkinson's Disease | 1 |
| 0a205aa0-6fe2-4e78-e906-08dcf2e1353e | 0.019 | 0.035 | 0.019 | 406 | Train | ALS | 1 |
| 11e4aa43-fc83-46fb-dd25-08db782122ba | 0.019 | 0.035 | 0.019 | 438 | Train | Parkinson's Disease | 1 |
| 4c4d9ab0-6bdd-41c5-4154-08dcddb9e4a3 | 0.019 | 0.038 | 0.019 | 446 | Train | Parkinson's Disease | 1 |
| 4e23b773-ec9d-4258-4588-08dcf3d34e85 | 0.019 | 0.038 | 0.019 | 418 | Train | ALS | 1 |
| 87828447-eda9-4e46-530f-08dc95210be1 | 0.019 | 0.035 | 0.019 | 429 | Train | Down Syndrome | 1 |
| 9e58a880-d0df-48a9-92b7-08dc971aa100 | 0.019 | 0.038 | 0.019 | 75 | Dev | ALS | 1 |
| e1d2e9c2-6a5f-461d-9b9f-08dd3ffcc9ff | 0.019 | 0.040 | 0.019 | 397 | Train | ALS | 1 |
| f5cfee85-0110-474a-6dab-08db348aa35d | 0.019 | 0.036 | 0.019 | 447 | Train | Parkinson's Disease | 1 |
| faf7f194-a739-4478-e597-08dd187996f2 | 0.019 | 0.034 | 0.019 | 349 | Train | Cerebral Palsy | 1 |
| 21d7dd89-eca0-4722-3a71-08dc183f4f57 | 0.019 | 0.041 | 0.019 | 450 | Train | ALS | 1 |
| 662ad6f3-d8fe-4bf5-d939-08db465e8b8a | 0.019 | 0.040 | 0.019 | 450 | Train | Parkinson's Disease | 1 |
| 8b43e597-8fb8-4a84-9319-08db7b2bf57b | 0.019 | 0.039 | 0.019 | 450 | Train | Parkinson's Disease | 1 |
| fc246a09-cac1-4830-3014-08dcc11ab035 | 0.019 | 0.041 | 0.019 | 450 | Train | ALS | 1 |
| 17ea9e04-d4c1-43d2-dec5-08dcb7c16175 | 0.018 | 0.037 | 0.018 | 401 | Train | Cerebral Palsy | 1 |
| 1f3ca0f5-18d5-471b-5f7f-08dcb30cef1c | 0.018 | 0.039 | 0.018 | 428 | Train | Down Syndrome | 1 |
| 2012b36e-28c0-45de-a16a-08dc11dcc589 | 0.018 | 0.050 | 0.018 | 75 | Train | ALS | 1 |
| 29446bcd-071b-4232-cf52-08dc36bdc819 | 0.018 | 0.037 | 0.018 | 448 | Train | Parkinson's Disease | 1 |
| 33a571de-54ef-4b4d-b2f0-08db6e8bdba4 | 0.018 | 0.033 | 0.018 | 450 | Train | Parkinson's Disease | 1 |
| 3fe63e4f-19b0-48dd-dd38-08db6544cb87 | 0.018 | 0.037 | 0.018 | 98 | Train | Parkinson's Disease | 1 |
| 3fe66d56-e194-4f6c-6998-08dc17913c94 | 0.018 | 0.039 | 0.018 | 450 | Train | ALS | 1 |
| 44745cf0-a215-40a1-54f4-08dc0e2a1c3e | 0.018 | 0.035 | 0.018 | 430 | Train | Down Syndrome | 1 |
| 4751f7a0-6709-411b-cf48-08dc89b72177 | 0.018 | 0.037 | 0.018 | 448 | Train | ALS | 1 |
| 49c0a40d-aa28-40c0-0fd6-08dcd99f98d3 | 0.018 | 0.032 | 0.018 | 450 | Train | ALS | 1 |
| 4f9999db-b1ed-4ac0-dede-08dcc31013c0 | 0.018 | 0.031 | 0.018 | 82 | Train | Cerebral Palsy | 1 |
| 6d065598-3db6-4934-c039-08dc605e0191 | 0.018 | 0.038 | 0.018 | 450 | Train | ALS | 1 |
| 85534091-2345-4f65-cf34-08dc89b72177 | 0.018 | 0.035 | 0.018 | 449 | Train | ALS | 1 |
| 8e27d987-52a1-4615-ada1-08dce09abeb4 | 0.018 | 0.044 | 0.018 | 430 | Train | Cerebral Palsy | 1 |
| 91ef5c26-f0af-455d-a464-08db2b045661 | 0.018 | 0.040 | 0.018 | 447 | Train | Parkinson's Disease | 1 |
| 95883e20-cef7-4d5f-9872-08db8e06f7f8 | 0.018 | 0.036 | 0.018 | 448 | Train | Parkinson's Disease | 1 |
| a2113b66-e656-4204-2e5d-08dc27684872 | 0.018 | 0.034 | 0.018 | 446 | Train | Parkinson's Disease | 1 |
| b09e3d07-8df9-4958-5cae-08db25ba8c25 | 0.018 | 0.036 | 0.018 | 447 | Train | Parkinson's Disease | 1 |
| cfdcd1d4-e2e4-49eb-b409-08db76ad1dc0 | 0.018 | 0.040 | 0.018 | 449 | Dev | Parkinson's Disease | 1 |
| da6dfde2-5658-4ed3-82ea-08db6cec1e82 | 0.018 | 0.033 | 0.018 | 450 | Train | Parkinson's Disease | 1 |
| e45c7af3-ab45-401b-87b3-08dc74e08a4e | 0.018 | 0.036 | 0.018 | 430 | Train | Cerebral Palsy | 1 |
| e9594e84-3837-4c23-d3f1-08db43eacc94 | 0.018 | 0.035 | 0.018 | 446 | Train | Parkinson's Disease | 1 |
| f981df16-1db1-40d9-2ecf-08dc27684872 | 0.018 | 0.032 | 0.018 | 433 | Train | Parkinson's Disease | 1 |
| 0a159981-665e-4b15-3a6c-08dc183f4f57 | 0.017 | 0.033 | 0.017 | 45 | Train | ALS | 1 |
| 11a9ea43-641f-49d1-a1b5-08dc11dcc589 | 0.017 | 0.036 | 0.017 | 80 | Dev | ALS | 1 |
| 162d9494-828f-4fa2-a85d-08dcf77c2ab9 | 0.017 | 0.034 | 0.017 | 448 | Train | Parkinson's Disease | 1 |
| 1dccccec-2fe4-47dc-fac3-08dd0a4af9ba | 0.017 | 0.037 | 0.017 | 429 | Dev | Cerebral Palsy | 1 |
| 2762ece0-65e8-4cf2-dec6-08dcb7c16175 | 0.017 | 0.031 | 0.017 | 430 | Train | Cerebral Palsy | 1 |
| 36aa3164-db71-4ee3-b6b1-08dc8d7bb350 | 0.017 | 0.038 | 0.017 | 450 | Dev | ALS | 1 |
| 52875471-c143-49b4-cb77-08dc45edfda4 | 0.017 | 0.031 | 0.017 | 449 | Train | ALS | 1 |
| 5d0e07ea-fb76-451e-f782-08dcb8bbedb8 | 0.017 | 0.029 | 0.017 | 350 | Train | Cerebral Palsy | 1 |
| 7468c5a9-6f0e-4c86-b2ef-08db6e8bdba4 | 0.017 | 0.035 | 0.017 | 447 | Train | Parkinson's Disease | 1 |
| 75acf6de-2864-4b6e-3d77-08dc325485f0 | 0.017 | 0.035 | 0.017 | 444 | Train | ALS | 1 |
| 79f4b8bb-7ffa-4422-115c-08dba7fa5465 | 0.017 | 0.033 | 0.017 | 446 | Dev | Parkinson's Disease | 1 |
| 8654a868-71db-42de-b21b-08dc6a2b69be | 0.017 | 0.036 | 0.017 | 447 | Train | Parkinson's Disease | 1 |
| 957c8030-a651-45ee-c2fc-08db67ba31e5 | 0.017 | 0.031 | 0.017 | 444 | Train | Parkinson's Disease | 1 |
| b7c2a941-a374-4a46-2199-08dc9072fb0e | 0.017 | 0.037 | 0.017 | 113 | Train | ALS | 1 |
| bdc32fc0-7ccb-4574-73f0-08db42074bf0 | 0.017 | 0.032 | 0.017 | 448 | Train | Parkinson's Disease | 1 |
| d66f55b5-0bd4-42fe-eca2-08dc9cb096c2 | 0.017 | 0.036 | 0.017 | 450 | Train | ALS | 1 |
| f449429b-9798-48b6-4ccf-08dd0b23004e | 0.017 | 0.035 | 0.017 | 437 | Train | ALS | 1 |
| 03f1dec0-0000-4e2a-cf67-08dc89b72177 | 0.016 | 0.032 | 0.016 | 443 | Train | ALS | 1 |
| 5e9b0847-248d-4a1d-7f90-08dc9f90df2f | 0.016 | 0.028 | 0.016 | 315 | Train | ALS | 1 |
| 68c56fd0-7757-4017-1ce0-08dcd3e137e8 | 0.016 | 0.031 | 0.016 | 430 | Train | Down Syndrome | 1 |
| 6986f30f-5d2d-449e-8bf9-08dbe1538f12 | 0.016 | 0.037 | 0.016 | 168 | Train | Down Syndrome | 1 |
| af6f951d-3697-4c5b-c5f8-08dc291fd57e | 0.016 | 0.036 | 0.016 | 446 | Train | Parkinson's Disease | 1 |
| b8c9a418-21f0-447f-a133-08db825e8b3c | 0.016 | 0.034 | 0.016 | 174 | Train | Parkinson's Disease | 1 |
| bfa24c09-2d2a-40d3-e165-08dc4555b94c | 0.016 | 0.035 | 0.016 | 447 | Train | ALS | 1 |
| e7bda08b-6296-4d01-a165-08dc11dcc589 | 0.016 | 0.031 | 0.016 | 450 | Dev | ALS | 1 |
| 56ab820f-c997-4dd4-2bf6-08dc9148fdda | 0.015 | 0.027 | 0.015 | 430 | Train | Cerebral Palsy | 1 |
| 776a933a-c9d6-495c-5bc5-08dcf1e988d8 | 0.015 | 0.030 | 0.015 | 444 | Train | Parkinson's Disease | 1 |
| 0c05204c-686a-4219-9fce-08dcee0760b0 | 0.015 | 0.032 | 0.015 | 446 | Train | Parkinson's Disease | 1 |
| 1df0f05f-f951-4945-e506-08dced32d6ea | 0.015 | 0.029 | 0.015 | 450 | Train | Parkinson's Disease | 1 |
| 284d7944-ac8e-47bb-1f66-08db3dcbbd09 | 0.015 | 0.032 | 0.015 | 450 | Dev | Parkinson's Disease | 1 |
| 53a684d5-d42f-49c3-dc90-08dbacb1d678 | 0.015 | 0.029 | 0.015 | 448 | Train | Parkinson's Disease | 1 |
| 5ad4cd6a-c79c-4952-3a22-08dc5fadb5c5 | 0.015 | 0.032 | 0.015 | 428 | Train | Down Syndrome | 1 |
| 6437b6d7-6381-4427-f1a5-08db41f4c88b | 0.015 | 0.033 | 0.015 | 450 | Train | Parkinson's Disease | 1 |
| 7c51bade-4203-4bba-37c3-08dce6e2632a | 0.015 | 0.031 | 0.015 | 450 | Dev | ALS | 1 |
| a17cfb8c-c8bc-4c68-a4a1-08dca8fcd16b | 0.015 | 0.028 | 0.015 | 443 | Train | Parkinson's Disease | 1 |
| b104b92a-1ff9-4675-ccdf-08dc48edc242 | 0.015 | 0.028 | 0.015 | 384 | Train | Cerebral Palsy | 1 |
| b4911a96-9457-484c-9996-08dcab8095cf | 0.015 | 0.035 | 0.015 | 354 | Train | ALS | 1 |
| c1d1e8b8-d852-470d-f345-08db39bf590b | 0.015 | 0.028 | 0.015 | 224 | Train | Parkinson's Disease | 1 |
| c5907823-602a-443c-1e31-08dbe1ed2b7f | 0.015 | 0.037 | 0.015 | 423 | Train | Down Syndrome | 1 |
| d7d0ae6d-9ca1-40f9-299b-08db848a8c45 | 0.015 | 0.032 | 0.015 | 449 | Train | Parkinson's Disease | 1 |
| df1bdab4-979a-451b-c2d9-08db6e0d6c39 | 0.015 | 0.028 | 0.015 | 432 | Dev | Parkinson's Disease | 1 |
| f5aa375b-c5eb-43e3-b06b-08db3156ae3a | 0.015 | 0.033 | 0.015 | 449 | Train | Parkinson's Disease | 1 |
| 8970db2b-7672-40f4-a178-08dc11dcc589 | 0.015 | 0.031 | 0.015 | 180 | Train | ALS | 1 |
| 19e5b81c-15e5-4f2b-dd02-08db380c575a | 0.014 | 0.027 | 0.014 | 450 | Train | Parkinson's Disease | 1 |
| 23736436-53fa-46dc-6226-08db384abf34 | 0.014 | 0.033 | 0.014 | 445 | Train | Parkinson's Disease | 1 |
| 270f9bb1-5f0b-4811-e970-08dc2e961576 | 0.014 | 0.029 | 0.014 | 87 | Train | Stroke | 1 |
| 54994211-7696-4987-02a1-08dcaa8c3d9d | 0.014 | 0.031 | 0.014 | 449 | Train | ALS | 1 |
| 6cfd7836-cf63-465c-5763-08dcfa856e25 | 0.014 | 0.027 | 0.014 | 450 | Train | Parkinson's Disease | 1 |
| 7bc4acce-fd1d-44f0-6119-08dcdb04185c | 0.014 | 0.031 | 0.014 | 449 | Train | ALS | 1 |
| 8e4386de-e685-45ae-8f23-08dcdbd22259 | 0.014 | 0.030 | 0.014 | 429 | Train | Down Syndrome | 1 |
| 915db191-604c-4dad-9991-08dcab8095cf | 0.014 | 0.034 | 0.014 | 439 | Dev | ALS | 1 |
| 98870e3b-2ca6-4216-8279-08dcdfc767fc | 0.014 | 0.030 | 0.014 | 430 | Train | Cerebral Palsy | 1 |
| aa95597e-5e07-48b5-219c-08dc9072fb0e | 0.014 | 0.027 | 0.014 | 446 | Train | ALS | 1 |
| b5ffc27c-d012-46ba-5bd0-08dcf1e988d8 | 0.014 | 0.032 | 0.014 | 449 | Train | Parkinson's Disease | 1 |
| bee3c346-3c69-425d-c923-08dd47c86be7 | 0.014 | 0.035 | 0.014 | 450 | Train | ALS | 1 |
| bf65084a-524b-458d-ac4c-08dc297d5492 | 0.014 | 0.026 | 0.014 | 308 | Train | Parkinson's Disease | 1 |
| e28286b0-a156-459a-b2f2-08db6e8bdba4 | 0.014 | 0.028 | 0.014 | 450 | Dev | Parkinson's Disease | 1 |
| eb90a6df-9b21-49bb-bb95-08db2f9d9555 | 0.014 | 0.026 | 0.014 | 450 | Train | Parkinson's Disease | 1 |
| f12fabe9-9bf5-4baa-75ed-08dc5951d476 | 0.014 | 0.030 | 0.014 | 448 | Train | ALS | 1 |
| 9441ac9b-5902-42ce-3a27-08dc5fadb5c5 | 0.014 | 0.026 | 0.014 | 302 | Train | ALS | 1 |
| 08a68bf1-65c5-4c37-7c87-08dcc6cfbf82 | 0.013 | 0.034 | 0.013 | 215 | Train | Cerebral Palsy | 1 |
| 1ea56339-9616-47da-0faf-08dcd99f98d3 | 0.013 | 0.027 | 0.013 | 450 | Train | ALS | 1 |
| 24a73324-3a99-46e3-a1aa-08dc11dcc589 | 0.013 | 0.028 | 0.013 | 433 | Train | ALS | 1 |
| 268adcfd-a262-4bb2-d2c2-08db4723ec09 | 0.013 | 0.030 | 0.013 | 441 | Train | Parkinson's Disease | 1 |
| 2cd1ce27-91cd-4b1f-2ec3-08dc27684872 | 0.013 | 0.030 | 0.013 | 450 | Train | Parkinson's Disease | 1 |
| 311638fc-a891-4ba8-7f97-08dc9f90df2f | 0.013 | 0.029 | 0.013 | 430 | Dev | Cerebral Palsy | 1 |
| 349041a7-7cbc-4327-f94f-08dc1c2dd218 | 0.013 | 0.027 | 0.013 | 450 | Train | ALS | 1 |
| 3b05351f-1cc7-40ae-cce2-08dd358723ba | 0.013 | 0.026 | 0.013 | 430 | Train | Down Syndrome | 1 |
| 4ee42ac6-45b5-4242-e7af-08dcd9e31338 | 0.013 | 0.028 | 0.013 | 450 | Train | ALS | 1 |
| 58cafa0c-85df-40eb-2eaf-08dc27684872 | 0.013 | 0.029 | 0.013 | 43 | Train | Parkinson's Disease | 1 |
| 5c8b9c7f-1ebb-4bd8-3aee-08dbe2b5c47a | 0.013 | 0.034 | 0.013 | 429 | Train | Down Syndrome | 1 |
| 64dc40ed-46c9-4f53-cf26-08dc89b72177 | 0.013 | 0.028 | 0.013 | 450 | Train | ALS | 1 |
| 7d7d589c-cfbd-4800-f6ea-08dc19181866 | 0.013 | 0.030 | 0.013 | 430 | Train | Cerebral Palsy | 1 |
| 8295012a-4710-496e-5bcd-08dcf1e988d8 | 0.013 | 0.031 | 0.013 | 344 | Dev | Cerebral Palsy | 1 |
| 849db66f-8282-47d2-6f6c-08db436e98a4 | 0.013 | 0.029 | 0.013 | 449 | Train | Parkinson's Disease | 1 |
| 88893849-2896-4fc6-cf1e-08dc89b72177 | 0.013 | 0.030 | 0.013 | 450 | Train | ALS | 1 |
| 925ac806-0107-47b5-fef8-08db49b30d79 | 0.013 | 0.029 | 0.013 | 443 | Train | Parkinson's Disease | 1 |
| 97773f9b-69a2-4d43-ec8a-08dc52853440 | 0.013 | 0.027 | 0.013 | 315 | Train | Parkinson's Disease | 1 |
| 99916464-7aed-4cbb-2e9e-08dc27684872 | 0.013 | 0.032 | 0.013 | 450 | Train | Parkinson's Disease | 1 |
| a15bbc72-4ade-43dc-b89c-08db74d9e4d8 | 0.013 | 0.025 | 0.013 | 442 | Train | Parkinson's Disease | 1 |
| a7e2add7-b9f4-46e9-9873-08db8e06f7f8 | 0.013 | 0.028 | 0.013 | 450 | Train | Parkinson's Disease | 1 |
| a94f44f1-aa52-4960-d2bd-08db4723ec09 | 0.013 | 0.030 | 0.013 | 450 | Train | Parkinson's Disease | 1 |
| c7042143-15f2-43f3-4cd1-08dd0b23004e | 0.013 | 0.029 | 0.013 | 249 | Train | ALS | 1 |
| c9c02a22-1993-4686-8dfb-08dd4ae40880 | 0.013 | 0.029 | 0.013 | 179 | Train | ALS | 1 |
| d10350f0-f36f-4d64-085f-08dcd1c0704e | 0.013 | 0.029 | 0.013 | 447 | Train | ALS | 1 |
| d712c8e1-fbf0-482d-3d78-08dc325485f0 | 0.013 | 0.033 | 0.013 | 450 | Train | Stroke | 1 |
| db462c08-94f3-4a07-5bcf-08dcf1e988d8 | 0.013 | 0.029 | 0.013 | 448 | Train | Parkinson's Disease | 1 |
| e92aac78-9175-48b2-33ee-08dbad6081c5 | 0.013 | 0.028 | 0.013 | 449 | Train | Parkinson's Disease | 1 |
| 148d82f1-418f-4adc-2bf9-08dc9148fdda | 0.012 | 0.027 | 0.012 | 447 | Train | Parkinson's Disease | 1 |
| 248b9155-c18c-450d-14d7-08db3f6f1688 | 0.012 | 0.028 | 0.012 | 449 | Train | Parkinson's Disease | 1 |
| 2816a74e-df3e-4ec3-cf24-08dc89b72177 | 0.012 | 0.029 | 0.012 | 450 | Dev | ALS | 1 |
| 3a67511d-bdb6-4e0b-0c46-08dbe9df9e4a | 0.012 | 0.039 | 0.012 | 428 | Train | Cerebral Palsy | 1 |
| 3c9f3061-e5bd-4f9c-16eb-08dc1eef205f | 0.012 | 0.023 | 0.012 | 430 | Train | Cerebral Palsy | 1 |
| 432bc723-0f23-4cc5-4ef2-08dcacc27c9e | 0.012 | 0.023 | 0.012 | 450 | Train | ALS | 1 |
| 4a901ec3-b373-41a3-7068-08db6375793f | 0.012 | 0.022 | 0.012 | 313 | Train | Parkinson's Disease | 1 |
| 4b4aeede-f4a5-49cf-808e-08dc28b09bf9 | 0.012 | 0.026 | 0.012 | 315 | Train | Parkinson's Disease | 1 |
| 558c8b14-7e5a-45d4-6b84-08db40e65de5 | 0.012 | 0.032 | 0.012 | 446 | Train | Parkinson's Disease | 1 |
| 625d8b11-cce4-4876-010d-08db2c67da8b | 0.012 | 0.022 | 0.012 | 450 | Train | Parkinson's Disease | 1 |
| 653eb6f8-1b8f-457c-c58a-08dc27c1bd26 | 0.012 | 0.028 | 0.012 | 446 | Train | Parkinson's Disease | 1 |
| 659f50e6-6690-435a-5cee-08db46a76191 | 0.012 | 0.025 | 0.012 | 439 | Dev | Parkinson's Disease | 1 |
| 678d5169-75fb-47e5-5bd2-08dcf1e988d8 | 0.012 | 0.027 | 0.012 | 449 | Train | ALS | 1 |
| 6f697009-8d43-4a35-3a1d-08dc5fadb5c5 | 0.012 | 0.024 | 0.012 | 89 | Train | ALS | 1 |
| 9f1b16cf-09ce-475c-c2c0-08dc124f903c | 0.012 | 0.032 | 0.012 | 85 | Train | ALS | 1 |
| 9fe1e8f9-c4dd-42fa-844b-08dce3a6cba6 | 0.012 | 0.024 | 0.012 | 446 | Train | ALS | 1 |
| a2c69bed-0f4e-43d2-1174-08dba7fa5465 | 0.012 | 0.029 | 0.012 | 445 | Train | Parkinson's Disease | 1 |
| ad7945d2-4d3a-4dc9-e7cf-08dcd9e31338 | 0.012 | 0.027 | 0.012 | 449 | Train | ALS | 1 |
| b0519b26-50b6-4eb7-2ea0-08dc27684872 | 0.012 | 0.026 | 0.012 | 449 | Train | Parkinson's Disease | 1 |
| b50d400a-fbe0-4e51-8df5-08dd4ae40880 | 0.012 | 0.024 | 0.012 | 300 | Train | ALS | 1 |
| bd9c4f59-9245-4fae-9fe6-08db25c774fb | 0.012 | 0.024 | 0.012 | 449 | Train | Parkinson's Disease | 1 |
| be9b5d21-718a-4346-27c2-08dc72e2a7b8 | 0.012 | 0.028 | 0.012 | 449 | Train | Parkinson's Disease | 1 |
| c2f222c1-4c6a-4fcc-627b-08dcdcbbcec7 | 0.012 | 0.019 | 0.012 | 450 | Train | ALS | 1 |
| e7295175-4edb-4d5c-a1e9-08dc11dcc589 | 0.012 | 0.027 | 0.012 | 450 | Train | Parkinson's Disease | 1 |
| efa8810e-a911-493d-09f1-08db87b19e27 | 0.012 | 0.025 | 0.012 | 448 | Train | Parkinson's Disease | 1 |
| f6b0d559-4f91-4f93-3a9c-08dc315aff7e | 0.012 | 0.027 | 0.012 | 449 | Train | Parkinson's Disease | 1 |
| 0c3278fa-e89c-4394-d69f-08db86874595 | 0.011 | 0.024 | 0.011 | 449 | Train | Parkinson's Disease | 1 |
| 305f56d6-2f54-4a1f-6957-08dbe84eccc1 | 0.011 | 0.024 | 0.011 | 330 | Train | Cerebral Palsy | 1 |
| 4419493f-cde2-40cb-611a-08dcdb04185c | 0.011 | 0.023 | 0.011 | 447 | Train | ALS | 1 |
| 5aa635ad-c165-4b2a-3de4-08dd04d8f6c9 | 0.011 | 0.024 | 0.011 | 449 | Train | ALS | 1 |
| 5e4b7521-8a66-4c8b-7a25-08dc2a829031 | 0.011 | 0.026 | 0.011 | 447 | Dev | Parkinson's Disease | 1 |
| 683f4dc1-195e-492e-3ae1-08dd5b4fffca | 0.011 | 0.022 | 0.011 | 425 | Train | Down Syndrome | 1 |
| 6db33070-fe04-4e1c-22b2-08dc56b55882 | 0.011 | 0.022 | 0.011 | 430 | Train | Down Syndrome | 1 |
| 7960602d-a55a-42e6-ef04-08db5cba8704 | 0.011 | 0.023 | 0.011 | 449 | Train | Parkinson's Disease | 1 |
| 836f18e3-3361-43ea-8cee-08dcff4f47ae | 0.011 | 0.028 | 0.011 | 425 | Train | Cerebral Palsy | 1 |
| 92b4a66a-ea07-4435-0bb6-08dcf9635df3 | 0.011 | 0.024 | 0.011 | 449 | Train | Parkinson's Disease | 1 |
| a94bf456-95e1-44ee-8f15-08dcdbd22259 | 0.011 | 0.025 | 0.011 | 448 | Train | Parkinson's Disease | 1 |
| b71911dc-0c02-4ae0-7b85-08dd465f9f88 | 0.011 | 0.026 | 0.011 | 430 | Train | Cerebral Palsy | 1 |
| b8be96ec-5298-4842-abaf-08dc5d6a38e4 | 0.011 | 0.026 | 0.011 | 448 | Train | ALS | 1 |
| c1b57fac-44ea-4928-08e7-08db6f745978 | 0.011 | 0.020 | 0.011 | 135 | Train | Parkinson's Disease | 1 |
| ceb93c6f-0b16-45e9-8096-08dc28b09bf9 | 0.011 | 0.025 | 0.011 | 448 | Train | Parkinson's Disease | 1 |
| d6d4e52a-87db-44b8-161d-08db89680dc1 | 0.011 | 0.027 | 0.011 | 448 | Train | Parkinson's Disease | 1 |
| 17073b31-5882-4a6f-680c-08db4cce187f | 0.011 | 0.023 | 0.011 | 450 | Dev | Parkinson's Disease | 1 |
| 1b369798-cbf7-4a94-4ef0-08dcacc27c9e | 0.011 | 0.024 | 0.011 | 450 | Train | ALS | 1 |
| 2685e5d9-b4f4-47d1-95f2-08dc379c1f1f | 0.011 | 0.026 | 0.011 | 450 | Dev | Parkinson's Disease | 1 |
| 3415facd-2541-47f9-5b86-08db2bb3509e | 0.011 | 0.026 | 0.011 | 450 | Train | Parkinson's Disease | 1 |
| 3e9ab29f-daf0-4a3c-a181-08dc11dcc589 | 0.011 | 0.027 | 0.011 | 450 | Dev | ALS | 1 |
| 55e37781-2d81-434e-3a28-08dc5fadb5c5 | 0.011 | 0.025 | 0.011 | 450 | Train | ALS | 1 |
| 5ea03b3c-4204-4f2f-15fc-08dbb62a2382 | 0.011 | 0.025 | 0.011 | 450 | Train | Parkinson's Disease | 1 |
| 75908261-5509-4a6e-7f9a-08dc9f90df2f | 0.011 | 0.023 | 0.011 | 428 | Train | Cerebral Palsy | 1 |
| 7d7c9257-5e01-4b9f-a196-08dc11dcc589 | 0.011 | 0.022 | 0.011 | 450 | Train | ALS | 1 |
| 93b8a8bb-e30c-4d51-307f-08dd5740f974 | 0.011 | 0.024 | 0.011 | 450 | Train | ALS | 1 |
| 9e7aa4fd-7ec8-4ae7-c277-08db783c5d41 | 0.011 | 0.022 | 0.011 | 450 | Train | Parkinson's Disease | 1 |
| d4b0ccc0-6a22-4b2f-8b2f-08dc44f243ab | 0.011 | 0.022 | 0.011 | 450 | Train | Parkinson's Disease | 1 |
| d83c96a2-eeb0-416f-116d-08dc623ec532 | 0.011 | 0.026 | 0.011 | 450 | Dev | ALS | 1 |
| e1ba230d-d2d0-4c90-327c-08dccddb15fe | 0.011 | 0.021 | 0.011 | 450 | Train | ALS | 1 |
| 1af4bcb6-5607-4fee-0fd7-08dcd99f98d3 | 0.010 | 0.023 | 0.010 | 444 | Train | ALS | 1 |
| 1b3e248a-f3dc-4173-2e7a-08dc27684872 | 0.010 | 0.022 | 0.010 | 443 | Train | Parkinson's Disease | 1 |
| 1d97f400-f70d-48da-6485-08db26850d18 | 0.010 | 0.020 | 0.010 | 449 | Train | Parkinson's Disease | 1 |
| 26c12635-5dde-45d0-e7a8-08dcd9e31338 | 0.010 | 0.022 | 0.010 | 450 | Dev | ALS | 1 |
| 2eb5f501-b067-46f9-e901-08dcf2e1353e | 0.010 | 0.023 | 0.010 | 449 | Train | ALS | 1 |
| 309e2a55-50a4-4c5a-2e7f-08dc27684872 | 0.010 | 0.024 | 0.010 | 449 | Train | Parkinson's Disease | 1 |
| 361d90cd-e838-451e-c58f-08dc27c1bd26 | 0.010 | 0.026 | 0.010 | 85 | Dev | Parkinson's Disease | 1 |
| 41cd19f7-8c7e-4845-4ccb-08dd60a97c83 | 0.010 | 0.021 | 0.010 | 344 | Train | Stroke | 1 |
| 50836d2a-d25b-48bf-ecff-08dbe1995a23 | 0.010 | 0.025 | 0.010 | 424 | Train | Down Syndrome | 1 |
| 632812b2-3a92-4e2a-699f-08dc17913c94 | 0.010 | 0.024 | 0.010 | 450 | Train | ALS | 1 |
| 6b1ea95a-ac97-404b-450b-08dc42c84745 | 0.010 | 0.023 | 0.010 | 448 | Train | Parkinson's Disease | 1 |
| 7f1d37a6-dc22-4bb8-b2f1-08db6e8bdba4 | 0.010 | 0.026 | 0.010 | 450 | Dev | Parkinson's Disease | 1 |
| 82118252-9858-4410-19b9-08db2fb58edf | 0.010 | 0.022 | 0.010 | 450 | Train | Parkinson's Disease | 1 |
| 8a8c72cc-2226-4786-4efa-08dcacc27c9e | 0.010 | 0.022 | 0.010 | 448 | Train | ALS | 1 |
| 8e2d6856-1d18-46a5-b68b-08dc1130022a | 0.010 | 0.022 | 0.010 | 430 | Dev | Cerebral Palsy | 1 |
| 93194409-cd02-46de-841d-08dc34b33839 | 0.010 | 0.025 | 0.010 | 449 | Train | Stroke | 1 |
| 962ef349-423c-4867-7c83-08dcc6cfbf82 | 0.010 | 0.018 | 0.010 | 430 | Train | Cerebral Palsy | 1 |
| 96ada12b-88af-44ce-0219-08dc41d581c9 | 0.010 | 0.027 | 0.010 | 428 | Dev | Cerebral Palsy | 1 |
| 99d161b1-b166-428b-d2c4-08db4723ec09 | 0.010 | 0.023 | 0.010 | 450 | Train | Parkinson's Disease | 1 |
| 9e80a90e-b226-428f-c657-08db73ef9d1c | 0.010 | 0.020 | 0.010 | 446 | Train | Parkinson's Disease | 1 |
| 9fa04401-2532-42e7-c578-08dc27c1bd26 | 0.010 | 0.027 | 0.010 | 448 | Dev | Parkinson's Disease | 1 |
| a38ae187-f5cc-4414-2713-08dc18a4ec91 | 0.010 | 0.022 | 0.010 | 450 | Train | ALS | 1 |
| a8728c20-ea2b-4a7d-717c-08db47ff8b9e | 0.010 | 0.021 | 0.010 | 75 | Train | Parkinson's Disease | 1 |
| b933acaf-01a9-4441-034e-08dcd2d6e84e | 0.010 | 0.020 | 0.010 | 449 | Train | Parkinson's Disease | 1 |
| c1fb56dd-977d-44a2-d2be-08db4723ec09 | 0.010 | 0.023 | 0.010 | 449 | Train | Parkinson's Disease | 1 |
| d314e258-097a-4d94-5766-08dcfa856e25 | 0.010 | 0.022 | 0.010 | 441 | Train | Parkinson's Disease | 1 |
| d365b0cf-1afc-4e37-a16d-08dc11dcc589 | 0.010 | 0.025 | 0.010 | 449 | Train | ALS | 1 |
| de0d6982-ae31-43fd-cce0-08dc48edc242 | 0.010 | 0.026 | 0.010 | 444 | Train | ALS | 1 |
| df01c071-8ac2-4b48-72e1-08dd51fb5ebc | 0.010 | 0.022 | 0.010 | 358 | Train | ALS | 1 |
| ecfe53e2-1780-4eab-6052-08dbc2f1ba22 | 0.010 | 0.022 | 0.010 | 450 | Train | Parkinson's Disease | 1 |
| edc855c9-4e06-4163-43da-08dc13e54ff5 | 0.010 | 0.024 | 0.010 | 429 | Train | Cerebral Palsy | 1 |
| eed7a92d-bbd8-49e7-0fa6-08dcd99f98d3 | 0.010 | 0.022 | 0.010 | 264 | Train | ALS | 1 |
| 031bd6e9-d0cb-4ac6-64d2-08dc18216525 | 0.009 | 0.023 | 0.009 | 223 | Train | ALS | 1 |
| 08626c89-3dbd-4756-488d-08db66e486e4 | 0.009 | 0.024 | 0.009 | 449 | Dev | Parkinson's Disease | 1 |
| 0ddac1b4-317c-4d5b-a1cc-08dc11dcc589 | 0.009 | 0.022 | 0.009 | 448 | Train | ALS | 1 |
| 2ab74a1c-a193-46c7-c591-08dc27c1bd26 | 0.009 | 0.024 | 0.009 | 430 | Train | Cerebral Palsy | 1 |
| 2e2f9aae-3d1d-4b97-8e90-08dc6c41cdfd | 0.009 | 0.019 | 0.009 | 90 | Train | ALS | 1 |
| 37a9fbdc-03a6-4ebd-1f62-08db3dcbbd09 | 0.009 | 0.021 | 0.009 | 447 | Train | Parkinson's Disease | 1 |
| 4071d589-6395-4486-ab97-08db26923497 | 0.009 | 0.020 | 0.009 | 449 | Train | Parkinson's Disease | 1 |
| 61867433-ca92-4ac7-70db-08dd7672eb03 | 0.009 | 0.022 | 0.009 | 294 | Train | ALS | 1 |
| 643b2422-2f9a-45d7-a16b-08dc11dcc589 | 0.009 | 0.022 | 0.009 | 450 | Train | ALS | 1 |
| 65870458-e018-461d-a172-08dc11dcc589 | 0.009 | 0.022 | 0.009 | 450 | Train | ALS | 1 |
| 66143dd2-c117-4e29-87af-08dc74e08a4e | 0.009 | 0.019 | 0.009 | 428 | Train | Cerebral Palsy | 1 |
| 682ed0c5-f41a-488b-0856-08db66fd04b0 | 0.009 | 0.024 | 0.009 | 436 | Train | Parkinson's Disease | 1 |
| 7215b659-d731-478c-7698-08dc54a70eeb | 0.009 | 0.021 | 0.009 | 430 | Train | Down Syndrome | 1 |
| 7282bd95-7385-432b-54ba-08dc17c7b3c4 | 0.009 | 0.020 | 0.009 | 450 | Train | ALS | 1 |
| 7b2fe565-fa97-4f75-d603-08dc12ec34ac | 0.009 | 0.022 | 0.009 | 219 | Train | ALS | 1 |
| 8e0bd322-5790-4f07-cf51-08dc89b72177 | 0.009 | 0.023 | 0.009 | 46 | Train | ALS | 1 |
| 8e1f74a8-8b7b-4f3f-db61-08db263bd57d | 0.009 | 0.023 | 0.009 | 444 | Train | Parkinson's Disease | 1 |
| a358b4db-04f6-4c40-3917-08dc358e2588 | 0.009 | 0.020 | 0.009 | 430 | Train | Cerebral Palsy | 1 |
| a8238cc0-9c3b-45a6-f9f6-08dc138a527b | 0.009 | 0.020 | 0.009 | 449 | Train | ALS | 1 |
| b23b4435-697e-4218-37c4-08dce6e2632a | 0.009 | 0.022 | 0.009 | 449 | Train | ALS | 1 |
| b85874e1-4722-461c-091a-08dd454e7a98 | 0.009 | 0.020 | 0.009 | 449 | Train | ALS | 1 |
| c2b6a53e-a301-4105-072c-08db6bc3d3c4 | 0.009 | 0.021 | 0.009 | 443 | Train | Parkinson's Disease | 1 |
| c54119ad-5b47-41d9-4153-08dcddb9e4a3 | 0.009 | 0.021 | 0.009 | 443 | Train | Parkinson's Disease | 1 |
| c55f7854-cee3-458a-b592-08dc5e199653 | 0.009 | 0.021 | 0.009 | 450 | Train | ALS | 1 |
| d3b31f8a-13a2-4ada-b954-08dc6eabb1a3 | 0.009 | 0.022 | 0.009 | 450 | Train | Parkinson's Disease | 1 |
| e38e67c1-2373-4578-6992-08dc17913c94 | 0.009 | 0.019 | 0.009 | 450 | Train | ALS | 1 |
| edbcc1e7-2fe7-41cf-7c8e-08dcc6cfbf82 | 0.009 | 0.027 | 0.009 | 429 | Train | Cerebral Palsy | 1 |
| f46b3335-0d95-48ec-7f98-08dc9f90df2f | 0.009 | 0.020 | 0.009 | 450 | Train | ALS | 1 |
| f60008c4-fe6e-4a38-aa58-08dbfc00603a | 0.009 | 0.022 | 0.009 | 430 | Train | Cerebral Palsy | 1 |
| 0298b0ec-4be0-4ed6-83ba-08db78b5561a | 0.008 | 0.019 | 0.008 | 449 | Train | Parkinson's Disease | 1 |
| 06e2c7a3-71e2-483b-ac50-08dc297d5492 | 0.008 | 0.014 | 0.008 | 423 | Train | Parkinson's Disease | 1 |
| 0b9b6a5a-fff7-4129-8082-08db3c5502ba | 0.008 | 0.022 | 0.008 | 439 | Train | Parkinson's Disease | 1 |
| 0c3530f6-c6d8-4b8f-06f5-08dc3393f0c2 | 0.008 | 0.017 | 0.008 | 450 | Train | Parkinson's Disease | 1 |
| 132876ee-6363-4789-4e12-08db39529b19 | 0.008 | 0.020 | 0.008 | 449 | Train | Parkinson's Disease | 1 |
| 1ef92aec-b267-4e16-0fc9-08dcd99f98d3 | 0.008 | 0.017 | 0.008 | 224 | Train | ALS | 1 |
| 1efde431-6c53-4fcc-1162-08db2577509f | 0.008 | 0.020 | 0.008 | 447 | Train | Parkinson's Disease | 1 |
| 27b5dbf8-d6ec-449e-627a-08dcdcbbcec7 | 0.008 | 0.026 | 0.008 | 141 | Dev | ALS | 1 |
| 2b4ebaba-cf6d-4c2c-25b5-08dc18e8f490 | 0.008 | 0.019 | 0.008 | 450 | Train | ALS | 1 |
| 2bee0d03-1967-4d7c-a1dc-08dc11dcc589 | 0.008 | 0.021 | 0.008 | 265 | Train | ALS | 1 |
| 3f9653f8-ffc8-44f6-10e6-08db6af1ce41 | 0.008 | 0.022 | 0.008 | 449 | Train | Parkinson's Disease | 1 |
| 42f64a0c-c928-4f74-8fb5-08dc5412807c | 0.008 | 0.034 | 0.008 | 32 | Train | Cerebral Palsy | 1 |
| 4cdd3d5d-1264-4bb2-3012-08dcc11ab035 | 0.008 | 0.020 | 0.008 | 450 | Train | ALS | 1 |
| 4fd6ac1c-7520-4603-cf46-08dc36bdc819 | 0.008 | 0.022 | 0.008 | 450 | Train | Parkinson's Disease | 1 |
| 513b2340-8493-4342-dde5-08dc9aac4c52 | 0.008 | 0.017 | 0.008 | 240 | Train | ALS | 1 |
| 52bb5a13-34c5-4f5c-4cca-08dd60a97c83 | 0.008 | 0.019 | 0.008 | 430 | Train | Down Syndrome | 1 |
| 59b47aea-1709-4559-aa22-08db7f28d1f2 | 0.008 | 0.017 | 0.008 | 450 | Train | Parkinson's Disease | 1 |
| 5e2ed8a5-a43c-4254-2e66-08dce1b26f4b | 0.008 | 0.021 | 0.008 | 449 | Train | ALS | 1 |
| 698a7386-afd4-4841-44ad-08dc2be1ce70 | 0.008 | 0.019 | 0.008 | 449 | Train | ALS | 1 |
| 6b83360c-897c-4188-1070-08dc4d0abe5b | 0.008 | 0.019 | 0.008 | 430 | Train | Cerebral Palsy | 1 |
| 6c6cbc6d-f66d-4b02-ea95-08db4e7b0019 | 0.008 | 0.020 | 0.008 | 440 | Train | Parkinson's Disease | 1 |
| 72b94312-b54a-4585-415d-08dcddb9e4a3 | 0.008 | 0.017 | 0.008 | 446 | Train | Parkinson's Disease | 1 |
| 74b14e89-4ea1-405e-d402-08dd72c9091a | 0.008 | 0.019 | 0.008 | 435 | Train | ALS | 1 |
| 7f36cf5a-a56b-4bd6-ef05-08db5cba8704 | 0.008 | 0.019 | 0.008 | 447 | Train | Parkinson's Disease | 1 |
| 8cf6d8fc-57c1-4fc1-b734-08dc443ba3cc | 0.008 | 0.019 | 0.008 | 420 | Train | Cerebral Palsy | 1 |
| 8dcc2534-4954-488d-bd51-08dc8ad4730d | 0.008 | 0.018 | 0.008 | 450 | Train | ALS | 1 |
| aa0f2353-c7bb-44a9-bdbe-08dc6936e41a | 0.008 | 0.021 | 0.008 | 450 | Train | ALS | 1 |
| b16688d5-8a1a-459b-4f02-08dcacc27c9e | 0.008 | 0.021 | 0.008 | 449 | Train | ALS | 1 |
| b333b2de-a4df-4cee-2e90-08dc27684872 | 0.008 | 0.020 | 0.008 | 448 | Train | Parkinson's Disease | 1 |
| b3ca3b66-a7ff-486d-a17e-08dc11dcc589 | 0.008 | 0.021 | 0.008 | 450 | Train | ALS | 1 |
| ba6febaf-25fc-4e8b-2e62-08dc27684872 | 0.008 | 0.020 | 0.008 | 445 | Train | Parkinson's Disease | 1 |
| bdf351d7-2875-41fc-1c44-08db344ca254 | 0.008 | 0.021 | 0.008 | 450 | Train | Parkinson's Disease | 1 |
| c83a14dd-2c43-4a82-506d-08db74cd0e8d | 0.008 | 0.017 | 0.008 | 450 | Train | Parkinson's Disease | 1 |
| c8a20349-2c7b-44f5-9829-08dc7e56149c | 0.008 | 0.018 | 0.008 | 430 | Train | Cerebral Palsy | 1 |
| f5394c87-9584-4986-b6b2-08dc8d7bb350 | 0.008 | 0.019 | 0.008 | 449 | Train | ALS | 1 |
| f7a16987-f872-4be8-df26-08dc12f39a63 | 0.008 | 0.021 | 0.008 | 450 | Dev | ALS | 1 |
| f84154b0-68f1-42ae-2e8e-08dc27684872 | 0.008 | 0.019 | 0.008 | 445 | Dev | Parkinson's Disease | 1 |
| fc3cb82b-198f-466d-19cd-08dc2c44c8f4 | 0.008 | 0.017 | 0.008 | 446 | Train | Parkinson's Disease | 1 |
| c762bb64-0df2-4549-abb0-08dc5d6a38e4 | 0.007 | 0.016 | 0.007 | 343 | Train | ALS | 1 |
| 1315d02d-1f43-4d11-a8ad-08dc1144581f | 0.007 | 0.017 | 0.007 | 430 | Train | Cerebral Palsy | 1 |
| 1572a6b0-4b83-4ff4-c589-08dc27c1bd26 | 0.007 | 0.016 | 0.007 | 449 | Train | Parkinson's Disease | 1 |
| 1a31d058-b4f0-4915-94e2-08dc0dffdde6 | 0.007 | 0.016 | 0.007 | 449 | Train | ALS | 1 |
| 2a3b2d95-92b6-44fd-c588-08dc27c1bd26 | 0.007 | 0.018 | 0.007 | 443 | Train | Parkinson's Disease | 1 |
| 36819bf1-b6a8-4b73-2eca-08dc27684872 | 0.007 | 0.017 | 0.007 | 450 | Train | Parkinson's Disease | 1 |
| 38bbecae-c73b-4791-f536-08db33311565 | 0.007 | 0.017 | 0.007 | 450 | Train | Parkinson's Disease | 1 |
| 43fbb21e-2627-46a1-6829-08dd025ce1a9 | 0.007 | 0.017 | 0.007 | 449 | Train | ALS | 1 |
| 4aa6c6f2-9f9f-4394-59e4-08dd3c96897d | 0.007 | 0.017 | 0.007 | 428 | Train | Down Syndrome | 1 |
| 55f3ac96-0f93-4f9a-8df8-08dd4ae40880 | 0.007 | 0.018 | 0.007 | 247 | Dev | ALS | 1 |
| 590fb318-bca6-4923-89f8-08db6b5f86fb | 0.007 | 0.017 | 0.007 | 449 | Train | Parkinson's Disease | 1 |
| 5a3c16b7-fd51-4c8a-cf50-08dc89b72177 | 0.007 | 0.018 | 0.007 | 450 | Dev | ALS | 1 |
| 687475ee-ac3a-4246-c563-08dc27c1bd26 | 0.007 | 0.016 | 0.007 | 448 | Train | Parkinson's Disease | 1 |
| 7b0f16fa-2404-4335-07ac-08dbaed83b41 | 0.007 | 0.018 | 0.007 | 449 | Train | Parkinson's Disease | 1 |
| b06a8833-f395-40ac-7cdb-08dc8ba4f236 | 0.007 | 0.019 | 0.007 | 450 | Train | ALS | 1 |
| bad794ff-c207-43b5-f3bc-08db49b9f20e | 0.007 | 0.018 | 0.007 | 450 | Dev | Parkinson's Disease | 1 |
| bc8e23bf-86bf-476d-0fcb-08dcd99f98d3 | 0.007 | 0.020 | 0.007 | 450 | Train | ALS | 1 |
| cd7832fd-30a6-4c40-db63-08db263bd57d | 0.007 | 0.016 | 0.007 | 433 | Train | Parkinson's Disease | 1 |
| cedf88b9-ada6-4d9f-e826-08dceaeac878 | 0.007 | 0.019 | 0.007 | 450 | Train | ALS | 1 |
| d18cc111-39bc-4e6e-f3bd-08db49b9f20e | 0.007 | 0.016 | 0.007 | 450 | Train | Parkinson's Disease | 1 |
| d4e6f4e3-9b35-4c7e-669b-08db44e7c916 | 0.007 | 0.022 | 0.007 | 58 | Dev | Parkinson's Disease | 1 |
| d59c9675-314c-4e81-1f68-08db3dcbbd09 | 0.007 | 0.019 | 0.007 | 450 | Train | Parkinson's Disease | 1 |
| dcc44a0e-a2d1-4a07-5312-08dc95210be1 | 0.007 | 0.018 | 0.007 | 303 | Train | Cerebral Palsy | 1 |
| ec7835ce-2057-49e5-a18a-08dc11dcc589 | 0.007 | 0.017 | 0.007 | 450 | Train | ALS | 1 |
| ecbe385b-1b5c-45aa-bc3c-08db7417355e | 0.007 | 0.016 | 0.007 | 449 | Train | Parkinson's Disease | 1 |
| f10f76ad-650c-4f1b-db5d-08db263bd57d | 0.007 | 0.017 | 0.007 | 443 | Train | Parkinson's Disease | 1 |
| f3575077-1763-443c-0fe0-08dcd99f98d3 | 0.007 | 0.019 | 0.007 | 447 | Train | ALS | 1 |
| f8e65210-0ac9-4c7c-c658-08db73ef9d1c | 0.007 | 0.018 | 0.007 | 443 | Dev | Parkinson's Disease | 1 |
| fb9386d2-b64c-4706-37ca-08dce6e2632a | 0.007 | 0.019 | 0.007 | 450 | Train | ALS | 1 |
| 2d120fc4-e851-4ab8-4eff-08dcacc27c9e | 0.007 | 0.026 | 0.007 | 85 | Train | ALS | 1 |
| 61c13881-3c87-4b92-5e18-08db426a2d1c | 0.007 | 0.020 | 0.007 | 84 | Train | Parkinson's Disease | 1 |
| 6f61dc7c-d9ba-4d52-914d-08dcd7fdf875 | 0.007 | 0.019 | 0.007 | 102 | Train | ALS | 1 |
| aa0dc730-acf2-4e6f-cb5b-08dc840245ea | 0.007 | 0.023 | 0.007 | 85 | Train | ALS | 1 |
| db83c1ba-3ccd-4939-c583-08dc27c1bd26 | 0.007 | 0.017 | 0.007 | 442 | Train | Parkinson's Disease | 1 |
| 0cc37842-3e60-493d-eab6-08db5ebeefc6 | 0.006 | 0.015 | 0.006 | 450 | Train | Parkinson's Disease | 1 |
| 16b68dd2-bfc4-45c5-8dfd-08dd4ae40880 | 0.006 | 0.015 | 0.006 | 445 | Train | ALS | 1 |
| 29bb2e3c-6eee-4a30-02a9-08dcaa8c3d9d | 0.006 | 0.016 | 0.006 | 446 | Train | ALS | 1 |
| 3f0de68f-e620-49ba-5cef-08db46a76191 | 0.006 | 0.019 | 0.006 | 447 | Train | Parkinson's Disease | 1 |
| 438039aa-f477-405e-d25a-08db32115f35 | 0.006 | 0.014 | 0.006 | 449 | Train | Parkinson's Disease | 1 |
| 479f6c3e-baa4-4782-27c3-08dc72e2a7b8 | 0.006 | 0.016 | 0.006 | 135 | Train | Parkinson's Disease | 1 |
| 511ea74b-4526-4237-a1d0-08dc11dcc589 | 0.006 | 0.017 | 0.006 | 446 | Train | ALS | 1 |
| 63ebcb02-e259-4632-1f63-08db3dcbbd09 | 0.006 | 0.014 | 0.006 | 450 | Train | Parkinson's Disease | 1 |
| 6ee7333a-ccb4-42f9-12aa-08db3e6e5021 | 0.006 | 0.015 | 0.006 | 449 | Train | Parkinson's Disease | 1 |
| 6fa3f212-6a4f-4019-f06f-08db4b4fdcbb | 0.006 | 0.014 | 0.006 | 449 | Train | Parkinson's Disease | 1 |
| 75884af1-0630-4e57-b82c-08dbb85ab880 | 0.006 | 0.014 | 0.006 | 449 | Train | Parkinson's Disease | 1 |
| 855424d7-22ff-4303-75a4-08dd3ba78fcd | 0.006 | 0.013 | 0.006 | 430 | Train | Down Syndrome | 1 |
| 860cc717-c664-4d80-e9a2-08dc2e961576 | 0.006 | 0.014 | 0.006 | 155 | Dev | Stroke | 1 |
| 888e9878-8142-4788-4ccd-08dd0b23004e | 0.006 | 0.016 | 0.006 | 449 | Train | ALS | 1 |
| b044cc61-1be8-4733-611e-08dcdb04185c | 0.006 | 0.015 | 0.006 | 442 | Train | ALS | 1 |
| b90d8200-649c-4709-0fc4-08dcd99f98d3 | 0.006 | 0.016 | 0.006 | 270 | Dev | ALS | 1 |
| cafede9d-42a3-473e-b12a-08dc804a93e8 | 0.006 | 0.018 | 0.006 | 446 | Train | Parkinson's Disease | 1 |
| cb693c5c-57a2-4ca1-24a3-08dd018a3881 | 0.006 | 0.013 | 0.006 | 45 | Train | Parkinson's Disease | 1 |
| cfafc3f7-cab9-48e2-d79c-08dc46c59895 | 0.006 | 0.016 | 0.006 | 450 | Train | ALS | 1 |
| d19f737f-9070-499c-5c23-08db7125e1cf | 0.006 | 0.015 | 0.006 | 450 | Train | Parkinson's Disease | 1 |
| d466cb1b-ade6-4cb6-e7bb-08dcd9e31338 | 0.006 | 0.016 | 0.006 | 450 | Train | ALS | 1 |
| e7d7e0b6-1bba-45f7-2e99-08dc27684872 | 0.006 | 0.015 | 0.006 | 450 | Train | Parkinson's Disease | 1 |
| f4977957-ef08-4173-cf2b-08dc89b72177 | 0.006 | 0.014 | 0.006 | 444 | Train | ALS | 1 |
| fb433483-7b5a-471d-0fe2-08dcd99f98d3 | 0.006 | 0.017 | 0.006 | 43 | Train | ALS | 1 |
| 07102085-639b-4910-0fd4-08dcd99f98d3 | 0.005 | 0.013 | 0.005 | 119 | Train | ALS | 1 |
| 07172c90-fcd6-4b5c-c4f1-08dcc960cba3 | 0.005 | 0.015 | 0.005 | 449 | Train | ALS | 1 |
| 0dea3495-b287-46ca-a1e8-08dc11dcc589 | 0.005 | 0.020 | 0.005 | 316 | Train | ALS | 1 |
| 153362b4-93c5-4860-9f9f-08dc61272c21 | 0.005 | 0.014 | 0.005 | 450 | Train | ALS | 1 |
| 28b53a9b-acd7-4b3e-ddeb-08dc9aac4c52 | 0.005 | 0.015 | 0.005 | 450 | Train | ALS | 1 |
| 2c6c3eb4-9956-48b2-a6d7-08dc15310511 | 0.005 | 0.014 | 0.005 | 450 | Train | ALS | 1 |
| 32aa9cef-4937-4cfa-7a0b-08db42147f9a | 0.005 | 0.014 | 0.005 | 450 | Train | Parkinson's Disease | 1 |
| 34644bd1-4c96-47ac-a1d2-08dc11dcc589 | 0.005 | 0.013 | 0.005 | 450 | Train | ALS | 1 |
| 3697f56c-bfa7-4bef-ff1e-08db750bb973 | 0.005 | 0.022 | 0.005 | 45 | Train | Parkinson's Disease | 1 |
| 4450c670-1015-4e12-ab55-08db7376d336 | 0.005 | 0.012 | 0.005 | 450 | Train | Parkinson's Disease | 1 |
| 54770062-db50-4f3b-bd52-08dc8ad4730d | 0.005 | 0.010 | 0.005 | 450 | Train | ALS | 1 |
| 5b52d5da-bf66-4309-a19c-08dc11dcc589 | 0.005 | 0.013 | 0.005 | 447 | Train | ALS | 1 |
| 6a4ed682-bcde-4fd9-807b-08dc2d678af8 | 0.005 | 0.013 | 0.005 | 430 | Train | Stroke | 1 |
| 6b40963e-06f4-4af2-d673-08dc687737d3 | 0.005 | 0.014 | 0.005 | 430 | Train | Cerebral Palsy | 1 |
| 6f7afcf6-5fea-4668-c724-08dd0d3b7be4 | 0.005 | 0.016 | 0.005 | 449 | Train | ALS | 1 |
| 8c341d58-2f7c-4404-0fb5-08dcd99f98d3 | 0.005 | 0.016 | 0.005 | 448 | Train | ALS | 1 |
| 8ee07e3b-57c6-4df3-f086-08dbffd6e72c | 0.005 | 0.016 | 0.005 | 430 | Train | Cerebral Palsy | 1 |
| a20d5dbd-fac5-4989-c56e-08dc27c1bd26 | 0.005 | 0.014 | 0.005 | 448 | Train | Parkinson's Disease | 1 |
| b171ad3c-5d86-4b56-dde8-08dc9aac4c52 | 0.005 | 0.015 | 0.005 | 449 | Train | ALS | 1 |
| b1eec993-dcde-428b-c4ca-08dc21e8e305 | 0.005 | 0.016 | 0.005 | 448 | Train | ALS | 1 |
| c35c82cd-4e97-4d47-1148-08db2b07b033 | 0.005 | 0.015 | 0.005 | 449 | Train | Parkinson's Disease | 1 |
| cf23e4d7-44a3-4c6a-c7cb-08dca9e51008 | 0.005 | 0.016 | 0.005 | 449 | Train | ALS | 1 |
| d0753161-5313-4593-8f22-08dcdbd22259 | 0.005 | 0.013 | 0.005 | 450 | Train | ALS | 1 |
| fa9f4370-e85f-4629-0c4a-08db33bf801f | 0.005 | 0.013 | 0.005 | 447 | Train | Parkinson's Disease | 1 |
| 27269d8c-d7c6-456c-6ece-08db6c5df3b4 | 0.005 | 0.017 | 0.005 | 439 | Train | Parkinson's Disease | 1 |
| 0089188f-a7ce-481a-4155-08dcddb9e4a3 | 0.004 | 0.012 | 0.004 | 449 | Train | Parkinson's Disease | 1 |
| 14d7c170-6b3a-4dbd-c576-08dc27c1bd26 | 0.004 | 0.012 | 0.004 | 447 | Train | Parkinson's Disease | 1 |
| 17412e2b-d84f-48b1-cf3d-08dc89b72177 | 0.004 | 0.012 | 0.004 | 448 | Dev | ALS | 1 |
| 1bfccfc9-298f-4352-a1cf-08dc11dcc589 | 0.004 | 0.007 | 0.004 | 134 | Train | ALS | 1 |
| 253ded82-b663-4ed7-0fd2-08dcd99f98d3 | 0.004 | 0.009 | 0.004 | 450 | Dev | ALS | 1 |
| 3793f574-311c-4146-699a-08dc17913c94 | 0.004 | 0.016 | 0.004 | 131 | Train | ALS | 1 |
| 49009238-7353-4d86-abc9-08dc5d6a38e4 | 0.004 | 0.011 | 0.004 | 430 | Train | Cerebral Palsy | 1 |
| 4b8aae89-754d-4c6e-f7da-08db65f35c8b | 0.004 | 0.013 | 0.004 | 447 | Train | Parkinson's Disease | 1 |
| 4eaaccc6-1908-4349-46be-08db82273f48 | 0.004 | 0.014 | 0.004 | 446 | Train | Parkinson's Disease | 1 |
| 51605a57-686d-40d3-6273-08dcdcbbcec7 | 0.004 | 0.013 | 0.004 | 449 | Train | Parkinson's Disease | 1 |
| 782857ee-1517-4b33-3a1e-08dc5fadb5c5 | 0.004 | 0.009 | 0.004 | 450 | Train | ALS | 1 |
| b7398ee3-0bd7-44cf-4cc6-08dd0b23004e | 0.004 | 0.016 | 0.004 | 430 | Dev | Cerebral Palsy | 1 |
| c8af1f79-07ad-4aca-0fe7-08dcd99f98d3 | 0.004 | 0.011 | 0.004 | 403 | Train | ALS | 1 |
| c904ef6b-7796-4d27-db5e-08db263bd57d | 0.004 | 0.014 | 0.004 | 447 | Train | Parkinson's Disease | 1 |
| e403c1ba-243b-4735-c2f7-08db4a8e24c0 | 0.004 | 0.013 | 0.004 | 447 | Train | Parkinson's Disease | 1 |
| f3c74cb8-cc12-4cc0-02a0-08dcaa8c3d9d | 0.004 | 0.012 | 0.004 | 450 | Train | ALS | 1 |
| 098c7b31-a1e2-4a9b-0bb0-08dcf9635df3 | 0.003 | 0.011 | 0.003 | 450 | Train | ALS | 1 |
| 0a71bb2c-5579-468f-3729-08dc13d38337 | 0.003 | 0.010 | 0.003 | 180 | Dev | ALS | 1 |
| 10988087-9d14-4c9d-b58a-08dc5e199653 | 0.003 | 0.013 | 0.003 | 383 | Train | ALS | 1 |
| 1b10a3f6-b3cd-460a-a1c7-08dc11dcc589 | 0.003 | 0.012 | 0.003 | 450 | Train | ALS | 1 |
| 1d02346c-0e65-4107-0a8f-08dc160787df | 0.003 | 0.011 | 0.003 | 55 | Train | ALS | 1 |
| 2369d561-cdde-48e0-9153-08dcd7fdf875 | 0.003 | 0.012 | 0.003 | 120 | Train | ALS | 1 |
| 627597df-ca41-44cd-0fcf-08dcd99f98d3 | 0.003 | 0.014 | 0.003 | 245 | Train | ALS | 1 |
| 7661028e-95ae-44cd-029a-08db8ea270da | 0.003 | 0.009 | 0.003 | 447 | Train | Parkinson's Disease | 1 |
| 974e88e4-238d-4830-6198-08db2a271679 | 0.003 | 0.012 | 0.003 | 448 | Train | Parkinson's Disease | 1 |
| b0ab3b58-fc9e-4f9b-87a9-08dc74e08a4e | 0.003 | 0.010 | 0.003 | 430 | Train | Cerebral Palsy | 1 |
| c640aa37-100e-4442-931a-08db7b2bf57b | 0.003 | 0.011 | 0.003 | 448 | Train | Parkinson's Disease | 1 |
| 056d402b-f64c-4e74-aba3-08dc5d6a38e4 | 0.002 | 0.008 | 0.002 | 135 | Train | ALS | 1 |
| abec150e-4e8b-4be2-cf11-08dc89b72177 | 0.002 | 0.012 | 0.002 | 55 | Train | ALS | 1 |
| 488e4f96-daaa-4013-87ab-08dc74e08a4e | 0.001 | 0.007 | 0.001 | 430 | Train | Cerebral Palsy | 1 |
| 55c1784a-ece4-414a-25b4-08dc18e8f490 | 0.000 | 0.000 | 0.000 | 2 | Dev | ALS | 1 |
| 7a1b14f7-4f67-4cf4-a1fe-08dc11dcc589 | 0.000 | 0.000 | 0.000 | 9 | Train | ALS | 1 |
