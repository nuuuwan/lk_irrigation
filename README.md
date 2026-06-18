# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_22:21:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,063 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 22:21:27 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-06-18 22:14:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.076 |  |
| 2026-06-18 22:08:52 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-06-18 22:07:15 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.051 |  |
| 2026-06-18 22:06:48 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:06:25 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 22:06:10 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-06-18 22:05:56 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 22:05:23 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | -0.038 |  |
| 2026-06-18 22:04:57 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-06-18 22:04:46 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 22:03:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-06-18 22:03:32 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:03:29 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.010 |  |
| 2026-06-18 22:03:22 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-18 22:02:58 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:51 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-06-18 22:02:37 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:28 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:21 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-18 22:02:12 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-18 22:02:06 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-18 22:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | -0.047 |  |
| 2026-06-18 22:02:01 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:45 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:43 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:31 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:20 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:00:57 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 22:00:53 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:00:40 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:00:33 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.005 |  |
| 2026-06-18 22:00:31 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 21:02:20 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-06-18 22:02:12 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-18 22:02:21 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-18 22:04:46 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 22:00:57 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 22:05:56 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 22:06:25 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 22:02:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:20 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:00:53 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:00:40 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:28 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:01 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:03:32 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:45 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:58 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:02:37 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:31 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:06:48 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:01:43 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 22:00:33 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.005 |  |
| 2026-06-18 22:06:10 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-06-18 22:03:29 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.010 |  |
| 2026-06-18 22:02:06 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-18 22:00:31 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-06-18 22:21:27 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-06-18 22:03:22 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-18 22:08:52 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-06-18 22:03:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-06-18 22:05:23 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | -0.038 |  |
| 2026-06-18 22:04:57 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-18 22:02:51 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-06-18 22:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | -0.047 |  |
| 2026-06-18 22:07:15 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.051 |  |
| 2026-06-18 22:14:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)