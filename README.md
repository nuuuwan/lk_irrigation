# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_22:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,101 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 22:11:08 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-13 22:10:57 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:06:06 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-10-13 22:06:04 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-10-13 22:05:58 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-10-13 22:05:53 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-13 22:05:40 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:05:29 | Magura (Kalu Ganga) | 4.56 | 🟡 Alert | 0.337 | 🔺 Rising |
| 2026-10-13 22:05:22 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:04:48 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-13 22:04:47 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:04:43 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:04:19 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-13 22:03:18 | Urawa (Nilwala Ganga) | 2.61 | 🟡 Alert | -0.092 |  |
| 2026-10-13 22:03:07 | Moraketiya (Walawe Ganga) | 1.91 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-13 22:03:04 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 22:03:01 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:02:56 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 22:02:42 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:02:42 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:02:22 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.066 |  |
| 2026-10-13 22:02:16 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-10-13 22:02:09 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-13 22:02:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:02:07 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-13 22:02:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:01:14 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:01:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:01:10 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-13 22:01:08 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 22:01:07 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:00:59 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 22:00:58 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:00:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 22:05:29 | Magura (Kalu Ganga) | 4.56 | 🟡 Alert | 0.337 | 🔺 Rising |
| 2026-10-13 22:02:16 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-10-13 22:04:19 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-13 22:00:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.021 |  |
| 2026-10-13 22:03:18 | Urawa (Nilwala Ganga) | 2.61 | 🟡 Alert | -0.092 |  |
| 2026-10-13 21:02:33 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.875 | 🔺 Rising |
| 2026-10-13 22:02:09 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-13 22:05:58 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-10-13 22:03:07 | Moraketiya (Walawe Ganga) | 1.91 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-13 22:06:06 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-10-13 22:05:53 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-13 22:11:08 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-13 22:01:08 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 22:01:10 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-13 22:02:56 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 22:04:48 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-13 22:00:59 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 22:03:04 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 22:02:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:01:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:04:43 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:01:07 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:02:42 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:03:01 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:10:57 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:05:22 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:05:40 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:00:58 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:02:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:01:14 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:02:42 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:04:47 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-10-13 22:06:04 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-10-13 22:02:07 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-13 22:02:22 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)