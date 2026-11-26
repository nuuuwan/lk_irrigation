# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_06:08:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 06:08:59 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.046 |  |
| 2026-11-26 06:08:49 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-26 06:07:16 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.077 |  |
| 2026-11-26 06:06:33 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-11-26 06:05:50 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.046 |  |
| 2026-11-26 06:05:08 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-26 06:05:08 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.120 |  |
| 2026-11-26 06:04:56 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-26 06:04:51 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-26 06:04:44 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-26 06:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-26 06:04:09 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-11-26 06:03:44 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-26 06:03:36 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.066 |  |
| 2026-11-26 06:03:30 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.157 |  |
| 2026-11-26 06:03:25 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.002 |  |
| 2026-11-26 06:03:14 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.109 |  |
| 2026-11-26 06:03:06 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 06:02:49 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-26 06:02:47 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-26 06:02:38 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-26 06:02:36 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-26 06:02:34 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-26 06:02:27 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-26 06:02:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-11-26 06:02:01 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.034 |  |
| 2026-11-26 06:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-26 06:01:52 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.068 |  |
| 2026-11-26 06:01:48 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.059 |  |
| 2026-11-26 06:01:32 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.103 |  |
| 2026-11-26 06:01:24 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.071 |  |
| 2026-11-26 06:01:23 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 06:01:17 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-26 06:00:46 | Moragaswewa (Deduru Oya) | 3.45 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-11-26 06:00:18 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 06:02:34 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-26 06:00:46 | Moragaswewa (Deduru Oya) | 3.45 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-11-26 06:01:17 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-26 06:04:44 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-26 06:03:44 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-26 06:02:49 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-26 06:02:38 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-26 06:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-26 06:08:49 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-26 06:03:06 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 06:01:23 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 06:02:47 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-26 06:05:08 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-26 06:02:27 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-26 06:03:25 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.002 |  |
| 2026-11-26 06:04:56 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-26 06:00:18 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-11-26 06:04:09 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-11-26 06:04:51 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-26 06:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-26 06:02:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 06:06:33 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-11-26 06:02:36 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-26 06:02:01 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.034 |  |
| 2026-11-26 06:08:59 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.046 |  |
| 2026-11-26 06:05:50 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.046 |  |
| 2026-11-26 06:01:48 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.059 |  |
| 2026-11-26 06:03:36 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.066 |  |
| 2026-11-26 06:01:52 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.068 |  |
| 2026-11-26 06:01:24 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.071 |  |
| 2026-11-26 06:07:16 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.077 |  |
| 2026-11-26 06:01:32 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.103 |  |
| 2026-11-26 06:03:14 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.109 |  |
| 2026-11-26 06:05:08 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.120 |  |
| 2026-11-26 06:03:30 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)