# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_20:15:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,571 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 20:15:20 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:15:09 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 20:12:24 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.414 | 🔺 Rising |
| 2025-12-27 20:11:15 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.023 |  |
| 2025-12-27 20:09:15 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:08:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:08:15 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.087 |  |
| 2025-12-27 20:08:00 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.014 |  |
| 2025-12-27 20:05:45 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:05:23 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.041 |  |
| 2025-12-27 20:05:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2025-12-27 20:05:04 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:04:20 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 20:04:17 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:04:00 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2025-12-27 20:03:56 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:54 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.015 |  |
| 2025-12-27 20:02:46 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:31 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:30 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:27 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2025-12-27 20:02:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:08 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.020 |  |
| 2025-12-27 20:01:55 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.320 |  |
| 2025-12-27 20:01:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-27 20:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:01:49 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:01:31 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-27 20:01:27 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2025-12-27 20:01:22 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 20:01:12 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:00:59 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-27 20:00:37 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:00:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-27 19:43:52 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:26:25 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.014 |  |
| 2025-12-27 19:23:09 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.015 |  |
| 2025-12-27 19:19:51 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-27 19:19:39 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 20:12:24 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.414 | 🔺 Rising |
| 2025-12-27 20:01:31 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-27 20:01:22 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 20:15:09 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 20:00:59 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-27 20:04:20 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:04:17 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:15:20 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:09:15 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:07:07 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:31 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:05:04 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:08:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:46 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:03:56 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:05:45 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:02:30 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:00:37 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:01:12 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:01:49 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:01:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 20:00:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-27 20:04:00 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2025-12-27 20:01:27 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2025-12-27 20:08:00 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.014 |  |
| 2025-12-27 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.015 |  |
| 2025-12-27 19:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.018 |  |
| 2025-12-27 20:02:08 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.020 |  |
| 2025-12-27 20:11:15 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.023 |  |
| 2025-12-27 20:05:23 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.041 |  |
| 2025-12-27 20:02:27 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2025-12-27 20:05:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2025-12-27 20:08:15 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.087 |  |
| 2025-12-27 20:01:55 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.320 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)