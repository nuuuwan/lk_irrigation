# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_02:05:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 02:05:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:05:48 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:05:01 | Moragaswewa (Deduru Oya) | 2.42 | 🟢 Normal | -0.136 |  |
| 2026-10-19 02:04:52 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-19 02:04:39 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-10-19 02:04:34 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.818 |  |
| 2026-10-19 02:04:28 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:04:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:03:51 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-19 02:03:50 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.818 |  |
| 2026-10-19 02:03:43 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.033 |  |
| 2026-10-19 02:03:37 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-19 02:02:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:28 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:22 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-19 02:02:14 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-19 02:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-19 02:01:50 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-10-19 02:01:47 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.061 |  |
| 2026-10-19 02:01:20 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.191 |  |
| 2026-10-19 02:01:15 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 02:01:02 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | -0.005 |  |
| 2026-10-19 02:00:53 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.090 |  |
| 2026-10-19 01:50:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 02:01:02 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | -0.005 |  |
| 2026-10-19 01:05:24 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-19 01:07:02 | Norwood (Kelani Ganga) | 1.56 | 🟡 Alert | -0.049 |  |
| 2026-10-19 02:03:51 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-19 02:02:14 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-19 00:02:16 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-19 01:06:06 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-19 02:01:15 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 01:01:57 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 02:05:48 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:02:28 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 01:12:45 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:05:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:04:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:04:28 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-19 02:01:50 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-19 02:03:37 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-19 02:02:22 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-19 02:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-19 02:04:52 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-19 02:04:39 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-10-19 01:03:51 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-19 02:03:43 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.033 |  |
| 2026-10-19 01:05:21 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | -0.042 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-19 02:01:47 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.061 |  |
| 2026-10-19 02:00:53 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.090 |  |
| 2026-10-19 01:07:52 | Glencourse (Kelani Ganga) | 12.21 | 🟢 Normal | -0.092 |  |
| 2026-10-19 01:01:47 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.112 |  |
| 2026-10-19 01:07:32 | Rathnapura (Kalu Ganga) | 4.31 | 🟢 Normal | -0.114 |  |
| 2026-10-19 02:05:01 | Moragaswewa (Deduru Oya) | 2.42 | 🟢 Normal | -0.136 |  |
| 2026-10-19 01:01:56 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.139 |  |
| 2026-10-19 02:01:20 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.191 |  |
| 2026-10-19 02:04:34 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.818 |  |
| 2026-10-19 00:14:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -2.667 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)