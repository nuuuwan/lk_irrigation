# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_18:12:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,272 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 18:12:46 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.036 |  |
| 2026-10-10 18:09:12 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.116 |  |
| 2026-10-10 18:09:05 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-10-10 18:08:57 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.129 |  |
| 2026-10-10 18:08:33 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.836 | 🔺 Rising |
| 2026-10-10 18:07:49 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:07:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-10-10 18:06:31 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-10 18:04:45 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-10-10 18:04:07 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:04:06 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.049 |  |
| 2026-10-10 18:03:56 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:03:54 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:03:50 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-10 18:03:48 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.069 |  |
| 2026-10-10 18:03:24 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-10 18:03:18 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:03:03 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.072 |  |
| 2026-10-10 18:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:02:51 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.020 |  |
| 2026-10-10 18:02:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-10 18:02:38 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | -0.081 |  |
| 2026-10-10 18:02:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 18:02:34 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:02:23 | Badalgama (Maha Oya) | 4.03 | 🟢 Normal | -0.063 |  |
| 2026-10-10 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-10 18:01:58 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:55 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.036 |  |
| 2026-10-10 18:01:47 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.049 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:09 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:09 | Moragaswewa (Deduru Oya) | 2.39 | 🟢 Normal | -0.021 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:47 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-10-10 18:00:21 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 18:08:33 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.836 | 🔺 Rising |
| 2026-10-10 18:03:50 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-10 18:03:24 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-10 18:02:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-10 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-10 18:02:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 18:03:18 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:02:34 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:09 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:21 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:58 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:07:49 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:03:54 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:06:31 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:03:56 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:03:21 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:04:07 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:09:05 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-10-10 18:04:45 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-10-10 18:02:51 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.020 |  |
| 2026-10-10 18:01:09 | Moragaswewa (Deduru Oya) | 2.39 | 🟢 Normal | -0.021 |  |
| 2026-10-10 18:00:47 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-10-10 18:12:46 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.036 |  |
| 2026-10-10 18:01:55 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.036 |  |
| 2026-10-10 18:07:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-10-10 18:04:06 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.049 |  |
| 2026-10-10 18:01:47 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.049 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-10 18:02:23 | Badalgama (Maha Oya) | 4.03 | 🟢 Normal | -0.063 |  |
| 2026-10-10 18:03:48 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.069 |  |
| 2026-10-10 18:03:03 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.072 |  |
| 2026-10-10 18:02:38 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | -0.081 |  |
| 2026-10-10 18:09:12 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.116 |  |
| 2026-10-10 18:08:57 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)