# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_20:21:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **217,026 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 20:21:54 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.024 |  |
| 2026-07-26 20:13:21 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:12:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-26 20:12:23 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:12:18 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:12:10 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:10:04 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-26 20:07:52 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.068 |  |
| 2026-07-26 20:07:37 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:07:07 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-26 20:06:06 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:06:01 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.040 |  |
| 2026-07-26 20:05:47 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:05:38 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-26 20:05:33 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-26 20:05:15 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:05:13 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-26 20:05:06 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:05:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:04:23 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-26 20:04:11 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:04:08 | Moraketiya (Walawe Ganga) | 0.08 | 🟢 Normal | -0.688 |  |
| 2026-07-26 20:03:43 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:03:30 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.029 |  |
| 2026-07-26 20:03:29 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:02:45 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 20:02:22 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-07-26 20:05:38 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-26 20:10:04 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-26 20:05:33 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-26 20:12:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-26 20:05:13 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-26 20:02:25 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 20:07:07 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-26 20:01:55 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:05:06 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:01:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:02:45 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:12:23 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 18:03:43 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:13:21 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:03:29 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:02:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:03:43 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:02:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:01:20 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:05:15 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:12:10 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:05:47 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:07:37 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:00:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-26 18:00:36 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:06:06 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:12:18 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:02:22 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:04:11 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 20:04:23 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-26 20:00:32 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-07-26 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.020 |  |
| 2026-07-26 20:21:54 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.024 |  |
| 2026-07-26 20:03:30 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.029 |  |
| 2026-07-26 20:06:01 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.040 |  |
| 2026-07-26 20:07:52 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.068 |  |
| 2026-07-26 20:04:08 | Moraketiya (Walawe Ganga) | 0.08 | 🟢 Normal | -0.688 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)