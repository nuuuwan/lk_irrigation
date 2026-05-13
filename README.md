# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_11:18:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,628 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 11:18:57 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -1.265 |  |
| 2026-05-13 11:18:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-05-13 11:17:14 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.027 |  |
| 2026-05-13 11:16:19 | Galgamuwa (Mee Oya) | 2.21 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-13 11:13:35 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-13 11:11:08 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-13 11:09:29 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-13 11:07:40 | Pitabeddara (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 11:07:32 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-13 11:06:42 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-05-13 11:06:20 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:06:07 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.032 |  |
| 2026-05-13 11:06:06 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 11:05:41 | Katharagama (Menik Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:05:40 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -1.265 |  |
| 2026-05-13 11:05:33 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-13 11:05:06 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-05-13 11:05:06 | Moragaswewa (Deduru Oya) | 2.59 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-13 11:04:47 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-13 11:04:17 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-13 11:04:13 | Rathnapura (Kalu Ganga) | 5.86 | 🟡 Alert | 0.433 | 🔺 Rising |
| 2026-05-13 11:04:07 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 11:03:52 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-13 11:03:51 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.557 | 🔺 Rising |
| 2026-05-13 11:03:40 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:03:26 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.462 | 🔺 Rising |
| 2026-05-13 11:03:12 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 11:02:58 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-13 11:02:56 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-13 11:02:56 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:02:08 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-13 11:02:01 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-05-13 11:01:40 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:01:23 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-13 11:01:21 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:01:11 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:01:10 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-13 11:00:51 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-13 11:00:30 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 11:03:26 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.462 | 🔺 Rising |
| 2026-05-13 11:04:13 | Rathnapura (Kalu Ganga) | 5.86 | 🟡 Alert | 0.433 | 🔺 Rising |
| 2026-05-13 11:18:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-05-13 11:03:51 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.557 | 🔺 Rising |
| 2026-05-13 11:06:42 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-05-13 11:05:06 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-05-13 11:11:08 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-13 11:04:17 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-13 11:09:29 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-13 11:01:10 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-13 11:04:47 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-13 11:03:52 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-13 11:05:06 | Moragaswewa (Deduru Oya) | 2.59 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-13 11:05:33 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-13 11:02:56 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-13 11:00:51 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-13 11:03:12 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 11:02:58 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-13 11:07:40 | Pitabeddara (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 11:16:19 | Galgamuwa (Mee Oya) | 2.21 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-13 11:04:07 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 11:06:06 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 11:13:35 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-13 11:02:01 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:06:20 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:03:40 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:02:56 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:05:41 | Katharagama (Menik Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:01:21 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:01:11 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:01:40 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-13 11:02:08 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-13 11:01:23 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-13 11:07:32 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-13 11:17:14 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.027 |  |
| 2026-05-13 11:00:30 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.031 |  |
| 2026-05-13 11:06:07 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.032 |  |
| 2026-05-13 11:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-05-13 11:18:57 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -1.265 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)