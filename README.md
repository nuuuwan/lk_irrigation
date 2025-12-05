# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_04:05:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 04:05:32 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:05:25 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.032 |  |
| 2025-12-06 04:05:00 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.048 |  |
| 2025-12-06 04:04:39 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.021 |  |
| 2025-12-06 04:04:36 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-06 04:04:26 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:04:00 | Yaka Wewa (Ma Oya) | 6.80 | 🔴 Major Flood | 314.471 | 🔺 Rising |
| 2025-12-06 04:03:46 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2025-12-06 04:03:09 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.024 |  |
| 2025-12-06 04:02:52 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 314.471 | 🔺 Rising |
| 2025-12-06 04:02:29 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:02:28 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:02:01 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-06 04:01:35 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.050 |  |
| 2025-12-06 04:01:33 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-06 04:01:19 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.183 |  |
| 2025-12-06 04:01:00 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.064 |  |
| 2025-12-06 03:28:17 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.032 |  |
| 2025-12-06 03:17:34 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.006 |  |
| 2025-12-06 03:14:12 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.064 |  |
| 2025-12-06 03:12:32 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:12:06 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.024 |  |
| 2025-12-06 03:10:35 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-06 03:09:43 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:09:21 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-06 03:07:56 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:07:51 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:07:27 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.064 |  |
| 2025-12-06 03:07:17 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.049 |  |
| 2025-12-06 03:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.15 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-06 03:06:53 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.021 |  |
| 2025-12-06 03:06:28 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 04:04:00 | Yaka Wewa (Ma Oya) | 6.80 | 🔴 Major Flood | 314.471 | 🔺 Rising |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 03:04:29 | Magura (Kalu Ganga) | 4.49 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2025-12-06 03:03:35 | Thanthirimale (Malwathu Oya) | 6.78 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 03:09:21 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-06 04:02:01 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-06 04:04:36 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-06 04:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-06 03:02:12 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 03:10:35 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-06 03:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:06:28 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:02:28 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:03:46 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:16:18 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:02:29 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:04:26 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:05:32 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:05:51 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:01:33 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:03:48 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.003 |  |
| 2025-12-06 03:17:34 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.006 |  |
| 2025-12-06 03:04:35 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-06 04:03:46 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2025-12-06 03:00:42 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-06 04:04:39 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.021 |  |
| 2025-12-06 04:03:09 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.024 |  |
| 2025-12-06 04:05:25 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.032 |  |
| 2025-12-06 04:05:00 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.048 |  |
| 2025-12-06 03:07:17 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.049 |  |
| 2025-12-06 04:01:35 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.050 |  |
| 2025-12-06 04:01:00 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.064 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |
| 2025-12-06 04:01:19 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.183 |  |
| 2025-12-06 03:03:32 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)