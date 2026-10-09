# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_19:25:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 19:25:51 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.052 |  |
| 2026-10-09 19:13:57 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-09 19:11:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:11:20 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-09 19:10:38 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.017 |  |
| 2026-10-09 19:07:38 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2026-10-09 19:07:33 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.009 |  |
| 2026-10-09 19:07:31 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.073 |  |
| 2026-10-09 19:07:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:07:14 | Holombuwa (Kelani Ganga) | 1.80 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-09 19:06:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.087 |  |
| 2026-10-09 19:06:32 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.028 |  |
| 2026-10-09 19:06:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:05:39 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-10-09 19:04:50 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 19:04:40 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.214 |  |
| 2026-10-09 19:04:17 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 19:04:15 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-09 19:04:11 | Giriulla (Maha Oya) | 3.06 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-09 19:04:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.190 |  |
| 2026-10-09 19:03:48 | Dunamale (Aththanagalu Oya) | 2.05 | 🟢 Normal | -0.108 |  |
| 2026-10-09 19:03:40 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | 1.137 | 🔺 Rising |
| 2026-10-09 19:03:25 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-09 19:03:15 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-09 19:02:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:02:28 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.020 |  |
| 2026-10-09 19:02:19 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | 0.571 | 🔺 Rising |
| 2026-10-09 19:02:08 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-09 19:01:52 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 19:01:46 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | -0.043 |  |
| 2026-10-09 19:01:11 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 19:01:09 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.043 |  |
| 2026-10-09 19:00:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.48 | 🟢 Normal | -0.053 |  |
| 2026-10-09 19:00:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-09 19:00:14 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | 0.617 | 🔺 Rising |
| 2026-10-09 19:00:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 19:25:51 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.052 |  |
| 2026-10-09 19:03:40 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | 1.137 | 🔺 Rising |
| 2026-10-09 19:00:14 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | 0.617 | 🔺 Rising |
| 2026-10-09 19:02:19 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | 0.571 | 🔺 Rising |
| 2026-10-09 19:05:39 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-10-09 19:07:14 | Holombuwa (Kelani Ganga) | 1.80 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-09 19:11:20 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-09 19:04:11 | Giriulla (Maha Oya) | 3.06 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-09 19:00:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-09 19:03:25 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-09 19:13:57 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-09 19:04:50 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 19:02:08 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-09 19:04:17 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 19:01:11 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 19:01:52 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 19:11:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:02:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:07:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:00:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:06:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 19:07:33 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.009 |  |
| 2026-10-09 19:04:15 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-09 19:10:38 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.017 |  |
| 2026-10-09 19:07:38 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2026-10-09 19:02:28 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.020 |  |
| 2026-10-09 19:03:15 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-09 19:06:32 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.028 |  |
| 2026-10-09 19:01:09 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.043 |  |
| 2026-10-09 19:01:46 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | -0.043 |  |
| 2026-10-09 19:00:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.48 | 🟢 Normal | -0.053 |  |
| 2026-10-09 19:07:31 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.073 |  |
| 2026-10-09 19:06:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.087 |  |
| 2026-10-09 19:03:48 | Dunamale (Aththanagalu Oya) | 2.05 | 🟢 Normal | -0.108 |  |
| 2026-10-09 19:04:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.190 |  |
| 2026-10-09 19:04:40 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)