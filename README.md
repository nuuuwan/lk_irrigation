# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_15:10:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,462 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **47** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 15:10:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:09:38 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:09:25 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:09:03 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:06:43 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-02-09 15:06:42 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:06:29 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:05:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.065 |  |
| 2026-02-09 15:04:21 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:04:13 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:04:11 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:04:02 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.015 |  |
| 2026-02-09 15:03:56 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-02-09 15:03:51 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:03:50 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:03:45 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:03:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:03:39 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-09 15:03:08 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-02-09 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-09 15:02:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:43 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.021 |  |
| 2026-02-09 15:02:43 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-09 15:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:02:32 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:20 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.013 |  |
| 2026-02-09 15:02:01 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:01 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:01:52 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:01:51 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.013 |  |
| 2026-02-09 15:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:01:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-09 15:01:36 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:01:24 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:01:21 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.020 |  |
| 2026-02-09 15:01:03 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:00:59 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:00:53 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-09 15:00:39 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:00:32 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-02-09 14:37:40 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 14:16:41 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 14:16:40 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.013 |  |
| 2026-02-09 14:16:09 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.013 |  |
| 2026-02-09 14:14:18 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 15:02:43 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-09 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-09 15:00:53 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-09 15:01:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-09 15:03:39 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-09 15:00:39 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:01:52 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:04:13 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:03:51 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:09:25 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:01 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:03:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:01 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:06:42 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:09:38 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:06:29 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:03:45 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:01:03 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:04:11 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:09:03 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:10:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 15:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:04:21 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:01:24 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:00:32 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:00:59 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:01:36 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-02-09 15:03:56 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-02-09 15:03:08 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-02-09 15:02:20 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.013 |  |
| 2026-02-09 15:01:51 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.013 |  |
| 2026-02-09 15:04:02 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.015 |  |
| 2026-02-09 15:06:43 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-02-09 15:01:21 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.020 |  |
| 2026-02-09 15:02:43 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.021 |  |
| 2026-02-09 15:05:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)