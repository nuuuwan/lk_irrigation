# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_19:13:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,704 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 19:13:03 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-24 19:11:58 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | -0.019 |  |
| 2026-11-24 19:10:48 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-24 19:10:25 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-24 19:09:38 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-24 19:09:02 | Holombuwa (Kelani Ganga) | 2.35 | 🟢 Normal | 0.731 | 🔺 Rising |
| 2026-11-24 19:08:18 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-24 19:08:05 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.067 |  |
| 2026-11-24 19:07:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.073 |  |
| 2026-11-24 19:07:57 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-24 19:07:42 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-24 19:07:34 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.698 | 🔺 Rising |
| 2026-11-24 19:07:14 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-11-24 19:05:27 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 19:05:07 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.059 |  |
| 2026-11-24 19:04:59 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.062 |  |
| 2026-11-24 19:04:38 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-11-24 19:04:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.060 |  |
| 2026-11-24 19:04:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:04:15 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-11-24 19:04:06 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-24 19:03:53 | Nawalapitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-24 19:03:32 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.056 |  |
| 2026-11-24 19:03:26 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-24 19:03:20 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.224 | 🔺 Rising |
| 2026-11-24 19:02:45 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 19:02:20 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 19:02:13 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:02:02 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 19:01:53 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:01:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-24 19:01:21 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-24 19:00:50 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.300 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 19:03:20 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.224 | 🔺 Rising |
| 2026-11-24 19:09:02 | Holombuwa (Kelani Ganga) | 2.35 | 🟢 Normal | 0.731 | 🔺 Rising |
| 2026-11-24 19:07:34 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.698 | 🔺 Rising |
| 2026-11-24 19:04:15 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-11-24 19:00:50 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-24 19:07:42 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-24 19:09:38 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-24 19:08:18 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-24 19:07:14 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-11-24 19:13:03 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-24 19:03:26 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-24 19:07:57 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-24 19:03:53 | Nawalapitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-24 19:01:21 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-24 19:04:06 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-24 18:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-24 19:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-24 19:02:20 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 19:02:02 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 19:02:45 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 19:10:25 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-24 19:10:48 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-24 19:05:27 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 19:01:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:04:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:02:13 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:01:53 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-24 19:04:38 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-24 19:11:58 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | -0.019 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 19:03:32 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.056 |  |
| 2026-11-24 19:05:07 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.059 |  |
| 2026-11-24 19:04:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.060 |  |
| 2026-11-24 19:04:59 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.062 |  |
| 2026-11-24 19:08:05 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.067 |  |
| 2026-11-24 19:07:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)