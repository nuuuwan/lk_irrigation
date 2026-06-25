# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_21:16:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 21:16:56 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:14:55 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-06-25 21:14:35 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:12:07 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.009 |  |
| 2026-06-25 21:09:43 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:08:41 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:06:33 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:05:25 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:05:10 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2026-06-25 21:04:55 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:04:51 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-06-25 21:04:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 21:04:30 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:03:44 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-06-25 21:03:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-06-25 21:03:27 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.059 |  |
| 2026-06-25 21:03:17 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:03:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:03:08 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:02:51 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:29 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-06-25 21:02:25 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:25 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-25 21:02:17 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:11 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:02 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:01:58 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-06-25 21:01:51 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:01:49 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:01:42 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-25 21:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 21:01:12 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-06-25 21:01:07 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-06-25 21:00:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:57:56 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 21:03:44 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-06-25 21:01:07 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-06-25 21:02:29 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-06-25 21:01:12 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-06-25 21:04:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 21:01:42 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-25 21:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 21:00:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:01:51 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:16:56 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:03:17 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:03:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:09:43 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:14:35 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:25 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:04:30 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:01:49 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:11 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:51 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:04:55 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:02:17 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:06:33 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 21:12:07 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.009 |  |
| 2026-06-25 21:14:55 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-06-25 21:03:08 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:05:25 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:02:02 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:08:41 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-25 21:01:58 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-06-25 21:02:25 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.024 |  |
| 2026-06-25 21:05:10 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2026-06-25 21:03:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-06-25 21:04:51 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-06-25 21:03:27 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)