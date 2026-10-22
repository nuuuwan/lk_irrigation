# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_22:27:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,248 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 22:27:24 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-22 22:13:18 | Pitabeddara (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 22:11:32 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:11:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 22:09:52 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.027 |  |
| 2026-10-22 22:08:01 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.048 |  |
| 2026-10-22 22:07:24 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-22 22:07:14 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 22:07:03 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-10-22 22:06:30 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:05:49 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-22 22:05:05 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | -0.011 |  |
| 2026-10-22 22:05:01 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 22:04:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 22:04:41 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:04:15 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 22:04:02 | Holombuwa (Kelani Ganga) | 1.69 | 🟢 Normal | -0.136 |  |
| 2026-10-22 22:03:41 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:03:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-10-22 22:03:24 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:03:20 | Rathnapura (Kalu Ganga) | 4.54 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-22 22:03:14 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 22:03:12 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-22 22:02:45 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-10-22 22:02:40 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-10-22 22:02:28 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:02:06 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:01:44 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:01:37 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:01:23 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:01:21 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:01:12 | Peradeniya (Mahaweli Ganga) | 3.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-22 22:01:09 | Moragaswewa (Deduru Oya) | 5.14 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-10-22 22:00:47 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 22:01:09 | Moragaswewa (Deduru Oya) | 5.14 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-10-22 22:07:03 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-10-22 22:07:24 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-22 22:04:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 22:27:24 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-22 22:03:20 | Rathnapura (Kalu Ganga) | 4.54 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-22 22:01:12 | Peradeniya (Mahaweli Ganga) | 3.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-22 22:05:49 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-22 22:03:14 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 22:03:12 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-22 22:04:15 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 22:05:01 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 22:11:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 21:06:10 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 22:07:14 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 22:13:18 | Pitabeddara (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 22:03:41 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:01:21 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:01:37 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:11:32 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:02:06 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:03:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:03:24 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:02:28 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:06:30 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:04:41 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:00:47 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:01:23 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:01:44 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-22 22:05:05 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | -0.011 |  |
| 2026-10-22 22:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-10-22 22:09:52 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.027 |  |
| 2026-10-22 22:02:40 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-10-22 22:08:01 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.048 |  |
| 2026-10-22 22:02:45 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-22 22:04:02 | Holombuwa (Kelani Ganga) | 1.69 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)