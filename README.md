# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_16:08:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,413 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 16:08:34 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:06:36 | Manampitiya (Mahaweli Ganga) | 4.48 | 🟠 Minor Flood | 0.114 | 🔺 Rising |
| 2025-12-18 16:06:34 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 16:06:14 | Galgamuwa (Mee Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 16:06:05 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2025-12-18 16:06:04 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:06:00 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 16:05:50 | Horowpothana (Yan Oya) | 5.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:05:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:05:22 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:04:55 | Nakkala (Kumbukkan Oya) | 2.52 | 🟢 Normal | -0.039 |  |
| 2025-12-18 16:04:51 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:04:07 | Padiyathalawa (Maduru Oya) | 2.25 | 🟢 Normal | 1.172 | 🔺 Rising |
| 2025-12-18 16:03:37 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 16:03:34 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:03:33 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-18 16:03:19 | Weraganthota (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 16:03:18 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-18 16:03:08 | Thanthirimale (Malwathu Oya) | 5.25 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2025-12-18 16:02:58 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2025-12-18 16:02:37 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2025-12-18 16:02:36 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:02:35 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 16:02:29 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:02:17 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-18 16:01:57 | Thaldena (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 16:01:54 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:01:39 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:01:36 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 16:01:20 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:00:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2025-12-18 16:00:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:00:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2025-12-18 16:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-18 15:17:08 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:15:11 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 16:06:36 | Manampitiya (Mahaweli Ganga) | 4.48 | 🟠 Minor Flood | 0.114 | 🔺 Rising |
| 2025-12-18 16:03:08 | Thanthirimale (Malwathu Oya) | 5.25 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2025-12-18 16:04:07 | Padiyathalawa (Maduru Oya) | 2.25 | 🟢 Normal | 1.172 | 🔺 Rising |
| 2025-12-18 16:02:37 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2025-12-18 16:03:33 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-18 16:02:17 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-18 16:03:19 | Weraganthota (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 16:02:35 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 16:06:00 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 16:06:34 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 16:03:37 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 15:06:10 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 15:02:43 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 16:01:36 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 16:01:57 | Thaldena (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 16:06:14 | Galgamuwa (Mee Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 16:01:39 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:01:54 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:05:50 | Horowpothana (Yan Oya) | 5.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:06:04 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:03:34 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:01:20 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:15:11 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:00:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:04:51 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:05:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:02:36 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:02:29 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:08:34 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-18 15:01:35 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-18 16:02:58 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2025-12-18 16:06:05 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2025-12-18 16:03:18 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-18 16:00:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2025-12-18 16:00:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2025-12-18 16:04:55 | Nakkala (Kumbukkan Oya) | 2.52 | 🟢 Normal | -0.039 |  |
| 2025-12-18 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.047 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)