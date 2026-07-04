# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_01:17:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 01:17:53 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:17:46 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.008 |  |
| 2026-07-05 01:15:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:14:01 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.072 |  |
| 2026-07-05 01:08:27 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.027 |  |
| 2026-07-05 01:07:51 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-07-05 01:07:17 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-05 01:06:23 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 01:06:18 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:05:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-05 01:04:39 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 01:04:23 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-07-05 01:03:52 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-05 01:03:36 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:03:20 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.173 |  |
| 2026-07-05 01:03:10 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-05 01:03:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:03:03 | Thalgahagoda (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.275 |  |
| 2026-07-05 01:02:50 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-07-05 01:02:39 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.051 |  |
| 2026-07-05 01:02:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:02:08 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-05 01:01:34 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.257 |  |
| 2026-07-05 01:01:32 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:01:12 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:01:06 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:54:20 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.275 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 01:02:08 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-05 01:05:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-05 01:03:52 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-05 01:07:17 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-05 01:02:50 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-07-05 01:03:10 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 23:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 01:06:23 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 01:04:39 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 22:14:56 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:17:53 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:01:12 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:03:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:02:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:15:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:23:33 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:01:06 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:03:36 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:14 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:06:18 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:59 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:01:32 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:03:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 01:17:46 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.008 |  |
| 2026-07-04 23:07:18 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-05 01:07:51 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-07-05 01:04:23 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-07-05 00:05:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-07-05 01:08:27 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.027 |  |
| 2026-07-05 01:02:39 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.051 |  |
| 2026-07-05 01:14:01 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.072 |  |
| 2026-07-04 22:12:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.092 |  |
| 2026-07-05 01:03:20 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.173 |  |
| 2026-07-05 01:01:34 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.257 |  |
| 2026-07-05 01:03:03 | Thalgahagoda (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.275 |  |
| 2026-07-05 00:09:49 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -6.995 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)