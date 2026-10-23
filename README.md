# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_10:10:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 10:10:37 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:10:24 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-10-23 10:09:49 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:09:19 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-10-23 10:08:26 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:08:23 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-10-23 10:07:59 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.042 |  |
| 2026-10-23 10:06:56 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.057 |  |
| 2026-10-23 10:06:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:06:05 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.075 |  |
| 2026-10-23 10:06:02 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:06:02 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-10-23 10:04:52 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:04:46 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-10-23 10:04:33 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-10-23 10:04:33 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:04:05 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:04:05 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | -0.025 |  |
| 2026-10-23 10:04:02 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-10-23 10:03:48 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.022 |  |
| 2026-10-23 10:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-10-23 10:03:08 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.058 |  |
| 2026-10-23 10:03:08 | Moragaswewa (Deduru Oya) | 4.81 | 🟡 Alert | -0.030 |  |
| 2026-10-23 10:03:05 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.105 |  |
| 2026-10-23 10:02:55 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-23 10:02:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:02:38 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.070 |  |
| 2026-10-23 10:02:36 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-10-23 10:02:22 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-23 10:02:09 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:02:06 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:01:40 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-10-23 10:01:34 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:01:29 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:00:35 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:00:29 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.101 |  |
| 2026-10-23 10:00:19 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.061 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 10:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-10-23 10:03:08 | Moragaswewa (Deduru Oya) | 4.81 | 🟡 Alert | -0.030 |  |
| 2026-10-23 10:01:40 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-10-23 10:00:19 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-23 10:08:26 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:00:35 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:10:37 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:06:02 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:04:33 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:06:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:02:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:04:05 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:09:49 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:01:29 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:02:09 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-23 10:08:23 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-10-23 10:04:52 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:02:06 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:01:34 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-23 10:04:33 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-10-23 10:10:24 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-10-23 10:04:46 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-10-23 10:02:55 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-23 10:02:22 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-23 10:03:48 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.022 |  |
| 2026-10-23 10:04:05 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | -0.025 |  |
| 2026-10-23 10:04:02 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-10-23 10:06:02 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-10-23 10:07:59 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.042 |  |
| 2026-10-23 10:02:36 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-10-23 10:09:19 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-10-23 10:06:56 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.057 |  |
| 2026-10-23 10:03:08 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.058 |  |
| 2026-10-23 10:02:38 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.070 |  |
| 2026-10-23 10:06:05 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.075 |  |
| 2026-10-23 10:00:29 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.101 |  |
| 2026-10-23 10:03:05 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)