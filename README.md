# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_16:07:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,126 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 16:07:57 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.038 |  |
| 2026-10-21 16:07:44 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:07:28 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:07:22 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.021 |  |
| 2026-10-21 16:07:04 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:06:49 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2026-10-21 16:06:38 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:05:34 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.009 |  |
| 2026-10-21 16:05:26 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 16:05:20 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-10-21 16:04:58 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-10-21 16:04:57 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:04:21 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:04:16 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-21 16:04:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-10-21 16:03:12 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.021 |  |
| 2026-10-21 16:03:03 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.090 |  |
| 2026-10-21 16:02:43 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-21 16:02:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:37 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:36 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-21 16:02:30 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:23 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-10-21 16:02:20 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:08 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 16:01:55 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.078 |  |
| 2026-10-21 16:01:27 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-10-21 16:01:22 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 16:01:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:01:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-21 16:01:06 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-21 16:00:59 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 16:00:34 | Thaldena (Mahaweli Ganga) | 1.70 | 🟢 Normal | 1.338 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 16:00:34 | Thaldena (Mahaweli Ganga) | 1.70 | 🟢 Normal | 1.338 | 🔺 Rising |
| 2026-10-21 16:04:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-10-21 16:02:43 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-21 16:02:36 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-21 16:04:16 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-21 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-21 16:01:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 16:01:22 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 16:00:59 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 16:02:08 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 16:05:26 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 16:02:30 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:01:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:06:38 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:05:38 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:04:53 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:37 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:20 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:07:28 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 15:06:19 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:02:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:04:57 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:07:04 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:07:44 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:03:03 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 16:05:34 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.009 |  |
| 2026-10-21 16:01:06 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-21 15:02:03 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.013 |  |
| 2026-10-21 16:04:58 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-10-21 16:07:22 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.021 |  |
| 2026-10-21 16:03:12 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.021 |  |
| 2026-10-21 16:05:20 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-10-21 16:07:57 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.038 |  |
| 2026-10-21 16:02:23 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-10-21 16:01:27 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-10-21 16:01:55 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.078 |  |
| 2026-10-21 16:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.090 |  |
| 2026-10-21 16:06:49 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)