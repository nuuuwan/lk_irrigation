# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_07:09:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 07:09:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:08:06 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:07:10 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-10-04 07:07:03 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.143 |  |
| 2026-10-04 07:06:36 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-10-04 07:05:50 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-04 07:05:41 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-04 07:05:30 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:05:24 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.002 |  |
| 2026-10-04 07:05:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-04 07:05:17 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-04 07:05:11 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 07:04:41 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:04:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:04:12 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:03:56 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 07:03:33 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.067 |  |
| 2026-10-04 07:03:10 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.086 |  |
| 2026-10-04 07:03:06 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 07:02:48 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.117 |  |
| 2026-10-04 07:02:36 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:02:29 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-10-04 07:02:23 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.315 |  |
| 2026-10-04 07:02:04 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:01:49 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.052 |  |
| 2026-10-04 07:01:48 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.092 |  |
| 2026-10-04 07:01:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:01:44 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.053 |  |
| 2026-10-04 07:01:25 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-04 07:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | -0.001 |  |
| 2026-10-04 07:01:19 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-04 07:01:08 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:00:31 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 07:05:50 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-04 07:05:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-04 07:01:25 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-04 07:05:41 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-04 07:03:06 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 07:05:11 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 07:03:56 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 07:05:24 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.002 |  |
| 2026-10-04 07:04:41 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:08:06 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:01:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:02:04 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-04 06:03:54 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 06:07:38 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:04:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:09:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:02:36 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:05:30 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 06:13:43 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:04:12 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 07:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | -0.001 |  |
| 2026-10-04 07:05:17 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-04 06:01:20 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-04 07:02:29 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-10-04 07:00:31 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-04 07:07:10 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-10-04 07:01:19 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-10-04 07:06:36 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-10-04 07:01:49 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.052 |  |
| 2026-10-04 07:01:44 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.053 |  |
| 2026-10-04 06:07:10 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.058 |  |
| 2026-10-04 07:03:33 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.067 |  |
| 2026-10-04 07:03:10 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.086 |  |
| 2026-10-04 07:01:48 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.092 |  |
| 2026-10-04 07:02:48 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.117 |  |
| 2026-10-04 07:07:03 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.143 |  |
| 2026-10-04 07:02:23 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.315 |  |
| 2026-10-04 06:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.694 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)