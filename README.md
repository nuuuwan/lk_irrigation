# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_06:25:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,116 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 06:25:08 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.043 |  |
| 2026-10-07 06:11:56 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-07 06:08:43 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-07 06:08:29 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:08:20 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-07 06:08:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-10-07 06:06:52 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:05:58 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.037 |  |
| 2026-10-07 06:05:55 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.078 |  |
| 2026-10-07 06:05:10 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.001 |  |
| 2026-10-07 06:04:47 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2026-10-07 06:04:33 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-07 06:04:31 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:04:25 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:03:57 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:03:02 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 06:03:00 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:02:53 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:02:43 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:02:33 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:02:21 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-07 06:02:21 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 06:02:14 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-07 06:02:13 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-10-07 06:01:59 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:01:53 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-07 06:01:51 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.046 |  |
| 2026-10-07 06:01:35 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.066 |  |
| 2026-10-07 06:01:33 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.083 |  |
| 2026-10-07 06:01:30 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:01:13 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-07 06:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:01:11 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | -2736.000 |  |
| 2026-10-07 06:01:10 | Pitabeddara (Nilwala Ganga) | 2.85 | 🟢 Normal | -2736.000 |  |
| 2026-10-07 06:01:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.025 |  |
| 2026-10-07 06:00:55 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:00:55 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 06:02:13 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | 0.015 | 🔺 Rising |
| 2026-10-07 06:04:33 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-07 06:08:43 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-07 06:01:13 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-07 06:01:53 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-07 06:02:14 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-07 06:02:21 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-07 06:08:20 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-07 06:11:56 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-07 06:02:21 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 06:00:55 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 06:03:02 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 06:05:10 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.001 |  |
| 2026-10-07 06:01:30 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:06:52 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:08:29 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:01:59 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:02:53 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:02:33 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:03:57 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:01:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-07 06:04:31 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:04:25 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:03:00 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:02:43 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-07 06:04:47 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2026-10-07 06:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.025 |  |
| 2026-10-07 06:05:58 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.037 |  |
| 2026-10-07 06:25:08 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.043 |  |
| 2026-10-07 06:01:51 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.046 |  |
| 2026-10-07 06:08:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-10-07 06:01:35 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.066 |  |
| 2026-10-07 06:05:55 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.078 |  |
| 2026-10-07 06:01:33 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.083 |  |
| 2026-10-07 06:01:11 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | -2736.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)