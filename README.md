# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_12:08:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 12:08:30 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:07:26 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2025-12-28 12:07:23 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:06:18 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:06:09 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:05:43 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:05:28 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:05:05 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-28 12:04:55 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:04:49 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:28 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:14 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.070 |  |
| 2025-12-28 12:04:12 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:11 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:03:43 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:03:22 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.105 |  |
| 2025-12-28 12:03:21 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:03:13 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:03:03 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:02:59 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2025-12-28 12:02:40 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:02:29 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-28 12:02:17 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-28 12:02:12 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:02:09 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:48 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:46 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.199 |  |
| 2025-12-28 12:01:44 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2025-12-28 12:01:43 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:42 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.031 |  |
| 2025-12-28 12:01:40 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:34 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:01:27 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.011 |  |
| 2025-12-28 12:01:19 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:01 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.050 |  |
| 2025-12-28 12:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:00:23 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-28 12:02:17 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-28 12:02:12 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:40 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:01:13 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:02:09 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:03:03 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:03:21 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:08:30 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:43 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:11 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:49 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:02:29 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:06:18 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:05:43 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:12 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:04:28 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:06:09 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:48 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:01:10 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:07:23 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:02:40 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 12:05:05 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-28 12:04:55 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:05:28 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:03:43 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:01:34 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:00:23 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:01:19 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-28 12:01:44 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2025-12-28 12:01:27 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.011 |  |
| 2025-12-28 12:01:42 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.031 |  |
| 2025-12-28 12:02:59 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2025-12-28 12:01:01 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.050 |  |
| 2025-12-28 12:07:26 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2025-12-28 12:04:14 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.070 |  |
| 2025-12-28 12:03:22 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.105 |  |
| 2025-12-28 12:01:46 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)