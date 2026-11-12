# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_19:28:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,060 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Norwood — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 19:28:34 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:17:47 | Magura (Kalu Ganga) | 4.89 | 🟡 Alert | -0.048 |  |
| 2026-11-12 19:16:16 | Urawa (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-11-12 19:13:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | -0.017 |  |
| 2026-11-12 19:10:46 | Peradeniya (Mahaweli Ganga) | 4.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-12 19:09:49 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.071 |  |
| 2026-11-12 19:09:00 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-12 19:07:52 | Badalgama (Maha Oya) | 3.89 | 🟢 Normal | -0.048 |  |
| 2026-11-12 19:06:53 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:05:19 | Pitabeddara (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:04:52 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 19:04:43 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.049 |  |
| 2026-11-12 19:04:34 | Thawalama (Gin Ganga) | 3.34 | 🟢 Normal | -0.104 |  |
| 2026-11-12 19:04:24 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-11-12 19:04:14 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-11-12 19:04:14 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.099 |  |
| 2026-11-12 19:04:04 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.000 |  |
| 2026-11-12 19:04:03 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.000 |  |
| 2026-11-12 19:03:34 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | -0.110 |  |
| 2026-11-12 19:03:33 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.039 |  |
| 2026-11-12 19:03:27 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 19:02:54 | Nakkala (Kumbukkan Oya) | 2.05 | 🟢 Normal | 0.581 | 🔺 Rising |
| 2026-11-12 19:02:51 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.064 |  |
| 2026-11-12 19:02:44 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:02:39 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.112 |  |
| 2026-11-12 19:02:32 | Moraketiya (Walawe Ganga) | 3.35 | 🟡 Alert | -0.299 |  |
| 2026-11-12 19:02:15 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-12 19:02:12 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-12 19:02:10 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-12 19:02:05 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | 0.147 | 🔺 Rising |
| 2026-11-12 19:01:59 | Thaldena (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.210 |  |
| 2026-11-12 19:01:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:01:49 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:01:10 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-12 19:01:06 | Wellawaya (Kirindi Oya) | 2.34 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-12 19:00:40 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 19:02:05 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | 0.147 | 🔺 Rising |
| 2026-11-12 19:09:00 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-12 19:04:52 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 19:02:15 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-12 19:04:04 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.000 |  |
| 2026-11-12 19:13:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | -0.017 |  |
| 2026-11-12 19:17:47 | Magura (Kalu Ganga) | 4.89 | 🟡 Alert | -0.048 |  |
| 2026-11-12 19:02:32 | Moraketiya (Walawe Ganga) | 3.35 | 🟡 Alert | -0.299 |  |
| 2026-11-12 19:02:54 | Nakkala (Kumbukkan Oya) | 2.05 | 🟢 Normal | 0.581 | 🔺 Rising |
| 2026-11-12 19:16:16 | Urawa (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-11-12 19:02:12 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 19:01:06 | Wellawaya (Kirindi Oya) | 2.34 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-12 19:01:10 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-12 19:02:10 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 19:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 19:10:46 | Peradeniya (Mahaweli Ganga) | 4.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-12 19:06:53 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:28:34 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:05:19 | Pitabeddara (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:03:27 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 19:01:49 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 19:02:44 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:01:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-12 19:04:24 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-11-12 19:00:40 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | -0.021 |  |
| 2026-11-12 19:04:14 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-11-12 19:03:33 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.039 |  |
| 2026-11-12 19:07:52 | Badalgama (Maha Oya) | 3.89 | 🟢 Normal | -0.048 |  |
| 2026-11-12 19:04:43 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.049 |  |
| 2026-11-12 19:02:51 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.064 |  |
| 2026-11-12 19:09:49 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.071 |  |
| 2026-11-12 19:04:14 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.099 |  |
| 2026-11-12 19:04:34 | Thawalama (Gin Ganga) | 3.34 | 🟢 Normal | -0.104 |  |
| 2026-11-12 19:03:34 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | -0.110 |  |
| 2026-11-12 19:02:39 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.112 |  |
| 2026-11-12 19:01:59 | Thaldena (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)