# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_09:06:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 09:06:34 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:06:07 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:06:04 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 09:05:44 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:05:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.092 |  |
| 2026-11-16 09:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 09:04:41 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:04:40 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-16 09:04:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:04:24 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:03:31 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:03:21 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:03:18 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-11-16 09:03:18 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:03:02 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:02:49 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:02:36 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 09:02:25 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:02:13 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:02:09 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:02:09 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:01:57 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | -0.031 |  |
| 2026-11-16 09:01:50 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 09:01:49 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:01:42 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:00:54 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:00:48 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 09:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 08:25:07 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 09:03:18 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-11-16 08:06:17 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-16 09:00:48 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-16 09:02:36 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 09:01:50 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 09:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 09:06:04 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 09:01:49 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:04:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:03:18 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-16 08:25:07 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 08:06:00 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:06:07 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:04:24 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 08:09:19 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:06:34 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:03:21 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:03:02 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:02:25 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:05:44 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 08:00:33 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 08:04:59 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:02:09 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-16 09:02:13 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-16 08:13:16 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.009 |  |
| 2026-11-16 09:04:41 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:03:31 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:00:54 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:02:49 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:01:42 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:02:09 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-16 09:04:40 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-16 08:03:52 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-16 06:10:46 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.022 |  |
| 2026-11-16 08:14:48 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.030 |  |
| 2026-11-16 09:01:57 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | -0.031 |  |
| 2026-11-16 08:04:27 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.048 |  |
| 2026-11-16 09:05:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)