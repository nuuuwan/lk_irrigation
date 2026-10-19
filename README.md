# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_19:29:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,432 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 19:29:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.021 |  |
| 2026-10-19 19:19:17 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 19:12:58 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:10:53 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-10-19 19:08:56 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-10-19 19:08:30 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:08:27 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-10-19 19:08:06 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | -0.027 |  |
| 2026-10-19 19:07:42 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.055 |  |
| 2026-10-19 19:07:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.047 |  |
| 2026-10-19 19:07:25 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.031 |  |
| 2026-10-19 19:07:13 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-10-19 19:06:51 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.019 |  |
| 2026-10-19 19:04:54 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:04:54 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 19:04:13 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 19:04:12 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-19 19:04:12 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-19 19:04:05 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.049 |  |
| 2026-10-19 19:03:35 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-19 19:03:35 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.042 |  |
| 2026-10-19 19:03:30 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-19 19:03:29 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.028 |  |
| 2026-10-19 19:03:20 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-10-19 19:03:11 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-19 19:02:31 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 19:02:28 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-10-19 19:02:17 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.084 |  |
| 2026-10-19 19:02:07 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-19 19:02:03 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:02:02 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 19:02:02 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:01:25 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:01:00 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-10-19 19:00:35 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 19:19:17 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 19:03:29 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.028 |  |
| 2026-10-19 19:01:00 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-10-19 19:04:12 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-19 19:03:30 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-19 19:02:07 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-19 19:03:35 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-19 19:00:35 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-19 19:04:12 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-19 19:04:13 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 19:02:31 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 19:02:02 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 19:01:25 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:02:02 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:12:58 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:08:30 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:04:54 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:02:03 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 19:10:53 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-10-19 19:08:56 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-10-19 19:04:54 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 19:08:27 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-10-19 19:06:51 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.019 |  |
| 2026-10-19 19:07:13 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-10-19 19:03:11 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-19 19:03:20 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-10-19 19:29:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.021 |  |
| 2026-10-19 19:08:06 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | -0.027 |  |
| 2026-10-19 19:07:25 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.031 |  |
| 2026-10-19 19:03:35 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.042 |  |
| 2026-10-19 19:07:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.047 |  |
| 2026-10-19 19:04:05 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.049 |  |
| 2026-10-19 19:07:42 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.055 |  |
| 2026-10-19 19:02:28 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-19 19:02:17 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)