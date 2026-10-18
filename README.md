# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_12:11:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,255 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 12:11:14 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-18 12:09:56 | Putupaula (Kalu Ganga) | 1.91 | 🟢 Normal | -0.018 |  |
| 2026-10-18 12:09:37 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.036 |  |
| 2026-10-18 12:08:23 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-10-18 12:07:57 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-18 12:07:32 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.024 |  |
| 2026-10-18 12:06:56 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.028 |  |
| 2026-10-18 12:06:51 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:06:37 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:06:31 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-18 12:04:59 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:04:59 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:04:31 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | -0.107 |  |
| 2026-10-18 12:04:31 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.124 |  |
| 2026-10-18 12:04:25 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 12:04:25 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.024 |  |
| 2026-10-18 12:04:10 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.106 |  |
| 2026-10-18 12:03:52 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-10-18 12:03:42 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | -0.073 |  |
| 2026-10-18 12:03:29 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-10-18 12:03:28 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-10-18 12:03:16 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.137 |  |
| 2026-10-18 12:03:05 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.069 |  |
| 2026-10-18 12:03:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:02:42 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 12:02:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:02:20 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.060 |  |
| 2026-10-18 12:02:16 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -1.152 |  |
| 2026-10-18 12:02:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 12:02:09 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.060 |  |
| 2026-10-18 12:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | -0.053 |  |
| 2026-10-18 12:02:03 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-10-18 12:02:00 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:01:58 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 12:01:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 12:01:25 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-18 12:01:16 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:01:09 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-10-18 12:00:30 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | -0.032 |  |
| 2026-10-18 12:00:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:00:11 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -1.152 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 12:04:25 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 12:09:37 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.036 |  |
| 2026-10-18 12:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | -0.053 |  |
| 2026-10-18 12:03:29 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-10-18 12:02:03 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-10-18 12:11:14 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-18 12:01:58 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 12:02:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 12:02:42 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 12:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 12:02:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:01:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:06:37 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:01:16 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:06:51 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:04:59 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:02:00 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:00:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:03:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:06:31 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-18 12:03:52 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-10-18 12:01:25 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-18 12:09:56 | Putupaula (Kalu Ganga) | 1.91 | 🟢 Normal | -0.018 |  |
| 2026-10-18 12:04:25 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.024 |  |
| 2026-10-18 12:07:32 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.024 |  |
| 2026-10-18 12:06:56 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.028 |  |
| 2026-10-18 12:07:57 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-18 12:00:30 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | -0.032 |  |
| 2026-10-18 12:01:09 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-10-18 12:08:23 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-10-18 12:02:20 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.060 |  |
| 2026-10-18 12:02:09 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.060 |  |
| 2026-10-18 12:03:05 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.069 |  |
| 2026-10-18 12:03:42 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | -0.073 |  |
| 2026-10-18 12:04:10 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.106 |  |
| 2026-10-18 12:04:31 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | -0.107 |  |
| 2026-10-18 12:04:31 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.124 |  |
| 2026-10-18 12:03:16 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.137 |  |
| 2026-10-18 12:02:16 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -1.152 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)