# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_13:25:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,505 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kithulgala — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 13:25:44 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:15:42 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:09:21 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:08:56 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-06 13:08:01 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:07:50 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:07:36 | Peradeniya (Mahaweli Ganga) | 4.25 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-06 13:06:38 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:06:10 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.152 |  |
| 2026-08-06 13:05:55 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 13:05:12 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-08-06 13:04:57 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-08-06 13:04:49 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:04:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.039 |  |
| 2026-08-06 13:04:38 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:04:25 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:04:06 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.039 |  |
| 2026-08-06 13:03:57 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-08-06 13:03:42 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:03:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:03:23 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.148 |  |
| 2026-08-06 13:03:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.064 |  |
| 2026-08-06 13:03:06 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:02:53 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:02:51 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-06 13:02:22 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-06 13:02:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:02:04 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-08-06 13:01:45 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:01:40 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:01:34 | Nawalapitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-08-06 13:01:25 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.054 |  |
| 2026-08-06 13:01:23 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:01:17 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:01:05 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:00:50 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:00:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:00:18 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 13:00:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 13:03:23 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.148 |  |
| 2026-08-06 13:01:34 | Nawalapitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-08-06 13:02:51 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-06 13:02:22 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-06 13:07:36 | Peradeniya (Mahaweli Ganga) | 4.25 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-06 13:08:56 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-06 13:00:18 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 13:05:55 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 13:00:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:03:42 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:03:06 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:25:44 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:00:50 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:00:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:08:01 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:02:53 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:03:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:04:49 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:07:50 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:02:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:06:38 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:04:25 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:15:42 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:01:45 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:01:40 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:04:38 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:09:21 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:01:23 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:01:17 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:01:05 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-08-06 13:03:57 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-08-06 13:05:12 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-08-06 13:04:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.039 |  |
| 2026-08-06 13:04:06 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.039 |  |
| 2026-08-06 13:04:57 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-08-06 13:01:25 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.054 |  |
| 2026-08-06 13:02:04 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-08-06 13:03:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.064 |  |
| 2026-08-06 13:06:10 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)