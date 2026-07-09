# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_01:27:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,987 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 01:27:44 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:20:31 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:13:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-07-10 01:11:41 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:07:36 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:07:04 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.005 |  |
| 2026-07-10 01:06:51 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:06:31 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:06:11 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 01:06:04 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:05:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:04:39 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:04:30 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:04:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:03:55 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:03:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-10 01:03:13 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:03:01 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-07-10 01:02:48 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.102 |  |
| 2026-07-10 01:02:39 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:02:17 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:02:09 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:02:00 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 01:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-07-10 01:01:20 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.021 |  |
| 2026-07-10 01:01:13 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-07-10 01:01:02 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.067 |  |
| 2026-07-10 01:00:50 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:00:32 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 01:13:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-07-10 01:02:00 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 01:06:11 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 01:07:04 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.005 |  |
| 2026-07-10 01:00:32 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 00:02:32 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:03:13 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 00:07:05 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:04:39 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:00:50 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:21 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:07:36 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 00:10:36 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:02:39 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:02:09 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-10 00:05:24 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:20:31 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:04:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:06:31 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | 0.000 |  |
| 2026-07-10 00:10:53 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:02:17 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:06:51 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:03:55 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:04:30 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:11:41 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:40 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:27:44 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:05:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:06:04 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 00:07:25 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 01:03:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-10 01:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-07-09 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.011 |  |
| 2026-07-10 01:03:01 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-07-10 01:01:20 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.021 |  |
| 2026-07-10 01:01:13 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-07-10 00:06:43 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.059 |  |
| 2026-07-10 01:01:02 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.067 |  |
| 2026-07-10 01:02:48 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)