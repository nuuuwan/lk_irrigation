# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_19:17:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **253,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 19:17:52 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.008 |  |
| 2026-09-06 19:10:00 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.099 |  |
| 2026-09-06 19:09:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-06 19:08:49 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:08:44 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-09-06 19:06:20 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-06 19:05:49 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.010 |  |
| 2026-09-06 19:05:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:05:07 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-06 19:04:02 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:04:00 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:50 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:25 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:21 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-09-06 19:03:19 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:02 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.051 |  |
| 2026-09-06 19:02:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:02:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-06 19:02:19 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:02:17 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-06 19:02:13 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-09-06 19:02:11 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:02:09 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-09-06 19:02:08 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-06 19:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.042 |  |
| 2026-09-06 19:02:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.030 |  |
| 2026-09-06 19:01:31 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-09-06 19:01:22 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:01:22 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:01:15 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:59 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:19 | Moraketiya (Walawe Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:16 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 19:01:31 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-09-06 19:08:44 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-09-06 19:02:08 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-06 19:02:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-06 19:05:07 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-06 19:06:20 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-06 19:09:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-06 19:01:15 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:02:11 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:02:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:50 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:16 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:06:01 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:08:49 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:05:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:04:00 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:19 | Moraketiya (Walawe Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:01:22 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:25 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:03:19 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:04:02 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:06:47 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:01:51 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:00:59 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:01:22 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:02:19 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-06 19:17:52 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.008 |  |
| 2026-09-06 19:05:49 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.010 |  |
| 2026-09-06 19:02:13 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-09-06 19:02:09 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-09-06 19:02:17 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-06 19:02:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.030 |  |
| 2026-09-06 19:03:21 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-09-06 19:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.042 |  |
| 2026-09-06 19:03:02 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.051 |  |
| 2026-09-06 19:10:00 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.099 |  |
| 2026-09-06 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)