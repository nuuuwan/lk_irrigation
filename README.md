# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_12:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 12:17:39 | Panadugama (Nilwala Ganga) | 6.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 12:16:12 | Urawa (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.025 |  |
| 2026-10-16 12:08:35 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.066 |  |
| 2026-10-16 12:07:56 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-10-16 12:05:13 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 12:04:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 12:04:41 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:04:36 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-10-16 12:04:34 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:04:31 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:03:55 | Panadugama (Nilwala Ganga) | 6.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 12:03:47 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.058 |  |
| 2026-10-16 12:03:43 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:03:39 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.030 |  |
| 2026-10-16 12:03:36 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.031 |  |
| 2026-10-16 12:03:34 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-10-16 12:03:27 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.127 |  |
| 2026-10-16 12:03:21 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.050 |  |
| 2026-10-16 12:03:09 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-16 12:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:59 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | -0.044 |  |
| 2026-10-16 12:02:54 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:49 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:47 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 12:02:40 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-16 12:02:26 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-16 12:02:22 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-10-16 12:02:21 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:19 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:08 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.136 |  |
| 2026-10-16 12:01:59 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.105 |  |
| 2026-10-16 12:01:49 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-16 12:01:38 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 12:01:27 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 12:01:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:01:20 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 12:00:55 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 12:00:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-16 12:00:51 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-16 12:00:19 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-10-16 12:00:11 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 12:17:39 | Panadugama (Nilwala Ganga) | 6.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 12:01:38 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 12:04:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 12:02:59 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | -0.044 |  |
| 2026-10-16 12:02:40 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-16 12:00:51 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-16 12:00:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-16 12:01:20 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 12:05:13 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 12:02:47 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 12:01:27 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 12:00:55 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 12:02:19 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:54 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:01:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:49 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:04:41 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:04:31 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:21 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:04:34 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 12:02:26 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-16 12:03:09 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-16 12:00:19 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-10-16 12:01:49 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-16 12:03:34 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-10-16 12:00:11 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-10-16 12:02:22 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-10-16 12:07:56 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-10-16 12:16:12 | Urawa (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.025 |  |
| 2026-10-16 12:03:39 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.030 |  |
| 2026-10-16 12:04:36 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-10-16 12:03:36 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.031 |  |
| 2026-10-16 12:03:21 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.050 |  |
| 2026-10-16 12:03:47 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.058 |  |
| 2026-10-16 12:08:35 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.066 |  |
| 2026-10-16 12:01:59 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.105 |  |
| 2026-10-16 12:03:27 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.127 |  |
| 2026-10-16 12:02:08 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)