# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_07:40:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,541 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 07:40:13 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:26:00 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.014 |  |
| 2026-10-03 07:16:41 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.170 |  |
| 2026-10-03 07:13:13 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.017 |  |
| 2026-10-03 07:11:12 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.035 |  |
| 2026-10-03 07:10:41 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-03 07:09:13 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:07:05 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-10-03 07:06:54 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:06:52 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-03 07:06:47 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.002 |  |
| 2026-10-03 07:06:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.099 |  |
| 2026-10-03 07:06:02 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.028 |  |
| 2026-10-03 07:05:41 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.065 |  |
| 2026-10-03 07:05:13 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.019 |  |
| 2026-10-03 07:04:50 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-03 07:04:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:04:36 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:04:04 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.053 |  |
| 2026-10-03 07:03:49 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:03:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:03:35 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.069 |  |
| 2026-10-03 07:03:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 07:03:16 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-03 07:03:12 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:02:49 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.135 |  |
| 2026-10-03 07:02:28 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:02:21 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.054 |  |
| 2026-10-03 07:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-10-03 07:02:18 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:01:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 07:01:55 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-10-03 07:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:01:36 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 07:01:32 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-03 07:01:31 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:01:30 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-10-03 07:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-03 07:00:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:00:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 07:07:05 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-10-03 07:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-10-03 07:04:50 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-03 07:01:32 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-03 07:03:16 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-03 07:10:41 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-03 07:03:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 07:01:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 07:01:36 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 07:06:52 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-03 07:00:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:40:13 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:00:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:06:54 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:03:49 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:03:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:04:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:02:28 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:01:31 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:03:12 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:09:13 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:04:36 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 07:06:47 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.002 |  |
| 2026-10-03 07:01:55 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-10-03 07:01:30 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-10-03 07:26:00 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.014 |  |
| 2026-10-03 07:13:13 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.017 |  |
| 2026-10-03 07:05:13 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.019 |  |
| 2026-10-03 07:06:02 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.028 |  |
| 2026-10-03 07:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-10-03 07:11:12 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.035 |  |
| 2026-10-03 07:04:04 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.053 |  |
| 2026-10-03 07:02:21 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.054 |  |
| 2026-10-03 07:05:41 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.065 |  |
| 2026-10-03 07:03:35 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.069 |  |
| 2026-10-03 07:06:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.099 |  |
| 2026-10-03 07:02:49 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.135 |  |
| 2026-10-03 07:16:41 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)