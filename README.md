# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_07:16:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,360 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 07:16:51 | Baddegama (Gin Ganga) | 4.66 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 07:12:14 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.053 |  |
| 2026-09-25 07:08:14 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.030 |  |
| 2026-09-25 07:07:57 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | -0.027 |  |
| 2026-09-25 07:06:57 | Putupaula (Kalu Ganga) | 2.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-25 07:06:41 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-09-25 07:06:40 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:06:24 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-25 07:06:18 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:05:54 | Norwood (Kelani Ganga) | 1.59 | 🟡 Alert | -0.111 |  |
| 2026-09-25 07:05:51 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 07:05:26 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:04:56 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-09-25 07:04:54 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-09-25 07:04:37 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:04:32 | Rathnapura (Kalu Ganga) | 6.44 | 🟡 Alert | -0.020 |  |
| 2026-09-25 07:04:16 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.019 |  |
| 2026-09-25 07:04:11 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-25 07:04:11 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 07:04:07 | Thawalama (Gin Ganga) | 4.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-25 07:03:58 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-25 07:03:39 | Nawalapitiya (Mahaweli Ganga) | 3.07 | 🟢 Normal | -0.084 |  |
| 2026-09-25 07:03:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:03:06 | Glencourse (Kelani Ganga) | 14.45 | 🟢 Normal | -0.061 |  |
| 2026-09-25 07:02:51 | Deraniyagala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.074 |  |
| 2026-09-25 07:02:33 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:02:30 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.95 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-25 07:02:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-09-25 07:02:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:02:04 | Panadugama (Nilwala Ganga) | 6.56 | 🟠 Minor Flood | -0.016 |  |
| 2026-09-25 07:01:59 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-25 07:01:44 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | -0.001 |  |
| 2026-09-25 07:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:01:11 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:00:54 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:00:46 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.050 |  |
| 2026-09-25 07:00:43 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 07:00:07 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 07:04:11 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-25 07:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.95 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-25 07:16:51 | Baddegama (Gin Ganga) | 4.66 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 07:02:04 | Panadugama (Nilwala Ganga) | 6.56 | 🟠 Minor Flood | -0.016 |  |
| 2026-09-25 07:04:07 | Thawalama (Gin Ganga) | 4.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-25 07:04:32 | Rathnapura (Kalu Ganga) | 6.44 | 🟡 Alert | -0.020 |  |
| 2026-09-25 07:07:57 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | -0.027 |  |
| 2026-09-25 07:05:54 | Norwood (Kelani Ganga) | 1.59 | 🟡 Alert | -0.111 |  |
| 2026-09-25 07:06:24 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-25 07:04:11 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 07:03:58 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-25 07:00:43 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 07:05:51 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 07:06:57 | Putupaula (Kalu Ganga) | 2.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-25 07:02:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:01:11 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:03:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:04:37 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:06:06 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:00:07 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:02:30 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:05:26 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:06:40 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:00:54 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:02:33 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 07:01:44 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | -0.001 |  |
| 2026-09-25 07:04:56 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-09-25 07:01:59 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-25 07:04:16 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.019 |  |
| 2026-09-25 07:08:14 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.030 |  |
| 2026-09-25 07:02:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-09-25 07:00:46 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.050 |  |
| 2026-09-25 07:04:54 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-09-25 07:12:14 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.053 |  |
| 2026-09-25 07:06:41 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-09-25 07:03:06 | Glencourse (Kelani Ganga) | 14.45 | 🟢 Normal | -0.061 |  |
| 2026-09-25 07:02:51 | Deraniyagala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.074 |  |
| 2026-09-25 07:03:39 | Nawalapitiya (Mahaweli Ganga) | 3.07 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)