# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_02:12:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 02:12:58 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:11:12 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-26 02:08:57 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:08:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:08:11 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.029 |  |
| 2026-05-26 02:06:34 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-05-26 02:06:24 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-26 02:05:46 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 02:05:44 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-05-26 02:05:11 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-26 02:04:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-26 02:03:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:03:43 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.019 |  |
| 2026-05-26 02:03:34 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-05-26 02:02:50 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-26 02:02:45 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:02:32 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-26 02:02:17 | Rathnapura (Kalu Ganga) | 4.46 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-05-26 02:01:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:01:32 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:00:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:00:35 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 01:25:19 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | 0.044 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 00:21:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.023 |  |
| 2026-05-26 02:02:17 | Rathnapura (Kalu Ganga) | 4.46 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-05-26 02:11:12 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-26 02:05:11 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-26 01:08:25 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-26 02:02:32 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-26 02:06:24 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-26 01:15:29 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-26 02:04:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-26 02:00:35 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 02:05:46 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 02:08:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:12:58 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:00:47 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:01:32 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:01:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:49 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:00:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:21:44 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:02:45 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:03:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:08:14 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:38 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:04:54 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:32 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-26 02:08:57 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:14:37 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-26 02:03:34 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-26 01:02:51 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-26 02:03:43 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.019 |  |
| 2026-05-26 02:05:44 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-05-26 02:02:50 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-26 02:08:11 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.029 |  |
| 2026-05-26 01:06:27 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-05-26 02:06:34 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)