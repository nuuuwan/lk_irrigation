# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_01:49:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,854 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 01:49:18 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:20:30 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:11:46 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:10:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:06:36 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:06:35 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:06:22 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.028 |  |
| 2025-12-27 01:06:18 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.012 |  |
| 2025-12-27 01:05:57 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:05:19 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:03:27 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:03:26 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:03:18 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:03:09 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:02:56 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 01:02:42 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2025-12-27 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2025-12-27 01:02:25 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 14.595 | 🔺 Rising |
| 2025-12-27 01:02:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2025-12-27 01:02:22 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:02:22 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.020 |  |
| 2025-12-27 01:02:21 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:01:40 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:01:24 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:01:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-27 01:01:11 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 14.595 | 🔺 Rising |
| 2025-12-27 01:01:00 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:00:33 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-27 01:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 01:02:25 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 14.595 | 🔺 Rising |
| 2025-12-27 00:05:29 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-27 01:00:33 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-27 01:01:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-27 01:02:56 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 00:02:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 00:00:17 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:02:21 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:03:27 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:05:57 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:01:40 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:49:18 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:03:18 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-26 23:03:48 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:10:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:02:22 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:06:35 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:01:24 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 00:04:02 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:20:30 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-27 01:05:19 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-27 00:06:34 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:03:09 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:06:36 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:11:46 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2025-12-27 00:00:36 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:01:00 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-27 01:02:42 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2025-12-27 01:06:18 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.012 |  |
| 2025-12-27 01:02:22 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.020 |  |
| 2025-12-26 22:00:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.022 |  |
| 2025-12-27 01:06:22 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.028 |  |
| 2025-12-26 18:05:51 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-27 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2025-12-27 01:02:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2025-12-27 00:04:06 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)