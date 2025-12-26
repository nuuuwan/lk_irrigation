# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_05:15:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 05:15:31 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-27 05:14:02 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-27 05:08:52 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 05:08:06 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-27 05:07:28 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:07:27 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:06:43 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2025-12-27 05:06:01 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:06:01 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:05:29 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-27 05:05:27 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.019 |  |
| 2025-12-27 05:05:00 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-27 05:04:42 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.040 |  |
| 2025-12-27 05:04:03 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.098 |  |
| 2025-12-27 05:03:18 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:03:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:03:02 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:58 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:52 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2025-12-27 05:02:51 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:47 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:38 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:36 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-27 05:02:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -71.562 |  |
| 2025-12-27 05:02:24 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:04 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.284 |  |
| 2025-12-27 05:01:44 | Nagalagam Street (Kelani Ganga) | 1.58 | 🟠 Minor Flood | -71.562 |  |
| 2025-12-27 05:01:32 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:01:29 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-27 05:01:12 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 05:00:20 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-27 05:00:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2025-12-27 04:35:25 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.019 |  |
| 2025-12-27 04:21:34 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-27 04:20:40 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 05:05:00 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-27 05:01:29 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-27 05:15:31 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-27 05:08:52 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 05:01:12 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 05:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:06:01 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:03:02 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:51 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:58 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:38 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:06:01 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:04:03 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:03:18 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:01:32 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:03:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:47 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 00:04:02 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:15:39 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:02:24 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:19:02 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2025-12-27 05:08:06 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-27 05:02:36 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-27 05:00:20 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-27 05:14:02 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-27 04:01:10 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2025-12-27 05:05:29 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-27 05:05:27 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.019 |  |
| 2025-12-27 05:06:43 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2025-12-27 05:02:52 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2025-12-26 18:05:51 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-27 05:00:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2025-12-27 05:04:42 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.040 |  |
| 2025-12-27 05:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.098 |  |
| 2025-12-27 05:02:04 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.284 |  |
| 2025-12-27 05:07:28 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:02:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -71.562 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)