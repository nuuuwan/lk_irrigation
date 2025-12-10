# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_21:10:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,459 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 21:10:52 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:42 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.079 |  |
| 2025-12-10 21:09:23 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2025-12-10 21:09:12 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:01 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:08:20 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:08:04 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.009 |  |
| 2025-12-10 21:08:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2025-12-10 21:07:48 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.013 |  |
| 2025-12-10 21:07:20 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 21:07:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2025-12-10 21:06:31 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-10 21:05:59 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:05:24 | Panadugama (Nilwala Ganga) | 3.42 | 🟢 Normal | -0.049 |  |
| 2025-12-10 21:04:49 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2025-12-10 21:04:12 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:04:11 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-10 21:04:07 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-10 21:03:51 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-10 21:03:45 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-10 21:03:34 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2025-12-10 21:03:21 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:03:07 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-10 21:02:56 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:56 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:36 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:35 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:07 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:06 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:01:56 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 21:01:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-10 21:00:52 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | -0.132 |  |
| 2025-12-10 21:00:15 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:26:05 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:21:46 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 21:07:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2025-12-10 21:03:51 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 21:04:07 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-10 21:01:56 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 21:07:20 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 21:00:15 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:56 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:35 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:06 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:56 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:05:59 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:10:52 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:12 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:36 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:13:22 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:03:21 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:07 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:01 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:08:04 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.009 |  |
| 2025-12-10 21:09:23 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2025-12-10 21:06:31 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-10 21:04:11 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-10 21:01:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-10 21:03:34 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2025-12-10 21:07:48 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.013 |  |
| 2025-12-10 21:03:07 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-10 21:03:45 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-10 21:04:49 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2025-12-10 21:08:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2025-12-10 21:05:24 | Panadugama (Nilwala Ganga) | 3.42 | 🟢 Normal | -0.049 |  |
| 2025-12-10 21:09:42 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.079 |  |
| 2025-12-10 21:00:52 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | -0.132 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)