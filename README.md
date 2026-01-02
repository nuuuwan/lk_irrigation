# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_10:12:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,513 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **98** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 10:12:32 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:11:51 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:06:14 | Katharagama (Menik Ganga) | 0.54 | 🟢 Normal | -24.000 |  |
| 2026-01-02 10:06:11 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | -24.000 |  |
| 2026-01-02 10:06:11 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:06:09 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -24.000 |  |
| 2026-01-02 10:06:09 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:06:08 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:06:07 | Katharagama (Menik Ganga) | 0.60 | 🟢 Normal | -24.000 |  |
| 2026-01-02 10:06:06 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:06:05 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | -24.000 |  |
| 2026-01-02 10:06:05 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:06:04 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:06:02 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | -24.000 |  |
| 2026-01-02 10:05:58 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-02 10:05:48 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:05:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-02 10:04:58 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:57 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:56 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:54 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:53 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:27 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:04:27 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:26 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:04:26 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-02 10:04:25 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:04:24 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:04:24 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.963 |  |
| 2026-01-02 10:04:22 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:04:21 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:04:13 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-02 10:04:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:50 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-01-02 10:03:42 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:28 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:26 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:25 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:24 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:19 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-02 10:03:17 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -360.000 |  |
| 2026-01-02 10:03:16 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -360.000 |  |
| 2026-01-02 10:03:14 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -360.000 |  |
| 2026-01-02 10:03:13 | Padiyathalawa (Maduru Oya) | 2.90 | 🟢 Normal | -360.000 |  |
| 2026-01-02 10:03:13 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.062 |  |
| 2026-01-02 10:03:11 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -360.000 |  |
| 2026-01-02 10:02:52 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.932 | 🔺 Rising |
| 2026-01-02 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.046 |  |
| 2026-01-02 10:02:41 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.021 |  |
| 2026-01-02 10:02:33 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:30 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:30 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:02:29 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:29 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:02:28 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:28 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:02:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.013 |  |
| 2026-01-02 10:02:26 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:26 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:02:25 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:02:24 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:02:22 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:01:57 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.095 |  |
| 2026-01-02 10:01:47 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
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
| 2026-01-02 09:58:10 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.963 |  |
| 2026-01-02 09:58:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.963 |  |
| 2026-01-02 09:58:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.963 |  |
| 2026-01-02 09:58:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.963 |  |
| 2026-01-02 09:49:15 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-02 09:49:12 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-02 09:49:07 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-02 09:49:02 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-02 09:43:33 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.932 | 🔺 Rising |
| 2026-01-02 09:39:18 | Thaldena (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.028 |  |
| 2026-01-02 09:39:17 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.028 |  |
| 2026-01-02 09:39:15 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.028 |  |
| 2026-01-02 09:39:14 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 10:02:52 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.932 | 🔺 Rising |
| 2026-01-02 10:05:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-02 10:04:13 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-02 10:04:26 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-02 10:05:58 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-02 10:03:19 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-02 05:06:54 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:01:47 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:30 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:27 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:11:35 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:28 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:58 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:04:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:05:48 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:03:42 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:12:32 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:33 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:14:27 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.004 |  |
| 2026-01-02 10:02:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.013 |  |
| 2026-01-02 10:02:41 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.021 |  |
| 2026-01-02 10:01:05 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.028 |  |
| 2026-01-02 10:03:50 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-01-02 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.046 |  |
| 2026-01-02 10:00:12 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.061 |  |
| 2026-01-02 10:03:13 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.062 |  |
| 2026-01-02 10:01:57 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.095 |  |
| 2026-01-02 10:00:58 | Siyambalanduwa (Heda Oya) | 1.69 | 🟢 Normal | -0.097 |  |
| 2026-01-02 10:04:24 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.963 |  |
| 2026-01-02 10:06:14 | Katharagama (Menik Ganga) | 0.54 | 🟢 Normal | -24.000 |  |
| 2026-01-02 10:06:11 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:02:30 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2026-01-02 10:04:27 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:00:17 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -72.000 |  |
| 2026-01-02 10:00:21 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -108.000 |  |
| 2026-01-02 10:03:17 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -360.000 |  |
| 2026-01-02 10:00:58 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | -468.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)