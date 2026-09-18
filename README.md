# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_08:09:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,065 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 08:09:43 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:08:51 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.101 |  |
| 2026-09-18 08:08:37 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.037 |  |
| 2026-09-18 08:08:13 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:07:29 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-18 08:06:42 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:06:28 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 08:06:07 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:05:39 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:05:26 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-09-18 08:05:24 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.075 |  |
| 2026-09-18 08:04:27 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:04:21 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.035 |  |
| 2026-09-18 08:04:11 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:04:06 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:03:57 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:03:43 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | -0.044 |  |
| 2026-09-18 08:03:32 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:02:59 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-09-18 08:02:48 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:41 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.030 |  |
| 2026-09-18 08:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:40 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:39 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:17 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:13 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:02:10 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:01:58 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:01:46 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:01:39 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | -0.084 |  |
| 2026-09-18 08:01:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:00:59 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.077 |  |
| 2026-09-18 08:00:57 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:45:05 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.101 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 08:01:39 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | -0.084 |  |
| 2026-09-18 08:07:29 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-18 08:06:28 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 08:01:58 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:40 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:48 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:03:15 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:05:39 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:17 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:06:42 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:08:13 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:03:57 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:01:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:04:06 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:39 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:06:07 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:09:43 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:00:57 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:10 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:05:21 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:04:11 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:02:13 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:04:27 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:01:46 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:03:32 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:05:26 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-09-18 08:02:59 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-09-18 07:01:44 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.021 |  |
| 2026-09-18 08:02:41 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.030 |  |
| 2026-09-18 08:04:21 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.035 |  |
| 2026-09-18 08:08:37 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.037 |  |
| 2026-09-18 07:01:09 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-09-18 08:03:43 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | -0.044 |  |
| 2026-09-18 08:05:24 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.075 |  |
| 2026-09-18 08:00:59 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.077 |  |
| 2026-09-18 08:08:51 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)