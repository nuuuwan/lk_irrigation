# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_22:14:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,492 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 22:14:21 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:10:11 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2025-12-10 22:06:26 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.097 |  |
| 2025-12-10 22:06:05 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-10 22:06:04 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2025-12-10 22:05:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2025-12-10 22:04:44 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-10 22:04:42 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-10 22:04:33 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:04:03 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2025-12-10 22:03:52 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2025-12-10 22:03:36 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:03:26 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-10 22:03:13 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:03:03 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-10 22:02:51 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-10 22:02:43 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.073 |  |
| 2025-12-10 22:02:33 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-10 22:02:28 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:02:21 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-10 22:01:56 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.003 |  |
| 2025-12-10 22:01:43 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:42 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-10 22:01:16 | Yaka Wewa (Ma Oya) | 1.59 | 🟢 Normal | -0.060 |  |
| 2025-12-10 22:01:10 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.011 |  |
| 2025-12-10 22:01:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.034 |  |
| 2025-12-10 22:01:06 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:00:40 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:00:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 22:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-10 22:04:42 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-10 22:02:21 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 22:03:26 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-10 21:07:20 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 22:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.003 |  |
| 2025-12-10 22:00:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:43 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:14:21 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:02:35 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:03:13 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:56 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:03:36 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:02:28 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:06 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:01:42 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:04:33 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-10 22:10:11 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2025-12-10 22:06:05 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-10 22:04:44 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-10 22:03:03 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-10 22:02:33 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-10 22:04:03 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2025-12-10 22:01:10 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.011 |  |
| 2025-12-10 22:06:04 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2025-12-10 22:02:51 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-10 22:05:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2025-12-10 22:03:52 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2025-12-10 22:01:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.034 |  |
| 2025-12-10 22:01:16 | Yaka Wewa (Ma Oya) | 1.59 | 🟢 Normal | -0.060 |  |
| 2025-12-10 22:02:43 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.073 |  |
| 2025-12-10 22:06:26 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.097 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)