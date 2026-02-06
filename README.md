# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_19:30:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **102** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 19:30:36 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:26:25 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-06 19:25:08 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:17:09 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-02-06 19:16:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:15:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:14:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:22 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-06 19:13:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:13:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:12:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:12:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:12:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:12:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:12:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:12:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:12:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:11:31 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.017 |  |
| 2026-02-06 19:11:29 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:09:29 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-06 19:09:27 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-02-06 19:09:19 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-06 19:07:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:06:58 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-06 19:06:22 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:31 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:19 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:14 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-06 19:05:12 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:05 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:04:46 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:04:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:03:28 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-02-06 19:03:15 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:47 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.062 |  |
| 2026-02-06 19:02:41 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:17 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:12 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:06 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-06 19:01:44 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:01:41 | Manampitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 19:01:26 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:00:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 19:17:09 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-02-06 19:09:19 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 19:06:58 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-06 19:13:22 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-06 19:05:14 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-06 19:09:29 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-06 19:26:25 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-06 19:01:41 | Manampitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 19:07:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:02:40 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:06:01 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:19 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:04:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:05 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:03:15 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:31 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:41 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:04:46 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:12 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:30:36 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:01:44 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:17 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:06:22 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:01:26 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:11:29 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:05:12 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:25:08 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:16:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-06 19:02:06 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-06 19:09:27 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-02-06 19:11:31 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.017 |  |
| 2026-02-06 19:03:28 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-06 19:02:47 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.062 |  |
| 2026-02-06 19:00:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)