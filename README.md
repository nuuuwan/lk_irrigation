# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_16:09:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 16:09:19 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-08-04 16:09:14 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.027 |  |
| 2026-08-04 16:07:17 | Rathnapura (Kalu Ganga) | 6.33 | 🟡 Alert | -0.095 |  |
| 2026-08-04 16:07:11 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-08-04 16:06:47 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 16:06:14 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.154 |  |
| 2026-08-04 16:06:10 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-08-04 16:05:58 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:05:18 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.049 |  |
| 2026-08-04 16:04:54 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 16:04:42 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-08-04 16:04:35 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-04 16:04:33 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-04 16:04:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:04:03 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:03:59 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 16:03:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:03:42 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | -0.180 |  |
| 2026-08-04 16:03:29 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-08-04 16:03:22 | Nawalapitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-08-04 16:03:14 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.081 |  |
| 2026-08-04 16:03:05 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-08-04 16:03:04 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:03:01 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-04 16:02:55 | Peradeniya (Mahaweli Ganga) | 4.63 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-08-04 16:02:54 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 16:02:48 | Deraniyagala (Kelani Ganga) | 2.47 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-08-04 16:02:34 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-08-04 16:02:34 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.027 |  |
| 2026-08-04 16:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | -0.030 |  |
| 2026-08-04 16:02:23 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:59 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | -0.024 |  |
| 2026-08-04 16:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:27 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:15 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.031 |  |
| 2026-08-04 16:01:03 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:00:22 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.072 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 16:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | -0.030 |  |
| 2026-08-04 16:07:17 | Rathnapura (Kalu Ganga) | 6.33 | 🟡 Alert | -0.095 |  |
| 2026-08-04 16:02:48 | Deraniyagala (Kelani Ganga) | 2.47 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-08-04 16:02:55 | Peradeniya (Mahaweli Ganga) | 4.63 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-08-04 16:03:01 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-04 16:02:54 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 16:04:54 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 16:03:59 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 16:06:47 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 15:02:15 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 16:04:33 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-04 16:01:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:02:23 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:27 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:04:03 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:04:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:03:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:01:03 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:05:58 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:03:04 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 16:04:35 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-04 16:09:19 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-08-04 16:07:11 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-08-04 16:03:29 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-08-04 16:02:34 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-08-04 16:01:59 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | -0.024 |  |
| 2026-08-04 16:02:34 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.027 |  |
| 2026-08-04 16:09:14 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.027 |  |
| 2026-08-04 16:04:42 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-08-04 16:01:15 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.031 |  |
| 2026-08-04 16:03:05 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-08-04 16:06:10 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-08-04 16:03:22 | Nawalapitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-08-04 16:05:18 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.049 |  |
| 2026-08-04 16:00:22 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.072 |  |
| 2026-08-04 16:03:14 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.081 |  |
| 2026-08-04 16:06:14 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.154 |  |
| 2026-08-04 16:03:42 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)