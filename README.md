# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_04:26:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,288 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 04:26:53 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:18:38 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.086 |  |
| 2026-09-04 04:17:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-04 04:17:29 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:15:40 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.008 |  |
| 2026-09-04 04:15:21 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:08:31 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-09-04 04:07:54 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-09-04 04:06:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:06:03 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.010 |  |
| 2026-09-04 04:05:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 04:04:59 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-04 04:04:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-09-04 04:03:35 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-04 04:02:48 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:02:46 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:02:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:02:29 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:01:58 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 04:04:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-09-04 03:43:34 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-04 04:17:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-04 04:03:35 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-04 04:01:03 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-04 03:00:44 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-04 04:01:46 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 04:05:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 04:02:48 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:01:27 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:00:47 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 02:50:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:02:29 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:01:37 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:02:40 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:26:53 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 03:03:55 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:15:21 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:00:41 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-04 03:02:45 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:02:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:02:46 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:01:11 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:06:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:01:20 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:01:22 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-04 04:15:40 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.008 |  |
| 2026-09-04 04:08:31 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-09-04 04:04:59 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-04 04:06:03 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.010 |  |
| 2026-09-04 04:01:58 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-09-04 03:01:15 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-09-04 01:10:29 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-09-04 04:07:54 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-09-04 03:26:37 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.022 |  |
| 2026-09-04 04:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.046 |  |
| 2026-09-03 18:02:27 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |
| 2026-09-04 04:18:38 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.086 |  |
| 2026-09-04 04:01:37 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)