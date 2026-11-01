# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_22:02:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 22:02:58 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-11-01 22:02:52 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:02:44 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:02:21 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-01 22:02:18 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 22:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:01:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:01:12 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.021 |  |
| 2026-11-01 22:01:03 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-01 22:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.061 |  |
| 2026-11-01 22:00:23 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.080 |  |
| 2026-11-01 21:18:10 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.000 |  |
| 2026-11-01 21:16:30 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.096 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 21:18:10 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.000 |  |
| 2026-11-01 22:02:58 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-11-01 21:01:25 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-11-01 21:08:28 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-01 21:05:24 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-01 21:16:30 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-01 21:01:28 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-01 21:01:38 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-01 21:05:13 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 21:08:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-01 22:02:18 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 22:02:21 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-01 21:02:21 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 21:00:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:02:52 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 22:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:40 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:03:32 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:54 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:13 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:02:18 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:10:39 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:09:11 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 21:10:47 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.005 |  |
| 2026-11-01 21:04:21 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:02:44 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 21:05:50 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:01:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-01 22:01:03 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-01 21:09:44 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-11-01 21:06:44 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-11-01 22:01:12 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.021 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 21:06:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.058 |  |
| 2026-11-01 22:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.061 |  |
| 2026-11-01 21:01:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.065 |  |
| 2026-11-01 22:00:23 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)