# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_01:29:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,815 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 01:29:55 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:26:42 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:21:51 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:20:21 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:18:32 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-10 01:12:41 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-02-10 01:07:56 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 7.910 | 🔺 Rising |
| 2026-02-10 01:07:03 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:06:14 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:05:47 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:04:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:04:12 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:03:54 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:03:38 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:03:37 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-02-10 01:03:01 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:02:47 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-10 01:02:10 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 01:02:10 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-10 01:02:01 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.149 |  |
| 2026-02-10 01:02:01 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 7.910 | 🔺 Rising |
| 2026-02-10 01:01:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:51 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:46 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:44 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:01:25 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:02 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-02-10 00:56:47 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 01:07:56 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 7.910 | 🔺 Rising |
| 2026-02-10 01:02:10 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-10 01:02:47 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-10 01:18:32 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-10 01:02:10 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 23:36:28 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-10 00:01:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 00:03:28 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:05:47 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:51 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:20:21 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:46 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:03:01 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:21:51 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:06:14 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:02 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:26:42 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:29:55 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:04:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:01:25 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 00:01:24 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 00:24:54 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-10 00:02:41 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:12:41 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-02-10 00:03:19 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:03:54 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-09 22:00:53 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:07:03 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:03:38 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-10 01:01:44 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-09 20:18:59 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-02-09 21:04:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.023 |  |
| 2026-02-10 01:03:37 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |
| 2026-02-09 23:06:15 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.108 |  |
| 2026-02-10 01:02:01 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)