# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_07:22:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 07:22:35 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:14:38 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-07 07:13:54 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.027 |  |
| 2025-12-07 07:12:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:11:39 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-07 07:09:52 | Galgamuwa (Mee Oya) | 1.59 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-07 07:09:45 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.035 |  |
| 2025-12-07 07:09:06 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:09:05 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.019 |  |
| 2025-12-07 07:08:25 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2025-12-07 07:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.156 |  |
| 2025-12-07 07:06:26 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:06:23 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.019 |  |
| 2025-12-07 07:05:47 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:05:45 | Weraganthota (Mahaweli Ganga) | 1.54 | 🟢 Normal | 11.597 | 🔺 Rising |
| 2025-12-07 07:05:32 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:05:28 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:05:05 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:05:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.090 |  |
| 2025-12-07 07:04:53 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:04:42 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-07 07:04:37 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:04:32 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:04:30 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2025-12-07 07:04:20 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2025-12-07 07:04:01 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:03:28 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.035 |  |
| 2025-12-07 07:03:22 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:02:55 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:02:26 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 07:02:25 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:01:34 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:01:26 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-07 07:01:19 | Thanthirimale (Malwathu Oya) | 6.19 | 🟡 Alert | -0.059 |  |
| 2025-12-07 07:01:04 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:00:04 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:50:23 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 11.597 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 07:01:19 | Thanthirimale (Malwathu Oya) | 6.19 | 🟡 Alert | -0.059 |  |
| 2025-12-07 07:05:45 | Weraganthota (Mahaweli Ganga) | 1.54 | 🟢 Normal | 11.597 | 🔺 Rising |
| 2025-12-07 07:04:42 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-07 07:02:26 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 07:11:39 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-07 07:09:52 | Galgamuwa (Mee Oya) | 1.59 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-07 07:01:26 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-07 07:14:38 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-07 07:12:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:00:04 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:05:28 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:02:55 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:05:47 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:01:04 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:03:22 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:01:34 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:05:32 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:09:06 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:04:37 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:06:26 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:22:35 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 07:08:25 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2025-12-07 07:04:32 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:04:01 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:05:05 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:02:25 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:04:53 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-07 07:04:30 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2025-12-07 07:06:23 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.019 |  |
| 2025-12-07 07:09:05 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.019 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 07:04:20 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2025-12-07 07:13:54 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.027 |  |
| 2025-12-07 07:03:28 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.035 |  |
| 2025-12-07 07:09:45 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.035 |  |
| 2025-12-07 07:05:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.090 |  |
| 2025-12-07 07:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)