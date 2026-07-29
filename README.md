# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_01:37:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 01:37:10 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:23:26 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:11:38 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:10:14 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:09:51 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:09:48 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-30 01:07:13 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-30 01:06:49 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.038 |  |
| 2026-07-30 01:06:39 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:06:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:05:56 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:05:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:04:39 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:04:21 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 01:04:21 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:04:04 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:03:59 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-30 01:03:41 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-07-30 01:03:14 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.061 |  |
| 2026-07-30 01:03:09 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:03:00 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:57 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:45 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:42 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 2.298 | 🔺 Rising |
| 2026-07-30 01:02:33 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:04 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:01:37 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:01:20 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-07-30 01:01:15 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:01:08 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 2.298 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 01:02:42 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 2.298 | 🔺 Rising |
| 2026-07-30 01:03:59 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-30 01:07:13 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-30 01:09:48 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-30 01:04:21 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 01:10:14 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-30 00:00:57 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 00:00:50 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:03:09 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:57 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:03:00 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:09:51 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:45 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:04:04 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:33 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:23:26 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:04 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:06:39 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-07-30 00:02:09 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:04:39 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:04:21 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:05:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:37:10 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:01:15 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:01:37 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:05:56 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-30 00:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-30 01:01:20 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-07-30 00:09:46 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-29 22:20:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.032 |  |
| 2026-07-29 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.034 |  |
| 2026-07-30 01:06:49 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.038 |  |
| 2026-07-30 01:03:41 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-07-30 01:03:14 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.061 |  |
| 2026-07-30 00:23:34 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.069 |  |
| 2026-07-30 00:02:19 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.338 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)