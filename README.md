# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **5,760 measurements**
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## Latest 20 Measurements

| Measured At | Station (River Basin) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 14:39:41 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal |
| 2025-11-30 14:12:20 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal |
| 2025-11-30 14:10:24 | Giriulla (Maha Oya) | 4.25 | 🟢 Normal |
| 2025-11-30 14:07:45 | Rathnapura (Kalu Ganga) | 6.80 | 🟡 Alert |
| 2025-11-30 14:06:46 | Siyambalanduwa (Heda Oya) | 1.37 | 🟢 Normal |
| 2025-11-30 14:06:22 | Glencourse (Kelani Ganga) | 17.09 | 🟠 Minor Flood |
| 2025-11-30 14:06:17 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal |
| 2025-11-30 14:05:02 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal |
| 2025-11-30 14:04:52 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal |
| 2025-11-30 14:04:48 | Hanwella (Kelani Ganga) | 10.69 | 🔴 Major Flood |
| 2025-11-30 14:04:40 | Horowpothana (Yan Oya) | 7.55 | 🟠 Minor Flood |
| 2025-11-30 14:04:02 | Nagalagam Street (Kelani Ganga) | 2.27 | 🔴 Major Flood |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal |
| 2025-11-30 14:03:55 | Katharagama (Menik Ganga) | 0.98 | 🟢 Normal |
| 2025-11-30 14:03:20 | Putupaula (Kalu Ganga) | 4.26 | 🟠 Minor Flood |
| 2025-11-30 14:02:49 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal |
| 2025-11-30 14:02:43 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal |
| 2025-11-30 14:02:42 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal |
| 2025-11-30 14:02:39 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 14:02:19 | Dunamale (Aththanagalu Oya) | 5.09 | 🟠 Minor Flood |

## Latest by Station

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 14:39:41 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal |
| 2025-11-30 14:12:20 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal |
| 2025-11-30 14:10:24 | Giriulla (Maha Oya) | 4.25 | 🟢 Normal |
| 2025-11-30 14:07:45 | Rathnapura (Kalu Ganga) | 6.80 | 🟡 Alert |
| 2025-11-30 14:06:46 | Siyambalanduwa (Heda Oya) | 1.37 | 🟢 Normal |
| 2025-11-30 14:06:22 | Glencourse (Kelani Ganga) | 17.09 | 🟠 Minor Flood |
| 2025-11-30 14:06:17 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal |
| 2025-11-30 14:05:02 | Yaka Wewa (Mukunu Oya) | 1.56 | 🟢 Normal |
| 2025-11-30 14:04:52 | Deraniyagala (Seethawaka Ganga) | 1.64 | 🟢 Normal |
| 2025-11-30 14:04:48 | Hanwella (Kelani Ganga) | 10.69 | 🔴 Major Flood |
| 2025-11-30 14:04:40 | Horowpothana (Yan Oya) | 7.55 | 🟠 Minor Flood |
| 2025-11-30 14:04:02 | Nagalagam Street (Kelani Ganga) | 2.27 | 🔴 Major Flood |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal |
| 2025-11-30 14:03:55 | Katharagama (Menik Ganga) | 0.98 | 🟢 Normal |
| 2025-11-30 14:03:20 | Putupaula (Kalu Ganga) | 4.26 | 🟠 Minor Flood |
| 2025-11-30 14:02:49 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal |
| 2025-11-30 14:02:43 | Holombuwa (Gurugoda Oya) | 1.98 | 🟢 Normal |
| 2025-11-30 14:02:42 | Magura (Maguru Ganga) | 3.30 | 🟢 Normal |
| 2025-11-30 14:02:39 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal |
| 2025-11-30 14:02:19 | Dunamale (Aththanagalu Oya) | 5.09 | 🟠 Minor Flood |
| 2025-11-30 14:02:17 | Norwood (Kehelgamu Oya) | 1.42 | 🟢 Normal |
| 2025-11-30 14:02:06 | Urawa (Urubokka Ganga) | 0.85 | 🟢 Normal |
| 2025-11-30 14:01:58 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal |
| 2025-11-30 14:01:53 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal |
| 2025-11-30 14:01:35 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal |
| 2025-11-30 14:01:29 | Ellagawa (Kalu Ganga) | 11.90 | 🟠 Minor Flood |
| 2025-11-30 14:01:24 | Kuda Oya (Kuda Oya) | 2.04 | 🟢 Normal |
| 2025-11-30 14:00:48 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal |
| 2025-11-30 13:59:56 | Nakkala (Kumbukkan Oya) | 1.84 | 🟢 Normal |
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