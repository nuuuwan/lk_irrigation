# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_22:15:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,950 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 22:15:45 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.017 |  |
| 2026-05-14 22:13:08 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-14 22:12:37 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-14 22:09:54 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-14 22:09:33 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:07:55 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 22:07:51 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:07:30 | Badalgama (Maha Oya) | 4.27 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-14 22:07:08 | Holombuwa (Kelani Ganga) | 1.72 | 🟢 Normal | -0.101 |  |
| 2026-05-14 22:07:07 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-05-14 22:07:01 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 22:06:51 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2026-05-14 22:06:29 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.075 |  |
| 2026-05-14 22:06:00 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.031 |  |
| 2026-05-14 22:05:48 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:05:40 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:05:06 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 22:05:04 | Hanwella (Kelani Ganga) | 5.07 | 🟢 Normal | 0.472 | 🔺 Rising |
| 2026-05-14 22:05:00 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-14 22:04:55 | Deraniyagala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.150 |  |
| 2026-05-14 22:04:55 | Glencourse (Kelani Ganga) | 13.94 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-05-14 22:04:44 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-05-14 22:04:40 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-14 22:04:30 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 22:03:39 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.030 |  |
| 2026-05-14 22:03:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-14 22:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.60 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-14 22:01:58 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:01:54 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:01:53 | Magura (Kalu Ganga) | 5.01 | 🟡 Alert | -0.010 |  |
| 2026-05-14 22:01:36 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.060 |  |
| 2026-05-14 22:01:21 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-05-14 22:01:15 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | 0.141 | 🔺 Rising |
| 2026-05-14 22:00:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-14 22:00:42 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:00:11 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 22:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.60 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-14 22:01:15 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | 0.141 | 🔺 Rising |
| 2026-05-14 22:01:53 | Magura (Kalu Ganga) | 5.01 | 🟡 Alert | -0.010 |  |
| 2026-05-14 22:05:04 | Hanwella (Kelani Ganga) | 5.07 | 🟢 Normal | 0.472 | 🔺 Rising |
| 2026-05-14 22:04:55 | Glencourse (Kelani Ganga) | 13.94 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-05-14 22:07:30 | Badalgama (Maha Oya) | 4.27 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-14 22:04:40 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-14 22:09:54 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-14 22:05:00 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-14 22:12:37 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-14 22:05:06 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 22:04:30 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 22:07:55 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 22:13:08 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-14 22:07:01 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:00:11 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:01:54 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:00:42 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:05:40 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:09:33 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:07:51 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:01:58 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:05:48 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 22:07:07 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-05-14 22:00:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-14 22:03:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-14 22:15:45 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.017 |  |
| 2026-05-14 22:06:51 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2026-05-14 22:04:44 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-05-14 22:01:21 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-05-14 22:03:39 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.030 |  |
| 2026-05-14 22:06:00 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.031 |  |
| 2026-05-14 22:01:36 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.060 |  |
| 2026-05-14 22:06:29 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.075 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-14 22:07:08 | Holombuwa (Kelani Ganga) | 1.72 | 🟢 Normal | -0.101 |  |
| 2026-05-14 22:04:55 | Deraniyagala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)