# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_03:15:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,279 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 03:15:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-05-23 03:13:12 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-23 03:11:34 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-05-23 03:11:03 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.039 |  |
| 2026-05-23 03:09:53 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 03:09:12 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.585 | 🔺 Rising |
| 2026-05-23 03:08:58 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:08:51 | Hanwella (Kelani Ganga) | 7.58 | 🟡 Alert | -0.095 |  |
| 2026-05-23 03:08:44 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-23 03:08:38 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-05-23 03:07:46 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-23 03:07:09 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.585 | 🔺 Rising |
| 2026-05-23 03:06:14 | Ellagawa (Kalu Ganga) | 9.86 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-23 03:05:56 | Rathnapura (Kalu Ganga) | 6.67 | 🟡 Alert | -0.075 |  |
| 2026-05-23 03:05:07 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-05-23 03:04:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:04:42 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:04:39 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:04:33 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.026 |  |
| 2026-05-23 03:04:18 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.023 |  |
| 2026-05-23 03:04:18 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:04:15 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-05-23 03:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:03:17 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | -0.437 |  |
| 2026-05-23 03:03:07 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:03:03 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-23 03:03:00 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-05-23 03:03:00 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-23 03:02:51 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:02:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:02:23 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:02:22 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.054 |  |
| 2026-05-23 03:02:03 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:01:38 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:01:24 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-05-23 03:00:58 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-23 03:00:54 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.017 |  |
| 2026-05-23 03:00:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:55:25 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:51:19 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 03:09:53 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 03:11:34 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-05-23 03:15:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-05-23 03:04:18 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.023 |  |
| 2026-05-23 03:05:56 | Rathnapura (Kalu Ganga) | 6.67 | 🟡 Alert | -0.075 |  |
| 2026-05-23 03:08:51 | Hanwella (Kelani Ganga) | 7.58 | 🟡 Alert | -0.095 |  |
| 2026-05-23 03:09:12 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.585 | 🔺 Rising |
| 2026-05-23 03:04:15 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-05-23 03:03:00 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-23 03:06:14 | Ellagawa (Kalu Ganga) | 9.86 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-23 03:13:12 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-23 03:08:44 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-23 03:07:46 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-23 03:08:58 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-23 01:03:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:00:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:04:18 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:02:51 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:03:07 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:02:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:01:38 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:04:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:02:03 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:02:23 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 03:03:03 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-23 03:00:58 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 03:00:54 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.017 |  |
| 2026-05-23 03:08:38 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-05-23 03:04:33 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.026 |  |
| 2026-05-23 03:05:07 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-05-23 03:03:00 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-23 03:01:24 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-05-23 03:11:03 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.039 |  |
| 2026-05-23 03:02:22 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.054 |  |
| 2026-05-23 03:03:17 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | -0.437 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)