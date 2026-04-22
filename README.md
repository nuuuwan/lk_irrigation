# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_13:13:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,986 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 13:13:36 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.034 |  |
| 2026-04-22 13:10:08 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.054 |  |
| 2026-04-22 13:09:38 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-04-22 13:08:26 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:08:24 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-04-22 13:07:56 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:07:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:07:04 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.018 |  |
| 2026-04-22 13:06:28 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-04-22 13:06:27 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.090 |  |
| 2026-04-22 13:06:06 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:04:45 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:04:12 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.024 |  |
| 2026-04-22 13:03:29 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-04-22 13:03:28 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-04-22 13:03:25 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-22 13:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:03:13 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.040 |  |
| 2026-04-22 13:03:07 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-04-22 13:03:01 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:02:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-22 13:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-04-22 13:02:48 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-22 13:02:32 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 13:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-04-22 13:02:23 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-04-22 13:02:19 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-04-22 13:02:11 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.021 |  |
| 2026-04-22 13:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:01:44 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-22 13:01:28 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:01:27 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:01:08 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.015 |  |
| 2026-04-22 13:01:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:00:56 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:00:56 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:00:48 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-22 13:00:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:50:49 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 13:02:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-22 13:02:48 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-22 13:02:32 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 13:01:28 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:00:56 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:08:26 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:01:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:00:56 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 12:20:23 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:00:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:06:06 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:07:56 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 13:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:04:45 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:07:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:03:01 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:01:27 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.010 |  |
| 2026-04-22 13:03:07 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-04-22 13:01:08 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.015 |  |
| 2026-04-22 13:06:28 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-04-22 13:07:04 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.018 |  |
| 2026-04-22 13:08:24 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-04-22 13:03:25 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-22 13:00:48 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-22 13:02:11 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.021 |  |
| 2026-04-22 13:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-04-22 13:04:12 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.024 |  |
| 2026-04-22 13:09:38 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-04-22 13:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-04-22 13:01:44 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-22 13:02:23 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-04-22 13:03:28 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-04-22 13:13:36 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.034 |  |
| 2026-04-22 13:03:13 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.040 |  |
| 2026-04-22 13:03:29 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-04-22 13:02:19 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-04-22 13:10:08 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.054 |  |
| 2026-04-22 13:06:27 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)