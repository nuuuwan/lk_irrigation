# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_19:02:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,942 measurements** from **39** stations.
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
| 2026-11-03 19:02:57 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:02:52 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:02:42 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.042 |  |
| 2026-11-03 19:02:29 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:02:13 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.070 |  |
| 2026-11-03 19:02:07 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.049 |  |
| 2026-11-03 19:01:55 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:01:41 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:01:25 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 19:01:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:00:40 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 19:00:24 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.252 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 18:09:18 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-11-03 18:08:03 | Urawa (Nilwala Ganga) | 1.75 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-03 18:01:22 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 18:03:16 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-03 19:01:25 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 18:06:40 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-03 19:00:40 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 18:03:38 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 18:04:39 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 18:03:47 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 18:00:17 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 18:08:40 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-03 18:01:15 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:02:52 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:02:29 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 19:01:41 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:04:26 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:02:14 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:02:07 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 19:02:57 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:01:55 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-03 19:01:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-03 18:02:17 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-11-03 18:04:16 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-03 17:10:38 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-11-03 18:01:36 | Moragaswewa (Deduru Oya) | 4.23 | 🟢 Normal | -0.021 |  |
| 2026-11-03 18:03:55 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.031 |  |
| 2026-11-03 18:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.039 |  |
| 2026-11-03 19:02:42 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.042 |  |
| 2026-11-03 19:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.049 |  |
| 2026-11-03 18:02:54 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-03 19:02:13 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.070 |  |
| 2026-11-03 18:02:37 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.075 |  |
| 2026-11-03 18:01:25 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.090 |  |
| 2026-11-03 18:08:11 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.090 |  |
| 2026-11-03 19:00:24 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.252 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)