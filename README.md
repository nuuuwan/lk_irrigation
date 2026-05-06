# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_00:16:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 00:16:01 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.146 |  |
| 2026-05-07 00:12:48 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:10:21 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | -0.029 |  |
| 2026-05-07 00:08:04 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-05-07 00:07:08 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-07 00:06:46 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-05-07 00:06:43 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:05:33 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 00:04:41 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:04:35 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 00:04:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-05-07 00:04:17 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-07 00:03:58 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-07 00:03:50 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-05-07 00:03:45 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:29 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-05-07 00:03:27 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:23 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:53 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:52 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-07 00:01:38 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-05-07 00:01:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:18 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-07 00:01:13 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:00:23 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 23:42:51 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.886 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 00:08:04 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 2.769 | 🔺 Rising |
| 2026-05-07 00:03:50 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-05-07 00:04:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-05-06 22:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-07 00:03:29 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-05-07 00:03:58 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-06 23:07:36 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-07 00:04:35 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 00:07:08 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-07 00:04:17 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-07 00:01:52 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-07 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-06 23:06:40 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 00:00:23 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 23:02:12 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 00:05:33 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 22:05:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 00:01:13 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:04:41 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:27 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:12:48 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:16:10 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:18 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:23 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:03:45 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:06:16 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:01:53 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-07 00:06:43 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-07 00:01:38 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-05-06 23:02:26 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-05-07 00:10:21 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | -0.029 |  |
| 2026-05-06 23:02:43 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.103 |  |
| 2026-05-07 00:16:01 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)