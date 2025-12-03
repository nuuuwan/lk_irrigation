# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_23:22:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 23:22:39 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:15:39 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.034 |  |
| 2025-12-03 23:12:50 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.009 |  |
| 2025-12-03 23:10:37 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:09:52 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:06:18 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:06:00 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-03 23:05:23 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:05:17 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.088 |  |
| 2025-12-03 23:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.338 |  |
| 2025-12-03 23:04:46 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:04:41 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.040 |  |
| 2025-12-03 23:04:35 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:04:26 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:04:09 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:03:58 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | -0.084 |  |
| 2025-12-03 23:03:37 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-03 23:02:52 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:02:43 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:02:38 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:02:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:02:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.139 |  |
| 2025-12-03 23:02:00 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-03 23:01:44 | Yaka Wewa (Ma Oya) | 1.68 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2025-12-03 23:01:28 | Thanthirimale (Malwathu Oya) | 6.72 | 🟡 Alert | -0.039 |  |
| 2025-12-03 23:01:08 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 23:01:28 | Thanthirimale (Malwathu Oya) | 6.72 | 🟡 Alert | -0.039 |  |
| 2025-12-03 23:01:44 | Yaka Wewa (Ma Oya) | 1.68 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2025-12-03 21:00:44 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 23:02:38 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:01:08 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:10:37 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:04:35 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:05:23 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:57 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:09:52 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:06:18 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:04:09 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:14:02 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:04:46 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:02:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:04:37 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:02:43 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:02:52 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:22:39 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:01:19 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 23:04:26 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:18:19 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.008 |  |
| 2025-12-03 23:12:50 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.009 |  |
| 2025-12-03 23:02:00 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-03 23:06:00 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-03 23:03:37 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-03 23:15:39 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.034 |  |
| 2025-12-03 23:04:41 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.040 |  |
| 2025-12-03 22:32:49 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.068 |  |
| 2025-12-03 23:03:58 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | -0.084 |  |
| 2025-12-03 23:05:17 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.088 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-03 23:02:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.139 |  |
| 2025-12-03 23:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.338 |  |
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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)