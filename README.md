# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_22:21:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 22:21:27 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-20 22:17:46 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-20 22:16:59 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-20 22:11:58 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-20 22:09:20 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:07:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:06:41 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | -0.018 |  |
| 2025-12-20 22:06:24 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-20 22:06:14 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:05:27 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:05:24 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2025-12-20 22:04:45 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:04:28 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:04:23 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.005 |  |
| 2025-12-20 22:04:14 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-20 22:04:08 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:03:58 | Manampitiya (Mahaweli Ganga) | 3.29 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2025-12-20 22:03:40 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:03:31 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-20 22:03:30 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-20 22:02:59 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 22:02:30 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-20 22:02:27 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:02:27 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-20 22:02:09 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:02:06 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-20 22:01:58 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:47 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:30 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:29 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2025-12-20 22:01:16 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:09 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-20 22:01:07 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:07 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-20 22:00:56 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:00:50 | Horowpothana (Yan Oya) | 6.18 | 🟡 Alert | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 22:03:58 | Manampitiya (Mahaweli Ganga) | 3.29 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2025-12-20 22:00:50 | Horowpothana (Yan Oya) | 6.18 | 🟡 Alert | -0.039 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-20 22:05:24 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2025-12-20 22:16:59 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-20 22:02:30 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-20 22:04:14 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-20 22:06:24 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-20 22:03:30 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-20 22:02:06 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-20 22:17:46 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-20 22:02:59 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 22:11:58 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-20 22:21:27 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-20 22:01:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-20 22:01:09 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:06:14 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:47 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:04:45 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:04:08 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:03:40 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:07:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:00:56 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:30 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:09:20 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:02:09 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:02:27 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:05:27 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:01:16 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:04:28 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:04:23 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.005 |  |
| 2025-12-20 22:03:31 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-20 22:02:27 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-20 22:01:07 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-20 22:01:29 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2025-12-20 22:06:41 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | -0.018 |  |
| 2025-12-20 21:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)