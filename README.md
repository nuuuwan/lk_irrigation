# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_02:33:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,481 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 02:33:50 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.007 |  |
| 2026-02-23 02:23:48 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:13:34 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 02:11:01 | Manampitiya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.064 |  |
| 2026-02-23 02:10:43 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.056 |  |
| 2026-02-23 02:09:40 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:09:20 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:08:34 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-02-23 02:07:19 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-23 02:07:00 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-23 02:06:06 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.022 |  |
| 2026-02-23 02:04:47 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-02-23 02:04:39 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -1.333 |  |
| 2026-02-23 02:04:35 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-02-23 02:04:25 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.086 |  |
| 2026-02-23 02:04:19 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -1.333 |  |
| 2026-02-23 02:03:48 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.206 |  |
| 2026-02-23 02:03:36 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | -0.020 |  |
| 2026-02-23 02:03:34 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-02-23 02:03:30 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:03:29 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.065 |  |
| 2026-02-23 02:03:28 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-23 02:03:07 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:03:03 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:02:51 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-23 02:02:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-23 02:02:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:02:13 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-02-23 02:02:01 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:01:39 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.102 |  |
| 2026-02-23 02:01:12 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:01:12 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-02-23 02:00:47 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.110 |  |
| 2026-02-23 02:00:22 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.076 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 02:02:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 02:02:51 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-23 02:13:34 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 02:23:48 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:04:19 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:00:53 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:02:40 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:03:30 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:01:12 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:03:03 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:09:40 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.005 |  |
| 2026-02-23 02:33:50 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.007 |  |
| 2026-02-23 02:08:34 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-02-23 02:07:19 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-23 02:03:28 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-23 02:07:00 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-23 02:04:47 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-02-23 02:01:12 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-02-23 02:03:36 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | -0.020 |  |
| 2026-02-23 02:03:34 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-02-23 02:06:06 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.022 |  |
| 2026-02-23 01:50:35 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.028 |  |
| 2026-02-23 02:02:13 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-02-23 02:04:35 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-02-23 02:10:43 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.056 |  |
| 2026-02-23 02:11:01 | Manampitiya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.064 |  |
| 2026-02-23 02:03:29 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.065 |  |
| 2026-02-23 01:01:09 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-02-23 02:00:22 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.076 |  |
| 2026-02-23 02:04:25 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.086 |  |
| 2026-02-23 02:01:39 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.102 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-23 02:00:47 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.110 |  |
| 2026-02-23 02:03:48 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.206 |  |
| 2026-02-23 02:04:39 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -1.333 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)