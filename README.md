# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_03:06:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,378 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 03:06:56 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-13 03:06:44 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-10-13 03:06:31 | Urawa (Nilwala Ganga) | 2.51 | 🟡 Alert | -0.292 |  |
| 2026-10-13 03:06:27 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-10-13 03:06:18 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:06:06 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 03:05:41 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:05:18 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-13 03:04:41 | Pitabeddara (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-13 03:04:33 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 03:04:32 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | 12.000 | 🔺 Rising |
| 2026-10-13 03:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.058 |  |
| 2026-10-13 03:04:08 | Panadugama (Nilwala Ganga) | 6.07 | 🟠 Minor Flood | 12.000 | 🔺 Rising |
| 2026-10-13 03:04:01 | Ellagawa (Kalu Ganga) | 6.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 03:03:30 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.020 |  |
| 2026-10-13 03:03:15 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-10-13 03:03:06 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:02:50 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-10-13 03:02:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.005 |  |
| 2026-10-13 03:02:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:02:38 | Panadugama (Nilwala Ganga) | 5.92 | 🟡 Alert | 12.000 | 🔺 Rising |
| 2026-10-13 03:02:10 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-13 03:01:41 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-13 03:01:40 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:01:27 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-10-13 03:01:26 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-13 03:01:17 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.117 |  |
| 2026-10-13 03:00:28 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 03:04:32 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | 12.000 | 🔺 Rising |
| 2026-10-13 02:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-13 03:06:31 | Urawa (Nilwala Ganga) | 2.51 | 🟡 Alert | -0.292 |  |
| 2026-10-13 02:11:44 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-10-13 03:04:41 | Pitabeddara (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-13 03:05:18 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-13 02:04:31 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-13 01:18:47 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-13 03:06:06 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 03:04:01 | Ellagawa (Kalu Ganga) | 6.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 03:06:56 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-13 03:04:33 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 03:02:50 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-10-13 03:03:06 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:00:28 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:06:18 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:01:40 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:05:41 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:02:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 02:01:32 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:02:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.005 |  |
| 2026-10-13 03:06:27 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-10-13 03:01:41 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-13 03:01:26 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-13 01:05:27 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-13 01:03:43 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-13 01:00:24 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.011 |  |
| 2026-10-13 02:10:07 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-10-13 03:03:15 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-10-13 03:02:10 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-13 03:03:30 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.020 |  |
| 2026-10-13 03:01:27 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-10-13 03:06:44 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-10-13 03:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.058 |  |
| 2026-10-13 03:01:17 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)