# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_20:07:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,051 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 20:07:40 | Rathnapura (Kalu Ganga) | 4.17 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-23 20:07:37 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-23 20:07:37 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-09-23 20:07:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-09-23 20:07:24 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.061 |  |
| 2026-09-23 20:07:10 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:06:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:06:29 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | -0.011 |  |
| 2026-09-23 20:06:02 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-09-23 20:05:26 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-09-23 20:04:55 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 20:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-23 20:04:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-23 20:04:15 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:04:03 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:03:43 | Hanwella (Kelani Ganga) | 4.63 | 🟢 Normal | -0.031 |  |
| 2026-09-23 20:03:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:03:05 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-23 20:03:03 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 20:02:41 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.86 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-23 20:02:33 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:02:20 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 20:01:55 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:01:51 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.061 |  |
| 2026-09-23 20:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:01:34 | Ellagawa (Kalu Ganga) | 7.86 | 🟢 Normal | -0.010 |  |
| 2026-09-23 20:01:22 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 20:01:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:00:38 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:00:16 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-23 20:00:16 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 20:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.86 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-23 19:11:10 | Baddegama (Gin Ganga) | 3.67 | 🟡 Alert | 0.000 |  |
| 2026-09-23 20:07:37 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-23 20:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-23 20:07:40 | Rathnapura (Kalu Ganga) | 4.17 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-23 20:00:16 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-23 19:09:30 | Thawalama (Gin Ganga) | 2.86 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-23 20:04:55 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 19:21:51 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-23 20:04:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-23 20:03:03 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 20:01:22 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 20:02:20 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 20:04:03 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:00:16 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:03:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:04:15 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:07:10 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:01:55 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:00:38 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:06:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:02:41 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:01:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 20:02:33 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 20:07:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-09-23 20:03:05 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-23 20:07:37 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-09-23 20:01:34 | Ellagawa (Kalu Ganga) | 7.86 | 🟢 Normal | -0.010 |  |
| 2026-09-23 20:05:26 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-09-23 20:06:29 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | -0.011 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 20:03:43 | Hanwella (Kelani Ganga) | 4.63 | 🟢 Normal | -0.031 |  |
| 2026-09-23 18:08:23 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.036 |  |
| 2026-09-23 20:06:02 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-09-23 20:01:51 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.061 |  |
| 2026-09-23 20:07:24 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)