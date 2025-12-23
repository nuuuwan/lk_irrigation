# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_15:16:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,801 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 15:16:26 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:09:36 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.009 |  |
| 2025-12-23 15:06:03 | Manampitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.060 |  |
| 2025-12-23 15:05:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.045 |  |
| 2025-12-23 15:05:22 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:05:10 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:05:09 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:04:38 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:04:25 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:04:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:03:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-23 15:03:55 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:03:39 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:03:34 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.122 |  |
| 2025-12-23 15:03:24 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:03:16 | Thanthirimale (Malwathu Oya) | 3.19 | 🟢 Normal | -0.038 |  |
| 2025-12-23 15:03:11 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2025-12-23 15:03:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-23 15:03:02 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-23 15:02:44 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.089 |  |
| 2025-12-23 15:02:28 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-23 15:02:26 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 15:02:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:17 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:11 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:02:06 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.133 |  |
| 2025-12-23 15:02:05 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:01:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:01:51 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:01:25 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:01:23 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.072 |  |
| 2025-12-23 15:01:14 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:01:14 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:01:03 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.299 |  |
| 2025-12-23 15:00:07 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 15:03:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-23 15:02:28 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-23 15:03:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-23 15:02:26 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 15:01:14 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-23 14:03:12 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:44 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:04:38 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:05 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:17 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:03:24 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:01:25 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:03:39 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:01:51 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:05:09 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:16:26 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:05:10 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:02:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 15:09:36 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.009 |  |
| 2025-12-23 15:05:22 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:03:55 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:01:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:04:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:00:07 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:02:11 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:04:25 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:01:14 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-23 15:03:02 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-23 15:03:11 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2025-12-23 15:03:16 | Thanthirimale (Malwathu Oya) | 3.19 | 🟢 Normal | -0.038 |  |
| 2025-12-23 15:05:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.045 |  |
| 2025-12-23 15:06:03 | Manampitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.060 |  |
| 2025-12-23 15:01:23 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.072 |  |
| 2025-12-23 15:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.089 |  |
| 2025-12-23 15:03:34 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.122 |  |
| 2025-12-23 15:02:06 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.133 |  |
| 2025-12-23 15:01:03 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)