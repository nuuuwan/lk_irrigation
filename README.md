# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_14:09:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 14:09:43 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.021 |  |
| 2025-12-01 14:09:10 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:08:27 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:07:48 | Hanwella (Kelani Ganga) | 8.94 | 🟠 Minor Flood | -0.084 |  |
| 2025-12-01 14:07:33 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-01 14:07:03 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | -0.014 |  |
| 2025-12-01 14:07:00 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.013 |  |
| 2025-12-01 14:06:39 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.031 |  |
| 2025-12-01 14:06:34 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-01 14:06:26 | Galgamuwa (Mee Oya) | 3.84 | 🟢 Normal | -0.172 |  |
| 2025-12-01 14:06:01 | Ellagawa (Kalu Ganga) | 11.02 | 🟠 Minor Flood | -0.021 |  |
| 2025-12-01 14:05:32 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2025-12-01 14:04:08 | Putupaula (Kalu Ganga) | 4.22 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 14:03:47 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:03:27 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2025-12-01 14:03:19 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.049 |  |
| 2025-12-01 14:02:59 | Glencourse (Kelani Ganga) | 12.58 | 🟢 Normal | -0.071 |  |
| 2025-12-01 14:02:53 | Moraketiya (Walawe Ganga) | 1.89 | 🟢 Normal | 0.649 | 🔺 Rising |
| 2025-12-01 14:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.12 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 14:02:41 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.050 |  |
| 2025-12-01 14:02:36 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:02:32 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-01 14:02:22 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:02:21 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:02:18 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:02:12 | Horowpothana (Yan Oya) | 6.86 | 🟡 Alert | -0.124 |  |
| 2025-12-01 14:01:38 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-01 14:00:49 | Thanthirimale (Malwathu Oya) | 9.54 | 🔴 Major Flood | -0.123 |  |
| 2025-12-01 14:00:10 | Nakkala (Kumbukkan Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-01 13:20:43 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.013 |  |
| 2025-12-01 13:14:07 | Galgamuwa (Mee Oya) | 3.99 | 🟢 Normal | -0.172 |  |
| 2025-12-01 13:13:51 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.023 |  |
| 2025-12-01 13:13:19 | Holombuwa (Kelani Ganga) | 1.47 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 14:07:03 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | -0.014 |  |
| 2025-12-01 14:00:49 | Thanthirimale (Malwathu Oya) | 9.54 | 🔴 Major Flood | -0.123 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 14:04:08 | Putupaula (Kalu Ganga) | 4.22 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 14:06:01 | Ellagawa (Kalu Ganga) | 11.02 | 🟠 Minor Flood | -0.021 |  |
| 2025-12-01 14:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.12 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 14:07:48 | Hanwella (Kelani Ganga) | 8.94 | 🟠 Minor Flood | -0.084 |  |
| 2025-12-01 14:02:41 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.050 |  |
| 2025-12-01 13:09:10 | Rathnapura (Kalu Ganga) | 5.36 | 🟡 Alert | -0.068 |  |
| 2025-12-01 14:02:12 | Horowpothana (Yan Oya) | 6.86 | 🟡 Alert | -0.124 |  |
| 2025-12-01 14:02:53 | Moraketiya (Walawe Ganga) | 1.89 | 🟢 Normal | 0.649 | 🔺 Rising |
| 2025-12-01 14:03:27 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2025-12-01 14:06:34 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-01 14:02:22 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:08:27 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:02:18 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:03:47 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:02:36 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:12:03 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:09:10 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:02:21 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-01 14:01:38 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-01 14:02:32 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-01 14:07:33 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2025-12-01 13:00:17 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-01 14:00:10 | Nakkala (Kumbukkan Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-01 14:07:00 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.013 |  |
| 2025-12-01 14:05:32 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2025-12-01 14:09:43 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.021 |  |
| 2025-12-01 13:13:51 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.023 |  |
| 2025-12-01 14:06:39 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.031 |  |
| 2025-12-01 14:03:19 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.049 |  |
| 2025-12-01 14:02:59 | Glencourse (Kelani Ganga) | 12.58 | 🟢 Normal | -0.071 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-01 14:06:26 | Galgamuwa (Mee Oya) | 3.84 | 🟢 Normal | -0.172 |  |
| 2025-12-01 13:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)