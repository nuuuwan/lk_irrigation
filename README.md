# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_12:12:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 12:12:25 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-02-17 12:09:44 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:09:27 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:09:17 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:08:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-17 12:08:02 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:07:46 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:07:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:07:14 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 12:07:13 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-17 12:06:30 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:06:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:06:18 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.016 |  |
| 2026-02-17 12:05:44 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:05:40 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-17 12:04:45 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.029 |  |
| 2026-02-17 12:04:18 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:03:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-17 12:03:51 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:03:50 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:03:47 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:03:41 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-17 12:03:34 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.031 |  |
| 2026-02-17 12:03:21 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-02-17 12:03:18 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.029 |  |
| 2026-02-17 12:03:05 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:02:52 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:02:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:02:22 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.198 |  |
| 2026-02-17 12:02:13 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 12:02:11 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:02:10 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-17 12:01:37 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-17 12:01:18 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:01:17 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:00:58 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:00:46 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 12:12:25 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-02-17 12:05:40 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-17 12:03:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-17 12:02:10 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-17 12:07:13 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-17 12:01:37 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-17 12:02:13 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 12:07:14 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 12:00:46 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:02:11 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:03:47 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:09:17 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 12:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:01:17 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:02:52 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:09:44 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:09:27 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:02:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:03:05 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:04:18 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:01:18 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:05:44 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:03:51 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:06:30 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:06:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:07:46 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:08:02 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:03:50 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:00:58 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:03:41 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-17 12:08:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-17 12:06:18 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.016 |  |
| 2026-02-17 11:09:28 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-02-17 12:04:45 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.029 |  |
| 2026-02-17 12:03:18 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.029 |  |
| 2026-02-17 12:03:34 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.031 |  |
| 2026-02-17 12:03:21 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-02-17 12:02:22 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.198 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)