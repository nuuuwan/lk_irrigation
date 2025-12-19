# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_13:05:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,187 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 13:05:12 | Padiyathalawa (Maduru Oya) | 2.95 | 🟢 Normal | 0.609 | 🔺 Rising |
| 2025-12-19 13:05:06 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:05:02 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:04:54 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:33 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:16 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:09 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:05 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 13:04:00 | Manampitiya (Mahaweli Ganga) | 4.66 | 🟠 Minor Flood | -0.038 |  |
| 2025-12-19 13:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-19 13:03:56 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-19 13:03:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.013 |  |
| 2025-12-19 13:03:37 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:03:33 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:03:25 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-19 13:03:24 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2025-12-19 13:03:18 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:02:52 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:02:19 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2025-12-19 13:02:19 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.030 |  |
| 2025-12-19 13:02:09 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:01:51 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:01:45 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:01:31 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.000 |  |
| 2025-12-19 13:01:26 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:01:08 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:00:48 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2025-12-19 13:00:10 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:00:08 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2025-12-19 12:17:19 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.013 |  |
| 2025-12-19 12:09:57 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:08:23 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:08:21 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:07:49 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:07:39 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:06:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:06:46 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 13:04:00 | Manampitiya (Mahaweli Ganga) | 4.66 | 🟠 Minor Flood | -0.038 |  |
| 2025-12-19 12:01:31 | Horowpothana (Yan Oya) | 6.21 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2025-12-19 13:01:31 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.000 |  |
| 2025-12-19 13:05:12 | Padiyathalawa (Maduru Oya) | 2.95 | 🟢 Normal | 0.609 | 🔺 Rising |
| 2025-12-19 13:02:19 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2025-12-19 12:05:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-19 13:03:25 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-19 13:04:05 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 13:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-19 13:01:51 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:01:45 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:03:33 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:09:57 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:02:09 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:02:52 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:07:49 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:54 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:09 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:16 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:03:37 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:05:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:01:08 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:04:33 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:03:18 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:01:26 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:05:06 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:05:02 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:00:10 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:04:22 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:03:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.013 |  |
| 2025-12-19 13:00:08 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2025-12-19 13:00:48 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2025-12-19 13:03:56 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-19 13:02:19 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.030 |  |
| 2025-12-19 12:05:25 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.040 |  |
| 2025-12-19 13:03:24 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2025-12-19 11:03:34 | Weraganthota (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.863 |  |
| 2025-12-19 12:04:44 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)