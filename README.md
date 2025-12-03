# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_04:16:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,770 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 04:16:21 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.008 |  |
| 2025-12-04 04:12:59 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:12:20 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:11:51 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:10:53 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 04:07:30 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-04 04:06:59 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:06:57 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-04 04:06:01 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.010 |  |
| 2025-12-04 04:05:06 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 04:05:06 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:03:42 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.005 |  |
| 2025-12-04 04:03:24 | Hanwella (Kelani Ganga) | 4.12 | 🟢 Normal | -0.067 |  |
| 2025-12-04 04:03:22 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.323 |  |
| 2025-12-04 04:03:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:03:02 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:03:02 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:02:41 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.035 |  |
| 2025-12-04 04:02:36 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:02:21 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.157 |  |
| 2025-12-04 04:02:20 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:01:46 | Thanthirimale (Malwathu Oya) | 6.48 | 🟡 Alert | -0.049 |  |
| 2025-12-04 04:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-04 04:01:17 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 04:01:46 | Thanthirimale (Malwathu Oya) | 6.48 | 🟡 Alert | -0.049 |  |
| 2025-12-04 04:05:06 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 04:07:30 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-04 04:10:53 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 03:06:50 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 03:02:53 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 04:12:20 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:01:17 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:02:36 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:02:20 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 02:10:20 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:03:02 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:03:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:17:00 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:05:06 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:06:59 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:03:00 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:12:59 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:03:02 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:10:27 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:11:51 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:03:42 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.005 |  |
| 2025-12-04 04:16:21 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.008 |  |
| 2025-12-04 04:06:01 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.010 |  |
| 2025-12-04 04:06:57 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-04 03:02:45 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2025-12-04 04:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-04 04:02:41 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.035 |  |
| 2025-12-04 04:03:24 | Hanwella (Kelani Ganga) | 4.12 | 🟢 Normal | -0.067 |  |
| 2025-12-04 03:09:33 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | -0.082 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-04 04:02:21 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.157 |  |
| 2025-12-04 04:03:22 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.323 |  |
| 2025-12-04 03:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -2.880 |  |
| 2025-12-03 18:03:18 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)