# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_22:22:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,041 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 22:22:51 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.042 |  |
| 2026-02-25 22:17:35 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:08:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-02-25 22:08:06 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 22:06:49 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-25 22:06:33 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-25 22:06:19 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:05:44 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:05:41 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:05:08 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:04:58 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:04:52 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-25 22:04:36 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:04:03 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 22:03:43 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:03:42 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:03:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:03:22 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:03:12 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:46 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-02-25 22:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:29 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:13 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:10 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-02-25 22:01:57 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:01:53 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:01:37 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:01:29 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-25 22:01:17 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-02-25 22:00:43 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-02-25 22:00:09 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 22:06:49 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-25 22:01:29 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-25 22:06:33 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-25 22:00:09 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-25 21:05:58 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-25 22:04:03 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 22:04:52 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 22:08:06 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 22:02:13 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:03:12 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:17:35 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:29 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:01:37 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:05:44 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:05:08 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:05:41 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:02:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 21:02:21 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:03:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:06:19 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 22:03:43 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-25 21:04:20 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:02:10 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:01:53 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:01:57 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:04:58 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:03:42 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:03:22 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-02-25 22:00:43 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-02-25 22:02:46 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-02-25 22:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-02-25 22:01:17 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-02-25 22:22:51 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.042 |  |
| 2026-02-25 22:08:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)