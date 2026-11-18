# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_11:16:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,114 measurements** from **39** stations.
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
| 2026-11-18 11:16:13 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.024 |  |
| 2026-11-18 11:11:13 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.017 |  |
| 2026-11-18 11:08:05 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:06:59 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:06:35 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:06:03 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:05:41 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:05:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-11-18 11:03:57 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-18 11:03:55 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:03:48 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 11:03:29 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:03:23 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:03:23 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:03:07 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2026-11-18 11:03:07 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:03:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.093 |  |
| 2026-11-18 11:02:51 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.043 |  |
| 2026-11-18 11:02:50 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:45 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:43 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-11-18 11:02:20 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.016 |  |
| 2026-11-18 11:02:14 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:14 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 11:02:10 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:08 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:01:55 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:54 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.062 |  |
| 2026-11-18 11:01:13 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:55 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:47 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:38 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:00:38 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.013 |  |
| 2026-11-18 11:00:22 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:13 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 11:02:14 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 11:03:48 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 11:00:13 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:55 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:47 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:50 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:08:05 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:22 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:51 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:13 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:06:03 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:05:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:14 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:03:55 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:55 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:03:23 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:03:29 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:54 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:06:35 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:06:59 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:08 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:45 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:03:07 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:10 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:00:38 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:05:41 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:03:23 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:00:38 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.013 |  |
| 2026-11-18 11:02:20 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.016 |  |
| 2026-11-18 11:11:13 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.017 |  |
| 2026-11-18 11:16:13 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.024 |  |
| 2026-11-18 11:03:57 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-18 11:02:43 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-11-18 11:03:07 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2026-11-18 11:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-11-18 11:02:51 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.043 |  |
| 2026-11-18 11:01:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.062 |  |
| 2026-11-18 11:03:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)