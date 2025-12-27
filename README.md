# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_10:10:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,181 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 10:10:15 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2025-12-27 10:09:50 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:07:09 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.038 |  |
| 2025-12-27 10:06:07 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:05:56 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:05:54 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2025-12-27 10:05:35 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:05:20 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.009 |  |
| 2025-12-27 10:05:18 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-27 10:04:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.094 |  |
| 2025-12-27 10:04:44 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.097 |  |
| 2025-12-27 10:04:31 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:04:26 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 10:03:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:03:24 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.078 |  |
| 2025-12-27 10:03:17 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 10:03:13 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:03:12 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2025-12-27 10:03:06 | Weraganthota (Mahaweli Ganga) | -1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-27 10:03:03 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:02:51 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 10:02:45 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:02:45 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.110 |  |
| 2025-12-27 10:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 10:01:32 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:29 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:25 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:01:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:16 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:10 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:00:38 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.310 |  |
| 2025-12-27 10:00:20 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:00:09 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:58:42 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.310 |  |
| 2025-12-27 09:13:18 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-27 09:12:43 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 09:13:18 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-27 10:03:06 | Weraganthota (Mahaweli Ganga) | -1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-27 10:03:17 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 10:02:51 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 10:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 10:04:26 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 10:01:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:00:20 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:16 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:03:03 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:29 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:04:31 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:10 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:03:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:01:32 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:05:56 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:09:50 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:02:45 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:07:09 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:07:08 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:00:09 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:10:15 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2025-12-27 10:05:20 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.009 |  |
| 2025-12-27 10:01:25 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:06:07 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:05:35 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:03:13 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:05:18 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-27 10:03:12 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:09:49 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:03:27 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2025-12-27 10:05:54 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2025-12-27 09:10:01 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.029 |  |
| 2025-12-27 10:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.038 |  |
| 2025-12-27 10:03:24 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.078 |  |
| 2025-12-27 10:04:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.094 |  |
| 2025-12-27 10:04:44 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.097 |  |
| 2025-12-27 10:02:45 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.110 |  |
| 2025-12-27 10:00:38 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.310 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)