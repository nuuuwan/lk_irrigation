# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_05:28:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 05:28:00 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-22 05:27:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.025 |  |
| 2026-11-22 05:20:54 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.008 |  |
| 2026-11-22 05:19:04 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-11-22 05:09:04 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:08:17 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-11-22 05:06:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.182 |  |
| 2026-11-22 05:06:03 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-11-22 05:05:50 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:04:52 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-22 05:04:25 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.135 |  |
| 2026-11-22 05:04:12 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.049 |  |
| 2026-11-22 05:03:55 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.023 |  |
| 2026-11-22 05:03:34 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 05:03:32 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.069 |  |
| 2026-11-22 05:03:20 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-22 05:03:16 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:02:55 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 05:02:52 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:02:42 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.032 |  |
| 2026-11-22 05:02:36 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:02:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:50 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-11-22 05:01:46 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:35 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:21 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:10 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-22 05:01:06 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-11-22 05:00:53 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 05:00:50 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-22 05:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:00:43 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 05:03:20 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-22 05:01:10 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-22 05:00:50 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-22 05:03:34 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 05:00:53 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 05:28:00 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-22 05:02:55 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:21 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:02:52 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:03:16 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:02:36 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:46 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:35 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:00:43 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:02:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:05:50 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:09:26 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:09:04 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:20:54 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.008 |  |
| 2026-11-22 05:19:04 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-11-22 05:04:52 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-22 05:01:50 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-11-22 05:08:17 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-11-22 05:06:03 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-11-22 04:00:39 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-11-22 05:01:06 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-11-22 05:03:55 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.023 |  |
| 2026-11-22 05:27:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.025 |  |
| 2026-11-22 05:02:42 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.032 |  |
| 2026-11-22 05:04:12 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.049 |  |
| 2026-11-22 05:03:32 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.069 |  |
| 2026-11-22 05:04:25 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.135 |  |
| 2026-11-22 05:06:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)