# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_15:11:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,365 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 15:11:49 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-10-08 15:10:06 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-10-08 15:09:04 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:08:58 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:08:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:08:20 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.138 |  |
| 2026-10-08 15:08:12 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:06:58 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:06:56 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-08 15:06:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:05:49 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.089 |  |
| 2026-10-08 15:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-08 15:05:31 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-08 15:04:07 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-08 15:03:57 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 15:03:31 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-08 15:03:29 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | -0.061 |  |
| 2026-10-08 15:03:26 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:03:11 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-10-08 15:02:57 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.070 |  |
| 2026-10-08 15:02:52 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-08 15:02:32 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:32 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-10-08 15:02:24 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:14 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-08 15:02:10 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-10-08 15:02:07 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:07 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 15:02:06 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | -0.057 |  |
| 2026-10-08 15:01:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-10-08 15:01:30 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.034 |  |
| 2026-10-08 15:01:23 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 15:01:10 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 15:01:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.078 |  |
| 2026-10-08 15:00:13 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 15:03:11 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-10-08 15:02:14 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-08 15:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-08 15:06:56 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-08 14:06:31 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-08 15:03:31 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-08 15:01:23 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 15:01:10 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 15:02:07 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 15:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 15:03:26 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:00:13 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:27 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:08:58 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:32 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 13:16:50 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:06:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:08:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:24 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:03:57 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:08:12 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:02:07 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:09:04 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 15:10:06 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-10-08 15:05:31 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-08 15:02:10 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-10-08 15:02:52 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-08 15:04:07 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-08 15:01:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-10-08 15:11:49 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-10-08 15:01:30 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.034 |  |
| 2026-10-08 15:02:32 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-10-08 15:02:06 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | -0.057 |  |
| 2026-10-08 15:03:29 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | -0.061 |  |
| 2026-10-08 15:02:57 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.070 |  |
| 2026-10-08 15:01:05 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.078 |  |
| 2026-10-08 15:05:49 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.089 |  |
| 2026-10-08 15:08:20 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)