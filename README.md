# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_19:30:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,812 measurements** from **39** stations.
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
| 2026-10-25 19:30:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-25 19:28:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:13:37 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-25 19:12:29 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-25 19:12:29 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:11:49 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:11:47 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:10:40 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 19:09:58 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.547 | 🔺 Rising |
| 2026-10-25 19:09:03 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:08:58 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-25 19:08:17 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-25 19:07:36 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-25 19:07:16 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:04:59 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 19:04:40 | Rathnapura (Kalu Ganga) | 4.06 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-10-25 19:04:36 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 19:04:27 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:04:25 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-25 19:03:53 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-10-25 19:03:33 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-25 19:03:31 | Ellagawa (Kalu Ganga) | 7.31 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-25 19:03:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:02:26 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-25 19:02:26 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:02:17 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:01:52 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-25 19:01:41 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 19:01:40 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 19:01:37 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-25 19:01:35 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 19:01:21 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-25 19:00:48 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:00:41 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-25 19:00:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.123 |  |
| 2026-10-25 19:00:25 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 19:09:58 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.547 | 🔺 Rising |
| 2026-10-25 19:04:40 | Rathnapura (Kalu Ganga) | 4.06 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-10-25 19:03:53 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-10-25 19:01:52 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-25 19:03:31 | Ellagawa (Kalu Ganga) | 7.31 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-25 19:02:26 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-25 19:08:17 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-25 19:01:37 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-25 19:04:25 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-25 19:03:33 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-25 19:00:41 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-25 19:01:40 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 19:08:58 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-25 19:07:36 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-25 19:12:29 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-25 19:04:36 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 19:13:37 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-25 19:01:21 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-25 19:00:25 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 19:01:41 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 19:01:35 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 19:10:40 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 19:30:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-25 19:04:27 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:00:48 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:28:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:09:03 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:07:16 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:12:29 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:02:17 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:11:49 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:03:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:02:26 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:00:06 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 19:04:59 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-25 19:00:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)