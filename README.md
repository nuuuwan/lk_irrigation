# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_16:31:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,996 measurements** from **39** stations.
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
| 2026-10-12 16:31:12 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.026 |  |
| 2026-10-12 16:27:57 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:23:12 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.015 |  |
| 2026-10-12 16:18:46 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.016 |  |
| 2026-10-12 16:14:00 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-12 16:11:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-10-12 16:08:55 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.020 |  |
| 2026-10-12 16:07:11 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-12 16:06:58 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.057 |  |
| 2026-10-12 16:06:03 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:05:31 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:05:14 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 16:04:45 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 16:04:41 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-12 16:04:31 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 16:04:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-10-12 16:04:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:04:15 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-10-12 16:03:37 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.065 |  |
| 2026-10-12 16:03:34 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:03:33 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:03:31 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:03:28 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:03:18 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-10-12 16:03:05 | Ellagawa (Kalu Ganga) | 7.01 | 🟢 Normal | -0.040 |  |
| 2026-10-12 16:03:04 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.104 |  |
| 2026-10-12 16:02:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.041 |  |
| 2026-10-12 16:02:24 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-10-12 16:02:22 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-10-12 16:02:12 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:02:06 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:01:49 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-12 16:01:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:01:26 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.051 |  |
| 2026-10-12 16:00:56 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | -0.056 |  |
| 2026-10-12 16:00:42 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:00:20 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 16:04:15 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-10-12 16:14:00 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-12 16:04:41 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-12 16:05:14 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 16:07:11 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-12 16:04:31 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 16:04:45 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 16:04:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:02:12 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:02:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:03:33 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:05:31 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-12 15:04:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:02:06 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:00:42 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:27:57 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-12 16:11:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-10-12 16:04:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-10-12 16:03:34 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:03:31 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:06:03 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:01:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:03:28 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:00:20 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:23:12 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.015 |  |
| 2026-10-12 16:18:46 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.016 |  |
| 2026-10-12 16:01:49 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-12 16:02:24 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-10-12 16:08:55 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.020 |  |
| 2026-10-12 16:31:12 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.026 |  |
| 2026-10-12 16:02:22 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-10-12 16:03:18 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-10-12 16:03:05 | Ellagawa (Kalu Ganga) | 7.01 | 🟢 Normal | -0.040 |  |
| 2026-10-12 16:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.041 |  |
| 2026-10-12 16:01:26 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.051 |  |
| 2026-10-12 16:00:56 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | -0.056 |  |
| 2026-10-12 16:06:58 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.057 |  |
| 2026-10-12 16:03:37 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.065 |  |
| 2026-10-12 16:03:04 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)