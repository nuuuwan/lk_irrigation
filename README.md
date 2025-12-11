# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_04:06:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,529 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 04:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-12 04:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-12 04:05:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-12 04:05:39 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:05:35 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:05:29 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.012 |  |
| 2025-12-12 04:05:23 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.072 |  |
| 2025-12-12 04:05:14 | Nakkala (Kumbukkan Oya) | 1.61 | 🟢 Normal | -0.068 |  |
| 2025-12-12 04:04:28 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2025-12-12 04:03:40 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2025-12-12 04:03:31 | Padiyathalawa (Maduru Oya) | 2.25 | 🟢 Normal | -0.267 |  |
| 2025-12-12 04:03:11 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-12 04:02:57 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2025-12-12 04:02:32 | Yaka Wewa (Ma Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2025-12-12 04:02:30 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:02:28 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.100 |  |
| 2025-12-12 04:02:16 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-12 04:02:14 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:01:51 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-12 04:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:01:36 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2025-12-12 04:01:35 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.032 |  |
| 2025-12-12 04:00:27 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 03:26:49 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:26:47 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:15:18 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.012 |  |
| 2025-12-12 03:13:31 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.008 |  |
| 2025-12-12 03:11:04 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:09:17 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-12 03:08:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2025-12-12 03:08:13 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2025-12-12 03:08:12 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.022 |  |
| 2025-12-12 03:07:57 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.247 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 04:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-12 04:01:36 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2025-12-12 04:04:28 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 04:02:57 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2025-12-12 03:09:17 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-12 04:02:16 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-12 03:02:23 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-12 04:03:11 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-12 03:03:26 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 03:03:33 | Horowpothana (Yan Oya) | 4.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-12 04:00:27 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 04:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:02:30 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:26:49 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:02:14 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:05:35 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:05:39 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:11:04 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:13:31 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.008 |  |
| 2025-12-12 04:01:51 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-12 04:05:29 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.012 |  |
| 2025-12-12 03:05:57 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2025-12-12 04:02:32 | Yaka Wewa (Ma Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2025-12-12 03:08:12 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.022 |  |
| 2025-12-12 04:01:35 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.032 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-12 04:03:40 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2025-12-12 03:02:21 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.049 |  |
| 2025-12-12 04:05:14 | Nakkala (Kumbukkan Oya) | 1.61 | 🟢 Normal | -0.068 |  |
| 2025-12-12 04:05:23 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.072 |  |
| 2025-12-12 03:07:33 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | -0.074 |  |
| 2025-12-12 03:02:28 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | -0.083 |  |
| 2025-12-12 04:02:28 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.100 |  |
| 2025-12-12 03:03:16 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.125 |  |
| 2025-12-12 04:03:31 | Padiyathalawa (Maduru Oya) | 2.25 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)