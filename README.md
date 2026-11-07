# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_12:04:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 12:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | -0.029 |  |
| 2026-11-07 12:03:59 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-07 12:03:52 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-11-07 12:03:35 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:03:11 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:05 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.150 |  |
| 2026-11-07 12:03:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-07 12:03:01 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:02:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.054 |  |
| 2026-11-07 12:02:38 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:02:37 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:37 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.090 |  |
| 2026-11-07 12:02:31 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-07 12:02:27 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:05 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:02 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 12:01:50 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.142 |  |
| 2026-11-07 12:01:50 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.033 |  |
| 2026-11-07 12:01:48 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-07 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:36 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:17 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.103 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 11:11:14 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | -0.018 |  |
| 2026-11-07 12:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | -0.029 |  |
| 2026-11-07 12:03:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-07 11:05:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-07 12:03:59 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-07 12:02:31 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-07 12:02:02 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 12:02:05 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:27 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:03:35 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:02:01 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:05:29 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:37 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:03:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:05:11 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:13:52 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:03:30 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:01 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:36 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:11 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:03:11 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.013 |  |
| 2026-11-07 12:03:52 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-11-07 12:01:48 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-07 12:02:38 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:01:17 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-11-07 11:01:10 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:01:50 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.033 |  |
| 2026-11-07 11:05:07 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.050 |  |
| 2026-11-07 12:02:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.054 |  |
| 2026-11-07 12:02:37 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.090 |  |
| 2026-11-07 11:06:59 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.096 |  |
| 2026-11-07 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.103 |  |
| 2026-11-07 11:12:27 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.126 |  |
| 2026-11-07 12:01:50 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.142 |  |
| 2026-11-07 12:03:05 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.150 |  |
| 2026-11-07 11:04:19 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.216 |  |
| 2026-11-07 11:05:09 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.235 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)