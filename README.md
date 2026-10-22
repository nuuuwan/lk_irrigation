# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_10:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,781 measurements** from **39** stations.
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
| 2026-10-22 10:10:18 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-22 10:09:37 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 10:09:33 | Hanwella (Kelani Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:08:39 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:06:41 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-22 10:06:31 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-10-22 10:05:09 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-22 10:05:08 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.047 |  |
| 2026-10-22 10:04:56 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-10-22 10:04:28 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:04:17 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 10:04:12 | Hanwella (Kelani Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:04:11 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.040 |  |
| 2026-10-22 10:04:09 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:04:08 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-22 10:03:51 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | -0.235 |  |
| 2026-10-22 10:03:50 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:03:34 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:03:09 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-10-22 10:03:07 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.258 |  |
| 2026-10-22 10:03:06 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:02:57 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.050 |  |
| 2026-10-22 10:02:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:02:37 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-10-22 10:02:30 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-22 10:02:27 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 10:01:59 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:01:31 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 10:01:31 | Moragaswewa (Deduru Oya) | 4.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 10:01:26 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-10-22 10:01:13 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:00:48 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.046 |  |
| 2026-10-22 10:00:48 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 10:00:47 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 10:01:26 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-10-22 10:06:41 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-22 10:05:09 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-22 10:04:08 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-22 10:01:31 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 09:03:41 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 10:09:37 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 10:10:18 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-22 10:04:17 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 10:00:48 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 10:01:31 | Moragaswewa (Deduru Oya) | 4.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 09:08:35 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 10:01:59 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:09:33 | Hanwella (Kelani Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:03:34 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:04:28 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:04:09 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:02:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:13:02 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-22 10:02:27 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:01:13 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:08:39 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:03:06 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:03:50 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-22 10:02:37 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-10-22 10:02:30 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-22 09:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-22 09:08:37 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.022 |  |
| 2026-10-22 10:03:09 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-10-22 10:04:56 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-10-22 10:04:11 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.040 |  |
| 2026-10-22 10:00:47 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.042 |  |
| 2026-10-22 10:00:48 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.046 |  |
| 2026-10-22 10:05:08 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.047 |  |
| 2026-10-22 10:02:57 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.050 |  |
| 2026-10-22 10:06:31 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-10-22 10:03:51 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | -0.235 |  |
| 2026-10-22 10:03:07 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.258 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)