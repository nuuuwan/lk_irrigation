# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_09:02:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 09:02:57 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:02:54 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-19 09:02:46 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-11-19 09:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.100 |  |
| 2026-11-19 09:02:34 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 09:02:20 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-19 09:02:19 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.087 |  |
| 2026-11-19 09:02:18 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-19 09:02:14 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 09:01:31 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:01:30 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-11-19 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:01:17 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:00:54 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 09:00:48 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:00:32 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-19 09:00:18 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-19 08:44:22 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.017 |  |
| 2026-11-19 08:32:41 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 09:02:18 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-19 09:02:14 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 09:02:34 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 09:00:18 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-19 09:02:20 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-19 09:00:32 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-19 09:00:54 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:01:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:02:08 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:00:19 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:09:55 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:01:38 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:02:51 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:20:19 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:01:04 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:02:46 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:04:46 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:07:09 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:32:41 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 08:05:00 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-19 08:06:23 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-11-19 08:02:46 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:02:57 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:00:48 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:01:31 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:01:17 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-19 09:02:54 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-19 09:01:30 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-11-19 08:01:23 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-19 08:07:36 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.013 |  |
| 2026-11-19 08:44:22 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.017 |  |
| 2026-11-19 08:10:38 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-11-19 09:02:46 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-11-19 08:04:12 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-11-19 08:03:03 | Katharagama (Menik Ganga) | 0.46 | 🟢 Normal | -0.043 |  |
| 2026-11-19 08:06:10 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.048 |  |
| 2026-11-19 09:02:19 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.087 |  |
| 2026-11-19 09:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)