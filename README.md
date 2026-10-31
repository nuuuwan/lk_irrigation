# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_17:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 17:14:30 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-31 17:12:25 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:12:09 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-31 17:10:31 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:10:23 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-31 17:09:15 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:09:01 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.027 |  |
| 2026-10-31 17:08:47 | Galgamuwa (Mee Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:08:09 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:06:08 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.030 |  |
| 2026-10-31 17:05:59 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:05:43 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.092 |  |
| 2026-10-31 17:05:34 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:05:30 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:04:56 | Putupaula (Kalu Ganga) | 1.89 | 🟢 Normal | -0.070 |  |
| 2026-10-31 17:04:20 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:04:13 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.059 |  |
| 2026-10-31 17:03:48 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.031 |  |
| 2026-10-31 17:03:48 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:03:46 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -0.112 |  |
| 2026-10-31 17:03:14 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.070 |  |
| 2026-10-31 17:03:11 | Hanwella (Kelani Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-10-31 17:03:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:48 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 17:02:47 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:27 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:09 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-31 17:02:08 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:01:32 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-10-31 17:01:31 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 17:01:28 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 17:01:16 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.014 |  |
| 2026-10-31 17:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:00:38 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:00:37 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:00:19 | Thalgahagoda (Nilwala Ganga) | 1.59 | 🟡 Alert | -0.010 |  |
| 2026-10-31 17:00:11 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:59:50 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 17:00:19 | Thalgahagoda (Nilwala Ganga) | 1.59 | 🟡 Alert | -0.010 |  |
| 2026-10-31 17:02:09 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-31 17:01:28 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 17:02:48 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 17:01:31 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 17:14:30 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-31 17:10:23 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-31 17:09:15 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:27 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:00:37 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:47 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:03:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:10:31 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:05:59 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:08:46 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:00:38 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:08 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:03:46 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:05:30 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:08:47 | Galgamuwa (Mee Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:03:48 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:08:09 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:05:34 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:12:25 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:00:11 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:04:20 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:01:16 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.014 |  |
| 2026-10-31 17:12:09 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-31 17:09:01 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.027 |  |
| 2026-10-31 17:01:32 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-10-31 17:03:11 | Hanwella (Kelani Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-10-31 17:06:08 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.030 |  |
| 2026-10-31 17:03:48 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.031 |  |
| 2026-10-31 17:04:13 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.059 |  |
| 2026-10-31 17:04:56 | Putupaula (Kalu Ganga) | 1.89 | 🟢 Normal | -0.070 |  |
| 2026-10-31 17:03:14 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.070 |  |
| 2026-10-31 17:05:43 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.092 |  |
| 2026-10-31 17:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)