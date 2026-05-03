# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_13:04:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,774 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 13:04:36 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:04:34 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-03 13:04:03 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:03:51 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:03:49 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-05-03 13:03:48 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:03:30 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.049 |  |
| 2026-05-03 13:03:21 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-05-03 13:02:38 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:02:37 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.061 |  |
| 2026-05-03 13:02:15 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-03 13:02:15 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | -0.011 |  |
| 2026-05-03 13:02:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:02:04 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:01:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-03 13:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:01:32 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 13:01:22 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:01:04 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-05-03 13:00:44 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.012 |  |
| 2026-05-03 13:00:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:00:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:17:12 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:14:22 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 12:06:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-05-03 13:02:15 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-03 13:01:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-03 12:06:19 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-03 12:09:08 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-03 13:01:32 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 12:01:30 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 12:00:33 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:02:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:00:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:03:48 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:05:03 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:09:33 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:03:51 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:03:21 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:04:03 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:06:58 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:00:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:02:04 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:03:53 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:04:45 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:02:38 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:04:36 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 13:01:22 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 12:05:50 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-05-03 13:04:34 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-03 12:03:07 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-03 13:01:04 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-05-03 13:02:15 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | -0.011 |  |
| 2026-05-03 12:04:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-05-03 13:00:44 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.012 |  |
| 2026-05-03 12:06:19 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.022 |  |
| 2026-05-03 13:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-05-03 13:03:49 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-05-03 13:03:30 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.049 |  |
| 2026-05-03 12:00:53 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.050 |  |
| 2026-05-03 13:02:37 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.061 |  |
| 2026-05-03 12:02:21 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)