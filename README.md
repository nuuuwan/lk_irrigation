# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_23:06:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,520 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 23:06:58 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2025-12-10 23:06:29 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.009 |  |
| 2025-12-10 23:06:21 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:06:14 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:05:38 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 23:04:56 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.009 |  |
| 2025-12-10 23:04:26 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:04:21 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-10 23:04:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 23:03:56 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:03:48 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:03:30 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.042 |  |
| 2025-12-10 23:02:56 | Yaka Wewa (Ma Oya) | 1.55 | 🟢 Normal | -0.039 |  |
| 2025-12-10 23:02:42 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-10 23:02:34 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2025-12-10 23:02:16 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:49 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:37 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-10 23:01:25 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:07 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-10 23:01:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-10 23:00:48 | Horowpothana (Yan Oya) | 5.18 | 🟢 Normal | -0.106 |  |
| 2025-12-10 23:00:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 22:32:34 | Horowpothana (Yan Oya) | 5.23 | 🟢 Normal | -0.106 |  |
| 2025-12-10 22:32:24 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2025-12-10 22:14:21 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:10:11 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 23:04:21 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-10 22:02:21 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-10 23:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 23:04:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 23:05:38 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-10 23:00:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 23:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:03:48 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:06:14 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:03:56 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:25 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:04:26 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:56 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:49 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:02:16 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:06:21 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-10 23:01:37 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:10:11 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2025-12-10 23:06:29 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.009 |  |
| 2025-12-10 23:04:56 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.009 |  |
| 2025-12-10 22:04:44 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-10 23:02:42 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-10 23:01:07 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-10 23:06:58 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2025-12-10 23:02:34 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2025-12-10 22:05:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2025-12-10 23:01:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-10 23:02:56 | Yaka Wewa (Ma Oya) | 1.55 | 🟢 Normal | -0.039 |  |
| 2025-12-10 23:03:30 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.042 |  |
| 2025-12-10 22:02:43 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.073 |  |
| 2025-12-10 22:06:26 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.097 |  |
| 2025-12-10 23:00:48 | Horowpothana (Yan Oya) | 5.18 | 🟢 Normal | -0.106 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)