# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_05:36:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 05:36:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | 3.038 | 🔺 Rising |
| 2026-09-15 05:33:36 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-09-15 05:33:35 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-09-15 05:31:48 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 05:31:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 3.038 | 🔺 Rising |
| 2026-09-15 05:16:28 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.026 |  |
| 2026-09-15 05:15:04 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:15:03 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:14:11 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:09:22 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.408 |  |
| 2026-09-15 05:08:57 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 360.000 | 🔺 Rising |
| 2026-09-15 05:08:56 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 360.000 | 🔺 Rising |
| 2026-09-15 05:08:33 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 360.000 | 🔺 Rising |
| 2026-09-15 05:08:32 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-09-15 05:08:29 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.134 |  |
| 2026-09-15 05:07:59 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 05:06:58 | Thawalama (Gin Ganga) | 3.87 | 🟢 Normal | -0.198 |  |
| 2026-09-15 05:06:35 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:05:29 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-15 05:04:45 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:04:34 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-15 05:04:23 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.115 |  |
| 2026-09-15 05:03:50 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 05:03:34 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-15 05:03:13 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -72.000 |  |
| 2026-09-15 05:03:11 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -72.000 |  |
| 2026-09-15 05:02:53 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | 0.439 | 🔺 Rising |
| 2026-09-15 05:02:46 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-15 05:02:39 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.041 |  |
| 2026-09-15 05:02:34 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-15 05:02:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:02:21 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-15 05:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-15 05:01:50 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:01:36 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 05:01:30 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:01:19 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:01:06 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-15 05:01:06 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | 0.100 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 05:08:57 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 360.000 | 🔺 Rising |
| 2026-09-15 05:33:36 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-09-15 05:36:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | 3.038 | 🔺 Rising |
| 2026-09-15 05:02:53 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | 0.439 | 🔺 Rising |
| 2026-09-15 04:10:32 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-09-15 05:03:34 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-15 05:04:34 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-15 05:01:06 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-15 05:02:46 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-15 05:02:34 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-15 05:02:21 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-15 05:31:48 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 05:03:50 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 05:05:29 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-15 05:07:59 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 05:01:36 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 05:15:04 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:02:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:04:45 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:04:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:01:50 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:14:11 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:01:19 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:01:30 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:06:35 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-15 05:01:06 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-15 04:01:48 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-09-15 05:16:28 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.026 |  |
| 2026-09-15 05:08:32 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-09-15 05:02:39 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.041 |  |
| 2026-09-15 05:04:23 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.115 |  |
| 2026-09-15 05:08:29 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.134 |  |
| 2026-09-15 05:06:58 | Thawalama (Gin Ganga) | 3.87 | 🟢 Normal | -0.198 |  |
| 2026-09-15 05:09:22 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.408 |  |
| 2026-09-15 05:03:13 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)