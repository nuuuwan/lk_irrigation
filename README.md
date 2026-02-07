# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_06:37:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,338 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **102** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 06:37:53 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.002 |  |
| 2026-02-07 06:20:55 | Panadugama (Nilwala Ganga) | 0.09 | 🟢 Normal | -57.383 |  |
| 2026-02-07 06:18:42 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -57.383 |  |
| 2026-02-07 06:17:48 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:47 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:45 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:44 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:43 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:42 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:41 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:40 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:39 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:37 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:36 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:34 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:33 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:32 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:31 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:30 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:29 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:28 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:27 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:26 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:25 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:24 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:22 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:21 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:17:20 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:16:42 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:15:55 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-07 06:15:11 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:10 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:09 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:08 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:06 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:05 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:04 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:03 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:01 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:00 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:58 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:57 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:55 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:52 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:49 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:48 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:46 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:45 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:43 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:41 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:39 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:36 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:34 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:32 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:29 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:27 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:26 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:25 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:23 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:21 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:20 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:19 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:12:18 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:17 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:16 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:14 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:13 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:12 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:10 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:08 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:05 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:03 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:02 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:12:00 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:58 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:57 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:55 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:54 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:53 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:51 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:50 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:48 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:47 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:45 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:44 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:42 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:40 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:39 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.036 |  |
| 2026-02-07 06:11:35 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:33 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:30 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:28 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:27 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:25 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:23 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:21 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:20 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:17 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:16 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:14 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:11:12 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 06:15:55 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-07 05:01:57 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-07 05:06:55 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 04:09:19 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 05:30:03 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:02:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:22:58 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:35 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:18:04 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:11 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:27:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:13:10 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:01:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:44 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:01:25 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:04:47 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:16:42 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:24 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:15:11 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:02:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:06:53 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 06:37:53 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.002 |  |
| 2026-02-07 04:04:23 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.003 |  |
| 2026-02-07 05:09:12 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:05:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:06:06 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-07 06:11:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.036 |  |
| 2026-02-07 05:06:35 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.037 |  |
| 2026-02-07 05:03:00 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-07 05:06:40 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | -0.047 |  |
| 2026-02-07 05:07:01 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.048 |  |
| 2026-02-07 05:00:48 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.461 |  |
| 2026-02-07 05:01:15 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.630 |  |
| 2026-02-07 05:07:45 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -9.000 |  |
| 2026-02-07 05:03:58 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -18.000 |  |
| 2026-02-07 06:17:48 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -36.000 |  |
| 2026-02-07 06:20:55 | Panadugama (Nilwala Ganga) | 0.09 | 🟢 Normal | -57.383 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)