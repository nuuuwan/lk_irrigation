# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_04:16:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **217,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 04:16:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-27 04:14:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-07-27 04:12:08 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:11:04 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.070 |  |
| 2026-07-27 04:09:47 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:06:40 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.047 |  |
| 2026-07-27 04:06:04 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:05:37 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-07-27 04:04:55 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:04:23 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.201 |  |
| 2026-07-27 04:03:27 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:17 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-27 04:03:12 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:11 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:02 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-07-27 04:02:50 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-27 04:02:45 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:02:36 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 04:02:20 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:02:17 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:02:05 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:01:57 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:01:42 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-27 04:01:36 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 04:01:23 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-07-27 04:00:52 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-27 04:00:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:00:48 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:00:45 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:00:27 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:00:27 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-07-27 03:58:21 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.053 |  |
| 2026-07-27 03:50:28 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:47:04 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 04:05:37 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-07-27 04:16:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-27 03:03:27 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-27 04:03:17 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-27 04:02:50 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-27 04:00:52 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-27 04:02:36 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 04:01:36 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 04:00:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:00:27 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:01:57 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:02:45 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:02:20 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 18:03:43 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:09:47 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:02 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:02:17 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:27 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:11 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:00:48 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:02:05 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:06:04 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:31 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:00:45 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 18:00:36 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:12:08 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-27 03:04:16 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:03:12 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:04:55 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-27 04:01:23 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-07-27 04:01:42 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-27 04:14:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-07-27 04:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-07-26 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.020 |  |
| 2026-07-27 04:00:27 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-07-27 04:06:40 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.047 |  |
| 2026-07-27 03:58:21 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.053 |  |
| 2026-07-27 04:11:04 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.070 |  |
| 2026-07-27 04:04:23 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)