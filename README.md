# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_18:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 18:13:08 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2025-12-06 18:12:34 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:07:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.084 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:44 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.046 |  |
| 2025-12-06 18:06:33 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-06 18:06:04 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.042 |  |
| 2025-12-06 18:05:43 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:05:30 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:05:00 | Thanthirimale (Malwathu Oya) | 6.69 | 🟡 Alert | -0.039 |  |
| 2025-12-06 18:04:47 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-06 18:04:44 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:04:43 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.023 |  |
| 2025-12-06 18:04:10 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.040 |  |
| 2025-12-06 18:04:09 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 18:03:51 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:03:46 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 18:03:40 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.048 |  |
| 2025-12-06 18:03:09 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.021 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-06 18:02:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.063 |  |
| 2025-12-06 18:02:20 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:02:12 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:02:11 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:02:11 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-06 18:02:00 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:01:42 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:01:29 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.073 |  |
| 2025-12-06 18:01:28 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:01:26 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:00:21 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.015 |  |
| 2025-12-06 17:20:42 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.015 |  |
| 2025-12-06 17:16:43 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 18:05:00 | Thanthirimale (Malwathu Oya) | 6.69 | 🟡 Alert | -0.039 |  |
| 2025-12-06 18:04:47 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-06 18:03:46 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 18:04:09 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 18:02:11 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-06 18:01:42 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:01:28 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:01:26 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:02:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:05:43 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:05:43 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:03:51 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:07:36 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:02:00 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:05:30 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 18:04:44 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:33 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:02:20 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:02:12 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:12:34 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-06 18:00:21 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.015 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:02:11 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:03:09 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.021 |  |
| 2025-12-06 18:04:43 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.023 |  |
| 2025-12-06 18:04:10 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.040 |  |
| 2025-12-06 18:13:08 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2025-12-06 18:06:04 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.042 |  |
| 2025-12-06 18:06:44 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.046 |  |
| 2025-12-06 18:03:40 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.048 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-06 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.063 |  |
| 2025-12-06 18:01:29 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.073 |  |
| 2025-12-06 18:07:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)