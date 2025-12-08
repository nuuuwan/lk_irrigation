# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_11:18:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,389 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 11:18:07 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-08 11:13:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.074 |  |
| 2025-12-08 11:11:24 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-08 11:10:33 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:10:31 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.041 |  |
| 2025-12-08 11:08:56 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:08:01 | Galgamuwa (Mee Oya) | 1.45 | 🟢 Normal | -0.019 |  |
| 2025-12-08 11:07:13 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.022 |  |
| 2025-12-08 11:06:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.132 |  |
| 2025-12-08 11:06:13 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-08 11:05:57 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:05:38 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:04:26 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-08 11:04:11 | Thanthirimale (Malwathu Oya) | 4.40 | 🟢 Normal | -0.076 |  |
| 2025-12-08 11:04:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:03:40 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:03:36 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:03:32 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.091 |  |
| 2025-12-08 11:03:24 | Weraganthota (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2025-12-08 11:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 11:03:13 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.060 |  |
| 2025-12-08 11:03:08 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.081 |  |
| 2025-12-08 11:02:51 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.042 |  |
| 2025-12-08 11:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -1.768 |  |
| 2025-12-08 11:02:43 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:02:22 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.221 |  |
| 2025-12-08 11:02:19 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:02:14 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 11:02:06 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-08 11:01:47 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:42 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:31 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:26 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-08 11:01:19 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:18 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-08 11:01:01 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:00:55 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-08 11:00:13 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-08 10:28:28 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-08 10:24:56 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 11:03:24 | Weraganthota (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2025-12-08 11:04:26 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-08 11:18:07 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-08 10:01:14 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 11:02:14 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 11:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 11:02:43 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:47 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:31 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:08:56 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:03:40 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:05:57 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:02:19 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:04:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:19 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:00:13 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:03:36 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:10:33 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:01:42 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 11:11:24 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-08 11:01:18 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-08 11:01:26 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-08 11:00:55 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-08 11:02:06 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-08 11:08:01 | Galgamuwa (Mee Oya) | 1.45 | 🟢 Normal | -0.019 |  |
| 2025-12-08 11:07:13 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.022 |  |
| 2025-12-08 11:06:13 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-08 11:10:31 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.041 |  |
| 2025-12-08 11:02:51 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.042 |  |
| 2025-12-08 11:03:13 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.060 |  |
| 2025-12-08 11:13:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.074 |  |
| 2025-12-08 11:04:11 | Thanthirimale (Malwathu Oya) | 4.40 | 🟢 Normal | -0.076 |  |
| 2025-12-08 11:03:08 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.081 |  |
| 2025-12-08 11:03:32 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.091 |  |
| 2025-12-08 11:06:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.132 |  |
| 2025-12-08 11:02:22 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.221 |  |
| 2025-12-08 11:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -1.768 |  |
| 2025-12-08 10:01:16 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -9.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)