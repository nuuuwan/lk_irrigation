# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_23:36:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,472 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 23:36:02 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:22:55 | Moraketiya (Walawe Ganga) | 1.69 | 🟢 Normal | -0.016 |  |
| 2026-02-21 23:17:06 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:15:47 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:13:21 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-02-21 23:11:58 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.104 |  |
| 2026-02-21 23:11:43 | Urawa (Nilwala Ganga) | 2.56 | 🟡 Alert | 0.267 | 🔺 Rising |
| 2026-02-21 23:11:27 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-21 23:10:06 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-02-21 23:08:48 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:07:43 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-02-21 23:07:34 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-21 23:06:33 | Rathnapura (Kalu Ganga) | 5.37 | 🟡 Alert | 0.215 | 🔺 Rising |
| 2026-02-21 23:06:32 | Thaldena (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.123 |  |
| 2026-02-21 23:06:00 | Wellawaya (Kirindi Oya) | 3.54 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-02-21 23:05:36 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-21 23:05:30 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.023 |  |
| 2026-02-21 23:05:15 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.685 | 🔺 Rising |
| 2026-02-21 23:05:14 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:05:01 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 23:04:40 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.032 |  |
| 2026-02-21 23:04:31 | Peradeniya (Mahaweli Ganga) | 4.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 23:04:27 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-21 23:04:22 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-02-21 23:03:41 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-02-21 23:03:37 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:03:22 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:03:10 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-21 23:02:58 | Nakkala (Kumbukkan Oya) | 2.48 | 🟢 Normal | -0.435 |  |
| 2026-02-21 23:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-21 23:02:55 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:02:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:02:26 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-02-21 23:02:21 | Holombuwa (Kelani Ganga) | 2.48 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-02-21 23:02:18 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-21 23:01:10 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 23:00:38 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 23:11:43 | Urawa (Nilwala Ganga) | 2.56 | 🟡 Alert | 0.267 | 🔺 Rising |
| 2026-02-21 23:06:33 | Rathnapura (Kalu Ganga) | 5.37 | 🟡 Alert | 0.215 | 🔺 Rising |
| 2026-02-21 23:05:15 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.685 | 🔺 Rising |
| 2026-02-21 23:03:41 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-02-21 23:02:26 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-02-21 23:07:43 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-02-21 23:10:06 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-02-21 23:02:21 | Holombuwa (Kelani Ganga) | 2.48 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-02-21 23:13:21 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-02-21 23:06:00 | Wellawaya (Kirindi Oya) | 3.54 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-02-21 23:05:36 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-21 23:04:27 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-21 23:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-21 23:11:27 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-21 23:03:10 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-21 23:04:31 | Peradeniya (Mahaweli Ganga) | 4.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 23:07:34 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-21 23:05:01 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 23:02:18 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-21 23:01:10 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 22:07:33 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 23:36:02 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:17:06 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:15:47 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:03:37 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:05:14 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:03:22 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:02:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 23:22:55 | Moraketiya (Walawe Ganga) | 1.69 | 🟢 Normal | -0.016 |  |
| 2026-02-21 23:04:22 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-21 23:05:30 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.023 |  |
| 2026-02-21 23:04:40 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.032 |  |
| 2026-02-21 23:00:38 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.063 |  |
| 2026-02-21 23:11:58 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.104 |  |
| 2026-02-21 23:06:32 | Thaldena (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.123 |  |
| 2026-02-21 23:02:58 | Nakkala (Kumbukkan Oya) | 2.48 | 🟢 Normal | -0.435 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)