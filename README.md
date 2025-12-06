# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_16:05:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,886 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 16:05:28 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:04:52 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:04:43 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2025-12-06 16:04:26 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 16:04:12 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:03:58 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:03:45 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:03:26 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.050 |  |
| 2025-12-06 16:03:12 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-06 16:03:11 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2025-12-06 16:03:10 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-06 16:02:55 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.020 |  |
| 2025-12-06 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:02:46 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 16:02:43 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:02:41 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:02:30 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2025-12-06 16:01:59 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:01:46 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:01:38 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.050 |  |
| 2025-12-06 16:01:36 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:01:33 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:01:32 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:01:13 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:01:10 | Thanthirimale (Malwathu Oya) | 6.77 | 🟡 Alert | -0.050 |  |
| 2025-12-06 16:00:45 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:00:33 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.041 |  |
| 2025-12-06 15:21:18 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 15:12:25 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.017 |  |
| 2025-12-06 15:10:45 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 15:10:37 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-06 15:07:05 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.031 |  |
| 2025-12-06 15:06:35 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 16:01:10 | Thanthirimale (Malwathu Oya) | 6.77 | 🟡 Alert | -0.050 |  |
| 2025-12-06 15:21:18 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 16:03:12 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-06 16:02:46 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 16:04:26 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 16:04:12 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:02:43 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 15:01:12 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:27 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-06 15:10:45 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:01:46 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 15:10:37 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:04:52 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:02:41 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:01:36 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:03:58 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:00:45 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:01:32 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:01:13 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:05:28 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-06 15:00:17 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:03:45 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:01:59 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 15:04:42 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2025-12-06 15:12:25 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.017 |  |
| 2025-12-06 16:03:10 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-06 16:02:55 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.020 |  |
| 2025-12-06 16:04:43 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2025-12-06 16:02:30 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2025-12-06 15:07:05 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.031 |  |
| 2025-12-06 16:00:33 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.041 |  |
| 2025-12-06 16:03:26 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.050 |  |
| 2025-12-06 16:01:38 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.050 |  |
| 2025-12-06 16:03:11 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2025-12-06 15:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | -0.089 |  |
| 2025-12-06 15:05:53 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)