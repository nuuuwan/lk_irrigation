# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_09:17:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 09:17:14 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.038 |  |
| 2025-12-24 09:15:19 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-24 09:08:20 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-24 09:08:00 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2025-12-24 09:07:59 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-24 09:07:53 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2025-12-24 09:06:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.163 |  |
| 2025-12-24 09:06:54 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2025-12-24 09:06:24 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-24 09:06:15 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:05:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.090 |  |
| 2025-12-24 09:05:09 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:05:05 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.013 |  |
| 2025-12-24 09:05:04 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2025-12-24 09:05:03 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2025-12-24 09:05:02 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 09:05:00 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2025-12-24 09:04:54 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:04:40 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:04:03 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:38 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:27 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:08 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:07 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2025-12-24 09:03:07 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.118 |  |
| 2025-12-24 09:02:40 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:02:26 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-24 09:02:21 | Thanthirimale (Malwathu Oya) | 2.48 | 🟢 Normal | -0.039 |  |
| 2025-12-24 09:02:08 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 09:01:39 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-24 09:01:34 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 09:01:32 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:01:17 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:01:16 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 09:01:11 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:00:20 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 09:03:07 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2025-12-24 09:05:04 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2025-12-24 09:08:20 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-24 09:06:54 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2025-12-24 09:15:19 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-24 09:02:26 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-24 09:01:39 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-24 09:05:02 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 09:02:08 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 09:01:16 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 09:01:34 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 09:03:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:01:11 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:01:17 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:01:32 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:04:03 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:00:20 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:38 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:08 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:05:09 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:06:15 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:04:54 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:04:40 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:27 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:02:40 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:03:07 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 09:05:03 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2025-12-24 09:07:59 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-24 09:06:24 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-24 09:05:05 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.013 |  |
| 2025-12-24 09:07:53 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2025-12-24 09:05:00 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2025-12-24 09:08:00 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2025-12-24 09:17:14 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.038 |  |
| 2025-12-24 09:02:21 | Thanthirimale (Malwathu Oya) | 2.48 | 🟢 Normal | -0.039 |  |
| 2025-12-24 09:05:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.090 |  |
| 2025-12-24 09:03:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.118 |  |
| 2025-12-24 09:06:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)