# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_16:19:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,896 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 16:19:47 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:19:05 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-13 16:15:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:14:28 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:14:08 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-13 16:13:21 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.018 |  |
| 2026-09-13 16:12:50 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-09-13 16:10:49 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:10:17 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:10:00 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 16:09:27 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.111 |  |
| 2026-09-13 16:08:33 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:08:03 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.039 |  |
| 2026-09-13 16:06:44 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:06:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:05:31 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-13 16:05:13 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-13 16:04:50 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:04:35 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:04:22 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:03:59 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-13 16:03:50 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.051 |  |
| 2026-09-13 16:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:03:21 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-09-13 16:03:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:55 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-09-13 16:02:52 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-09-13 16:02:49 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:39 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:34 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-09-13 16:02:33 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-09-13 16:02:27 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:13 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:03 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:01:57 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:01:57 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:01:54 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-09-13 16:01:46 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:00:57 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:00:34 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.093 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 16:02:34 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-09-13 16:03:21 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-09-13 16:00:34 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-13 16:19:05 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-13 16:05:31 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-13 16:14:08 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-13 16:03:59 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-13 16:10:00 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 16:02:39 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:01:57 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:01:57 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:03 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:10:49 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:03:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:19:47 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:14:28 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:04:35 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:01:46 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:27 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:00:57 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:04:22 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:06:44 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:08:33 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:49 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:04:50 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:15:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:02:13 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:06:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-09-13 16:05:13 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-13 16:02:33 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-09-13 16:13:21 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.018 |  |
| 2026-09-13 16:12:50 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-09-13 16:02:55 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-09-13 16:02:52 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-09-13 16:08:03 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.039 |  |
| 2026-09-13 16:01:54 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-09-13 16:03:50 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.051 |  |
| 2026-09-13 16:09:27 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)