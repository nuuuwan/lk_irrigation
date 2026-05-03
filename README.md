# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_18:20:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,988 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 18:20:16 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:10:24 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-05-03 18:09:14 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.022 |  |
| 2026-05-03 18:08:56 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.036 |  |
| 2026-05-03 18:08:20 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-03 18:08:01 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:07:01 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:06:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.115 |  |
| 2026-05-03 18:05:47 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:05:22 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:05:12 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:04:17 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-03 18:04:12 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.029 |  |
| 2026-05-03 18:04:11 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:03:51 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:03:41 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:03:14 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-03 18:02:57 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:27 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:26 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:22 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:06 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 18:01:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-03 18:01:37 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:28 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:27 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.034 |  |
| 2026-05-03 18:01:26 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.040 |  |
| 2026-05-03 18:01:03 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:47 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:33 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 18:01:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 18:04:17 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-03 18:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 18:02:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:06 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:05:22 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:47 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:57 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:04:11 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:07:01 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:20:16 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:28 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:03:41 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:05:47 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:03 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:22 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:05:12 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:02:27 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:03:51 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:10:24 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-05-03 18:08:20 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-03 18:03:14 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-03 18:01:37 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:26 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:08:01 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-03 18:09:14 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.022 |  |
| 2026-05-03 18:04:12 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.029 |  |
| 2026-05-03 18:01:27 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.034 |  |
| 2026-05-03 18:08:56 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.036 |  |
| 2026-05-03 18:01:26 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.040 |  |
| 2026-05-03 17:04:17 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-05-03 18:06:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)