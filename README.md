# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_07:18:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 07:18:06 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:14:21 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.001 |  |
| 2026-09-30 07:13:41 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-30 07:10:22 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-30 07:10:14 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:09:47 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:08:49 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:08:06 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:07:30 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.030 |  |
| 2026-09-30 07:06:36 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.019 |  |
| 2026-09-30 07:04:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-09-30 07:04:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.039 |  |
| 2026-09-30 07:04:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:04:12 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-30 07:03:57 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-09-30 07:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:03:24 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.120 |  |
| 2026-09-30 07:03:19 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:03:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.063 |  |
| 2026-09-30 07:03:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.042 |  |
| 2026-09-30 07:02:46 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.125 |  |
| 2026-09-30 07:02:42 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | -0.093 |  |
| 2026-09-30 07:02:37 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-30 07:02:36 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:02:23 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.023 |  |
| 2026-09-30 07:02:19 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-09-30 07:02:17 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:02:02 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:49 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:37 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.098 |  |
| 2026-09-30 07:01:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-09-30 07:01:13 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-09-30 07:01:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:10 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:02 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-30 07:00:46 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:00:23 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 07:01:02 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-30 07:04:12 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-30 07:10:22 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-30 07:02:02 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:10:14 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:00:23 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:03:19 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:02:36 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:18:06 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:00:46 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:04:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:08:49 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:01:49 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:09:47 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:08:06 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 06:00:33 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:02:17 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-09-30 07:14:21 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.001 |  |
| 2026-09-30 07:03:57 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-09-30 07:02:37 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-30 07:13:41 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-30 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-09-30 07:02:19 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-09-30 07:06:36 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.019 |  |
| 2026-09-30 07:04:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-09-30 07:02:23 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.023 |  |
| 2026-09-30 07:07:30 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.030 |  |
| 2026-09-30 07:01:13 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-09-30 07:01:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-09-30 07:04:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.039 |  |
| 2026-09-30 07:03:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.042 |  |
| 2026-09-30 07:03:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.063 |  |
| 2026-09-30 07:02:42 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | -0.093 |  |
| 2026-09-30 07:01:37 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.098 |  |
| 2026-09-30 07:03:24 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.120 |  |
| 2026-09-30 07:02:46 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)