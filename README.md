# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_11:12:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,027 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 11:12:35 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:11:24 | Weraganthota (Mahaweli Ganga) | -0.70 | 🟢 Normal | -0.318 |  |
| 2025-12-04 11:10:07 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:10:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-04 11:09:49 | Thanthirimale (Malwathu Oya) | 6.16 | 🟡 Alert | -0.035 |  |
| 2025-12-04 11:08:39 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:08:38 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.036 |  |
| 2025-12-04 11:08:29 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:07:16 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.005 |  |
| 2025-12-04 11:06:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:06:22 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 11:06:13 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-04 11:05:57 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.105 |  |
| 2025-12-04 11:05:55 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:05:37 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:04:37 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:04:35 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:04:33 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:04:19 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | -0.039 |  |
| 2025-12-04 11:04:11 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2025-12-04 11:03:31 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:02:52 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 11:02:46 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2025-12-04 11:02:33 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:02:09 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.048 |  |
| 2025-12-04 11:02:00 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.023 |  |
| 2025-12-04 11:01:58 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:01:38 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:01:33 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:01:29 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:01:16 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:01:09 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:01:08 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:00:51 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.041 |  |
| 2025-12-04 11:00:39 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:24:16 | Weraganthota (Mahaweli Ganga) | -0.45 | 🟢 Normal | -0.318 |  |
| 2025-12-04 10:20:27 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:20:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.105 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 11:09:49 | Thanthirimale (Malwathu Oya) | 6.16 | 🟡 Alert | -0.035 |  |
| 2025-12-04 11:02:52 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 11:10:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-04 09:05:02 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 11:06:22 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 11:01:09 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:08:39 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:03:31 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:05:55 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:04:37 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:00:39 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:01:29 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:04:33 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:06:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:12:35 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:10:07 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:01:16 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 11:07:16 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.005 |  |
| 2025-12-04 11:04:35 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:05:37 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:01:33 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:01:58 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:01:38 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:08:29 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:02:33 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:01:08 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-04 11:06:13 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-04 11:04:11 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2025-12-04 11:02:00 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.023 |  |
| 2025-12-04 11:08:38 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.036 |  |
| 2025-12-04 11:04:19 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | -0.039 |  |
| 2025-12-04 11:00:51 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.041 |  |
| 2025-12-04 11:02:46 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2025-12-04 11:02:09 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.048 |  |
| 2025-12-04 11:05:57 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.105 |  |
| 2025-12-04 11:11:24 | Weraganthota (Mahaweli Ganga) | -0.70 | 🟢 Normal | -0.318 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)