# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_23:12:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,572 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 23:12:49 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:12:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-18 23:11:29 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-18 23:11:23 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:08:36 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-18 23:06:44 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:06:07 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:05:42 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-11-18 23:05:17 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:39 | Moraketiya (Walawe Ganga) | 2.21 | 🟢 Normal | -0.236 |  |
| 2026-11-18 23:04:32 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:30 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:09 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:09 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:07 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:56 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:49 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:36 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 23:03:14 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:12 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:02:46 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-18 23:02:29 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-11-18 23:02:08 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.050 |  |
| 2026-11-18 23:02:08 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:51 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:36 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:35 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:25 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.014 |  |
| 2026-11-18 23:01:24 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-11-18 23:01:18 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:00 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:00:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 23:02:46 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-18 23:03:36 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 23:11:29 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-18 23:08:36 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-18 23:12:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-18 23:01:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:14 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:06:07 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:00 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:09 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:02:29 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:18 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:11:23 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:30 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:09 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:00:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:07 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:12 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:05:17 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:56 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:10 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:04:32 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:03:49 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:35 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:36 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:47:43 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-11-18 23:05:42 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-11-18 23:12:49 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:51 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:06:44 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:02:08 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:24 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-11-18 23:01:25 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.014 |  |
| 2026-11-18 23:02:08 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.050 |  |
| 2026-11-18 23:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-11-18 23:04:39 | Moraketiya (Walawe Ganga) | 2.21 | 🟢 Normal | -0.236 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)