# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_20:21:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,225 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 20:21:53 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.008 |  |
| 2026-09-01 20:19:28 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:16:27 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:14:54 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:12:44 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:12:11 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:11:21 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:11:12 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.009 |  |
| 2026-09-01 20:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2026-09-01 20:08:53 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:08:35 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-01 20:07:51 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-01 20:06:39 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.186 |  |
| 2026-09-01 20:06:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-01 20:06:30 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-09-01 20:06:24 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:05:36 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-09-01 20:04:47 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:04:28 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-09-01 20:04:22 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:04:17 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:04:11 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-09-01 20:04:08 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 20:04:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:03:36 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:03:31 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:03:26 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2026-09-01 20:03:23 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:03:20 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:02:55 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:02:44 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:02:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.120 |  |
| 2026-09-01 20:02:15 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 20:02:13 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:01:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:01:11 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:01:00 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 20:04:28 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-09-01 20:02:15 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 20:04:08 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 20:07:51 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-01 20:08:35 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-01 20:01:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:08:53 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:04:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:12:44 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:04:17 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:11:21 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:03:31 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:02:13 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:04:47 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:03:23 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:03:20 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:02:55 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:06:24 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:19:28 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:16:27 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:12:11 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:14:54 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:01:11 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:02:44 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 20:21:53 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.008 |  |
| 2026-09-01 20:11:12 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.009 |  |
| 2026-09-01 20:06:30 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-09-01 20:06:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-01 20:01:00 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-01 18:04:47 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-01 20:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2026-09-01 20:04:11 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-09-01 20:03:26 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2026-09-01 20:05:36 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-09-01 19:08:46 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.044 |  |
| 2026-09-01 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.060 |  |
| 2026-09-01 20:02:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.120 |  |
| 2026-09-01 20:06:39 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)