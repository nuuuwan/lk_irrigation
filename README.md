# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_00:08:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,616 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 00:08:47 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:08:40 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:08:36 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:07:24 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:06:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.031 |  |
| 2026-01-07 00:06:15 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-07 00:05:59 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.075 |  |
| 2026-01-07 00:05:35 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-07 00:05:18 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-01-07 00:04:47 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-07 00:04:31 | Manampitiya (Mahaweli Ganga) | 3.65 | 🟡 Alert | -0.060 |  |
| 2026-01-07 00:04:23 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-07 00:04:18 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:04:08 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:51 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 00:03:49 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 00:03:43 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:26 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:22 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | -0.116 |  |
| 2026-01-07 00:03:19 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:09 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:02:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:02:26 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-07 00:02:15 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-07 00:02:13 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 00:01:52 | Nakkala (Kumbukkan Oya) | 1.61 | 🟢 Normal | -0.049 |  |
| 2026-01-07 00:01:15 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.062 |  |
| 2026-01-07 00:01:15 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:00:19 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-06 23:32:11 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 00:04:31 | Manampitiya (Mahaweli Ganga) | 3.65 | 🟡 Alert | -0.060 |  |
| 2026-01-07 00:04:23 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-07 00:05:35 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-07 00:00:19 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-06 23:32:11 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 00:03:51 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 00:02:13 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 00:03:49 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 23:02:51 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:43 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:26 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:19 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:01:15 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:08:40 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:02:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:09 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:07:24 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:08:47 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:04:08 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:04:18 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-06 23:03:25 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 22:26:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.008 |  |
| 2026-01-06 23:14:13 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.009 |  |
| 2026-01-07 00:04:47 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-06 22:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-01-07 00:06:15 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-07 00:02:26 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-06 23:07:13 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-01-07 00:02:15 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-07 00:06:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.031 |  |
| 2026-01-07 00:01:52 | Nakkala (Kumbukkan Oya) | 1.61 | 🟢 Normal | -0.049 |  |
| 2026-01-07 00:01:15 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.062 |  |
| 2026-01-07 00:05:18 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-01-07 00:05:59 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.075 |  |
| 2026-01-07 00:03:22 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)