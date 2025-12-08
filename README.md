# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_08:26:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,276 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 08:26:55 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:19:25 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:17:15 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:16:56 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.016 |  |
| 2025-12-08 08:15:07 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2025-12-08 08:12:31 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | -0.067 |  |
| 2025-12-08 08:10:38 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.027 |  |
| 2025-12-08 08:08:06 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 08:06:28 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 08:06:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.038 |  |
| 2025-12-08 08:05:59 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:05:31 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.011 |  |
| 2025-12-08 08:04:57 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.040 |  |
| 2025-12-08 08:04:52 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 08:04:40 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.072 |  |
| 2025-12-08 08:04:12 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2025-12-08 08:04:02 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.080 |  |
| 2025-12-08 08:03:56 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.062 |  |
| 2025-12-08 08:03:49 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:03:43 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-08 08:03:19 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-08 08:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-08 08:03:01 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.004 |  |
| 2025-12-08 08:02:37 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.059 |  |
| 2025-12-08 08:02:25 | Weraganthota (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.697 | 🔺 Rising |
| 2025-12-08 08:02:21 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:02:15 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-08 08:02:14 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:02:09 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-08 08:01:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.091 |  |
| 2025-12-08 08:01:28 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:01:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.063 |  |
| 2025-12-08 08:01:11 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2025-12-08 08:01:11 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 08:01:04 | Thanthirimale (Malwathu Oya) | 4.65 | 🟢 Normal | -0.126 |  |
| 2025-12-08 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:00:16 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 07:44:51 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 08:02:25 | Weraganthota (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.697 | 🔺 Rising |
| 2025-12-08 08:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-08 08:03:43 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-08 08:06:28 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 08:04:52 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 08:01:11 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 08:08:06 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 08:03:01 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.004 |  |
| 2025-12-08 08:00:16 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:26:55 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:05:59 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:03:49 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:02:14 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:19:25 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:02:21 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:01:28 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:08:55 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.002 |  |
| 2025-12-08 08:15:07 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2025-12-08 08:02:15 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-08 08:02:09 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-08 08:04:12 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2025-12-08 08:05:31 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.011 |  |
| 2025-12-08 08:03:19 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-08 08:16:56 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.016 |  |
| 2025-12-08 08:01:11 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2025-12-08 08:10:38 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.027 |  |
| 2025-12-08 08:06:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.038 |  |
| 2025-12-08 08:04:57 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.040 |  |
| 2025-12-08 08:02:37 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.059 |  |
| 2025-12-08 08:03:56 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.062 |  |
| 2025-12-08 08:01:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.063 |  |
| 2025-12-08 08:12:31 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | -0.067 |  |
| 2025-12-08 08:04:40 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.072 |  |
| 2025-12-08 08:04:02 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.080 |  |
| 2025-12-08 08:01:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.091 |  |
| 2025-12-08 08:01:04 | Thanthirimale (Malwathu Oya) | 4.65 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)