# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_09:11:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 09:11:22 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:10:23 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2025-12-11 09:09:01 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:08:33 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.101 |  |
| 2025-12-11 09:07:45 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:06:30 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.059 |  |
| 2025-12-11 09:06:04 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:05:16 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-11 09:05:15 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 09:05:11 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:04:43 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2025-12-11 09:04:37 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:04:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-11 09:04:03 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:03:46 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.020 |  |
| 2025-12-11 09:03:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:03:26 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.045 |  |
| 2025-12-11 09:03:22 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:03:14 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 09:02:42 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:02:37 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2025-12-11 09:02:35 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:02:32 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 09:02:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.153 |  |
| 2025-12-11 09:02:11 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 09:02:09 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.062 |  |
| 2025-12-11 09:02:07 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-11 09:01:58 | Weraganthota (Mahaweli Ganga) | -1.13 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2025-12-11 09:01:58 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:01:55 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2025-12-11 09:01:31 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 09:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:01:27 | Horowpothana (Yan Oya) | 4.65 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:01:25 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.024 |  |
| 2025-12-11 09:00:57 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:00:37 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.032 |  |
| 2025-12-11 09:00:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2025-12-11 09:00:20 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-11 09:00:17 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 09:01:58 | Weraganthota (Mahaweli Ganga) | -1.13 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2025-12-11 09:05:16 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-11 09:02:11 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 09:03:14 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 09:01:31 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 09:02:32 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 09:01:58 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:00:17 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:04:37 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:01:27 | Horowpothana (Yan Oya) | 4.65 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:02:42 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:03:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:00:57 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:02:09 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:07:45 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:03:22 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:09:01 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:05:11 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:06:04 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:02:35 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:11:22 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:10:23 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2025-12-11 09:05:15 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 09:02:07 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-11 09:04:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-11 09:00:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2025-12-11 09:04:43 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2025-12-11 09:03:46 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.020 |  |
| 2025-12-11 09:00:20 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-11 09:01:25 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.024 |  |
| 2025-12-11 09:02:37 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2025-12-11 09:00:37 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.032 |  |
| 2025-12-11 09:03:26 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.045 |  |
| 2025-12-11 09:06:30 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.059 |  |
| 2025-12-11 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.062 |  |
| 2025-12-11 09:08:33 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.101 |  |
| 2025-12-11 09:02:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)