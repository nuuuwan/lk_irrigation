# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_00:17:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,248 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 00:17:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | -0.024 |  |
| 2026-05-30 00:08:08 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.009 |  |
| 2026-05-30 00:07:28 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:06:39 | Baddegama (Gin Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:06:38 | Baddegama (Gin Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:06:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:05:50 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.100 |  |
| 2026-05-30 00:05:25 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:05:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:05:00 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:04:21 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:03:58 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-30 00:03:46 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.005 |  |
| 2026-05-30 00:03:37 | Baddegama (Gin Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:03:36 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-05-30 00:03:34 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-05-30 00:03:28 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.030 |  |
| 2026-05-30 00:03:25 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-05-30 00:03:24 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:03:20 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:19 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-30 00:03:10 | Ellagawa (Kalu Ganga) | 8.37 | 🟢 Normal | -0.031 |  |
| 2026-05-30 00:02:55 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.059 |  |
| 2026-05-30 00:02:52 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:02:37 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.049 |  |
| 2026-05-30 00:02:33 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-05-30 00:02:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:01:54 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.040 |  |
| 2026-05-30 00:01:53 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.052 |  |
| 2026-05-30 00:01:52 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:01:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:01:31 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:01:23 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 00:01:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 00:17:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | -0.024 |  |
| 2026-05-29 23:42:39 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 50.521 | 🔺 Rising |
| 2026-05-30 00:03:36 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-05-30 00:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-30 00:03:19 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-30 00:01:23 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 00:05:00 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:01:31 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:02:08 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:01:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:02:52 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:06:39 | Baddegama (Gin Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:03:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:02:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:05:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:04:21 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:06:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:01:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-30 00:03:46 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.005 |  |
| 2026-05-30 00:08:08 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.009 |  |
| 2026-05-30 00:07:28 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:05:25 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:58 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:20 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:01:52 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:24 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-30 00:03:25 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-05-30 00:02:33 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-05-30 00:03:28 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.030 |  |
| 2026-05-30 00:03:34 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-05-30 00:03:10 | Ellagawa (Kalu Ganga) | 8.37 | 🟢 Normal | -0.031 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-30 00:01:54 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.040 |  |
| 2026-05-30 00:02:37 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.049 |  |
| 2026-05-30 00:01:53 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.052 |  |
| 2026-05-30 00:02:55 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.059 |  |
| 2026-05-30 00:05:50 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)