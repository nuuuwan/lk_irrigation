# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_00:26:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 00:26:29 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:19:13 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -180.000 |  |
| 2026-10-20 00:19:12 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -180.000 |  |
| 2026-10-20 00:14:30 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-10-20 00:13:32 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-10-20 00:12:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.028 |  |
| 2026-10-20 00:08:19 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-10-20 00:06:43 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:06:26 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.032 |  |
| 2026-10-20 00:06:07 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:05:50 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:05:46 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:05:26 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-20 00:04:45 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | -0.010 |  |
| 2026-10-20 00:04:28 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.015 |  |
| 2026-10-20 00:04:05 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -4.500 |  |
| 2026-10-20 00:03:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-20 00:03:49 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -4.500 |  |
| 2026-10-20 00:03:39 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-20 00:03:36 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.218 |  |
| 2026-10-20 00:03:35 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-10-20 00:03:25 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:03:14 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-20 00:03:08 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:02:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-20 00:02:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:02:38 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.100 |  |
| 2026-10-20 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-10-20 00:02:30 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:02:16 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:02:05 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-20 00:01:36 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:01:15 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-20 00:01:08 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-20 00:00:27 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 00:03:39 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-19 23:13:46 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-20 00:01:15 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-20 00:05:26 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-20 00:02:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-20 00:01:08 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-20 00:02:16 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:02:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:01:36 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:03:25 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:06:43 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:02:30 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:06:07 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:12:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:05:50 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:03:08 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:05:46 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:26:29 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:14:30 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-10-20 00:04:45 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | -0.010 |  |
| 2026-10-20 00:03:14 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-20 00:03:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-20 00:04:28 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.015 |  |
| 2026-10-20 00:08:19 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-10-20 00:02:05 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-20 00:03:35 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-10-20 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-10-20 00:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.028 |  |
| 2026-10-20 00:06:26 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.032 |  |
| 2026-10-20 00:00:27 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-10-19 23:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.049 |  |
| 2026-10-20 00:13:32 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-20 00:02:38 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.100 |  |
| 2026-10-20 00:03:36 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.218 |  |
| 2026-10-20 00:04:05 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -4.500 |  |
| 2026-10-20 00:19:13 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)