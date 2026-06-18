# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_21:10:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,026 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 21:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:08:38 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.028 |  |
| 2026-06-18 21:08:03 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:06:48 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-06-18 21:05:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.099 |  |
| 2026-06-18 21:05:18 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 21:05:14 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 21:05:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.122 |  |
| 2026-06-18 21:05:00 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:04:18 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.031 |  |
| 2026-06-18 21:04:03 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-06-18 21:04:03 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.019 |  |
| 2026-06-18 21:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:03:49 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:03:43 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.029 |  |
| 2026-06-18 21:03:17 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:03:04 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:54 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-18 21:02:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:32 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:32 | Dunamale (Aththanagalu Oya) | 2.83 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-18 21:02:27 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-06-18 21:02:27 | Hanwella (Kelani Ganga) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 21:02:23 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:20 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-06-18 21:02:05 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 21:01:46 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.034 |  |
| 2026-06-18 21:01:36 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.032 |  |
| 2026-06-18 21:01:33 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:01:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:01:19 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:01:04 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:00:33 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 21:02:20 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-06-18 21:02:32 | Dunamale (Aththanagalu Oya) | 2.83 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-18 21:02:27 | Hanwella (Kelani Ganga) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 21:05:14 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 21:05:18 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 21:02:05 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 21:03:17 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:00:33 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:23 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:01:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:08:03 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:32 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:03:49 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:02:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:05:00 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:03:04 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:01:33 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:01:19 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 21:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-06-18 20:00:59 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-18 21:04:03 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-06-18 20:03:52 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-06-18 21:04:03 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.019 |  |
| 2026-06-18 21:02:27 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-06-18 21:02:54 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-18 21:06:48 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-06-18 21:08:38 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.028 |  |
| 2026-06-18 21:03:43 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.029 |  |
| 2026-06-18 21:04:18 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.031 |  |
| 2026-06-18 21:01:36 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.032 |  |
| 2026-06-18 21:01:46 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.034 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-18 21:05:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.099 |  |
| 2026-06-18 21:05:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)