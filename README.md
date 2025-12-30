# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_02:42:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,425 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 02:42:57 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-31 02:28:17 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:19:55 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:14:54 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:09:54 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:07:02 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:07:02 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-31 02:06:16 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:05:23 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.005 |  |
| 2025-12-31 02:05:19 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:05:05 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2025-12-31 02:05:01 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:04:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:04:13 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:03:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:03:05 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:02:58 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.049 |  |
| 2025-12-31 02:02:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-31 02:02:36 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-31 02:02:11 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:02:08 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2025-12-31 02:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:43 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:40 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:35 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:12 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:00:42 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:57:18 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:54:59 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 02:42:57 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 18:03:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 01:00:49 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 00:03:57 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 02:01:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:02:30 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:40 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:02:11 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:05:01 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:35 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:57:18 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:28:17 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:14:54 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:01:12 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:06:16 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:19:55 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:04:13 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:09:54 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:16:37 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:00:42 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:04:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:03:05 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:34 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:05:19 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:07:02 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:03:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:05:23 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.005 |  |
| 2025-12-31 02:07:02 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-30 23:01:41 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-31 02:02:36 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-31 02:05:05 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2025-12-30 20:16:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.029 |  |
| 2025-12-31 01:26:32 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2025-12-31 02:02:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-31 02:02:08 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2025-12-31 02:02:58 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)