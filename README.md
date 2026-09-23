# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_12:13:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,745 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 12:13:02 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-09-23 12:07:28 | Baddegama (Gin Ganga) | 3.76 | 🟡 Alert | -0.030 |  |
| 2026-09-23 12:07:27 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-09-23 12:06:55 | Glencourse (Kelani Ganga) | 12.78 | 🟢 Normal | -0.037 |  |
| 2026-09-23 12:06:54 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:05:32 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:05:25 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:05:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:04:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:04:45 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-09-23 12:04:43 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 12:04:35 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.030 |  |
| 2026-09-23 12:04:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 12:04:13 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:57 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.011 |  |
| 2026-09-23 12:03:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-23 12:03:23 | Hanwella (Kelani Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:13 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-09-23 12:03:10 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.042 |  |
| 2026-09-23 12:03:07 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:02:59 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:02:59 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:02:52 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-23 12:02:40 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | 0.000 |  |
| 2026-09-23 12:02:30 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:02:19 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.011 |  |
| 2026-09-23 12:02:15 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 12:02:07 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:02:05 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:01:57 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.019 |  |
| 2026-09-23 12:01:54 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 12:01:50 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:01:33 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.102 |  |
| 2026-09-23 12:01:28 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:00:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:00:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 12:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-23 12:02:40 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | 0.000 |  |
| 2026-09-23 12:07:28 | Baddegama (Gin Ganga) | 3.76 | 🟡 Alert | -0.030 |  |
| 2026-09-23 12:02:52 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-23 12:04:43 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 12:02:15 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 12:01:54 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 12:04:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 12:02:30 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:00:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:04:13 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:05:25 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:23 | Hanwella (Kelani Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:00:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:02:07 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:01:28 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:05:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:03:07 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:05:32 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:02:59 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 12:13:02 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-09-23 12:06:54 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:02:59 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:04:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:01:50 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:02:05 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-23 12:02:19 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.011 |  |
| 2026-09-23 12:03:57 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.011 |  |
| 2026-09-23 12:07:27 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-09-23 12:04:45 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-09-23 12:01:57 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.019 |  |
| 2026-09-23 12:04:35 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.030 |  |
| 2026-09-23 12:06:55 | Glencourse (Kelani Ganga) | 12.78 | 🟢 Normal | -0.037 |  |
| 2026-09-23 12:03:13 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-09-23 12:03:10 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.042 |  |
| 2026-09-23 12:01:33 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)