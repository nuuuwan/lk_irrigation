# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_10:19:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,035 measurements** from **39** stations.
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
| 2026-08-15 10:19:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:12:06 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-15 10:09:59 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-08-15 10:09:00 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.118 |  |
| 2026-08-15 10:08:16 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 10:08:06 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:07:56 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 10:06:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:06:11 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.057 |  |
| 2026-08-15 10:05:54 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-08-15 10:05:50 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:05:31 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 10:05:14 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.098 |  |
| 2026-08-15 10:04:51 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.019 |  |
| 2026-08-15 10:04:37 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:04:26 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-15 10:04:15 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.059 |  |
| 2026-08-15 10:04:04 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:03:52 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.029 |  |
| 2026-08-15 10:03:40 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-15 10:03:31 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-15 10:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.072 |  |
| 2026-08-15 10:02:46 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:45 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-08-15 10:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:30 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.081 |  |
| 2026-08-15 10:02:27 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-15 10:02:26 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-08-15 10:02:25 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:12 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 10:02:10 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:09 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:01:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:01:50 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:00:33 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:00:17 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 10:02:45 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-08-15 10:12:06 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-15 10:04:26 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-15 10:03:31 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-15 10:05:31 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 10:07:56 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 10:02:12 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 10:08:16 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 10:02:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:00:33 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 09:02:41 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:25 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:08:06 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:00:17 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:46 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:06:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:04:04 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:04:37 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:05:50 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:01:50 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:01:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:19:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:09 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:10 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 10:09:59 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-08-15 10:05:54 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-08-15 10:03:40 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-15 10:02:27 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-15 10:04:51 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.019 |  |
| 2026-08-15 10:03:52 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.029 |  |
| 2026-08-15 10:02:26 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-08-15 10:06:11 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.057 |  |
| 2026-08-15 10:04:15 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.059 |  |
| 2026-08-15 10:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.072 |  |
| 2026-08-15 10:02:30 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.081 |  |
| 2026-08-15 10:05:14 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.098 |  |
| 2026-08-15 10:09:00 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)