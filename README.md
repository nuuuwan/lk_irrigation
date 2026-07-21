# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_19:20:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **212,487 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 19:20:45 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:16:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.033 |  |
| 2026-07-21 19:10:57 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-21 19:10:27 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.132 |  |
| 2026-07-21 19:08:36 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:07:45 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.067 |  |
| 2026-07-21 19:07:18 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:51 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-21 19:05:47 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-07-21 19:05:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:37 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:22 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:15 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:05 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 19:04:59 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:04:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-21 19:04:31 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:03:19 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:03:18 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:03:03 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:49 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:43 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.038 |  |
| 2026-07-21 19:02:40 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 19:02:32 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-07-21 19:02:31 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:21 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:02 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:01:49 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-21 19:01:15 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:01:08 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-07-21 19:01:03 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:00:55 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:00:49 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 19:05:47 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-07-21 19:05:51 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-21 19:04:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-21 19:00:49 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-21 19:05:05 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 19:02:40 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 19:02:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:01:49 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:02 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:37 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:01:03 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:07:18 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:31 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:04:59 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:03:19 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:04:31 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:49 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:02:21 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:08:36 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:03:18 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:00 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:05:22 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:20:45 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:00:55 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:01:15 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:03:03 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 19:10:57 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-21 19:02:32 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-07-21 19:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-21 18:04:58 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.028 |  |
| 2026-07-21 19:01:08 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-07-21 19:16:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.033 |  |
| 2026-07-21 19:02:43 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.038 |  |
| 2026-07-21 19:07:45 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.067 |  |
| 2026-07-21 19:10:27 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)