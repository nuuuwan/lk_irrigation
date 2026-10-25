# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_21:14:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,884 measurements** from **39** stations.
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
| 2026-10-25 21:14:46 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-25 21:09:18 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 21:08:46 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 21:08:36 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:08:21 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-25 21:08:12 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:08:02 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:07:54 | Holombuwa (Kelani Ganga) | 2.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-25 21:07:42 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-25 21:07:31 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-10-25 21:07:04 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 21:07:01 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 21:06:28 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-25 21:06:12 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-25 21:06:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 21:05:59 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-25 21:05:42 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-25 21:05:30 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-25 21:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.52 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-25 21:05:02 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.077 |  |
| 2026-10-25 21:04:43 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 21:04:36 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:19 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:15 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-25 21:04:04 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 21:03:40 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-25 21:03:32 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-25 21:03:15 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 21:03:10 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 21:02:52 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-25 21:02:31 | Rathnapura (Kalu Ganga) | 5.04 | 🟢 Normal | 0.555 | 🔺 Rising |
| 2026-10-25 21:01:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-25 21:01:38 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:00:50 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-25 21:00:27 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:00:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 21:02:31 | Rathnapura (Kalu Ganga) | 5.04 | 🟢 Normal | 0.555 | 🔺 Rising |
| 2026-10-25 21:07:31 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-10-25 21:06:28 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-25 21:08:21 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-25 21:05:42 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-25 21:03:32 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-25 21:07:42 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-25 21:14:46 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-25 21:03:40 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-25 21:04:15 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-25 21:05:59 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-25 21:07:54 | Holombuwa (Kelani Ganga) | 2.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-25 21:02:52 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-25 21:00:50 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-25 21:05:30 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-25 21:09:18 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 21:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.52 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-25 21:04:43 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 21:03:15 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 21:06:12 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-25 21:03:10 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 21:07:04 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 21:04:04 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 21:07:01 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 20:17:12 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 21:08:46 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 21:06:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 21:00:27 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:19 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:36 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:08:36 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:01:38 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:08:12 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:01:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-25 21:00:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-25 21:05:02 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)