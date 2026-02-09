# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_11:14:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 11:14:09 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-02-09 11:11:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-02-09 11:11:25 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-02-09 11:08:56 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:08:44 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:08:36 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.048 |  |
| 2026-02-09 11:07:39 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-02-09 11:06:30 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.200 |  |
| 2026-02-09 11:05:40 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.039 |  |
| 2026-02-09 11:04:56 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:04:22 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:04:02 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 11:03:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:03:52 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-09 11:03:45 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.068 |  |
| 2026-02-09 11:03:39 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-02-09 11:03:35 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:03:05 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-02-09 11:02:40 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-09 11:02:36 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:02:20 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:02:13 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:46 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:39 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 11:01:37 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:35 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 11:01:35 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.081 |  |
| 2026-02-09 11:01:22 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:22 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.063 |  |
| 2026-02-09 11:01:15 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:06 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-09 11:01:06 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 11:00:48 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:00:42 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:00:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-09 10:30:18 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 11:04:02 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 11:03:52 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-09 11:01:46 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 11:01:35 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 11:01:39 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 11:01:06 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 11:00:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:00:48 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:02:13 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:02:20 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:08:44 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:08:56 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:03:35 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:37 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:15 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:02:36 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:04:56 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:03:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:04:22 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-09 10:30:18 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:01:22 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:00:42 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-09 11:03:39 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-02-09 11:01:06 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-09 11:02:40 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-09 11:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-09 11:03:05 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-02-09 11:11:25 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-02-09 11:11:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-02-09 11:07:39 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-02-09 11:14:09 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-02-09 11:05:40 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.039 |  |
| 2026-02-09 11:08:36 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.048 |  |
| 2026-02-09 11:01:22 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.063 |  |
| 2026-02-09 11:03:45 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.068 |  |
| 2026-02-09 11:01:35 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.081 |  |
| 2026-02-09 11:06:30 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)