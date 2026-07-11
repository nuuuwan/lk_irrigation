# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_03:04:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,853 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 03:04:19 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.169 |  |
| 2026-07-12 03:04:18 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-07-12 03:04:11 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2026-07-12 03:04:05 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-07-12 03:03:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:03:39 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-12 03:03:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:03:11 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:03:07 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.013 |  |
| 2026-07-12 03:02:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:02:44 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-12 03:02:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:02:20 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:02:07 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-07-12 03:01:42 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-12 03:01:17 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.005 |  |
| 2026-07-12 03:01:08 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:52:04 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-12 02:43:29 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-12 02:37:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:23:15 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.005 |  |
| 2026-07-12 02:17:06 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.013 |  |
| 2026-07-12 02:16:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 02:43:29 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-12 02:52:04 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-12 03:03:39 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-12 03:02:44 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-12 02:23:15 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.005 |  |
| 2026-07-12 03:03:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:02:07 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:03:11 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:03:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 00:02:04 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:37:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:28 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:08:34 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 01:01:05 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-12 00:12:19 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:02:20 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:05:39 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:02:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:14:18 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:04:37 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:09:29 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:00:48 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:02:03 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:02:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:01:08 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-12 02:01:27 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 03:01:17 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.005 |  |
| 2026-07-12 02:05:28 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-07-12 03:04:05 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-07-12 02:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-12 03:01:42 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-12 03:03:07 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.013 |  |
| 2026-07-12 03:04:18 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-07-12 02:07:37 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.022 |  |
| 2026-07-12 02:16:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.027 |  |
| 2026-07-12 03:04:11 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2026-07-12 03:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.041 |  |
| 2026-07-12 03:04:19 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)