# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_15:10:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,273 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 15:10:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:10:03 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:08:32 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-11-18 15:06:58 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | -0.029 |  |
| 2026-11-18 15:06:31 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.048 |  |
| 2026-11-18 15:06:00 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:05:58 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:05:40 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:05:14 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-11-18 15:05:12 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.037 |  |
| 2026-11-18 15:04:30 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:04:27 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:04:13 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 15:04:12 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.021 |  |
| 2026-11-18 15:04:07 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-11-18 15:03:54 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:46 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:03:32 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:30 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:03:29 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:03:19 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:00 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.100 |  |
| 2026-11-18 15:02:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-18 15:02:23 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.034 |  |
| 2026-11-18 15:02:17 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-18 15:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:14 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:02:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:09 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:08 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:01:50 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:01:47 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:01:21 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-18 15:01:20 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 15:01:18 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:01:15 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:00:44 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 15:01:21 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-18 15:02:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-18 15:04:13 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 15:01:20 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 15:02:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:54 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:01:47 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:09 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:00:44 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:00 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:19 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:01:50 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:06:00 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:03:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:04:27 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:01:15 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:10:03 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:02:08 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:04:30 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:10:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:05:40 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 15:08:32 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-11-18 15:05:58 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:03:46 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:03:29 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:01:18 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:03:30 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:02:14 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-18 15:05:14 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-11-18 14:23:32 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-11-18 15:04:07 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-11-18 15:02:17 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-18 15:04:12 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.021 |  |
| 2026-11-18 15:06:58 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | -0.029 |  |
| 2026-11-18 15:02:23 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.034 |  |
| 2026-11-18 15:05:12 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.037 |  |
| 2026-11-18 15:06:31 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.048 |  |
| 2026-11-18 15:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)