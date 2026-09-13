# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_14:51:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,815 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 14:51:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-13 14:40:38 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:24:19 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:19:20 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:15:31 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:13:16 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-13 14:11:18 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-09-13 14:11:02 | Magura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.143 |  |
| 2026-09-13 14:10:55 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.181 |  |
| 2026-09-13 14:10:06 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:09:05 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-09-13 14:08:27 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:08:23 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-13 14:07:43 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 14:13:16 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-13 14:01:21 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-13 14:06:36 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-13 14:08:23 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-13 14:51:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-13 14:03:19 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 14:05:32 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 14:07:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 14:01:28 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:02:47 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:02:13 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:10:06 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:08:27 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:00:43 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:19:20 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:40:38 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:06:36 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:04:51 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:01:39 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:07:00 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:02:09 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:06:13 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:07:43 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:00:18 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:15:31 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:04:01 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:03:57 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:11:18 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-09-13 14:02:26 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-13 14:09:05 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-09-13 14:02:22 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-09-13 14:06:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-09-13 14:03:31 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-09-13 14:02:44 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-09-13 14:06:39 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.084 |  |
| 2026-09-13 14:11:02 | Magura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.143 |  |
| 2026-09-13 14:04:47 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.148 |  |
| 2026-09-13 14:10:55 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)