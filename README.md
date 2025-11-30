# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **5,731 measurements**
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38) Public Domain. Please share and reuse!

## Latest 20 Measurements

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 13:50:12 | Giriulla (Maha Oya) | 4.32 | 🟢 Normal |
| 2025-11-30 13:15:13 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal |
| 2025-11-30 13:15:06 | Ellagawa (Kalu Ganga) | 11.93 | 🟠 Minor Flood |
| 2025-11-30 13:15:00 | Ellagawa (Kalu Ganga) | 11.93 | 🟠 Minor Flood |
| 2025-11-30 13:12:16 | Holombuwa (Gurugoda Oya) | 1.98 | 🟢 Normal |
| 2025-11-30 13:12:03 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal |
| 2025-11-30 13:11:05 | Ellagawa (Kalu Ganga) | 11.92 | 🟠 Minor Flood |
| 2025-11-30 13:10:15 | Yaka Wewa (Mukunu Oya) | 1.59 | 🟢 Normal |
| 2025-11-30 13:09:31 | Horowpothana (Yan Oya) | 7.56 | 🟠 Minor Flood |
| 2025-11-30 13:09:04 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal |
| 2025-11-30 13:08:18 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal |
| 2025-11-30 13:08:17 | Rathnapura (Kalu Ganga) | 6.88 | 🟡 Alert |
| 2025-11-30 13:06:30 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal |
| 2025-11-30 13:06:12 | Urawa (Urubokka Ganga) | 0.85 | 🟢 Normal |
| 2025-11-30 13:05:52 | Katharagama (Menik Ganga) | 1.06 | 🟢 Normal |
| 2025-11-30 13:05:28 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal |
| 2025-11-30 13:04:07 | Hanwella (Kelani Ganga) | 10.72 | 🔴 Major Flood |
| 2025-11-30 13:04:07 | Kuda Oya (Kuda Oya) | 2.05 | 🟢 Normal |
| 2025-11-30 13:03:33 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 13:03:32 | Deraniyagala (Seethawaka Ganga) | 1.65 | 🟢 Normal |

## Latest by Station

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 13:50:12 | Giriulla (Maha Oya) | 4.32 | 🟢 Normal |
| 2025-11-30 13:15:13 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal |
| 2025-11-30 13:15:06 | Ellagawa (Kalu Ganga) | 11.93 | 🟠 Minor Flood |
| 2025-11-30 13:12:16 | Holombuwa (Gurugoda Oya) | 1.98 | 🟢 Normal |
| 2025-11-30 13:12:03 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal |
| 2025-11-30 13:10:15 | Yaka Wewa (Mukunu Oya) | 1.59 | 🟢 Normal |
| 2025-11-30 13:09:31 | Horowpothana (Yan Oya) | 7.56 | 🟠 Minor Flood |
| 2025-11-30 13:09:04 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal |
| 2025-11-30 13:08:18 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal |
| 2025-11-30 13:08:17 | Rathnapura (Kalu Ganga) | 6.88 | 🟡 Alert |
| 2025-11-30 13:06:30 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal |
| 2025-11-30 13:06:12 | Urawa (Urubokka Ganga) | 0.85 | 🟢 Normal |
| 2025-11-30 13:05:52 | Katharagama (Menik Ganga) | 1.06 | 🟢 Normal |
| 2025-11-30 13:05:28 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal |
| 2025-11-30 13:04:07 | Hanwella (Kelani Ganga) | 10.72 | 🔴 Major Flood |
| 2025-11-30 13:04:07 | Kuda Oya (Kuda Oya) | 2.05 | 🟢 Normal |
| 2025-11-30 13:03:33 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 13:03:32 | Deraniyagala (Seethawaka Ganga) | 1.65 | 🟢 Normal |
| 2025-11-30 13:03:26 | Nagalagam Street (Kelani Ganga) | 2.27 | 🔴 Major Flood |
| 2025-11-30 13:03:24 | Glencourse (Kelani Ganga) | 17.29 | 🟠 Minor Flood |
| 2025-11-30 13:02:51 | Dunamale (Aththanagalu Oya) | 5.14 | 🟠 Minor Flood |
| 2025-11-30 13:02:27 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal |
| 2025-11-30 13:02:26 | Putupaula (Kalu Ganga) | 4.25 | 🟠 Minor Flood |
| 2025-11-30 13:02:14 | Magura (Maguru Ganga) | 3.38 | 🟢 Normal |
| 2025-11-30 13:02:10 | Norwood (Kehelgamu Oya) | 1.43 | 🟢 Normal |
| 2025-11-30 13:01:46 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal |
| 2025-11-30 13:01:27 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal |
| 2025-11-30 13:00:54 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal |
| 2025-11-30 13:00:09 | Nakkala (Kumbukkan Oya) | 1.86 | 🟢 Normal |
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