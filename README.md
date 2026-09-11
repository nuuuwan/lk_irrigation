# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_14:23:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,020 measurements** from **39** stations.
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
| 2026-09-11 14:23:50 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:14:11 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:12:39 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:10:37 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:10:09 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-11 14:09:04 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.103 |  |
| 2026-09-11 14:08:49 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-11 14:07:58 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-09-11 14:07:53 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.012 |  |
| 2026-09-11 14:07:12 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:06:59 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:06:16 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:05:40 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-11 14:05:37 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:05:32 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-09-11 14:05:22 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 14:04:48 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:04:46 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:04:27 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:03:10 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-11 14:03:07 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-11 14:03:01 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:02:59 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:02:51 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:02:45 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 14:02:37 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:02:37 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.029 |  |
| 2026-09-11 14:02:36 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:02:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-09-11 14:02:08 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 14:01:47 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:01:45 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:01:22 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:01:19 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:01:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:01:16 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:01:07 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | -0.012 |  |
| 2026-09-11 14:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 14:03:10 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-11 14:08:49 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-11 14:03:07 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-11 14:10:09 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-11 14:05:40 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-11 14:02:45 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 14:02:08 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 14:05:22 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 14:04:27 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:01:19 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:07:12 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:02:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:02:36 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:12:39 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:14:11 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:01:45 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:23:50 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-11 13:01:54 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:02:37 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:06:59 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:04:48 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:10:37 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:03:01 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-11 14:07:58 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-09-11 14:01:47 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:01:22 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:06:16 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:01:16 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-11 14:02:59 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:01:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:02:51 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:05:37 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-09-11 14:01:07 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | -0.012 |  |
| 2026-09-11 14:07:53 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.012 |  |
| 2026-09-11 14:05:32 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-09-11 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-09-11 14:02:37 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.029 |  |
| 2026-09-11 14:09:04 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)