# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_20:25:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 20:25:25 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.028 |  |
| 2025-12-06 20:08:38 | Thanthirimale (Malwathu Oya) | 6.61 | 🟡 Alert | -0.069 |  |
| 2025-12-06 20:07:00 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.039 |  |
| 2025-12-06 20:06:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -0.037 |  |
| 2025-12-06 20:06:43 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.022 |  |
| 2025-12-06 20:06:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2025-12-06 20:06:19 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.064 |  |
| 2025-12-06 20:06:08 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-06 20:05:58 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:35 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:05:21 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:20 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:12 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:07 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 20:05:03 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:00 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:04:57 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:04:42 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:04:35 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.091 |  |
| 2025-12-06 20:03:41 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.011 |  |
| 2025-12-06 20:03:20 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:03:06 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.062 |  |
| 2025-12-06 20:02:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:50 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-06 20:02:39 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2025-12-06 20:02:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.134 |  |
| 2025-12-06 20:02:28 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:05 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:02:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:19 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:10 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:00:20 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-06 19:35:03 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:34:03 | Thanthirimale (Malwathu Oya) | 6.65 | 🟡 Alert | -0.069 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 20:08:38 | Thanthirimale (Malwathu Oya) | 6.61 | 🟡 Alert | -0.069 |  |
| 2025-12-06 20:06:08 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-06 20:05:07 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 20:02:50 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-06 20:01:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:10 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:12 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:21 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:20 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:28 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:04:57 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:58 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:19 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:03:20 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:03 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:35 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:00:20 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:02:05 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:04:42 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:03:41 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-06 20:02:39 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2025-12-06 20:06:43 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.022 |  |
| 2025-12-06 20:25:25 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.028 |  |
| 2025-12-06 20:06:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2025-12-06 20:06:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -0.037 |  |
| 2025-12-06 20:07:00 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.039 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-06 20:03:06 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.062 |  |
| 2025-12-06 20:06:19 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.064 |  |
| 2025-12-06 20:04:35 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.091 |  |
| 2025-12-06 20:02:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)