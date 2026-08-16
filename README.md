# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_06:31:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,777 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 06:31:58 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.001 |  |
| 2026-08-16 06:19:54 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:10:25 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.011 |  |
| 2026-08-16 06:08:25 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.038 |  |
| 2026-08-16 06:07:47 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:07:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 06:07:19 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:07:04 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:06:47 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:06:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:06:09 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:05:51 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:04:53 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:04:32 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:04:24 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.057 |  |
| 2026-08-16 06:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:04:00 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.038 |  |
| 2026-08-16 06:03:49 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.025 |  |
| 2026-08-16 06:03:48 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:03:35 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:03:18 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:03:02 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:02:47 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-08-16 06:02:44 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 06:02:24 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:02:24 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-16 06:02:01 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:01:46 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:01:38 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.040 |  |
| 2026-08-16 06:01:27 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:01:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:01:18 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-16 06:01:18 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-08-16 06:01:13 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:01:08 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-16 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.180 |  |
| 2026-08-16 06:00:48 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.022 |  |
| 2026-08-16 06:00:16 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 06:01:18 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-16 06:02:24 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-16 06:01:08 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-16 06:02:44 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 06:07:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 06:01:27 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:01:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:02:01 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:04:32 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:02:24 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:00:16 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:07:04 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:07:47 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:19:54 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:04:53 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:03:18 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:03:48 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:05:51 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:07:19 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:01:43 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:06:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:01:13 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:03:35 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-16 06:31:58 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.001 |  |
| 2026-08-16 06:06:47 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:03:02 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:01:46 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:06:09 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-16 06:10:25 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.011 |  |
| 2026-08-16 06:02:47 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-08-16 06:01:18 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-08-16 06:00:48 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.022 |  |
| 2026-08-16 06:03:49 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.025 |  |
| 2026-08-16 06:08:25 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.038 |  |
| 2026-08-16 06:04:00 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.038 |  |
| 2026-08-16 06:01:38 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.040 |  |
| 2026-08-16 06:04:24 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.057 |  |
| 2026-08-16 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)