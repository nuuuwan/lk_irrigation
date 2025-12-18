# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_23:07:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,670 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 23:07:56 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2025-12-18 23:07:53 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:05:17 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | -0.074 |  |
| 2025-12-18 23:05:08 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2025-12-18 23:05:06 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-18 23:05:05 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:04:58 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | -0.081 |  |
| 2025-12-18 23:04:54 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:04:42 | Manampitiya (Mahaweli Ganga) | 4.93 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2025-12-18 23:04:37 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:04:21 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:04:01 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:03:37 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:03:31 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:03:17 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:03:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:02:48 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:02:47 | Horowpothana (Yan Oya) | 5.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-18 23:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:02:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:02:16 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:02:15 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:02:11 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:01:59 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-18 23:01:58 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 23:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 23:00:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2025-12-18 23:00:43 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:00:14 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.051 |  |
| 2025-12-18 22:15:05 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:09:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 23:04:42 | Manampitiya (Mahaweli Ganga) | 4.93 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-18 23:00:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2025-12-18 22:07:57 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-18 23:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 23:02:47 | Horowpothana (Yan Oya) | 5.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 23:01:58 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 23:01:59 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-18 23:03:31 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:02:11 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:02:16 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:04:54 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 23:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:03:17 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:03:37 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:02:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:04:21 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:02:15 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:07:53 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:05:05 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:08:12 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:04:01 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:01:17 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:09:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2025-12-18 23:07:56 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2025-12-18 23:04:37 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:02:48 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:02:34 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:03:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:00:43 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-18 23:05:06 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-18 22:01:08 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2025-12-18 23:05:08 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2025-12-18 22:08:40 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.030 |  |
| 2025-12-18 23:00:14 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.051 |  |
| 2025-12-18 23:05:17 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | -0.074 |  |
| 2025-12-18 23:04:58 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)