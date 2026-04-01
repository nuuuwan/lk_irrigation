# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_15:09:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,330 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 15:09:31 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-04-01 15:09:13 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-04-01 15:08:23 | Glencourse (Kelani Ganga) | 8.16 | 🟢 Normal | -0.019 |  |
| 2026-04-01 15:07:19 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:06:12 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:05:01 | Rathnapura (Kalu Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-04-01 15:04:59 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:04:55 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-01 15:04:30 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:04:01 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:03:51 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:03:27 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 15:03:24 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-01 15:03:14 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-01 15:03:14 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:03:13 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-01 15:02:51 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-01 15:02:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -2.000 |  |
| 2026-04-01 15:02:29 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:17 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:17 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -2.000 |  |
| 2026-04-01 15:02:14 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:58 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-01 15:01:58 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-01 15:01:43 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:33 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-01 15:01:30 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.165 |  |
| 2026-04-01 15:01:21 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:14 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:09 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-01 15:00:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-01 15:00:32 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:00:27 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-01 14:29:47 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 15:01:09 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-01 15:00:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-01 15:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-01 15:01:33 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-01 15:03:14 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-01 15:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-01 15:03:27 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 15:02:17 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:14 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:51 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:00:32 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:03:51 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:21 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:58 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:04:01 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:06:12 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:14 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:04:59 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:03:13 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:07:19 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:04:30 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:03:14 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:01:43 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:08:34 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:29 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:02:17 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 15:04:55 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-01 15:01:58 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-01 15:09:13 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-04-01 15:03:24 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-01 15:00:27 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-01 15:09:31 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-04-01 15:08:23 | Glencourse (Kelani Ganga) | 8.16 | 🟢 Normal | -0.019 |  |
| 2026-04-01 15:05:01 | Rathnapura (Kalu Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-04-01 15:01:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-01 15:01:30 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.165 |  |
| 2026-04-01 15:02:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -2.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)