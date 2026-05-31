# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_23:33:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 23:33:10 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.008 |  |
| 2026-05-31 23:20:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.032 |  |
| 2026-05-31 23:17:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:17:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:13:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:06:40 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:06:37 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-31 23:06:26 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:06:23 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 12.381 | 🔺 Rising |
| 2026-05-31 23:05:52 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-05-31 23:05:32 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.038 |  |
| 2026-05-31 23:05:19 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:05:12 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.059 |  |
| 2026-05-31 23:05:11 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:05:02 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:04:50 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:04:33 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 23:04:19 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-31 23:03:48 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-05-31 23:03:44 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:03:43 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-05-31 23:03:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-31 23:03:14 | Kuda Oya (Kirindi Oya) | 0.63 | 🟢 Normal | 12.381 | 🔺 Rising |
| 2026-05-31 23:03:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:02:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-31 23:02:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-31 23:02:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:02:23 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-05-31 23:02:21 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 23:02:19 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-05-31 23:02:17 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:01:59 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:01:53 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 23:06:23 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 12.381 | 🔺 Rising |
| 2026-05-31 22:02:59 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-31 23:06:37 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-31 23:02:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-31 23:02:21 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 23:04:33 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:02:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:13:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:02:17 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:03:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:04:50 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:17:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:06:40 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:06:26 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:05:11 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:03:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:05:19 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:01:53 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:05:02 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:17:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:03:44 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:16:28 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:04:21 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:33:10 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.008 |  |
| 2026-05-31 23:02:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-31 23:04:19 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-31 23:05:52 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-05-31 23:03:48 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-05-31 23:02:19 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-05-31 23:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-05-31 23:03:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-31 23:03:43 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-05-31 23:02:23 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-05-31 23:20:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.032 |  |
| 2026-05-31 23:05:32 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.038 |  |
| 2026-05-31 23:05:12 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)