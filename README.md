# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_21:16:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,440 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 21:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.024 |  |
| 2026-07-13 21:11:02 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:08:13 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-07-13 21:07:21 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-13 21:06:53 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:06:04 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:05:56 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:05:44 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-07-13 21:05:28 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:05:15 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.041 |  |
| 2026-07-13 21:05:06 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:04:32 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:55 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-13 21:03:54 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:46 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-07-13 21:03:30 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:24 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:22 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:55 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:41 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-13 21:02:39 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:11 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 21:02:03 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:58 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:46 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:29 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 21:01:19 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:16 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.021 |  |
| 2026-07-13 21:01:11 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:08 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | -0.054 |  |
| 2026-07-13 21:00:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 20:59:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 21:03:46 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-07-13 21:03:55 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-13 21:07:21 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-13 21:02:11 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 21:01:29 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 20:59:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 20:14:05 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:46 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:00:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:22 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:06:53 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:04:32 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:55 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:05:06 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:39 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:19 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:30 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:05:56 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-13 20:02:44 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:02:03 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:05:28 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:24 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:04 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:58 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:03:54 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:01:11 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:11:02 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 21:08:13 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-07-13 21:05:44 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-07-13 21:02:41 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-07-13 21:01:16 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.021 |  |
| 2026-07-13 21:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.024 |  |
| 2026-07-13 21:05:15 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.041 |  |
| 2026-07-13 21:01:08 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | -0.054 |  |
| 2026-07-13 18:03:05 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)