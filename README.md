# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_19:18:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,874 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 19:18:51 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:15:23 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-04 19:13:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-11-04 19:12:51 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.029 |  |
| 2026-11-04 19:11:16 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 19:08:21 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-04 19:08:09 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.018 |  |
| 2026-11-04 19:07:56 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.028 |  |
| 2026-11-04 19:06:34 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-04 19:06:24 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.020 |  |
| 2026-11-04 19:05:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:05:40 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:05:38 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-11-04 19:05:21 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | -0.020 |  |
| 2026-11-04 19:05:10 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-04 19:05:07 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-04 19:04:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:04:49 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.068 |  |
| 2026-11-04 19:04:46 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-11-04 19:04:44 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-11-04 19:04:43 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:04:41 | Kuda Oya (Kirindi Oya) | 2.54 | 🟢 Normal | 0.936 | 🔺 Rising |
| 2026-11-04 19:04:34 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-04 19:04:19 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-04 19:03:29 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-04 19:02:47 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-11-04 19:02:43 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.059 |  |
| 2026-11-04 19:02:42 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-04 19:02:30 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-11-04 19:01:58 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:01:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:01:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:01:24 | Peradeniya (Mahaweli Ganga) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 19:01:17 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 19:00:17 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | 0.661 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 19:13:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-11-04 19:04:41 | Kuda Oya (Kirindi Oya) | 2.54 | 🟢 Normal | 0.936 | 🔺 Rising |
| 2026-11-04 19:00:17 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | 0.661 | 🔺 Rising |
| 2026-11-04 19:04:19 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-04 19:02:42 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-04 19:06:34 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-04 19:04:34 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-04 19:15:23 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-04 19:11:16 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 19:05:10 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-04 19:08:21 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-04 19:01:24 | Peradeniya (Mahaweli Ganga) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 19:01:17 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 19:05:07 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-04 19:01:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:01:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:18:51 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:04:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:05:40 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:04:43 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:05:38 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-11-04 19:01:58 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:05:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:03:29 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:08:09 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.018 |  |
| 2026-11-04 19:02:47 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-11-04 19:06:24 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.020 |  |
| 2026-11-04 19:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-04 19:05:21 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | -0.020 |  |
| 2026-11-04 19:04:46 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-11-04 19:07:56 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.028 |  |
| 2026-11-04 19:12:51 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.029 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 19:04:44 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-11-04 19:02:30 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-11-04 19:02:43 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.059 |  |
| 2026-11-04 19:04:49 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)