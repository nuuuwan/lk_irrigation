# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_05:38:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,374 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 05:38:56 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 05:36:21 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 4.320 | 🔺 Rising |
| 2026-10-04 05:35:56 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 4.320 | 🔺 Rising |
| 2026-10-04 05:16:06 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-04 05:15:27 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-04 05:15:06 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 05:12:40 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-04 05:12:28 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-04 05:11:04 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-04 05:11:00 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:08:24 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.019 |  |
| 2026-10-04 05:07:34 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-04 05:07:30 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:05:52 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.088 |  |
| 2026-10-04 05:04:44 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-04 05:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:03:57 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:03:51 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.045 |  |
| 2026-10-04 05:03:23 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-04 05:03:05 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 05:02:53 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.060 |  |
| 2026-10-04 05:02:41 | Peradeniya (Mahaweli Ganga) | 3.69 | 🟢 Normal | -0.110 |  |
| 2026-10-04 05:02:40 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-04 05:02:29 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-04 05:02:28 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 05:01:56 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-04 05:01:55 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 05:36:21 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 4.320 | 🔺 Rising |
| 2026-10-04 05:01:00 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-10-04 05:02:29 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-04 05:16:06 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-04 05:12:40 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-04 05:38:56 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 05:01:56 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-04 05:02:40 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-04 05:15:27 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-04 05:01:27 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 04:56:52 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 05:03:05 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 05:01:04 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 05:01:43 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 02:02:29 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 05:02:28 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 05:11:04 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-04 05:11:00 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:01:47 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:07:30 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:00:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:00:25 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:03:57 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 05:12:28 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-04 05:04:44 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-04 05:03:23 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-04 05:01:55 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-10-04 05:08:24 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.019 |  |
| 2026-10-04 05:00:41 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.027 |  |
| 2026-10-04 05:03:51 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.045 |  |
| 2026-10-04 05:02:53 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.060 |  |
| 2026-10-04 04:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.065 |  |
| 2026-10-04 05:05:52 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.088 |  |
| 2026-10-04 05:02:41 | Peradeniya (Mahaweli Ganga) | 3.69 | 🟢 Normal | -0.110 |  |
| 2026-10-04 04:04:44 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)