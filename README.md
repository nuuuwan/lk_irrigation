# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_15:08:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 15:08:56 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-18 15:08:19 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 15:07:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-18 15:06:25 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 15:06:10 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 15:06:01 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:05:39 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2025-12-18 15:04:05 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:03:40 | Weraganthota (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-18 15:03:26 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2025-12-18 15:03:24 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:03:22 | Galgamuwa (Mee Oya) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 15:03:21 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:03:10 | Manampitiya (Mahaweli Ganga) | 4.36 | 🟠 Minor Flood | 0.160 | 🔺 Rising |
| 2025-12-18 15:03:00 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:54 | Nakkala (Kumbukkan Oya) | 2.56 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-18 15:02:43 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:02:20 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.216 |  |
| 2025-12-18 15:02:18 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-18 15:02:18 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:16 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2025-12-18 15:02:14 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:11 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:09 | Thanthirimale (Malwathu Oya) | 5.18 | 🟡 Alert | 0.139 | 🔺 Rising |
| 2025-12-18 15:02:09 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:00 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:01:57 | Siyambalanduwa (Heda Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:01:49 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.058 |  |
| 2025-12-18 15:01:35 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-18 15:01:35 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.047 |  |
| 2025-12-18 15:01:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:00:26 | Horowpothana (Yan Oya) | 5.32 | 🟢 Normal | -36.000 |  |
| 2025-12-18 15:00:25 | Horowpothana (Yan Oya) | 5.33 | 🟢 Normal | -36.000 |  |
| 2025-12-18 15:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:58:15 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:19:40 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-18 14:12:27 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:12:21 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2025-12-18 14:11:22 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 15:03:10 | Manampitiya (Mahaweli Ganga) | 4.36 | 🟠 Minor Flood | 0.160 | 🔺 Rising |
| 2025-12-18 15:02:09 | Thanthirimale (Malwathu Oya) | 5.18 | 🟡 Alert | 0.139 | 🔺 Rising |
| 2025-12-18 15:03:40 | Weraganthota (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-18 15:02:54 | Nakkala (Kumbukkan Oya) | 2.56 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-18 15:08:56 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-18 15:08:19 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 15:06:25 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 15:02:18 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-18 15:07:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-18 15:03:22 | Galgamuwa (Mee Oya) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 15:06:10 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 15:01:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:02:43 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:01:57 | Siyambalanduwa (Heda Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:02:16 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 15:02:11 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:01:35 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:14 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:06:01 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:03:21 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:03:24 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:18 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:03:00 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:11:22 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:00 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:02:09 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 15:04:05 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:12 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.005 |  |
| 2025-12-18 14:12:21 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2025-12-18 15:05:39 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2025-12-18 15:01:35 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-18 15:03:26 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2025-12-18 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2025-12-18 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.047 |  |
| 2025-12-18 15:01:49 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.058 |  |
| 2025-12-18 15:02:20 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.216 |  |
| 2025-12-18 14:02:53 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.410 |  |
| 2025-12-18 15:00:26 | Horowpothana (Yan Oya) | 5.32 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)