# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_12:12:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,649 measurements** from **39** stations.
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
| 2026-10-24 12:12:29 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-10-24 12:08:49 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-24 12:08:19 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-10-24 12:07:55 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 12:07:02 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.032 |  |
| 2026-10-24 12:06:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:06:41 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.039 |  |
| 2026-10-24 12:06:13 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:56 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:48 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-24 12:04:41 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:27 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-24 12:04:04 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-24 12:04:00 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.049 |  |
| 2026-10-24 12:03:41 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-10-24 12:03:38 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:03:34 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.043 |  |
| 2026-10-24 12:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.030 |  |
| 2026-10-24 12:03:20 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-24 12:03:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:03:04 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:54 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:54 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.071 |  |
| 2026-10-24 12:02:35 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:32 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:28 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-24 12:02:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.040 |  |
| 2026-10-24 12:02:18 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.031 |  |
| 2026-10-24 12:02:11 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.021 |  |
| 2026-10-24 12:02:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:01:56 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:01:45 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:01:33 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.039 |  |
| 2026-10-24 12:01:29 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | -0.326 |  |
| 2026-10-24 12:01:16 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.169 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 12:01:16 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-24 12:04:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-24 12:04:04 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-24 12:08:49 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-24 12:03:20 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-24 12:04:48 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-24 12:07:55 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 12:01:45 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:32 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:01:31 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:01:56 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:56 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:35 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:06:13 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:03:38 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:41 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:03:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:03:04 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:27 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:54 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:06:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:02:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:06:27 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-10-24 12:02:28 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-24 12:12:29 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-10-24 12:08:19 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-10-24 12:03:41 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-10-24 12:02:11 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.021 |  |
| 2026-10-24 12:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.030 |  |
| 2026-10-24 12:02:18 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.031 |  |
| 2026-10-24 12:07:02 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | -0.032 |  |
| 2026-10-24 12:06:41 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.039 |  |
| 2026-10-24 12:01:33 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.039 |  |
| 2026-10-24 12:02:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.040 |  |
| 2026-10-24 12:03:34 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.043 |  |
| 2026-10-24 12:04:00 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.049 |  |
| 2026-10-24 12:02:54 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.071 |  |
| 2026-10-24 12:01:29 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | -0.326 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)