# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_04:06:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,047 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 04:06:10 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.187 |  |
| 2025-12-26 04:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-26 04:05:34 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:05:15 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-26 04:04:32 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:04:14 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:04:08 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-26 04:03:52 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:03:36 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-26 04:03:17 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:02:47 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-26 04:01:41 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:01:33 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-26 04:01:18 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:00:45 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-26 04:00:14 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.043 |  |
| 2025-12-26 03:59:00 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:35:42 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.021 |  |
| 2025-12-26 03:33:01 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:24:12 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:23:53 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:21:01 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:20:31 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.006 |  |
| 2025-12-26 03:19:57 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-26 03:18:37 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-26 03:16:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-26 03:12:46 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-26 03:12:14 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.009 |  |
| 2025-12-26 03:08:52 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2025-12-26 03:08:25 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:08:24 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:08:13 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 03:08:52 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2025-12-26 03:16:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-26 03:19:57 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 04:04:08 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-26 04:05:15 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-26 04:02:47 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-26 02:03:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-26 04:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-26 04:03:36 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-26 04:01:41 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:04:14 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:01:02 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:01:18 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:04:14 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:03:17 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:05:34 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:07:18 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:07:08 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:21:01 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:03:52 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 04:04:32 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:08:25 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:24:12 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:02:31 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 02:00:12 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.005 |  |
| 2025-12-26 03:20:31 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.006 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-26 03:12:14 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.009 |  |
| 2025-12-26 03:02:14 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2025-12-26 04:00:45 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-26 03:04:47 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 04:01:33 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-26 03:35:42 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.021 |  |
| 2025-12-26 04:00:14 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.043 |  |
| 2025-12-26 03:02:28 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.054 |  |
| 2025-12-26 04:06:10 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.187 |  |

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)