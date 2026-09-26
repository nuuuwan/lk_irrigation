# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_00:08:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 00:08:06 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-27 00:07:33 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:07:08 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:07:04 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.024 |  |
| 2026-09-27 00:06:14 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-27 00:06:07 | Rathnapura (Kalu Ganga) | 4.45 | 🟢 Normal | -0.084 |  |
| 2026-09-27 00:06:01 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 00:05:38 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-27 00:05:30 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | -0.020 |  |
| 2026-09-27 00:05:06 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.076 |  |
| 2026-09-27 00:04:42 | Thalgahagoda (Nilwala Ganga) | 1.96 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 00:04:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:03:55 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:03:38 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-27 00:03:37 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-09-27 00:03:24 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 00:03:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:02:57 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | -0.020 |  |
| 2026-09-27 00:02:52 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:02:24 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.042 |  |
| 2026-09-27 00:02:20 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-09-27 00:02:20 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | -0.060 |  |
| 2026-09-27 00:02:19 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.011 |  |
| 2026-09-27 00:02:08 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:02:04 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:02:00 | Nawalapitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.013 |  |
| 2026-09-27 00:01:41 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.022 |  |
| 2026-09-27 00:01:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-27 00:01:11 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:01:05 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:00:36 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-26 23:54:40 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:31:13 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:27:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 00:04:42 | Thalgahagoda (Nilwala Ganga) | 1.96 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 23:27:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | -0.007 |  |
| 2026-09-26 23:11:01 | Baddegama (Gin Ganga) | 4.79 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-27 00:05:30 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | -0.020 |  |
| 2026-09-27 00:06:14 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-27 00:01:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-27 00:08:06 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-26 23:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-27 00:03:24 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 00:01:05 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:03:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:04:28 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:07:08 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:04:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:02:52 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:07:33 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:03:55 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:06:44 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:01:11 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:02:08 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:05:38 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-27 00:06:01 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 00:03:38 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-27 00:00:36 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 00:02:19 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.011 |  |
| 2026-09-27 00:02:00 | Nawalapitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.013 |  |
| 2026-09-27 00:02:57 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | -0.020 |  |
| 2026-09-27 00:03:37 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-09-27 00:02:20 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-09-27 00:01:41 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.022 |  |
| 2026-09-27 00:07:04 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.024 |  |
| 2026-09-27 00:02:24 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.042 |  |
| 2026-09-27 00:02:20 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | -0.060 |  |
| 2026-09-27 00:05:06 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.076 |  |
| 2026-09-27 00:06:07 | Rathnapura (Kalu Ganga) | 4.45 | 🟢 Normal | -0.084 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)