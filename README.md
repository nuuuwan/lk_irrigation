# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_03:11:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 03:11:52 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:08:25 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-07 03:07:18 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:07:06 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.079 |  |
| 2026-07-07 03:06:50 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-07 03:06:41 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.018 |  |
| 2026-07-07 03:06:11 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-07-07 03:06:11 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.009 |  |
| 2026-07-07 03:06:00 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:04:57 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:04:25 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.321 |  |
| 2026-07-07 03:04:05 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:41 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:38 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:31 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-07-07 03:03:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:22 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-07 03:03:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-07-07 03:03:11 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:04 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:02:55 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-07 03:02:43 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:02:42 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 03:02:34 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-07 03:02:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:02:16 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:02:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.047 |  |
| 2026-07-07 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:00:59 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.015 |  |
| 2026-07-07 03:00:50 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:00:45 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-07 02:59:28 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.079 |  |
| 2026-07-07 02:44:20 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.006 |  |
| 2026-07-07 02:36:04 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 03:03:31 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-07-07 03:06:11 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-07-07 03:03:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-07-07 03:00:45 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-07 03:08:25 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-07 03:06:50 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-07 03:02:42 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 03:02:34 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-07 03:00:50 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:41 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:07:18 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:11 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:06:00 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:04:05 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:02:16 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:03:04 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:04:57 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:15:51 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:00:56 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:08:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:02:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 03:11:52 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:44:20 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.006 |  |
| 2026-07-07 03:06:11 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.009 |  |
| 2026-07-06 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:06:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-07 03:02:55 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-07 03:03:22 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-07 02:01:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-07-07 03:00:59 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.015 |  |
| 2026-07-07 02:15:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.017 |  |
| 2026-07-07 03:06:41 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.018 |  |
| 2026-07-07 02:03:05 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-07-07 03:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.047 |  |
| 2026-07-07 03:07:06 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.079 |  |
| 2026-07-07 02:12:29 | Yaka Wewa (Ma Oya) | 0.12 | 🟢 Normal | -0.314 |  |
| 2026-07-07 03:04:25 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.321 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)