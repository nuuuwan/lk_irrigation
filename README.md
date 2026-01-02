# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_10:01:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **124** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 10:01:47 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-02 10:01:05 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.028 |  |
| 2026-01-02 10:00:58 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | -468.000 |  |
| 2026-01-02 10:00:58 | Siyambalanduwa (Heda Oya) | 1.69 | 🟢 Normal | -0.097 |  |
| 2026-01-02 10:00:57 | Horowpothana (Yan Oya) | 3.58 | 🟢 Normal | -468.000 |  |
| 2026-01-02 10:00:56 | Horowpothana (Yan Oya) | 3.68 | 🟢 Normal | -468.000 |  |
| 2026-01-02 10:00:54 | Horowpothana (Yan Oya) | 3.76 | 🟢 Normal | -468.000 |  |
| 2026-01-02 10:00:53 | Horowpothana (Yan Oya) | 3.88 | 🟢 Normal | -468.000 |  |
| 2026-01-02 10:00:21 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -108.000 |  |
| 2026-01-02 10:00:20 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -108.000 |  |
| 2026-01-02 10:00:19 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -108.000 |  |
| 2026-01-02 10:00:18 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -108.000 |  |
| 2026-01-02 10:00:17 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:00:16 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:00:16 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -108.000 |  |
| 2026-01-02 10:00:14 | Weraganthota (Mahaweli Ganga) | -1.17 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:00:13 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:00:12 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.061 |  |
| 2026-01-02 10:00:11 | Weraganthota (Mahaweli Ganga) | -1.09 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:58:10 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -720.000 |  |
| 2026-01-02 09:58:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -720.000 |  |
| 2026-01-02 09:58:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -720.000 |  |
| 2026-01-02 09:58:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -720.000 |  |
| 2026-01-02 09:49:15 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:49:12 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:49:07 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:49:02 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:43:33 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:39:18 | Thaldena (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.028 |  |
| 2026-01-02 09:39:17 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.028 |  |
| 2026-01-02 09:39:15 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.028 |  |
| 2026-01-02 09:39:14 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.028 |  |
| 2026-01-02 09:34:19 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -18.000 |  |
| 2026-01-02 09:34:17 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -18.000 |  |
| 2026-01-02 09:34:12 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -18.000 |  |
| 2026-01-02 09:34:09 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -18.000 |  |
| 2026-01-02 09:28:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:28:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:28:22 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:28:21 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:28:20 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:28:19 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:28:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:28:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:28:04 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:27:03 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-02 09:25:36 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -720.000 |  |
| 2026-01-02 09:25:35 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -720.000 |  |
| 2026-01-02 09:23:50 | Siyambalanduwa (Heda Oya) | 1.75 | 🟢 Normal | -0.097 |  |
| 2026-01-02 09:23:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:23:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:23:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:23:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:23:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:23:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:21:50 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:21:49 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:21:48 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:21:47 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:21:32 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:21:25 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:21:20 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:21:15 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:21:13 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:21:01 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:20:11 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:20:10 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:20:09 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:20:07 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:20:06 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:26 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:24 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:23 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:21 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:20 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:18 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:16 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:57 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:56 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:55 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:54 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:53 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:52 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:50 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:49 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -144.000 |  |
| 2026-01-02 09:18:23 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -144.000 |  |
| 2026-01-02 09:18:21 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -144.000 |  |
| 2026-01-02 09:17:46 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:17:45 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:17:43 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:17:42 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:17:41 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:17:39 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:17:38 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:17:01 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:59 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:57 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:53 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:34 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:33 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:31 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:30 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:29 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:14:59 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-02 09:14:58 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-02 09:14:57 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-02 09:14:56 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-02 09:14:56 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-02 09:14:55 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-02 09:14:55 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-02 09:14:54 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-02 09:14:41 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:14:40 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:14:38 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:14:37 | Thanamalwila (Kirindi Oya) | 1.59 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:14:27 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.004 |  |
| 2026-01-02 09:10:38 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.002 |  |
| 2026-01-02 09:09:32 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:09:31 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:09:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:07:42 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 09:14:57 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-02 09:14:59 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-02 05:14:39 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-02 09:27:03 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-02 05:03:33 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.005 |  |
| 2026-01-02 09:17:46 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:06:54 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:01:47 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:16:34 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:11:35 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:05:21 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:28:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:19:26 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:21:32 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:28:04 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:43:33 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:23:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:10:38 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.002 |  |
| 2026-01-02 09:14:27 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.004 |  |
| 2026-01-02 08:41:39 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.006 |  |
| 2026-01-02 10:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-02 04:47:54 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-01-02 10:01:05 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.028 |  |
| 2026-01-02 10:00:12 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.061 |  |
| 2026-01-02 10:00:58 | Siyambalanduwa (Heda Oya) | 1.69 | 🟢 Normal | -0.097 |  |
| 2026-01-02 05:05:44 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | -0.186 |  |
| 2026-01-02 09:34:19 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -18.000 |  |
| 2026-01-02 09:28:22 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -36.000 |  |
| 2026-01-02 09:49:15 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:00:17 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:21:50 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -72.000 |  |
| 2026-01-02 09:14:41 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:00:21 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -108.000 |  |
| 2026-01-02 09:18:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -144.000 |  |
| 2026-01-02 10:00:58 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | -468.000 |  |
| 2026-01-02 09:58:10 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -720.000 |  |
| 2026-01-02 09:25:36 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -720.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)