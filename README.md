# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_11:06:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,864 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 11:06:00 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:59 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:48 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2025-12-05 11:04:50 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | -0.030 |  |
| 2025-12-05 11:04:30 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2025-12-05 11:03:58 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.064 |  |
| 2025-12-05 11:03:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.044 |  |
| 2025-12-05 11:03:48 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.040 |  |
| 2025-12-05 11:03:38 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:03:35 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:49 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.055 |  |
| 2025-12-05 11:02:47 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.273 |  |
| 2025-12-05 11:02:27 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:19 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-05 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2025-12-05 11:02:14 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2025-12-05 11:02:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:01:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-05 11:01:38 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:01:31 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:01:14 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.155 |  |
| 2025-12-05 11:00:39 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:00:30 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:24:08 | Thanthirimale (Malwathu Oya) | 6.18 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2025-12-05 10:14:01 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-05 10:10:55 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.050 |  |
| 2025-12-05 10:10:31 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.155 |  |
| 2025-12-05 10:09:12 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.044 |  |
| 2025-12-05 10:08:58 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:56 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2025-12-05 10:08:22 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2025-12-05 10:08:19 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:07 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.064 |  |
| 2025-12-05 10:07:53 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.273 |  |
| 2025-12-05 10:07:52 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.055 |  |
| 2025-12-05 10:06:57 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.037 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 10:24:08 | Thanthirimale (Malwathu Oya) | 6.18 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2025-12-05 11:01:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-05 11:02:19 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-05 10:03:12 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 11:02:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:02:41 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:06:00 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:05:33 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:03:35 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:48 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:03:23 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:19 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:01:31 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:03:38 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:59 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:27 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:00:39 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:00:30 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:01:38 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:02:14 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2025-12-05 11:04:30 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2025-12-05 10:08:56 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2025-12-05 11:04:50 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | -0.030 |  |
| 2025-12-05 10:06:57 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.037 |  |
| 2025-12-05 11:05:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2025-12-05 11:03:48 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.040 |  |
| 2025-12-05 11:03:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.044 |  |
| 2025-12-05 10:10:55 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.050 |  |
| 2025-12-05 11:02:49 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.055 |  |
| 2025-12-05 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2025-12-05 11:03:58 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.064 |  |
| 2025-12-05 10:01:29 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.092 |  |
| 2025-12-05 11:01:14 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.155 |  |
| 2025-12-05 10:10:31 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.155 |  |
| 2025-12-05 11:02:47 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)