# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_15:04:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 15:04:52 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.041 |  |
| 2026-11-23 15:04:50 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | -0.046 |  |
| 2026-11-23 15:04:43 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:04:37 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-23 15:04:31 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-11-23 15:04:12 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:04:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:03:54 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 15:03:52 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:03:46 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:03:35 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:03:33 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.058 |  |
| 2026-11-23 15:03:32 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.031 |  |
| 2026-11-23 15:03:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-23 15:03:15 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.039 |  |
| 2026-11-23 15:03:12 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:03:08 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-11-23 15:02:57 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:02:50 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:02:29 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:02:26 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 15:02:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 15:02:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.096 |  |
| 2026-11-23 15:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:01:55 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.033 |  |
| 2026-11-23 15:01:50 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-23 15:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.033 |  |
| 2026-11-23 15:01:20 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:01:16 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:01:16 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:01:15 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 15:00:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.020 |  |
| 2026-11-23 15:00:10 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:35:55 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.026 |  |
| 2026-11-23 14:30:13 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:17:46 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 15:03:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-23 15:04:37 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-23 15:01:50 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-23 15:01:15 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 15:02:26 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 15:02:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 14:00:59 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 15:03:54 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 15:00:10 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:01:16 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:02:57 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:02:50 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:02:29 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:01:16 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:04:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:04:43 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:05:19 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:01:20 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:03:52 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 15:03:46 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:04:12 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:03:35 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:03:12 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-23 15:04:31 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-11-23 15:03:08 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-11-23 15:00:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 14:35:55 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.026 |  |
| 2026-11-23 15:03:32 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.031 |  |
| 2026-11-23 15:01:55 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.033 |  |
| 2026-11-23 15:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.033 |  |
| 2026-11-23 15:03:15 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.039 |  |
| 2026-11-23 14:02:15 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.040 |  |
| 2026-11-23 15:04:52 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.041 |  |
| 2026-11-23 15:04:50 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | -0.046 |  |
| 2026-11-23 15:03:33 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.058 |  |
| 2026-11-23 15:02:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.096 |  |
| 2026-11-23 14:02:12 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)