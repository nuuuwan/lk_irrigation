# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_14:23:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 14:23:32 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-11-18 14:13:09 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:12:33 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:09:46 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-18 14:08:42 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:07:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 14:07:32 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.022 |  |
| 2026-11-18 14:07:23 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:07:22 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-11-18 14:05:22 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:04:37 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:04:21 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-11-18 14:04:15 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:04:13 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 14:03:56 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:43 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:29 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-11-18 14:03:29 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-18 14:03:29 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:23 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.110 |  |
| 2026-11-18 14:03:01 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 14:02:56 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:54 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:46 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-18 14:02:13 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:11 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-11-18 14:02:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-18 14:02:08 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:02:03 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:01:53 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:01:49 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.031 |  |
| 2026-11-18 14:01:41 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:01:09 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:00:59 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2026-11-18 14:00:44 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:00:37 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:00:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 14:02:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-18 14:04:13 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 14:03:01 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 14:07:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 14:09:46 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-18 14:01:53 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:00:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:56 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:01:41 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:54 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:56 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:46 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:29 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:02:13 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:01:09 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:12:33 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:00:37 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:00:44 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:05:22 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:43 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:03:23 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:08:42 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 14:13:09 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:02:03 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:02:08 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:04:15 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:04:37 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-18 14:02:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-18 14:03:29 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-11-18 14:02:11 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-11-18 14:23:32 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-11-18 14:03:29 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-18 14:07:32 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.022 |  |
| 2026-11-18 14:07:22 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-11-18 14:04:21 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-11-18 14:01:49 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.031 |  |
| 2026-11-18 14:00:59 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2026-11-18 14:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)