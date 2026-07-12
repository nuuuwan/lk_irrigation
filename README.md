# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_11:23:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,173 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 11:23:35 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:22:55 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:09:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2026-07-12 11:08:37 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-07-12 11:08:04 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:07:38 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:07:18 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:06:36 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:06:23 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.020 |  |
| 2026-07-12 11:05:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:54 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:36 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:11 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-07-12 11:04:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:04:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-07-12 11:04:29 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-07-12 11:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:04:05 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.035 |  |
| 2026-07-12 11:03:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:03:25 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-12 11:03:10 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-07-12 11:03:06 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:03:05 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-07-12 11:03:02 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 11:02:56 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:02:47 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.065 |  |
| 2026-07-12 11:02:40 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-07-12 11:02:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-12 11:02:29 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-12 11:02:14 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.020 |  |
| 2026-07-12 11:01:49 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:44 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:24 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:19 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-12 11:01:11 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:10 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:00:52 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:00:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 11:05:11 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-07-12 11:03:05 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-07-12 11:04:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-07-12 11:03:02 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 11:01:11 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:06:36 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:44 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:00:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:08:04 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:07:38 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:10 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:04:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:23:35 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:03:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:02:56 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:36 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:03:06 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:54 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:07:18 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:49 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:00:52 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:05:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:22:55 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:01:24 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 11:03:25 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-12 11:02:29 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-12 11:01:19 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-12 11:02:40 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-07-12 11:02:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-12 11:04:29 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-07-12 11:08:37 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-07-12 11:06:23 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.020 |  |
| 2026-07-12 11:02:14 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.020 |  |
| 2026-07-12 11:03:10 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-07-12 11:04:05 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.035 |  |
| 2026-07-12 11:09:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2026-07-12 11:02:47 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)