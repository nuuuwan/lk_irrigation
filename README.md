# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_02:05:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,746 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 02:05:05 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:05:05 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 02:04:54 | Thalgahagoda (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-09-29 02:04:15 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:04:06 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:04:05 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:03:33 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.033 |  |
| 2026-09-29 02:03:26 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.005 |  |
| 2026-09-29 02:03:21 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:03:17 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-09-29 02:02:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:02:14 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:02:13 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-29 02:02:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:02:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:51 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:48 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.060 |  |
| 2026-09-29 02:01:36 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:18 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:16 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 02:01:11 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-09-29 02:00:57 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:00:11 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-29 01:27:36 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 00:18:32 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.000 |  |
| 2026-09-29 02:01:11 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-09-29 02:02:13 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-29 02:00:11 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-29 02:01:16 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 02:05:05 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-28 23:00:40 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:00:48 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:02:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:04:15 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:12:37 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:04:06 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:02:14 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:36 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:00:57 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:02:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:03:21 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:02:21 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:05:05 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:08:49 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:18 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:51 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:01:48 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:03:26 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.005 |  |
| 2026-09-29 01:19:24 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-09-29 02:03:17 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 23:13:43 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-09-29 01:24:13 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.015 |  |
| 2026-09-29 02:04:54 | Thalgahagoda (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-09-29 01:13:29 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.025 |  |
| 2026-09-29 02:03:33 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.033 |  |
| 2026-09-29 02:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.060 |  |
| 2026-09-29 01:06:16 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | -0.120 |  |
| 2026-09-29 00:21:32 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.180 |  |
| 2026-09-29 01:09:22 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.848 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)