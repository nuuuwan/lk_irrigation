# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_08:11:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,296 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 08:11:02 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.079 |  |
| 2026-10-16 08:10:15 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.027 |  |
| 2026-10-16 08:06:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:06:14 | Galgamuwa (Mee Oya) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-10-16 08:05:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 08:05:42 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-16 08:05:38 | Thanthirimale (Malwathu Oya) | 1.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-16 08:05:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.100 |  |
| 2026-10-16 08:05:03 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | -0.079 |  |
| 2026-10-16 08:04:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-16 08:04:43 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.012 |  |
| 2026-10-16 08:04:35 | Panadugama (Nilwala Ganga) | 6.96 | 🟠 Minor Flood | 0.276 | 🔺 Rising |
| 2026-10-16 08:04:34 | Rathnapura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.048 |  |
| 2026-10-16 08:04:25 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:04:05 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-10-16 08:04:02 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:03:55 | Pitabeddara (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.162 |  |
| 2026-10-16 08:03:36 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:03:34 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:03:33 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 08:03:30 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | -0.160 |  |
| 2026-10-16 08:03:27 | Dunamale (Aththanagalu Oya) | 3.62 | 🟡 Alert | -0.040 |  |
| 2026-10-16 08:03:24 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.110 |  |
| 2026-10-16 08:03:20 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 08:03:16 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-16 08:03:02 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:02:35 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.021 |  |
| 2026-10-16 08:02:34 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-16 08:02:17 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.227 |  |
| 2026-10-16 08:02:16 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2026-10-16 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | 0.000 |  |
| 2026-10-16 08:02:15 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:02:13 | Ellagawa (Kalu Ganga) | 7.52 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:01:39 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:01:39 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-16 08:01:14 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 08:00:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 08:04:35 | Panadugama (Nilwala Ganga) | 6.96 | 🟠 Minor Flood | 0.276 | 🔺 Rising |
| 2026-10-16 08:03:33 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | 0.000 |  |
| 2026-10-16 08:03:27 | Dunamale (Aththanagalu Oya) | 3.62 | 🟡 Alert | -0.040 |  |
| 2026-10-16 08:04:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-16 08:05:38 | Thanthirimale (Malwathu Oya) | 1.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-16 08:05:42 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-16 08:01:14 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 08:02:34 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-16 08:03:20 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 08:03:16 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-16 08:05:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:02:20 | Urawa (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-16 08:01:39 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-16 08:03:02 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:04:25 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:03:34 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:01:39 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:02:13 | Ellagawa (Kalu Ganga) | 7.52 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-16 08:06:14 | Galgamuwa (Mee Oya) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-10-16 08:04:05 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-10-16 08:04:43 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.012 |  |
| 2026-10-16 08:03:36 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:02:15 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:04:02 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:06:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-10-16 08:02:35 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.021 |  |
| 2026-10-16 08:10:15 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.027 |  |
| 2026-10-16 08:04:34 | Rathnapura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.048 |  |
| 2026-10-16 08:02:16 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2026-10-16 08:00:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.056 |  |
| 2026-10-16 08:05:03 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | -0.079 |  |
| 2026-10-16 08:11:02 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.079 |  |
| 2026-10-16 08:05:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.100 |  |
| 2026-10-16 08:03:24 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.110 |  |
| 2026-10-16 08:03:30 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | -0.160 |  |
| 2026-10-16 08:03:55 | Pitabeddara (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.162 |  |
| 2026-10-16 08:02:17 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.227 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)