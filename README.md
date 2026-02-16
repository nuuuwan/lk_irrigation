# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_14:32:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,665 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 14:32:31 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:17:16 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:15:07 | Thawalama (Gin Ganga) | 0.22 | 🟢 Normal | -7.455 |  |
| 2026-02-16 14:14:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:12:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-16 14:08:31 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -7.455 |  |
| 2026-02-16 14:08:21 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:07:51 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:06:10 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.015 |  |
| 2026-02-16 14:05:50 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:05:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.093 |  |
| 2026-02-16 14:04:49 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:04:30 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-16 14:04:09 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:04:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-16 14:03:22 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:20 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:03:16 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:03:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:07 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-02-16 14:03:07 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:02 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:00 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:02:53 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:42 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:40 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:39 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-16 14:02:07 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:07 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:01:54 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:01:53 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.206 |  |
| 2026-02-16 14:01:53 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:01:50 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:01:46 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:01:41 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:01:03 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:00:27 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 14:04:30 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-16 14:03:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-16 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-16 14:12:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-16 14:00:27 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 14:02:07 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:07 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:32:31 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:01:50 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:53 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:42 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-16 12:08:43 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-16 13:03:36 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:03:16 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:07:51 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:17:16 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:14:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:01:53 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:02:39 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:03:20 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:04:49 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:05:50 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:08:21 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:01:03 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 14:03:00 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:01:54 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:01:46 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:07 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:22 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:04:09 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:04:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:03:02 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-16 14:06:10 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.015 |  |
| 2026-02-16 13:01:31 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.021 |  |
| 2026-02-16 14:03:07 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-02-16 14:05:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.093 |  |
| 2026-02-16 14:01:53 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.206 |  |
| 2026-02-16 14:15:07 | Thawalama (Gin Ganga) | 0.22 | 🟢 Normal | -7.455 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)