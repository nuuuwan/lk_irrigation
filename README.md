# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_15:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,397 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 15:03:07 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-11-07 15:03:05 | Moragaswewa (Deduru Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-07 15:03:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-07 15:02:58 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2026-11-07 15:02:58 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:02:57 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:02:56 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.139 |  |
| 2026-11-07 15:02:45 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.019 |  |
| 2026-11-07 15:02:28 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-07 15:01:57 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:01:54 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 15:01:36 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 15:01:02 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:01:02 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.119 |  |
| 2026-11-07 15:00:50 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 15:00:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 14:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.031 |  |
| 2026-11-07 14:01:53 | Dunamale (Aththanagalu Oya) | 3.74 | 🟡 Alert | -0.063 |  |
| 2026-11-07 15:02:28 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-07 15:01:54 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 14:03:31 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 15:00:50 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 15:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 14:02:01 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 14:04:01 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:00:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:01:57 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 14:03:49 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:02:57 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:01:02 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-07 14:02:33 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:02:58 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:06:35 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-07 14:02:47 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-07 14:01:35 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:01:36 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:02:58 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2026-11-07 14:04:43 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.016 |  |
| 2026-11-07 15:02:45 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.019 |  |
| 2026-11-07 15:03:05 | Moragaswewa (Deduru Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-07 15:03:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-07 14:02:30 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-07 14:01:37 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.023 |  |
| 2026-11-07 14:08:20 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.036 |  |
| 2026-11-07 15:03:07 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-11-07 14:01:48 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.040 |  |
| 2026-11-07 14:05:07 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.050 |  |
| 2026-11-07 14:02:25 | Giriulla (Maha Oya) | 2.38 | 🟢 Normal | -0.070 |  |
| 2026-11-07 14:06:56 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.073 |  |
| 2026-11-07 14:14:24 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.082 |  |
| 2026-11-07 14:05:17 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.112 |  |
| 2026-11-07 15:01:02 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.119 |  |
| 2026-11-07 15:02:56 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.139 |  |
| 2026-11-07 14:05:29 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)