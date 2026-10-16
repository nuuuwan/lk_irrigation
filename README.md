# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_13:08:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,491 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 13:08:45 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.072 |  |
| 2026-10-16 13:07:45 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-10-16 13:05:46 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:05:25 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:05:19 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.039 |  |
| 2026-10-16 13:05:18 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-10-16 13:05:18 | Glencourse (Kelani Ganga) | 11.09 | 🟢 Normal | -0.029 |  |
| 2026-10-16 13:04:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:04:43 | Panadugama (Nilwala Ganga) | 6.58 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-16 13:04:18 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.039 |  |
| 2026-10-16 13:03:48 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:03:42 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-10-16 13:03:32 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-16 13:03:30 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 13:03:29 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:03:26 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-16 13:03:13 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:03:08 | Ellagawa (Kalu Ganga) | 7.42 | 🟢 Normal | -0.021 |  |
| 2026-10-16 13:03:01 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:02:57 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:02:57 | Thawalama (Gin Ganga) | 3.06 | 🟢 Normal | -0.111 |  |
| 2026-10-16 13:02:18 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 13:02:16 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-10-16 13:02:08 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-16 13:01:46 | Pitabeddara (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.093 |  |
| 2026-10-16 13:01:46 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:01:40 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 13:01:23 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-10-16 13:01:11 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 13:00:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:00:50 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 13:02:18 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 13:04:43 | Panadugama (Nilwala Ganga) | 6.58 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-16 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 13:05:19 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.039 |  |
| 2026-10-16 13:03:32 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-16 13:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 13:02:08 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-16 13:01:11 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 13:03:30 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 12:01:27 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 13:02:57 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:03:01 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:04:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:03:29 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:05:46 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:00:57 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:01:40 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-16 13:05:25 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:03:48 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:01:46 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-16 13:03:13 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-10-16 12:00:19 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-10-16 13:07:45 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-10-16 13:05:18 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-10-16 13:03:26 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-16 13:03:42 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-10-16 12:00:11 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-10-16 13:03:08 | Ellagawa (Kalu Ganga) | 7.42 | 🟢 Normal | -0.021 |  |
| 2026-10-16 13:01:23 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-10-16 12:16:12 | Urawa (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.025 |  |
| 2026-10-16 13:05:18 | Glencourse (Kelani Ganga) | 11.09 | 🟢 Normal | -0.029 |  |
| 2026-10-16 13:02:16 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-10-16 13:00:50 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.032 |  |
| 2026-10-16 13:04:18 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.039 |  |
| 2026-10-16 12:08:35 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.066 |  |
| 2026-10-16 13:08:45 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.072 |  |
| 2026-10-16 13:01:46 | Pitabeddara (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.093 |  |
| 2026-10-16 13:02:57 | Thawalama (Gin Ganga) | 3.06 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)