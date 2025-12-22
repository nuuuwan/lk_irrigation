# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_04:43:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,385 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 04:43:22 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:42:48 | Horowpothana (Yan Oya) | 3.04 | 🟢 Normal | -0.018 |  |
| 2025-12-23 04:33:37 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:31:33 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-23 04:27:29 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.007 |  |
| 2025-12-23 04:21:54 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:21:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-23 04:17:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:17:01 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:17:00 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:16:58 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:16:57 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:16:56 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:13:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-23 04:12:55 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:08:27 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-23 04:08:26 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-23 04:08:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:08:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2025-12-23 04:07:23 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:58 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:54 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:44 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:06 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:05:36 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.019 |  |
| 2025-12-23 04:05:27 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:04:29 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.009 |  |
| 2025-12-23 04:04:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:47 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:25 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.069 |  |
| 2025-12-23 04:02:21 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:09 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:08 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:01:59 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 04:01:40 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:01:31 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 04:01:14 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 04:01:10 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:01:05 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 04:13:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-23 04:08:26 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-23 04:21:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-23 04:01:14 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 04:01:59 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 04:31:33 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-23 04:12:55 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:08 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:43:22 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:21 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:54 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:47 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:10:44 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:01:05 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:08:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:33:37 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:07:23 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:21:54 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:02:09 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:01:40 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:17:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:04:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:44 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:06 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:06:58 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 04:27:29 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.007 |  |
| 2025-12-23 04:08:27 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-23 04:04:29 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.009 |  |
| 2025-12-23 04:01:31 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:06:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2025-12-23 04:42:48 | Horowpothana (Yan Oya) | 3.04 | 🟢 Normal | -0.018 |  |
| 2025-12-23 04:05:36 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.019 |  |
| 2025-12-23 04:08:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-23 04:02:25 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.069 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)