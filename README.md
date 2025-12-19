# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_04:10:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 04:10:48 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.008 |  |
| 2025-12-20 04:07:59 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.005 |  |
| 2025-12-20 04:07:45 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:07:05 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:06:32 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.112 |  |
| 2025-12-20 04:06:15 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 04:05:53 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 04:04:43 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-20 04:03:59 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2025-12-20 04:03:49 | Manampitiya (Mahaweli Ganga) | 4.22 | 🟡 Alert | -0.010 |  |
| 2025-12-20 04:03:40 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:03:27 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:03:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2025-12-20 04:03:09 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:02:54 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-20 04:02:11 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-20 04:02:10 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:02:01 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.018 |  |
| 2025-12-20 04:01:59 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-20 04:01:38 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:01:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2025-12-20 04:01:11 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:01:06 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2025-12-20 04:00:49 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:00:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:00:21 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:59:53 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:29:10 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-20 02:04:29 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 04:03:49 | Manampitiya (Mahaweli Ganga) | 4.22 | 🟡 Alert | -0.010 |  |
| 2025-12-20 04:02:11 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-20 01:09:42 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-20 04:01:59 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-20 04:06:15 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 04:04:43 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-20 04:02:54 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-20 04:05:53 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 04:00:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:01:14 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:01:38 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:01:11 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:07:45 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:07:05 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:02:10 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:03:27 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:11:32 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:06:32 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-20 03:09:18 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 04:07:59 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.005 |  |
| 2025-12-20 04:10:48 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.008 |  |
| 2025-12-20 03:03:46 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:03:40 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:03:09 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:00:49 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:03:59 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2025-12-20 04:02:01 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.018 |  |
| 2025-12-20 04:01:06 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2025-12-20 04:03:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2025-12-20 03:01:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.036 |  |
| 2025-12-20 03:07:24 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -0.049 |  |
| 2025-12-20 03:08:14 | Glencourse (Kelani Ganga) | 9.01 | 🟢 Normal | -0.082 |  |
| 2025-12-20 04:01:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2025-12-20 04:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)