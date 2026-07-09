# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_03:22:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 03:22:10 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:19:40 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.008 |  |
| 2026-07-10 03:19:24 | Putupaula (Kalu Ganga) | 3.38 | 🟡 Alert | 0.959 | 🔺 Rising |
| 2026-07-10 03:18:49 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:12:19 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-10 03:08:32 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -1.305 |  |
| 2026-07-10 03:08:18 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 03:08:08 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-10 03:08:06 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-10 03:07:21 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.042 |  |
| 2026-07-10 03:06:23 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:06:16 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:06:11 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-10 03:06:05 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:05:59 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:05:58 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 03:05:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-07-10 03:05:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:05:02 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:04:54 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:04:17 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-10 03:03:22 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:03:03 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:37 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:33 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.065 |  |
| 2026-07-10 03:02:21 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:05 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:01:58 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.089 |  |
| 2026-07-10 03:01:44 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:00:15 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:00:13 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 02:53:19 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 03:19:24 | Putupaula (Kalu Ganga) | 3.38 | 🟡 Alert | 0.959 | 🔺 Rising |
| 2026-07-10 03:08:06 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-10 03:06:11 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-10 03:04:17 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-10 03:05:58 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 03:12:19 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-10 03:08:18 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 03:00:13 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:18:49 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 02:11:54 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:03:22 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:01:44 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:21 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:05:02 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 02:00:31 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:37 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:22:10 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:06:23 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:06:16 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:05:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:05 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:02:21 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:07:21 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:03:03 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:04:54 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:40 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 02:07:24 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:05:59 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:06:05 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-10 03:19:40 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.008 |  |
| 2026-07-10 03:08:08 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-09 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.011 |  |
| 2026-07-10 01:01:20 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.021 |  |
| 2026-07-10 03:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.042 |  |
| 2026-07-10 03:05:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-07-10 03:02:33 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.065 |  |
| 2026-07-10 03:01:58 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.089 |  |
| 2026-07-10 03:08:32 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -1.305 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)