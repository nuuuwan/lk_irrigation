# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_04:29:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,235 measurements** from **39** stations.
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
| 2026-10-25 04:29:44 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:17:41 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-25 04:14:14 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:14:14 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.026 |  |
| 2026-10-25 04:11:19 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:10:30 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-10-25 04:08:52 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.011 |  |
| 2026-10-25 04:08:33 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 2.262 | 🔺 Rising |
| 2026-10-25 04:07:02 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:05:58 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.011 |  |
| 2026-10-25 04:05:21 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-10-25 04:05:07 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-25 04:04:50 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:04:43 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:04:36 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 04:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:04:16 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:03:23 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-10-25 04:02:58 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:02:54 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:02:15 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:02:05 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-10-25 04:02:05 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.068 |  |
| 2026-10-25 04:02:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:01:48 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -72.000 |  |
| 2026-10-25 04:01:47 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -72.000 |  |
| 2026-10-25 04:01:45 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -72.000 |  |
| 2026-10-25 04:01:44 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-10-25 04:01:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 04:01:23 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:01:18 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:01:15 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-10-25 04:01:14 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:00:31 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.031 |  |
| 2026-10-25 04:00:27 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 04:08:33 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 2.262 | 🔺 Rising |
| 2026-10-25 04:01:44 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-10-25 04:05:07 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-25 04:17:41 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-25 04:04:36 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 04:01:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 04:00:27 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:02:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:04:43 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:02:54 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:01:18 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:29:44 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:14:14 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:04:50 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:11:19 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:01:14 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:02:15 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 04:01:23 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:02:58 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:04:16 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:07:02 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-10-25 04:05:58 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.011 |  |
| 2026-10-25 04:08:52 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.011 |  |
| 2026-10-25 04:05:21 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-10-25 03:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.020 |  |
| 2026-10-24 18:00:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-25 04:01:15 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-10-25 04:02:05 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-10-25 04:10:30 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-10-25 04:14:14 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.026 |  |
| 2026-10-25 04:03:23 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-10-24 18:02:58 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-24 18:01:50 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-25 04:00:31 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.031 |  |
| 2026-10-25 03:02:18 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-10-25 03:02:27 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2026-10-25 04:02:05 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.068 |  |
| 2026-10-25 04:01:48 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)