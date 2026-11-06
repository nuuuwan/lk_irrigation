# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_06:11:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 06:11:10 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-06 06:09:51 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:09:35 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.085 |  |
| 2026-11-06 06:08:39 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-06 06:07:59 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.031 |  |
| 2026-11-06 06:07:32 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.076 |  |
| 2026-11-06 06:07:29 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-06 06:06:18 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-11-06 06:06:10 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:05:40 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:04:40 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.051 |  |
| 2026-11-06 06:04:21 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:03:58 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-11-06 06:03:47 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-11-06 06:03:46 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-11-06 06:03:40 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -1.055 |  |
| 2026-11-06 06:03:38 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:03:11 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-11-06 06:03:06 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-11-06 06:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.042 |  |
| 2026-11-06 06:02:58 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.030 |  |
| 2026-11-06 06:02:52 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.044 |  |
| 2026-11-06 06:02:52 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.153 |  |
| 2026-11-06 06:02:47 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:02:42 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:02:04 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:01:54 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | -0.055 |  |
| 2026-11-06 06:01:51 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-06 06:01:42 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:01:30 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-11-06 06:01:23 | Kuda Oya (Kirindi Oya) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-11-06 06:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:00:54 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-11-06 06:00:43 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-06 06:00:41 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 06:03:06 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-11-06 06:01:51 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-06 06:00:43 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-06 06:08:39 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-06 06:01:42 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:09:51 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:02:47 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:06:10 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:03:38 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:02:04 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:52:19 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-11-06 06:06:18 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-11-06 05:05:21 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:05:40 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:00:41 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:04:21 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-06 06:11:10 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-06 06:00:54 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-11-06 06:01:30 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-11-06 05:32:21 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.022 |  |
| 2026-11-06 06:03:46 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-11-06 06:03:47 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-11-06 06:02:58 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.030 |  |
| 2026-11-06 06:07:59 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.031 |  |
| 2026-11-06 06:01:23 | Kuda Oya (Kirindi Oya) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-11-06 06:03:11 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-11-06 06:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.042 |  |
| 2026-11-06 06:02:52 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.044 |  |
| 2026-11-06 06:04:40 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.051 |  |
| 2026-11-06 06:01:54 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | -0.055 |  |
| 2026-11-06 06:03:58 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-11-06 06:07:32 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.076 |  |
| 2026-11-06 06:07:29 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-06 06:09:35 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.085 |  |
| 2026-11-06 06:02:52 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.153 |  |
| 2026-11-06 06:03:40 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -1.055 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)