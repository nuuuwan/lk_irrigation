# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_16:16:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,312 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 16:16:21 | Manampitiya (Mahaweli Ganga) | 4.46 | 🟠 Minor Flood | -0.064 |  |
| 2025-12-19 16:13:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:11:50 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:11:20 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:09:32 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2025-12-19 16:09:12 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:07:38 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-19 16:06:59 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2025-12-19 16:06:41 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:06:18 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:05:52 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:05:38 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.019 |  |
| 2025-12-19 16:05:32 | Thanthirimale (Malwathu Oya) | 5.43 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2025-12-19 16:05:04 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:05:00 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2025-12-19 16:04:39 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:04:30 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2025-12-19 16:03:41 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:03:39 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 16:02:45 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:02:38 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:02:36 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2025-12-19 16:02:21 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:02:14 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.060 |  |
| 2025-12-19 16:02:01 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:01:59 | Moragaswewa (Deduru Oya) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 16:01:50 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:01:45 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2025-12-19 16:01:26 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:01:24 | Weraganthota (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-19 16:01:22 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:01:20 | Horowpothana (Yan Oya) | 6.27 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2025-12-19 16:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:01:15 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:00:39 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:00:31 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 16:16:21 | Manampitiya (Mahaweli Ganga) | 4.46 | 🟠 Minor Flood | -0.064 |  |
| 2025-12-19 16:05:32 | Thanthirimale (Malwathu Oya) | 5.43 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2025-12-19 16:01:20 | Horowpothana (Yan Oya) | 6.27 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2025-12-19 16:04:30 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2025-12-19 16:01:24 | Weraganthota (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-19 16:03:39 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 16:01:59 | Moragaswewa (Deduru Oya) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 16:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-19 16:01:22 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:02:21 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:07:11 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:06:18 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:11:20 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:06:41 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:02:38 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:11:50 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:13:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:00:39 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:07:38 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:09:12 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:03:14 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:04:39 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:07:06 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 16:01:50 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:05:04 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:03:41 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:05:52 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:02:45 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:02:01 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:01:15 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:01:26 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-19 16:01:45 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2025-12-19 16:05:38 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.019 |  |
| 2025-12-19 16:02:36 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2025-12-19 16:09:32 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2025-12-19 16:05:00 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2025-12-19 16:06:59 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2025-12-19 16:02:14 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)