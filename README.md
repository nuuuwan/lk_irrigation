# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_11:06:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,895 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 11:06:43 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:06:34 | Hanwella (Kelani Ganga) | 6.32 | 🟢 Normal | -0.104 |  |
| 2026-09-21 11:06:18 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-21 11:06:06 | Nagalagam Street (Kelani Ganga) | 1.11 | 🟢 Normal | -0.014 |  |
| 2026-09-21 11:06:00 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:05:59 | Glencourse (Kelani Ganga) | 13.47 | 🟢 Normal | -0.216 |  |
| 2026-09-21 11:05:54 | Magura (Kalu Ganga) | 5.53 | 🟡 Alert | -0.022 |  |
| 2026-09-21 11:05:46 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:05:22 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-09-21 11:05:18 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.091 |  |
| 2026-09-21 11:05:16 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.049 |  |
| 2026-09-21 11:05:15 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.042 |  |
| 2026-09-21 11:05:13 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-21 11:05:06 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | -0.049 |  |
| 2026-09-21 11:04:41 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-09-21 11:04:32 | Baddegama (Gin Ganga) | 3.95 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 11:04:30 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-21 11:04:28 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.107 |  |
| 2026-09-21 11:04:20 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-09-21 11:03:54 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 11:03:23 | Rathnapura (Kalu Ganga) | 5.73 | 🟡 Alert | -0.040 |  |
| 2026-09-21 11:03:14 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.82 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-09-21 11:02:46 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 11:02:40 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-21 11:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-21 11:02:27 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-21 11:02:24 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-21 11:02:20 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-09-21 11:01:56 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:01:41 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.043 |  |
| 2026-09-21 11:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:01:24 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:00:59 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:00:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.010 |  |
| 2026-09-21 11:00:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:58:45 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 11:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.82 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-09-21 11:04:32 | Baddegama (Gin Ganga) | 3.95 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 11:03:54 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 11:05:54 | Magura (Kalu Ganga) | 5.53 | 🟡 Alert | -0.022 |  |
| 2026-09-21 11:03:23 | Rathnapura (Kalu Ganga) | 5.73 | 🟡 Alert | -0.040 |  |
| 2026-09-21 11:05:15 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.042 |  |
| 2026-09-21 11:02:40 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-21 11:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-21 11:02:24 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-21 11:06:18 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-21 11:04:30 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-21 11:02:46 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 11:01:24 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:06:43 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 10:58:45 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:05:46 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:03:14 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:06:00 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:00:59 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:00:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:01:56 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 11:04:20 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-09-21 11:05:13 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-21 10:04:39 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-21 11:00:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.010 |  |
| 2026-09-21 10:06:17 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2026-09-21 11:06:06 | Nagalagam Street (Kelani Ganga) | 1.11 | 🟢 Normal | -0.014 |  |
| 2026-09-21 11:02:27 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-21 11:04:41 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-09-21 11:02:20 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-09-21 11:01:41 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.043 |  |
| 2026-09-21 11:05:16 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.049 |  |
| 2026-09-21 11:05:06 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | -0.049 |  |
| 2026-09-21 11:05:18 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.091 |  |
| 2026-09-21 11:05:22 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-09-21 11:06:34 | Hanwella (Kelani Ganga) | 6.32 | 🟢 Normal | -0.104 |  |
| 2026-09-21 11:04:28 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.107 |  |
| 2026-09-21 11:05:59 | Glencourse (Kelani Ganga) | 13.47 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)