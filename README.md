# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_05:04:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,073 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 05:04:12 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:11 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.015 |  |
| 2025-12-26 05:03:39 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-26 05:03:20 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 05:03:18 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:02:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:56 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:36 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.227 |  |
| 2025-12-26 05:01:07 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2025-12-26 05:01:06 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.040 |  |
| 2025-12-26 05:00:22 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2025-12-26 04:31:31 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:31:02 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.040 |  |
| 2025-12-26 04:23:06 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.015 |  |
| 2025-12-26 04:22:45 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.015 |  |
| 2025-12-26 04:22:31 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-26 04:19:25 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:17:20 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:12:12 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:09:34 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-26 04:08:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-26 04:08:05 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:06:40 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-26 04:06:39 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:06:10 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.227 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 03:08:52 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2025-12-26 04:08:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-26 04:22:31 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 04:04:08 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-26 04:05:15 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-26 04:02:47 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-26 02:03:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-26 04:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-26 04:03:36 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-26 05:03:20 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 05:02:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:03:18 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:01:18 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:19:25 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:03:17 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:07:18 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:07:08 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:03:39 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:03:52 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:04:32 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:17:20 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:56 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:12 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:12 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.005 |  |
| 2025-12-26 03:20:31 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.006 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-26 03:12:14 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.009 |  |
| 2025-12-26 05:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-26 04:06:40 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-26 04:00:45 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-26 05:01:07 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2025-12-26 05:04:11 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.015 |  |
| 2025-12-26 03:35:42 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.021 |  |
| 2025-12-26 05:01:06 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.040 |  |
| 2025-12-26 05:00:22 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2025-12-26 05:01:36 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.227 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)