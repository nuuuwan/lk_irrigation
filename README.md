# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_04:17:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 04:17:12 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.036 |  |
| 2026-09-29 04:16:34 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:11:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | -0.071 |  |
| 2026-09-29 04:11:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-29 04:09:45 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | -0.053 |  |
| 2026-09-29 04:07:48 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | -0.097 |  |
| 2026-09-29 04:06:12 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 04:05:29 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-09-29 04:04:36 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:04:33 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:04:08 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.071 |  |
| 2026-09-29 04:03:35 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:03:16 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:03:06 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-09-29 04:03:00 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.079 |  |
| 2026-09-29 04:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.348 |  |
| 2026-09-29 04:02:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-09-29 04:02:30 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-09-29 04:02:20 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:02:09 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.021 |  |
| 2026-09-29 04:02:08 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:02:04 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:54 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:47 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:23 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-29 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:12 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:00:38 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.015 |  |
| 2026-09-29 04:00:37 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-09-29 04:00:12 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 04:03:06 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-29 04:01:23 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-29 04:06:12 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 04:02:04 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:47 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:00:37 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:04:33 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:16:34 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:38:12 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:02:08 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:54 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:00:12 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:03:35 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:04:36 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:02:20 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:01:12 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:03:16 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 04:02:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-09-29 04:11:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-29 04:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-09-29 04:00:38 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.015 |  |
| 2026-09-29 04:05:29 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-09-29 04:02:30 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-09-29 04:02:09 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.021 |  |
| 2026-09-29 04:17:12 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.036 |  |
| 2026-09-29 03:02:25 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-09-29 04:09:45 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | -0.053 |  |
| 2026-09-29 04:11:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | -0.071 |  |
| 2026-09-29 04:04:08 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.071 |  |
| 2026-09-29 04:03:00 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.079 |  |
| 2026-09-29 03:03:48 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.091 |  |
| 2026-09-29 04:07:48 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | -0.097 |  |
| 2026-09-29 04:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.348 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)