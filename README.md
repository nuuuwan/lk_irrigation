# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_07:21:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,490 measurements** from **39** stations.
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
| 2026-11-22 07:21:39 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-11-22 07:19:55 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.024 |  |
| 2026-11-22 07:10:54 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.012 |  |
| 2026-11-22 07:09:04 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.106 |  |
| 2026-11-22 07:08:00 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 07:07:24 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-22 07:07:19 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.037 |  |
| 2026-11-22 07:07:19 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.047 |  |
| 2026-11-22 07:06:59 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.019 |  |
| 2026-11-22 07:05:39 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.167 |  |
| 2026-11-22 07:05:34 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-11-22 07:05:15 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.174 |  |
| 2026-11-22 07:05:07 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 07:04:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:04:41 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-22 07:04:29 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 0.460 | 🔺 Rising |
| 2026-11-22 07:04:27 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.029 |  |
| 2026-11-22 07:04:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:03:51 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:03:45 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:03:09 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.041 |  |
| 2026-11-22 07:02:57 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-11-22 07:02:53 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.032 |  |
| 2026-11-22 07:02:44 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:02:43 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:02:40 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-11-22 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.143 |  |
| 2026-11-22 07:02:23 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-22 07:02:11 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-22 07:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:01:26 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:01:25 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-22 07:01:20 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:00:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:00:55 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:00:46 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 07:04:29 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 0.460 | 🔺 Rising |
| 2026-11-22 07:07:24 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-22 07:01:25 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-22 07:02:23 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-22 07:05:07 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 07:08:00 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 07:00:46 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 07:04:41 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-22 07:03:51 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:00:55 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:04:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:00:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:04:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:01:20 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:02:49 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:02:44 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:03:45 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:01:26 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:02:43 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:10:54 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.012 |  |
| 2026-11-22 07:05:34 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-11-22 07:06:59 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.019 |  |
| 2026-11-22 07:02:11 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-22 07:02:40 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-11-22 07:19:55 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.024 |  |
| 2026-11-22 07:04:27 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.029 |  |
| 2026-11-22 07:21:39 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-11-22 07:02:53 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.032 |  |
| 2026-11-22 07:07:19 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.037 |  |
| 2026-11-22 07:02:57 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-11-22 07:03:09 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.041 |  |
| 2026-11-22 07:07:19 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.047 |  |
| 2026-11-22 07:09:04 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.106 |  |
| 2026-11-22 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.143 |  |
| 2026-11-22 07:05:39 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.167 |  |
| 2026-11-22 07:05:15 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)