# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_03:12:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 03:12:16 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:12:09 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.028 |  |
| 2026-05-21 03:10:58 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-05-21 03:10:41 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.027 |  |
| 2026-05-21 03:08:17 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:07:43 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:07:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:07:09 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-05-21 03:06:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:05:50 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-21 03:05:42 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.937 |  |
| 2026-05-21 03:04:40 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.004 |  |
| 2026-05-21 03:04:25 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-21 03:03:55 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:03:53 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-21 03:03:50 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:03:46 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.153 |  |
| 2026-05-21 03:02:58 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.041 |  |
| 2026-05-21 03:02:56 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-21 03:02:53 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-05-21 03:02:45 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-21 03:02:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-05-21 03:02:20 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-21 03:02:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:02:10 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 03:01:55 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:01:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:01:26 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:01:21 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-05-21 02:44:53 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 03:02:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-05-21 03:02:45 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-21 03:05:50 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-21 03:03:53 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-21 03:02:10 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 03:02:20 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-21 03:04:40 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.004 |  |
| 2026-05-21 03:12:16 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:02:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:07:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:01:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:01:01 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:08:59 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:07:43 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:01:26 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-21 02:01:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:06:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:03:55 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:08:17 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:01:21 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:03:50 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.003 |  |
| 2026-05-21 03:10:58 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-05-21 02:13:48 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-05-21 03:02:56 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-21 03:04:25 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-21 01:08:41 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-21 03:02:53 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-05-21 02:04:36 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.021 |  |
| 2026-05-21 03:07:09 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-05-21 03:10:41 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.027 |  |
| 2026-05-21 03:12:09 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.028 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-21 03:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-05-21 03:02:58 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.041 |  |
| 2026-05-21 03:03:46 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.153 |  |
| 2026-05-21 03:05:42 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.937 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)