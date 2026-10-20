# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_20:26:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 20:26:58 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-10-20 20:26:29 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-10-20 20:15:55 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.008 |  |
| 2026-10-20 20:14:36 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.061 |  |
| 2026-10-20 20:11:04 | Thaldena (Mahaweli Ganga) | 1.45 | 🟢 Normal | 1.084 | 🔺 Rising |
| 2026-10-20 20:10:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:09:19 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | -0.022 |  |
| 2026-10-20 20:08:15 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.031 |  |
| 2026-10-20 20:07:42 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-20 20:07:14 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:06:21 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 20:06:02 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:06:00 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-10-20 20:05:54 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:05:53 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.017 |  |
| 2026-10-20 20:05:35 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-20 20:05:33 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:05:33 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-20 20:05:30 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 20:05:21 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-20 20:04:58 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 20:04:55 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:04:52 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-10-20 20:04:33 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.035 |  |
| 2026-10-20 20:04:02 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 20:03:09 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.033 |  |
| 2026-10-20 20:02:40 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 20:02:35 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 20:02:24 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 20:02:24 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-20 20:02:16 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.041 |  |
| 2026-10-20 20:02:10 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-20 20:01:27 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:01:20 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.040 |  |
| 2026-10-20 20:01:10 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.043 |  |
| 2026-10-20 20:00:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-20 20:00:32 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.152 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 20:09:19 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | -0.022 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 20:26:58 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-10-20 20:11:04 | Thaldena (Mahaweli Ganga) | 1.45 | 🟢 Normal | 1.084 | 🔺 Rising |
| 2026-10-20 20:02:24 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-20 20:02:35 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 20:05:21 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-20 20:07:42 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-20 20:02:10 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-20 20:00:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-20 20:05:35 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-20 20:02:40 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 20:06:21 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 20:05:30 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 20:04:58 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 20:04:02 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 20:02:24 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 20:06:00 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 20:15:55 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.008 |  |
| 2026-10-20 20:05:33 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:05:54 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:01:27 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:10:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:04:52 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-10-20 20:05:53 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.017 |  |
| 2026-10-20 20:04:55 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:07:14 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:06:02 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:05:33 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-20 20:08:15 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.031 |  |
| 2026-10-20 20:03:09 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.033 |  |
| 2026-10-20 20:04:33 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.035 |  |
| 2026-10-20 20:01:20 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.040 |  |
| 2026-10-20 20:02:16 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.041 |  |
| 2026-10-20 20:01:10 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.043 |  |
| 2026-10-20 20:14:36 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.061 |  |
| 2026-10-20 20:00:32 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)