# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_08:17:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 08:17:54 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:15:51 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-19 08:12:49 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:10:51 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.036 |  |
| 2025-12-19 08:07:23 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.023 |  |
| 2025-12-19 08:06:29 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2025-12-19 08:06:13 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 08:06:05 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:05:49 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.080 |  |
| 2025-12-19 08:05:44 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:05:28 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | 0.000 |  |
| 2025-12-19 08:04:26 | Manampitiya (Mahaweli Ganga) | 4.85 | 🟠 Minor Flood | -0.038 |  |
| 2025-12-19 08:04:09 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.029 |  |
| 2025-12-19 08:03:54 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.068 |  |
| 2025-12-19 08:03:50 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-19 08:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.097 |  |
| 2025-12-19 08:03:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.116 |  |
| 2025-12-19 08:03:13 | Galgamuwa (Mee Oya) | 1.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-19 08:03:06 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:57 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 08:02:57 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-19 08:02:22 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:17 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:16 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-19 08:02:14 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:08 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2025-12-19 08:01:58 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.040 |  |
| 2025-12-19 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 08:01:39 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2025-12-19 08:01:31 | Horowpothana (Yan Oya) | 6.02 | 🟡 Alert | 0.000 |  |
| 2025-12-19 08:01:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-19 08:01:08 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:00:39 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-19 07:48:26 | Horowpothana (Yan Oya) | 6.02 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 08:04:26 | Manampitiya (Mahaweli Ganga) | 4.85 | 🟠 Minor Flood | -0.038 |  |
| 2025-12-19 08:01:31 | Horowpothana (Yan Oya) | 6.02 | 🟡 Alert | 0.000 |  |
| 2025-12-19 08:05:28 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | 0.000 |  |
| 2025-12-19 07:00:52 | Weraganthota (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2025-12-19 08:02:16 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-19 08:03:13 | Galgamuwa (Mee Oya) | 1.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-19 07:02:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 08:06:13 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 08:02:57 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 07:02:52 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 08:02:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:01:08 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:12:49 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:17:54 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:57 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:14 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:05:44 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:22 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:03:06 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:06:05 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 08:02:17 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:21:28 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.007 |  |
| 2025-12-19 08:01:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-19 08:00:39 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-19 08:02:08 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2025-12-19 08:15:51 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-19 08:03:50 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-19 08:06:29 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2025-12-19 08:07:23 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.023 |  |
| 2025-12-19 08:04:09 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.029 |  |
| 2025-12-19 08:01:39 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2025-12-19 08:02:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-19 08:10:51 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.036 |  |
| 2025-12-19 08:01:58 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.040 |  |
| 2025-12-19 08:03:54 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.068 |  |
| 2025-12-19 08:05:49 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.080 |  |
| 2025-12-19 08:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.097 |  |
| 2025-12-19 08:03:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)