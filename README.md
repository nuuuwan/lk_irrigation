# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_09:19:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,335 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 09:19:39 | Urawa (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.082 |  |
| 2026-10-16 09:09:44 | Galgamuwa (Mee Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:09:19 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.041 |  |
| 2026-10-16 09:09:02 | Rathnapura (Kalu Ganga) | 3.51 | 🟢 Normal | -0.056 |  |
| 2026-10-16 09:08:15 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-16 09:07:40 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:07:17 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-10-16 09:05:47 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-16 09:05:22 | Pitabeddara (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.332 |  |
| 2026-10-16 09:05:11 | Moragaswewa (Deduru Oya) | 2.13 | 🟢 Normal | -0.114 |  |
| 2026-10-16 09:05:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 09:04:56 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-10-16 09:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 09:04:21 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.052 |  |
| 2026-10-16 09:04:10 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | -0.068 |  |
| 2026-10-16 09:03:44 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.236 |  |
| 2026-10-16 09:03:40 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:03:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 09:03:35 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-16 09:03:31 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-16 09:03:25 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.040 |  |
| 2026-10-16 09:03:22 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | -0.281 |  |
| 2026-10-16 09:03:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.020 |  |
| 2026-10-16 09:03:17 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | -0.040 |  |
| 2026-10-16 09:02:51 | Panadugama (Nilwala Ganga) | 6.67 | 🟠 Minor Flood | -0.039 |  |
| 2026-10-16 09:02:43 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | -0.031 |  |
| 2026-10-16 09:02:35 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.040 |  |
| 2026-10-16 09:02:21 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-16 09:02:14 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-16 09:01:53 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.046 |  |
| 2026-10-16 09:01:51 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-10-16 09:01:27 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-16 09:01:10 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-10-16 09:00:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:00:27 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-16 09:00:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.116 |  |
| 2026-10-16 09:00:13 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 09:05:47 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-16 09:02:51 | Panadugama (Nilwala Ganga) | 6.67 | 🟠 Minor Flood | -0.039 |  |
| 2026-10-16 09:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 09:03:25 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.040 |  |
| 2026-10-16 09:01:27 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-16 09:02:21 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-16 09:08:15 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-16 09:03:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 09:05:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 08:03:16 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:03:40 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:09:44 | Galgamuwa (Mee Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:00:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:07:40 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:07:17 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-10-16 08:03:02 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-16 09:03:31 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-16 09:02:14 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-16 09:00:27 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-16 09:01:10 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-10-16 09:03:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.020 |  |
| 2026-10-16 09:03:35 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-16 09:04:56 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-10-16 09:01:51 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-10-16 09:02:43 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | -0.031 |  |
| 2026-10-16 09:02:35 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.040 |  |
| 2026-10-16 09:03:17 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | -0.040 |  |
| 2026-10-16 09:09:19 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.041 |  |
| 2026-10-16 09:01:53 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.046 |  |
| 2026-10-16 09:04:21 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.052 |  |
| 2026-10-16 09:09:02 | Rathnapura (Kalu Ganga) | 3.51 | 🟢 Normal | -0.056 |  |
| 2026-10-16 09:00:13 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.060 |  |
| 2026-10-16 09:04:10 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | -0.068 |  |
| 2026-10-16 09:19:39 | Urawa (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.082 |  |
| 2026-10-16 09:05:11 | Moragaswewa (Deduru Oya) | 2.13 | 🟢 Normal | -0.114 |  |
| 2026-10-16 09:00:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.116 |  |
| 2026-10-16 09:03:44 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.236 |  |
| 2026-10-16 09:03:22 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | -0.281 |  |
| 2026-10-16 09:05:22 | Pitabeddara (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.332 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)