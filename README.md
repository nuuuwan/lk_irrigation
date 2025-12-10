# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_19:21:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,387 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 19:21:52 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:16:43 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.024 |  |
| 2025-12-10 19:15:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:14:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-10 19:12:46 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-10 19:12:22 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-10 19:08:50 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:06:53 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2025-12-10 19:06:19 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:06:14 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.009 |  |
| 2025-12-10 19:05:43 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:05:28 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:05:13 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.021 |  |
| 2025-12-10 19:04:51 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-10 19:04:45 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:04:39 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:04:33 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 19:03:38 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.083 |  |
| 2025-12-10 19:03:37 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2025-12-10 19:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:03:30 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 19:02:57 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:50 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:20 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.097 |  |
| 2025-12-10 19:01:58 | Yaka Wewa (Ma Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-10 19:01:12 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:00:59 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:00:29 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:00:27 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 19:04:51 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-10 19:12:46 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 19:03:30 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 19:04:33 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 19:14:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-10 18:02:50 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 19:12:22 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-10 19:06:19 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:15:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:50 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:21:52 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:00:27 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:57 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:08:50 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:02:20 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:01:12 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:06:14 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.009 |  |
| 2025-12-10 19:04:45 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:05:28 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:04:39 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:05:43 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:00:29 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:02:49 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:02:56 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:00:59 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-10 19:06:53 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2025-12-10 19:01:58 | Yaka Wewa (Ma Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-10 19:05:13 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.021 |  |
| 2025-12-10 19:16:43 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.024 |  |
| 2025-12-10 19:03:37 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2025-12-10 19:03:38 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.083 |  |
| 2025-12-10 19:02:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.097 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)