# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_17:23:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,630 measurements** from **39** stations.
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
| 2026-11-24 17:23:54 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.042 |  |
| 2026-11-24 17:16:54 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 17:13:27 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-24 17:10:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-11-24 17:09:42 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-24 17:08:06 | Peradeniya (Mahaweli Ganga) | 3.85 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-24 17:07:50 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:07:40 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-11-24 17:07:12 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.528 | 🔺 Rising |
| 2026-11-24 17:07:02 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 17:06:24 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:05:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:05:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.030 |  |
| 2026-11-24 17:04:59 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-24 17:04:28 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-24 17:04:13 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-24 17:04:05 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-24 17:03:53 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 17:03:51 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.049 |  |
| 2026-11-24 17:03:48 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:03:27 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 17:03:26 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-24 17:03:21 | Moraketiya (Walawe Ganga) | 2.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 17:03:17 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:03:11 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-11-24 17:02:53 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-11-24 17:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-24 17:02:30 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-24 17:02:15 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.071 |  |
| 2026-11-24 17:02:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.129 |  |
| 2026-11-24 17:02:01 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:01:48 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-11-24 17:01:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:01:28 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 17:01:09 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 17:00:36 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.020 |  |
| 2026-11-24 17:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.152 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 17:07:12 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.528 | 🔺 Rising |
| 2026-11-24 17:07:40 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-11-24 17:02:53 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-11-24 17:10:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-11-24 17:03:11 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-11-24 17:08:06 | Peradeniya (Mahaweli Ganga) | 3.85 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-24 17:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-24 17:04:13 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-24 17:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-24 17:04:59 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-24 17:03:53 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 17:16:54 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 17:07:02 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 17:03:26 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-24 17:01:09 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 17:04:05 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-24 17:03:21 | Moraketiya (Walawe Ganga) | 2.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 17:01:28 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 17:03:27 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 17:13:27 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-24 17:09:42 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-24 17:03:17 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:01:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:02:01 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:03:48 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:05:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:07:50 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:06:24 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 17:04:28 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-24 16:03:40 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-24 17:00:36 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.020 |  |
| 2026-11-24 17:02:30 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 17:05:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.030 |  |
| 2026-11-24 17:01:48 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-11-24 17:23:54 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.042 |  |
| 2026-11-24 17:03:51 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.049 |  |
| 2026-11-24 17:02:15 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.071 |  |
| 2026-11-24 17:02:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)