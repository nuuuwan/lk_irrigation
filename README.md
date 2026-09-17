# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_21:15:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 21:15:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-09-17 21:13:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:12:30 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-17 21:07:56 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 21:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 21:07:23 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 21:06:55 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:06:34 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-17 21:06:21 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:06:07 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:06:00 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | -0.011 |  |
| 2026-09-17 21:05:41 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-17 21:05:17 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:04:45 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:04:23 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:04:13 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | -0.019 |  |
| 2026-09-17 21:03:44 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-17 21:03:42 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 21:03:27 | Baddegama (Gin Ganga) | 3.54 | 🟡 Alert | -0.011 |  |
| 2026-09-17 21:03:21 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:03:13 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:03:00 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:02:59 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-17 21:02:53 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:02:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |
| 2026-09-17 21:02:38 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.168 |  |
| 2026-09-17 21:02:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:02:18 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-09-17 21:02:17 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:02:08 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:02:06 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:01:59 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-17 21:01:31 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:01:20 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:01:19 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 21:02:59 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-17 21:03:27 | Baddegama (Gin Ganga) | 3.54 | 🟡 Alert | -0.011 |  |
| 2026-09-17 21:05:41 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-17 21:03:44 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-17 21:06:34 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-17 21:12:30 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-17 21:01:59 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-17 21:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 21:07:56 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 21:03:42 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 21:07:23 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:02:17 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:03:00 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:02:08 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:06:07 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:01:31 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:08:20 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:13:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:01:20 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:03:21 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:04:45 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:06:55 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:01:19 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:02:53 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:15:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-09-17 21:05:17 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:02:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:02:06 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:04:23 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:06:21 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-17 21:06:00 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | -0.011 |  |
| 2026-09-17 21:04:13 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | -0.019 |  |
| 2026-09-17 21:02:18 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-09-17 21:02:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |
| 2026-09-17 21:02:38 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)