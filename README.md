# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_06:19:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 06:19:22 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 06:18:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:12:18 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-07-11 06:10:59 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.126 |  |
| 2026-07-11 06:09:55 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:08:57 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.073 |  |
| 2026-07-11 06:08:37 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:08:33 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-11 06:07:41 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.036 |  |
| 2026-07-11 06:06:56 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:06:23 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.101 |  |
| 2026-07-11 06:05:29 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:05:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:05:20 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:04:55 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.029 |  |
| 2026-07-11 06:04:17 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:03:46 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 06:03:44 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-11 06:03:38 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:03:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:03:19 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-11 06:03:14 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.022 |  |
| 2026-07-11 06:03:07 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:02:50 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:02:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-11 06:02:46 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-11 06:02:17 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-11 06:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:01:48 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 06:01:47 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 06:01:41 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-11 06:01:21 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 06:01:18 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:01:10 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:00:43 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-07-11 06:00:32 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-11 05:51:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 06:02:17 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-11 06:01:41 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-11 06:03:19 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-11 06:19:22 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 06:02:46 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-11 06:01:48 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 06:01:47 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 06:01:21 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 06:03:46 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 06:02:50 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:05:20 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:00:32 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:08:37 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:00:43 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:09:34 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:03:38 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:09:55 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:04:17 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:18:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:05:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:03:07 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:03:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:06:56 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:05:29 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:01:18 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:01:10 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-11 06:12:18 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-07-11 06:08:33 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-11 06:03:44 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-11 06:02:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-11 06:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-07-11 06:03:14 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.022 |  |
| 2026-07-11 06:04:55 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.029 |  |
| 2026-07-11 06:07:41 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.036 |  |
| 2026-07-11 06:08:57 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.073 |  |
| 2026-07-11 06:06:23 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.101 |  |
| 2026-07-11 06:10:59 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)