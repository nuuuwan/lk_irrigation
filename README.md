# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_02:30:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 02:30:01 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:29:37 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:15:57 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.017 |  |
| 2026-10-25 02:13:09 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 02:09:09 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:07:28 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:07:04 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:06:42 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:06:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 02:06:12 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:06:09 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-10-25 02:06:01 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-25 02:05:20 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 02:04:58 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.063 |  |
| 2026-10-25 02:04:19 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:04:01 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-25 02:03:20 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 02:03:07 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-10-25 02:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.020 |  |
| 2026-10-25 02:02:53 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-10-25 02:02:51 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:02:34 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:02:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:01:47 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-25 02:01:32 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-25 02:01:23 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-25 02:01:17 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 02:01:16 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:01:11 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:00:53 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 02:01:32 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-25 02:06:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 02:03:20 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 02:00:53 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 02:13:09 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 02:01:17 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 02:05:20 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 02:09:09 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:01:11 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:04:19 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:02:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:30:01 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:02:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:06:12 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:07:28 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-24 23:02:47 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:07:04 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:01:16 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:02:51 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:02:34 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 02:01:47 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:06:01 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-25 02:03:07 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-10-25 00:01:09 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-25 02:06:01 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:01:42 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-25 00:02:34 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-10-25 02:04:01 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-25 01:03:01 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.013 |  |
| 2026-10-25 02:15:57 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.017 |  |
| 2026-10-25 02:01:23 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-24 18:00:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-25 02:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.020 |  |
| 2026-10-25 02:06:09 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-10-24 21:12:32 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.022 |  |
| 2026-10-24 18:02:58 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-24 18:01:50 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-25 02:02:53 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-10-25 02:04:58 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)