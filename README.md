# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_01:18:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,055 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 01:18:03 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:17:47 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.041 |  |
| 2026-05-15 01:11:50 | Badalgama (Maha Oya) | 4.58 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-15 01:11:32 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-15 01:10:22 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-05-15 01:10:11 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 01:07:02 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-15 01:06:57 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.022 |  |
| 2026-05-15 01:06:36 | Rathnapura (Kalu Ganga) | 4.87 | 🟢 Normal | -0.019 |  |
| 2026-05-15 01:06:35 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 01:05:53 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2026-05-15 01:05:35 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-15 01:05:24 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:05:14 | Dunamale (Aththanagalu Oya) | 4.55 | 🟠 Minor Flood | 0.114 | 🔺 Rising |
| 2026-05-15 01:04:49 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-15 01:04:00 | Hanwella (Kelani Ganga) | 5.70 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-15 01:03:09 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-15 01:03:04 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-05-15 01:03:01 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.021 |  |
| 2026-05-15 01:02:55 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:02:39 | Giriulla (Maha Oya) | 3.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 01:02:35 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 01:02:26 | Glencourse (Kelani Ganga) | 14.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 01:02:23 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | -0.020 |  |
| 2026-05-15 01:01:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:33 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-05-15 01:01:29 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:14 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:10 | Deraniyagala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:00:58 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:00:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 01:00:50 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 01:05:14 | Dunamale (Aththanagalu Oya) | 4.55 | 🟠 Minor Flood | 0.114 | 🔺 Rising |
| 2026-05-15 01:00:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 01:06:57 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.022 |  |
| 2026-05-15 01:04:00 | Hanwella (Kelani Ganga) | 5.70 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-15 01:04:49 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-15 01:03:09 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-15 00:02:19 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-15 01:11:50 | Badalgama (Maha Oya) | 4.58 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-15 01:05:35 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-15 01:11:32 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-15 01:10:11 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 00:22:27 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-15 01:02:39 | Giriulla (Maha Oya) | 3.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 01:02:35 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 00:07:45 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-15 01:02:26 | Glencourse (Kelani Ganga) | 14.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 01:06:35 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:14 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:10 | Deraniyagala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:05:24 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:02:55 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:29 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:18:03 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:00:58 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:00:50 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 01:01:33 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-05-15 01:05:53 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2026-05-15 01:10:22 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-05-15 01:06:36 | Rathnapura (Kalu Ganga) | 4.87 | 🟢 Normal | -0.019 |  |
| 2026-05-15 01:07:02 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-15 01:03:04 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-05-15 01:02:23 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | -0.020 |  |
| 2026-05-15 01:03:01 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.021 |  |
| 2026-05-14 23:01:54 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-05-15 01:17:47 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.041 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)