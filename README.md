# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_15:11:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,686 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 15:11:59 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:09:19 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-14 15:08:44 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-14 15:08:13 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.055 |  |
| 2026-05-14 15:06:38 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-14 15:06:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.124 |  |
| 2026-05-14 15:06:16 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:06:06 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | -0.337 |  |
| 2026-05-14 15:05:37 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:05:18 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-05-14 15:05:15 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | 0.707 | 🔺 Rising |
| 2026-05-14 15:04:52 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:04:48 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-05-14 15:04:48 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:04:48 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-05-14 15:04:35 | Deraniyagala (Kelani Ganga) | 3.56 | 🟢 Normal | 2.662 | 🔺 Rising |
| 2026-05-14 15:04:25 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-14 15:03:56 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.082 |  |
| 2026-05-14 15:03:49 | Rathnapura (Kalu Ganga) | 4.38 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-14 15:03:27 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-14 15:03:26 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-14 15:03:15 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-14 15:03:00 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.255 |  |
| 2026-05-14 15:02:52 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-05-14 15:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-14 15:02:43 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-14 15:02:38 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.187 | 🔺 Rising |
| 2026-05-14 15:02:34 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-14 15:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.43 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 15:02:19 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:02:17 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-05-14 15:02:11 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:02:11 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-14 15:02:09 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-05-14 15:02:01 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-14 15:01:54 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:01:44 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:01:23 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:01:08 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 15:00:23 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-14 15:00:07 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:59:40 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 15:02:38 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.187 | 🔺 Rising |
| 2026-05-14 15:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.43 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 15:04:35 | Deraniyagala (Kelani Ganga) | 3.56 | 🟢 Normal | 2.662 | 🔺 Rising |
| 2026-05-14 15:05:15 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | 0.707 | 🔺 Rising |
| 2026-05-14 15:04:48 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-05-14 15:08:44 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-14 15:03:49 | Rathnapura (Kalu Ganga) | 4.38 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-14 15:04:25 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-14 15:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-14 15:02:34 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-14 15:09:19 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-14 15:03:15 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-14 15:06:38 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-14 15:02:11 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-14 15:02:43 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-14 15:01:08 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 15:00:07 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:01:23 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:04:48 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:04:52 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:06:16 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:02:11 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:02:19 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:11:59 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:01:54 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-14 15:03:27 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-14 15:00:23 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-14 15:02:01 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-14 15:05:18 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-05-14 15:04:48 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-05-14 15:03:26 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-14 15:02:52 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-05-14 15:02:09 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-05-14 15:02:17 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-05-14 15:08:13 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.055 |  |
| 2026-05-14 15:03:56 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.082 |  |
| 2026-05-14 15:06:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.124 |  |
| 2026-05-14 15:03:00 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.255 |  |
| 2026-05-14 15:06:06 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)