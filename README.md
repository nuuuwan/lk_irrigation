# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_01:01:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 01:01:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-21 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.029 |  |
| 2025-12-21 01:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:36 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 01:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:05 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:33:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-21 00:20:53 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-21 00:18:48 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2025-12-21 00:13:37 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2025-12-21 00:09:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:09:00 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.019 |  |
| 2025-12-21 00:09:00 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-21 00:06:24 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-21 00:06:21 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:06:20 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-21 00:06:02 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-21 00:05:47 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-21 00:05:06 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 00:04:45 | Manampitiya (Mahaweli Ganga) | 3.42 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2025-12-21 00:04:34 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-21 00:03:36 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-21 00:03:20 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2025-12-21 00:03:17 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 00:04:45 | Manampitiya (Mahaweli Ganga) | 3.42 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2025-12-21 00:02:10 | Horowpothana (Yan Oya) | 6.13 | 🟡 Alert | -0.046 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-21 00:03:20 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2025-12-21 00:06:02 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-21 00:18:48 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2025-12-21 00:01:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-21 00:09:00 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-21 00:06:20 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-21 00:01:42 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-21 01:01:36 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 00:04:34 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-20 23:03:37 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 00:20:53 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-20 23:07:14 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 00:05:06 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 00:01:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:00:19 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:01:43 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:03:17 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:09:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:06:21 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:01:36 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:05 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:03:36 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-21 00:05:47 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-21 01:01:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-21 00:02:11 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2025-12-21 00:01:24 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-21 00:02:20 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.013 |  |
| 2025-12-21 00:06:24 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-21 00:09:00 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.019 |  |
| 2025-12-21 00:33:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-21 00:02:41 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2025-12-21 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)