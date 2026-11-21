# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_07:04:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 07:04:14 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 07:04:04 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-11-21 07:03:55 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.062 |  |
| 2026-11-21 07:03:43 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.083 |  |
| 2026-11-21 07:03:36 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-11-21 07:03:27 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.677 |  |
| 2026-11-21 07:03:15 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-11-21 07:03:01 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-21 07:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-21 07:02:54 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-21 07:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.041 |  |
| 2026-11-21 07:02:31 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.118 |  |
| 2026-11-21 07:01:56 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:24 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 07:01:24 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-21 07:01:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:07 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-21 07:00:46 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-21 07:00:43 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:00:43 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:00:07 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 07:04:04 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-11-21 07:03:15 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-11-21 07:02:54 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-21 07:03:01 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-21 07:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-21 07:01:07 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-21 06:03:24 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-21 06:03:00 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-21 07:04:14 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 06:04:41 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-21 06:08:20 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-21 07:01:24 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 07:00:07 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 06:00:59 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 07:00:46 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-21 06:02:41 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 06:06:45 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-21 06:04:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:00:43 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:00:43 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:56 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:24 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-21 06:01:58 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-11-21 06:08:17 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.037 |  |
| 2026-11-21 07:03:36 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-11-21 07:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.041 |  |
| 2026-11-21 06:01:00 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-11-21 06:01:16 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.053 |  |
| 2026-11-21 07:03:55 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.062 |  |
| 2026-11-21 07:03:43 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.083 |  |
| 2026-11-21 06:04:03 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.095 |  |
| 2026-11-21 06:03:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.101 |  |
| 2026-11-21 07:02:31 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.118 |  |
| 2026-11-21 06:08:03 | Urawa (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.128 |  |
| 2026-11-21 07:03:27 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.677 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)