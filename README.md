# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_00:17:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,562 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 00:17:02 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 00:15:22 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-05-27 00:09:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 00:09:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:09:30 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-27 00:09:21 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 00:08:39 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.063 |  |
| 2026-05-27 00:07:47 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:41 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:11 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:11 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:08 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-27 00:06:04 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 00:05:22 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | -0.048 |  |
| 2026-05-27 00:05:13 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:04:31 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.375 |  |
| 2026-05-27 00:04:09 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-05-27 00:03:51 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-27 00:03:49 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:03:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.021 |  |
| 2026-05-27 00:03:36 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | -0.070 |  |
| 2026-05-27 00:02:59 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-27 00:02:56 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-27 00:02:55 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.375 |  |
| 2026-05-27 00:02:41 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 00:02:22 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:02:19 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-05-27 00:02:18 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:02:11 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:02:08 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:19 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:00:55 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 22:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 00:02:56 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-27 00:09:21 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 00:02:41 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 00:17:02 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 00:06:04 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 00:09:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 00:02:18 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:19 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:05:13 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:11 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:41 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:02:08 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:07:47 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:11 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:09:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:03:49 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:02:22 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:28:37 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.007 |  |
| 2026-05-27 00:15:22 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-05-27 00:06:08 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-27 00:02:59 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-27 00:03:51 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-27 00:09:30 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-27 00:00:55 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-27 00:03:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.021 |  |
| 2026-05-27 00:04:09 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-05-27 00:02:19 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-05-27 00:05:22 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | -0.048 |  |
| 2026-05-27 00:08:39 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.063 |  |
| 2026-05-27 00:03:36 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | -0.070 |  |
| 2026-05-27 00:04:31 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.375 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)