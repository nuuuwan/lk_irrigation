# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_12:13:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,843 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 12:13:49 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:10:08 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.046 |  |
| 2025-12-12 12:07:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:07:20 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-12 12:06:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 12:05:50 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:05:12 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 12:04:56 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:04:53 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.059 |  |
| 2025-12-12 12:04:40 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:04:32 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:04:20 | Manampitiya (Mahaweli Ganga) | 3.35 | 🟡 Alert | -0.052 |  |
| 2025-12-12 12:04:14 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2025-12-12 12:04:03 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 12:03:55 | Padiyathalawa (Maduru Oya) | 1.46 | 🟢 Normal | -0.012 |  |
| 2025-12-12 12:03:24 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:03:20 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.121 |  |
| 2025-12-12 12:03:08 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 12:02:56 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:02:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:02:50 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2025-12-12 12:02:43 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:02:43 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:02:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-12 12:02:40 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.074 |  |
| 2025-12-12 12:02:36 | Moragaswewa (Deduru Oya) | 1.69 | 🟢 Normal | -0.053 |  |
| 2025-12-12 12:02:30 | Weraganthota (Mahaweli Ganga) | -0.60 | 🟢 Normal | -0.157 |  |
| 2025-12-12 12:02:26 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:02:07 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:02:07 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:02:05 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.063 |  |
| 2025-12-12 12:01:46 | Thanthirimale (Malwathu Oya) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 12:01:44 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:01:15 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 12:00:37 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2025-12-12 12:00:26 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 12:04:20 | Manampitiya (Mahaweli Ganga) | 3.35 | 🟡 Alert | -0.052 |  |
| 2025-12-12 11:02:11 | Horowpothana (Yan Oya) | 5.88 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-12 12:07:20 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-12 12:03:08 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 12:06:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 12:05:12 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 12:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 12:04:03 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 12:01:46 | Thanthirimale (Malwathu Oya) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 12:01:15 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:05:50 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:02:43 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:04:32 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:02:26 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:13:49 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:00:26 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:02:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:04:56 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:03:24 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:02:07 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:02:56 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:03:55 | Padiyathalawa (Maduru Oya) | 1.46 | 🟢 Normal | -0.012 |  |
| 2025-12-12 12:02:50 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2025-12-12 12:01:44 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:02:07 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:02:43 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:04:40 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2025-12-12 12:00:37 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2025-12-12 12:02:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-12 11:11:32 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2025-12-12 12:10:08 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.046 |  |
| 2025-12-12 12:04:14 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2025-12-12 12:02:36 | Moragaswewa (Deduru Oya) | 1.69 | 🟢 Normal | -0.053 |  |
| 2025-12-12 12:04:53 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.059 |  |
| 2025-12-12 12:02:05 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.063 |  |
| 2025-12-12 12:02:40 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.074 |  |
| 2025-12-12 12:03:20 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.121 |  |
| 2025-12-12 12:02:30 | Weraganthota (Mahaweli Ganga) | -0.60 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)