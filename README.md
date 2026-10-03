# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_01:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,232 measurements** from **39** stations.
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
| 2026-10-04 01:11:08 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-10-04 01:10:48 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.028 |  |
| 2026-10-04 01:09:40 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:07:48 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-04 01:07:43 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 01:06:52 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-10-04 01:06:38 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-04 01:06:09 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-04 01:05:37 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 01:05:25 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.055 |  |
| 2026-10-04 01:04:44 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:04:21 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 01:04:21 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-04 01:04:03 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-04 01:03:58 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-04 01:03:43 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:03:41 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:03:34 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 01:03:32 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 01:03:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-04 01:03:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-04 01:03:06 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 01:02:57 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-04 01:02:18 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.040 |  |
| 2026-10-04 01:02:15 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.156 |  |
| 2026-10-04 01:02:10 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:02:06 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-10-04 01:01:56 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 01:01:44 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.012 |  |
| 2026-10-04 01:01:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:01:12 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 01:00:14 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-04 00:39:08 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 00:04:28 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-04 01:00:14 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-04 01:07:48 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-04 01:06:38 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-04 01:03:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-04 01:01:56 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 01:02:57 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-04 01:04:21 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-04 01:03:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-04 01:03:34 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 01:04:21 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 01:03:06 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 01:05:37 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 01:01:12 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 01:03:32 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 01:07:43 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 01:03:43 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:02:10 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:03:41 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:01:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:00:40 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:09:40 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:04:44 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:04:03 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-04 01:06:09 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-04 01:02:06 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-10-04 01:01:44 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.012 |  |
| 2026-10-04 01:11:08 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-10-04 01:03:58 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-04 01:10:48 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.028 |  |
| 2026-10-04 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.029 |  |
| 2026-10-04 01:06:52 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-10-04 01:02:18 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.040 |  |
| 2026-10-04 01:05:25 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.055 |  |
| 2026-10-04 00:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.055 |  |
| 2026-10-04 01:02:15 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)