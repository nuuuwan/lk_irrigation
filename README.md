# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_15:18:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 15:18:54 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:14:29 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:10:46 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-13 15:09:29 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:09:11 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-13 15:07:27 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-07-13 15:07:04 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:07:03 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-07-13 15:06:30 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:05:59 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 15:05:41 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:04:06 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-13 15:03:48 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:41 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 15:03:37 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-13 15:03:31 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:21 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:13 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:11 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-13 15:02:58 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-13 15:02:55 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:51 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:44 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:29 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:27 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-07-13 15:02:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:01:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-13 15:01:35 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:01:33 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-07-13 15:01:10 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:00:28 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.100 |  |
| 2026-07-13 15:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:00:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 15:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-13 15:01:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-13 15:10:46 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-13 15:03:11 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-13 15:09:11 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-13 15:03:41 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 15:05:59 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 15:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:14:29 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:01:35 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:44 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:00:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:51 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:48 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:13 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:01:10 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:37 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:06:30 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:29 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:05:41 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:27 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:55 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:02:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:31 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:18:54 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:03:21 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:07:04 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:09:29 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-13 15:07:27 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-07-13 15:02:58 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-13 15:04:06 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-13 15:07:03 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-07-13 14:08:57 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-07-13 15:01:33 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-07-13 15:02:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-07-13 15:00:28 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)