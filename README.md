# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_16:11:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,184 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 16:11:27 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:11:22 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:11:05 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-12 16:10:09 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 16:09:56 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:08:45 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-12 16:08:20 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-12 16:06:54 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-12 16:06:22 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-02-12 16:06:20 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:06:12 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:06:07 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 16:05:43 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 16:05:30 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.009 |  |
| 2026-02-12 16:04:28 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-12 16:04:25 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:03:49 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:03:29 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-02-12 16:03:29 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:03:12 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:37 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:29 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:27 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-12 16:02:22 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:01:58 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:01:54 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:01:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:01:48 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-12 16:01:43 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-02-12 16:01:36 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:01:09 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:00:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-12 16:00:42 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-02-12 16:00:41 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 16:00:27 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 16:11:05 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-12 16:00:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-12 16:10:09 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 16:01:48 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-12 16:04:28 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-12 16:08:20 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-12 16:02:27 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-12 16:08:45 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-12 16:00:41 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 16:06:07 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 16:05:43 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 16:06:54 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-12 16:01:54 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:01:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:00:27 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:03:29 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:29 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:04:25 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:11:27 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:01:58 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:06:20 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:11:22 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:03:49 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:06:12 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:03:12 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:01:09 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:22 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:06:22 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-02-12 16:05:30 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.009 |  |
| 2026-02-12 16:01:36 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:02:37 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:02:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:09:56 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-12 16:03:29 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-02-12 16:00:42 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-02-12 16:01:43 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)