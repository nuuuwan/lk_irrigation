# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_13:30:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,424 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 13:30:00 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:23:21 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:19:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-29 13:16:10 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-29 13:15:47 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:12:08 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:11:36 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:11:28 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:11:14 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-29 13:10:26 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:09:36 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.208 |  |
| 2026-07-29 13:08:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:08:40 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:08:30 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:07:01 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-07-29 13:06:22 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:05:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:05:18 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:05:17 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:05:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-29 13:04:39 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:04:24 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-07-29 13:04:18 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-07-29 13:03:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:03:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 13:03:22 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 13:03:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:44 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:41 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:38 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:03 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-07-29 13:01:58 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:01:35 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-29 13:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:01:26 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-07-29 13:01:14 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:01:08 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-29 13:00:57 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:00:33 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 13:07:01 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-07-29 13:02:03 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-07-29 13:04:24 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-07-29 13:05:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-29 13:19:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-29 13:04:18 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-07-29 13:01:08 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-29 13:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 13:11:14 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-29 13:03:22 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 13:16:10 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-29 13:03:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:11:36 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:03:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:41 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:01:14 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:05:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:06:22 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:38 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:12:08 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:23:21 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:05:17 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:02:44 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:05:18 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:01:58 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:08:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:08:30 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:04:39 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:00:33 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:30:00 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:00:57 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:08:40 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:10:26 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:11:28 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:01:26 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-07-29 13:01:35 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-29 13:09:36 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)