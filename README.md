# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_01:29:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 01:29:30 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.007 |  |
| 2026-11-19 01:18:05 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:13:26 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.008 |  |
| 2026-11-19 01:12:32 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:09:57 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:07:55 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-11-19 01:05:47 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:05:42 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:05:29 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:04:46 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:04:25 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.035 |  |
| 2026-11-19 01:04:20 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:04:00 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-11-19 01:03:47 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:03:38 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-11-19 01:03:35 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-11-19 01:03:06 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-19 01:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-11-19 01:02:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:02:37 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.011 |  |
| 2026-11-19 01:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:35 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:34 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.044 |  |
| 2026-11-19 01:01:22 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:22 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:01 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:00:45 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-19 01:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 00:59:46 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 01:07:55 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-11-19 01:03:06 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-19 00:05:57 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-19 00:59:46 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-18 18:02:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:22 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 00:02:14 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:01 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:18:05 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 00:02:47 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:04:46 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:22 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:09:57 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:05:29 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:01:35 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:02:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:05:47 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:05:42 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 00:01:06 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:10 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:04:20 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:03:47 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:12:32 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:29:30 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.007 |  |
| 2026-11-19 00:20:17 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | -0.008 |  |
| 2026-11-19 01:13:26 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.008 |  |
| 2026-11-19 01:00:45 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-19 01:03:35 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-11-19 01:02:37 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.011 |  |
| 2026-11-19 01:04:00 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-11-19 01:03:38 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-11-19 01:04:25 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.035 |  |
| 2026-11-19 01:01:34 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.044 |  |
| 2026-11-19 01:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-11-19 00:12:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.052 |  |
| 2026-11-19 00:06:11 | Moraketiya (Walawe Ganga) | 2.01 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)