# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_14:27:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,508 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 14:27:18 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.023 |  |
| 2025-12-08 14:20:54 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.048 |  |
| 2025-12-08 14:13:03 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.014 |  |
| 2025-12-08 14:12:56 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2025-12-08 14:09:51 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.035 |  |
| 2025-12-08 14:07:28 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:07:18 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:07:12 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:06:59 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.028 |  |
| 2025-12-08 14:05:59 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:05:52 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.076 |  |
| 2025-12-08 14:05:17 | Galgamuwa (Mee Oya) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-08 14:05:02 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:05:02 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:04:50 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.091 |  |
| 2025-12-08 14:04:39 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 14:04:31 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:03:57 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:03:46 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2025-12-08 14:03:41 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:03:32 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.051 |  |
| 2025-12-08 14:03:25 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.287 |  |
| 2025-12-08 14:03:13 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.078 |  |
| 2025-12-08 14:02:51 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 14:02:39 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:02:37 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.039 |  |
| 2025-12-08 14:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2025-12-08 14:02:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-08 14:02:08 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | -0.439 |  |
| 2025-12-08 14:01:55 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -1.638 |  |
| 2025-12-08 14:01:43 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:01:41 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-08 14:01:28 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2025-12-08 14:01:26 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:01:21 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-08 14:00:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:00:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 14:01:28 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2025-12-08 14:01:41 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-08 14:05:17 | Galgamuwa (Mee Oya) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-08 14:02:51 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 14:04:39 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 14:01:55 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:01:43 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:01:26 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:05:02 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:00:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:00:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:04:31 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:07:18 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:05:59 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:02:39 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:03:57 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:03:41 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:07:12 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:07:28 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:05:02 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:01:21 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-08 14:13:03 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.014 |  |
| 2025-12-08 14:02:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-08 14:12:56 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2025-12-08 14:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2025-12-08 14:03:46 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2025-12-08 14:27:18 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.023 |  |
| 2025-12-08 14:06:59 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.028 |  |
| 2025-12-08 14:09:51 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.035 |  |
| 2025-12-08 14:02:37 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.039 |  |
| 2025-12-08 14:20:54 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.048 |  |
| 2025-12-08 14:03:32 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.051 |  |
| 2025-12-08 14:05:52 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.076 |  |
| 2025-12-08 14:03:13 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.078 |  |
| 2025-12-08 14:04:50 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.091 |  |
| 2025-12-08 14:03:25 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.287 |  |
| 2025-12-08 14:02:08 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | -0.439 |  |
| 2025-12-08 14:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -1.638 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)