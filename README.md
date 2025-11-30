# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **5,699 measurements**
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38) Public Domain. Please share and reuse!

## Latest 20 Measurements

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 12:28:47 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal |
| 2025-11-30 12:12:21 | Yaka Wewa (Mukunu Oya) | 1.63 | 🟢 Normal |
| 2025-11-30 12:08:51 | Hanwella (Kelani Ganga) | 10.75 | 🔴 Major Flood |
| 2025-11-30 12:08:46 | Holombuwa (Gurugoda Oya) | 1.98 | 🟢 Normal |
| 2025-11-30 12:08:46 | Urawa (Urubokka Ganga) | 0.85 | 🟢 Normal |
| 2025-11-30 12:07:43 | Nagalagam Street (Kelani Ganga) | 2.27 | 🔴 Major Flood |
| 2025-11-30 12:06:55 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal |
| 2025-11-30 12:06:20 | Rathnapura (Kalu Ganga) | 6.96 | 🟡 Alert |
| 2025-11-30 12:05:28 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal |
| 2025-11-30 12:04:46 | Deraniyagala (Seethawaka Ganga) | 1.66 | 🟢 Normal |
| 2025-11-30 12:04:08 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal |
| 2025-11-30 12:03:26 | Glencourse (Kelani Ganga) | 17.47 | 🟠 Minor Flood |
| 2025-11-30 12:03:18 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal |
| 2025-11-30 12:03:18 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal |
| 2025-11-30 12:03:12 | Putupaula (Kalu Ganga) | 4.25 | 🟠 Minor Flood |
| 2025-11-30 12:02:29 | Kithulgala (Kelani Ganga) | 2.48 | 🟢 Normal |
| 2025-11-30 12:02:24 | Dunamale (Aththanagalu Oya) | 5.19 | 🟠 Minor Flood |
| 2025-11-30 12:02:20 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal |
| 2025-11-30 12:02:15 | Kuda Oya (Kuda Oya) | 2.06 | 🟢 Normal |
| 2025-11-30 12:02:13 | Katharagama (Menik Ganga) | 1.19 | 🟢 Normal |

## Latest by Station

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 12:28:47 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal |
| 2025-11-30 12:12:21 | Yaka Wewa (Mukunu Oya) | 1.63 | 🟢 Normal |
| 2025-11-30 12:08:51 | Hanwella (Kelani Ganga) | 10.75 | 🔴 Major Flood |
| 2025-11-30 12:08:46 | Holombuwa (Gurugoda Oya) | 1.98 | 🟢 Normal |
| 2025-11-30 12:08:46 | Urawa (Urubokka Ganga) | 0.85 | 🟢 Normal |
| 2025-11-30 12:07:43 | Nagalagam Street (Kelani Ganga) | 2.27 | 🔴 Major Flood |
| 2025-11-30 12:06:55 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal |
| 2025-11-30 12:06:20 | Rathnapura (Kalu Ganga) | 6.96 | 🟡 Alert |
| 2025-11-30 12:05:28 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal |
| 2025-11-30 12:04:46 | Deraniyagala (Seethawaka Ganga) | 1.66 | 🟢 Normal |
| 2025-11-30 12:04:08 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal |
| 2025-11-30 12:03:26 | Glencourse (Kelani Ganga) | 17.47 | 🟠 Minor Flood |
| 2025-11-30 12:03:18 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal |
| 2025-11-30 12:03:18 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal |
| 2025-11-30 12:03:12 | Putupaula (Kalu Ganga) | 4.25 | 🟠 Minor Flood |
| 2025-11-30 12:02:29 | Kithulgala (Kelani Ganga) | 2.48 | 🟢 Normal |
| 2025-11-30 12:02:24 | Dunamale (Aththanagalu Oya) | 5.19 | 🟠 Minor Flood |
| 2025-11-30 12:02:20 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal |
| 2025-11-30 12:02:15 | Kuda Oya (Kuda Oya) | 2.06 | 🟢 Normal |
| 2025-11-30 12:02:13 | Katharagama (Menik Ganga) | 1.19 | 🟢 Normal |
| 2025-11-30 12:02:08 | Magura (Maguru Ganga) | 3.46 | 🟢 Normal |
| 2025-11-30 12:02:08 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal |
| 2025-11-30 12:01:54 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal |
| 2025-11-30 12:01:17 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal |
| 2025-11-30 12:01:14 | Horowpothana (Yan Oya) | 7.56 | 🟠 Minor Flood |
| 2025-11-30 12:00:38 | Norwood (Kehelgamu Oya) | 1.44 | 🟢 Normal |
| 2025-11-30 12:00:09 | Nakkala (Kumbukkan Oya) | 1.87 | 🟢 Normal |
| 2025-11-30 11:00:26 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood |
| 2025-11-30 06:09:31 | Giriulla (Maha Oya) | 4.80 | 🟢 Normal |
| 2025-11-30 03:16:47 | Badalgama (Maha Oya) | 11.35 | 🔴 Major Flood |
| 2025-11-28 15:00:24 | Thanthirimale (Malwathu Oya) | 10.30 | 🔴 Major Flood |
| 2025-11-28 06:04:09 | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood |
| 2025-11-28 02:13:33 | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood |
| 2025-11-27 23:05:48 | Nawalapitiya (Mahaweli Ganga) | 6.55 | 🔴 Major Flood |
| 2025-11-27 20:03:23 | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood |
| 2025-11-27 18:42:59 | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood |
| 2025-11-27 13:00:40 | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood |
| 2025-11-27 08:02:16 | Thaldena (Badulu Oya) | 4.25 | 🟠 Minor Flood |

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)