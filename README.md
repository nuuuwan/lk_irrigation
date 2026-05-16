# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_19:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,661 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 19:12:12 | Rathnapura (Kalu Ganga) | 4.01 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-16 19:11:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | -0.009 |  |
| 2026-05-16 19:10:15 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-05-16 19:07:15 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.009 |  |
| 2026-05-16 19:06:47 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.028 |  |
| 2026-05-16 19:06:32 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.027 |  |
| 2026-05-16 19:06:18 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.019 |  |
| 2026-05-16 19:06:03 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.044 |  |
| 2026-05-16 19:05:51 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 19:05:42 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 19:04:44 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:04:36 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:04:33 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | -0.040 |  |
| 2026-05-16 19:04:08 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | -0.061 |  |
| 2026-05-16 19:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 19:03:42 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:03:38 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:03:37 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-05-16 19:03:36 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 19:03:35 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:03:23 | Dunamale (Aththanagalu Oya) | 3.66 | 🟡 Alert | -0.088 |  |
| 2026-05-16 19:03:03 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:02:49 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-05-16 19:02:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.119 |  |
| 2026-05-16 19:02:43 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 19:02:33 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-16 19:02:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:01:58 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:01:47 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:01:45 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-16 19:01:33 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-05-16 19:01:19 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.041 |  |
| 2026-05-16 19:01:13 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-16 19:01:09 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-05-16 19:00:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-16 19:00:36 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 19:11:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | -0.009 |  |
| 2026-05-16 19:03:23 | Dunamale (Aththanagalu Oya) | 3.66 | 🟡 Alert | -0.088 |  |
| 2026-05-16 19:00:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-16 19:12:12 | Rathnapura (Kalu Ganga) | 4.01 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-16 19:02:33 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-16 19:01:45 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-16 19:03:36 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 19:05:42 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 19:02:43 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 19:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 19:05:51 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 19:03:38 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:03:35 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:03:03 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:00:36 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:02:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:04:44 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:04:36 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:03:42 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:01:47 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:01:58 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 19:07:15 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.009 |  |
| 2026-05-16 19:01:13 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-16 19:10:15 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-05-16 19:06:18 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.019 |  |
| 2026-05-16 19:01:09 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-05-16 19:02:49 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-05-16 19:06:32 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.027 |  |
| 2026-05-16 19:06:47 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.028 |  |
| 2026-05-16 19:01:33 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 19:04:33 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | -0.040 |  |
| 2026-05-16 19:03:37 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-05-16 19:01:19 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.041 |  |
| 2026-05-16 19:06:03 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.044 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-16 19:04:08 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | -0.061 |  |
| 2026-05-16 19:02:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)