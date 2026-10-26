# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_01:11:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Moragaswewa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 01:11:32 | Panadugama (Nilwala Ganga) | 6.37 | 🟠 Minor Flood | 0.089 | 🔺 Rising |
| 2026-10-27 01:11:28 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | -0.037 |  |
| 2026-10-27 01:08:56 | Kithulgala (Kelani Ganga) | 2.44 | 🟢 Normal | -0.009 |  |
| 2026-10-27 01:07:46 | Thawalama (Gin Ganga) | 5.34 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-10-27 01:07:32 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:07:14 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.027 |  |
| 2026-10-27 01:07:12 | Putupaula (Kalu Ganga) | 3.07 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-10-27 01:06:58 | Pitabeddara (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-27 01:06:04 | Norwood (Kelani Ganga) | 1.80 | 🟡 Alert | -0.039 |  |
| 2026-10-27 01:05:39 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-10-27 01:05:17 | Badalgama (Maha Oya) | 5.63 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-10-27 01:04:43 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-27 01:04:41 | Hanwella (Kelani Ganga) | 6.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-27 01:04:23 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-27 01:04:12 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-10-27 01:04:05 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.070 |  |
| 2026-10-27 01:04:00 | Rathnapura (Kalu Ganga) | 8.64 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-27 01:03:50 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.038 |  |
| 2026-10-27 01:03:37 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:03:21 | Giriulla (Maha Oya) | 5.18 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-27 01:03:19 | Holombuwa (Kelani Ganga) | 2.84 | 🟢 Normal | -0.118 |  |
| 2026-10-27 01:03:08 | Glencourse (Kelani Ganga) | 15.04 | 🟡 Alert | -0.108 |  |
| 2026-10-27 01:02:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:02:41 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.060 | 🔺 Rising |
| 2026-10-27 01:02:23 | Peradeniya (Mahaweli Ganga) | 4.52 | 🟢 Normal | -0.181 |  |
| 2026-10-27 01:02:10 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.049 |  |
| 2026-10-27 01:01:47 | Moragaswewa (Deduru Oya) | 4.82 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-10-27 01:01:45 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:01:34 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 01:01:07 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-10-27 01:00:45 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-10-27 01:00:12 | Moraketiya (Walawe Ganga) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 01:11:32 | Panadugama (Nilwala Ganga) | 6.37 | 🟠 Minor Flood | 0.089 | 🔺 Rising |
| 2026-10-27 00:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-10-27 01:02:41 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.060 | 🔺 Rising |
| 2026-10-27 01:04:00 | Rathnapura (Kalu Ganga) | 8.64 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-27 01:01:47 | Moragaswewa (Deduru Oya) | 4.82 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-10-27 01:05:17 | Badalgama (Maha Oya) | 5.63 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-10-27 01:04:12 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-10-27 01:07:46 | Thawalama (Gin Ganga) | 5.34 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-10-27 01:07:12 | Putupaula (Kalu Ganga) | 3.07 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-10-27 01:05:39 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-10-27 01:01:34 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 01:11:28 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | -0.037 |  |
| 2026-10-27 01:06:04 | Norwood (Kelani Ganga) | 1.80 | 🟡 Alert | -0.039 |  |
| 2026-10-27 01:03:08 | Glencourse (Kelani Ganga) | 15.04 | 🟡 Alert | -0.108 |  |
| 2026-10-27 01:00:45 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-27 01:04:23 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 01:04:41 | Hanwella (Kelani Ganga) | 6.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-27 01:03:21 | Giriulla (Maha Oya) | 5.18 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-27 00:02:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-27 01:06:58 | Pitabeddara (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-27 00:01:13 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 01:00:12 | Moraketiya (Walawe Ganga) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 01:03:37 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:01:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:07:32 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:01:45 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:02:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 01:08:56 | Kithulgala (Kelani Ganga) | 2.44 | 🟢 Normal | -0.009 |  |
| 2026-10-27 01:04:43 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-27 01:01:07 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-10-27 01:07:14 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.027 |  |
| 2026-10-27 01:03:50 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.038 |  |
| 2026-10-27 01:02:10 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.049 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-27 01:04:05 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.070 |  |
| 2026-10-27 01:03:19 | Holombuwa (Kelani Ganga) | 2.84 | 🟢 Normal | -0.118 |  |
| 2026-10-27 01:02:23 | Peradeniya (Mahaweli Ganga) | 4.52 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)