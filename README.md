# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_17:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,218 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 17:03:17 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:12 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-19 17:03:00 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 17:02:47 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:38 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:31 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:29 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 17:02:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-19 17:01:23 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:06 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:05 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 16:03:14 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-19 16:04:42 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-19 17:02:29 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 16:08:13 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-19 17:03:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-19 17:01:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-19 17:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 16:00:31 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:23 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:03:53 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:31 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:17 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:06:43 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:00:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:00:55 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:08:16 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:52 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:38 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:47 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:07:29 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:06 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:12 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:04:44 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:00 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:07:23 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:06:49 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:03:16 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:01:59 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:01:11 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-11-19 16:04:18 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-11-19 16:07:46 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.019 |  |
| 2026-11-19 16:01:25 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-11-19 16:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.082 |  |
| 2026-11-19 16:04:43 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.420 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)