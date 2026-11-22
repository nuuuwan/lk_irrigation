# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_14:29:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,767 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 14:29:50 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:16:26 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:16:01 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:13:48 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:12:00 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.035 |  |
| 2026-11-22 14:10:27 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-11-22 14:10:24 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:10:03 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:09:25 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:09:16 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.113 |  |
| 2026-11-22 14:08:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.067 |  |
| 2026-11-22 14:08:02 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.040 |  |
| 2026-11-22 14:06:45 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:06:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.071 |  |
| 2026-11-22 14:06:06 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:04:23 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.041 |  |
| 2026-11-22 14:04:14 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.076 |  |
| 2026-11-22 14:03:49 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-11-22 14:03:35 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:03:25 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 14:03:23 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.020 |  |
| 2026-11-22 14:03:08 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:02:57 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 14:02:48 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-22 14:02:40 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:02:39 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.151 |  |
| 2026-11-22 14:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.089 |  |
| 2026-11-22 14:02:04 | Moragaswewa (Deduru Oya) | 3.60 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-22 14:01:56 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 14:01:49 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.015 |  |
| 2026-11-22 14:01:44 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-22 14:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:01:39 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 14:01:37 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-11-22 14:01:12 | Thanamalwila (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-22 14:01:05 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 14:00:53 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-11-22 14:00:47 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 14:02:04 | Moragaswewa (Deduru Oya) | 3.60 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-22 14:01:44 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-22 14:02:57 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 14:01:05 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 14:01:39 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 14:00:47 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 14:01:56 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 14:03:35 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:06:45 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:09:25 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:13:48 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:16:01 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:02:40 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:10:03 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:10:24 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:06:06 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:03:08 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:16:26 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:29:50 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:03:25 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 14:01:12 | Thanamalwila (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-22 14:02:48 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-22 14:00:53 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-11-22 14:01:49 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.015 |  |
| 2026-11-22 14:10:27 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-11-22 14:03:23 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.020 |  |
| 2026-11-22 14:03:49 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-11-22 14:01:37 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-11-22 14:12:00 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.035 |  |
| 2026-11-22 14:08:02 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.040 |  |
| 2026-11-22 14:04:23 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.041 |  |
| 2026-11-22 14:08:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.067 |  |
| 2026-11-22 14:06:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.071 |  |
| 2026-11-22 14:04:14 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.076 |  |
| 2026-11-22 14:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.089 |  |
| 2026-11-22 14:09:16 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.113 |  |
| 2026-11-22 14:02:39 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)