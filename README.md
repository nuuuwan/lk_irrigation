# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_10:24:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,895 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 10:24:14 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.022 |  |
| 2026-07-14 10:22:12 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.008 |  |
| 2026-07-14 10:19:12 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:14:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:12:50 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-14 10:10:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-07-14 10:10:02 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:08:49 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 10:08:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:07:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-14 10:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.018 |  |
| 2026-07-14 10:06:45 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:06:18 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:06:13 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.197 |  |
| 2026-07-14 10:06:08 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:05:58 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-07-14 10:05:08 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-07-14 10:04:56 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:04:43 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:04:24 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:04:23 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-14 10:03:38 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-14 10:03:34 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:03:28 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.043 |  |
| 2026-07-14 10:03:22 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:59 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.041 |  |
| 2026-07-14 10:02:50 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:42 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:37 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:23 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.011 |  |
| 2026-07-14 10:02:17 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:01:57 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:01:50 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:01:48 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-07-14 10:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:00:48 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:00:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 10:10:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-07-14 10:03:38 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-14 10:07:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-14 10:12:50 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-14 10:08:49 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 10:00:48 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:00:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:03:34 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:01:57 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:08:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:17 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:04:43 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:10:02 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:06:08 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:42 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:50 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:14:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:04:56 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:03:22 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:06:18 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:04:24 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:01:50 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-14 09:00:39 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:19:12 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:06:45 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:02:37 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 10:22:12 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.008 |  |
| 2026-07-14 10:05:08 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-07-14 10:01:48 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-07-14 10:04:23 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-14 10:02:23 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.011 |  |
| 2026-07-14 10:05:58 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-07-14 10:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.018 |  |
| 2026-07-14 10:24:14 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.022 |  |
| 2026-07-14 10:02:59 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.041 |  |
| 2026-07-14 10:03:28 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.043 |  |
| 2026-07-14 10:06:13 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)