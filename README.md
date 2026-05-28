# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_16:17:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,067 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 16:17:26 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 16:14:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.052 |  |
| 2026-05-28 16:12:23 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:10:23 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-28 16:09:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:08:54 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.018 |  |
| 2026-05-28 16:08:41 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-05-28 16:08:26 | Urawa (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.471 | 🔺 Rising |
| 2026-05-28 16:08:07 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -1.516 |  |
| 2026-05-28 16:07:22 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-05-28 16:05:34 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-28 16:05:24 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:04:51 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.060 |  |
| 2026-05-28 16:04:29 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-05-28 16:04:27 | Magura (Kalu Ganga) | 4.91 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-05-28 16:03:22 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -1.516 |  |
| 2026-05-28 16:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.25 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 16:03:11 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:03:06 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.034 |  |
| 2026-05-28 16:02:44 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:27 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2026-05-28 16:02:24 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 16:02:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:13 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 16:02:13 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 16:02:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:08 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:02 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-05-28 16:01:59 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 16:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 16:01:48 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:40 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:27 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:15 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:14 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-28 16:01:08 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:00:16 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:00:11 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:00:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 16:04:27 | Magura (Kalu Ganga) | 4.91 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-05-28 16:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.25 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 16:08:26 | Urawa (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.471 | 🔺 Rising |
| 2026-05-28 16:04:29 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-05-28 16:08:41 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-05-28 16:10:23 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-28 16:02:13 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 16:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 16:01:59 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 16:02:13 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 16:02:24 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 16:17:26 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 16:02:44 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:40 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:00:11 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:27 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:00:16 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:48 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:03:11 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:15 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:09:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:01:08 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:05:24 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:02:08 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:12:23 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 16:07:22 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-05-28 16:05:34 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-28 16:01:14 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-28 16:00:11 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-28 16:08:54 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.018 |  |
| 2026-05-28 16:02:02 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-05-28 16:02:27 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2026-05-28 16:03:06 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.034 |  |
| 2026-05-28 16:14:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.052 |  |
| 2026-05-28 16:04:51 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.060 |  |
| 2026-05-28 16:08:07 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -1.516 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)